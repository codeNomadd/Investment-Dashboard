from flask import Blueprint, jsonify
from app.models.stock import Stock
from app.utils.stock_data import update_stock_data
import os

bp = Blueprint('stock', __name__)

@bp.route('/api/stocks', methods=['GET'])
def get_stocks():
    """Get all tracked stocks"""
    symbols = os.getenv('STOCK_SYMBOLS', '').split(',')
    return jsonify({'symbols': symbols})

@bp.route('/api/stocks/<symbol>', methods=['GET'])
def get_stock_data(symbol):
    """Get data for a specific stock"""
    try:
        update_stock_data([symbol])
        return jsonify({'message': f'Data updated for {symbol}'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/api/stocks/update', methods=['POST'])
def update_all_stocks():
    """Update data for all tracked stocks"""
    try:
        symbols = os.getenv('STOCK_SYMBOLS', '').split(',')
        update_stock_data(symbols)
        return jsonify({'message': 'All stocks updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500 