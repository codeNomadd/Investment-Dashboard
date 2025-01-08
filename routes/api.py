from flask import Blueprint, request, jsonify
from mysql.connector import connect, Error
from stock_data import update_stock_data
import os

app = Blueprint('api', __name__)
SYMBOLS = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]

def get_db_connection():
    return connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

@app.route('/portfolio', methods=['POST'])
def add_to_portfolio():
    data = request.json
    user_id = data.get('user_id')
    symbol = data.get('symbol')
    quantity = data.get('quantity')
    purchase_price = data.get('purchase_price')

    if not all([user_id, symbol, quantity, purchase_price]):
        return jsonify({'error': 'All fields are required'}), 400

    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
        INSERT INTO portfolios (user_id, symbol, quantity, purchase_price)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (user_id, symbol, quantity, purchase_price))
        connection.commit()
        return jsonify({'message': 'Stock added to portfolio successfully'}), 201
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection:
            cursor.close()
            connection.close()

@app.route('/portfolio', methods=['GET'])
def get_portfolio():
    user_id = request.args.get('user_id')

    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM portfolios WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        portfolio = cursor.fetchall()
        return jsonify(portfolio), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection:
            cursor.close()
            connection.close()

@app.route('/update-stocks', methods=['GET'])
def update_stocks_ui():
    """
    Trigger stock data updates manually through the UI.
    """
    symbols = SYMBOLS  # Replace SYMBOLS with your list of stock symbols
    try:
        update_stock_data(symbols)
        return "Stock data updated successfully! Go back to the <a href='/'>homepage</a>.", 200
    except Exception as e:
        return f"Error updating stock data: {str(e)}", 500



@app.route('/portfolio/<int:portfolio_id>', methods=['PUT'])
def update_portfolio(portfolio_id):
    data = request.json
    quantity = data.get('quantity')
    purchase_price = data.get('purchase_price')

    if not any([quantity, purchase_price]):
        return jsonify({'error': 'At least one field (quantity or purchase_price) is required'}), 400

    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "UPDATE portfolios SET "
        params = []

        if quantity is not None:
            query += "quantity = %s, "
            params.append(quantity)

        if purchase_price is not None:
            query += "purchase_price = %s, "
            params.append(purchase_price)

        query = query.rstrip(', ') + " WHERE id = %s"
        params.append(portfolio_id)

        cursor.execute(query, tuple(params))
        connection.commit()
        return jsonify({'message': 'Portfolio updated successfully'}), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection:
            cursor.close()
            connection.close()

@app.route('/portfolio/<int:portfolio_id>', methods=['DELETE'])
def delete_stock(portfolio_id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "DELETE FROM portfolios WHERE id = %s"
        cursor.execute(query, (portfolio_id,))
        connection.commit()
        return jsonify({'message': 'Stock deleted successfully'}), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection:
            cursor.close()
            connection.close()

@app.route('/update-stocks', methods=['POST'])
def update_stocks():
    """
    Trigger stock data updates manually.
    """
    symbols = request.json.get('symbols', [])
    if not symbols:
        return jsonify({'error': 'No symbols provided'}), 400

    update_stock_data(symbols)
    return jsonify({'message': 'Stock data update triggered'}), 200

@app.route('/historical-data/<string:symbol>', methods=['GET'])
def get_historical_data(symbol):
    """
    Retrieve historical data for a specific stock symbol from the database.
    """
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        query = f"SELECT timestamp, high FROM {symbol}_stock ORDER BY timestamp ASC"
        cursor.execute(query)
        data = cursor.fetchall()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection:
            cursor.close()
            connection.close()
