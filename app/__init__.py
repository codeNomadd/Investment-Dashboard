from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize extensions
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configure the app
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions with app
    db.init_app(app)
    
    # Register routes
    from app.services import stock_service
    app.register_blueprint(stock_service.bp)
    
    return app

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
