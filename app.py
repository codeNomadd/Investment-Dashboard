from flask import Flask
from routes.api import app as api_app

# Initialize Flask app
app = Flask(__name__)

# Register routes
app.register_blueprint(api_app)

if __name__ == "__main__":
    app.run(debug=True)
