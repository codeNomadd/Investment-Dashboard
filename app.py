from flask import Flask
from routes.api import app as api_app

# Initialize Flask app
app = Flask(__name__)

# Register routes
app.register_blueprint(api_app)

# Default route for '/'
@app.route('/')
def home():
    return "Welcome to the Investment Dashboard API! Use the available endpoints."

# Optional: Handle favicon request
@app.route('/favicon.ico')
def favicon():
    return '', 204  # Return an empty response with a 204 (No Content) status code

if __name__ == "__main__":
    app.run(debug=True)
