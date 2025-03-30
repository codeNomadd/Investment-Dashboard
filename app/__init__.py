from flask import Flask, render_template, request, jsonify
from mysql.connector import connect, Error
import os
from dotenv import load_dotenv
from app.extensions import db

# Load environment variables
load_dotenv()

def create_app(config_object=None):
    app = Flask(__name__)
    
    # Configure the app
    if config_object:
        app.config.from_object(config_object)
    else:
        app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
        app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['ALPHA_VANTAGE_API_KEY'] = os.getenv('ALPHA_VANTAGE_API_KEY')
        app.config['STOCK_SYMBOLS'] = os.getenv('STOCK_SYMBOLS', 'AAPL,MSFT')
    
    # Initialize extensions with app
    db.init_app(app)
    
    # Register routes
    from app.services import stock_service
    app.register_blueprint(stock_service.bp)
    
    def get_db_connection():
        return connect(
            host=app.config.get("DB_HOST"),
            user=app.config.get("DB_USER"),
            password=app.config.get("DB_PASSWORD"),
            database=app.config.get("DB_NAME")
        )
    
    @app.route('/health')
    def health_check():
        return jsonify({"status": "healthy"}), 200
    
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
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
