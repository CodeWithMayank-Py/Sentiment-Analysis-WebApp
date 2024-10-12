from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    # Load environment variables from .env file
    load_dotenv()

    app = Flask(__name__)

    # Import routes
    from app.routes import main
    app.register_blueprint(main)

    return app
