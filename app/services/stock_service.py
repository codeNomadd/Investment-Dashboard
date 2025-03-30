from flask import Blueprint, jsonify, current_app
from app.models.stock import Stock
from app.extensions import db
from app.exceptions import AlphaVantageError
import requests
from datetime import datetime
import os

bp = Blueprint('stock', __name__)

class StockService:
    def __init__(self):
        self.api_key = current_app.config['ALPHA_VANTAGE_API_KEY']
        self.base_url = "https://www.alphavantage.co/query"
    
    def fetch_stock_data(self, symbol):
        """Fetch stock data from Alpha Vantage API"""
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": self.api_key
        }
        
        response = requests.get(self.base_url, params=params)
        if response.status_code == 429:
            raise AlphaVantageError("API rate limit exceeded")
        
        data = response.json()
        if "Error Message" in data:
            raise AlphaVantageError(data["Error Message"])
        if "Note" in data and "API rate limit" in data["Note"]:
            raise AlphaVantageError(data["Note"])
            
        return data
    
    def update_stock_data(self, symbol):
        """Update stock data in the database"""
        data = self.fetch_stock_data(symbol)
        time_series = data.get("Time Series (Daily)", {})
        updated_stocks = []
        
        for date_str, values in time_series.items():
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            stock = Stock.query.filter_by(symbol=symbol, date=date).first()
            
            if not stock:
                stock = Stock(symbol=symbol, date=date)
            
            stock.open_price = float(values["1. open"])
            stock.high_price = float(values["2. high"])
            stock.low_price = float(values["3. low"])
            stock.close_price = float(values["4. close"])
            stock.volume = int(values["5. volume"])
            
            if not stock.id:
                db.session.add(stock)
            updated_stocks.append(stock)
        
        db.session.commit()
        return updated_stocks
    
    def get_stock_history(self, symbol, limit=30):
        """Get historical data for a stock"""
        return Stock.query.filter_by(symbol=symbol)\
                        .order_by(Stock.date.desc())\
                        .limit(limit)\
                        .all()
    
    def get_latest_stock_data(self, symbol):
        """Get the most recent data for a stock"""
        return Stock.query.filter_by(symbol=symbol)\
                        .order_by(Stock.date.desc())\
                        .first()
    
    def get_stock_by_date(self, symbol, date):
        """Get stock data for a specific date"""
        return Stock.query.filter_by(symbol=symbol, date=date).first()

@bp.route('/api/stocks', methods=['GET'])
def get_stocks():
    """Get all tracked stocks"""
    symbols = current_app.config['STOCK_SYMBOLS'].split(',')
    return jsonify({'symbols': symbols})

@bp.route('/api/stocks/<symbol>', methods=['GET'])
def get_stock_data(symbol):
    """Get data for a specific stock"""
    try:
        service = StockService()
        stocks = service.update_stock_data(symbol)
        return jsonify({
            'symbol': symbol,
            'data': [
                {
                    'date': stock.date.isoformat(),
                    'open': stock.open_price,
                    'high': stock.high_price,
                    'low': stock.low_price,
                    'close': stock.close_price,
                    'volume': stock.volume
                }
                for stock in stocks
            ]
        })
    except AlphaVantageError as e:
        return jsonify({'error': str(e)}), 429
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/api/stocks/update', methods=['POST'])
def update_all_stocks():
    """Update data for all tracked stocks"""
    try:
        service = StockService()
        symbols = current_app.config['STOCK_SYMBOLS'].split(',')
        results = {}
        
        for symbol in symbols:
            try:
                stocks = service.update_stock_data(symbol)
                results[symbol] = len(stocks)
            except AlphaVantageError as e:
                results[symbol] = str(e)
        
        return jsonify({'results': results})
    except Exception as e:
        return jsonify({'error': str(e)}), 500 