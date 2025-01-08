from flask import Flask, render_template
from routes.api import app as api_app
from mysql.connector import connect, Error
import os

app = Flask(__name__)
app.register_blueprint(api_app)

def get_db_connection():
    return connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    user_id = request.args.get('user_id')

    if not user_id:
        return render_template("portfolio.html", portfolio=[])

    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM portfolios WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        portfolio_data = cursor.fetchall()
        return render_template('portfolio.html', portfolio=portfolio_data)
    except Error as e:
        return f"Error fetching portfolio: {e}", 500
    finally:
        if connection:
            cursor.close()
            connection.close()


if __name__ == "__main__":
    app.run(debug=True)
