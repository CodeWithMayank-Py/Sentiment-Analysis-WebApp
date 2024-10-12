from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration from config.py
    app.config.from_object('config')

    # Import routes
    from app.routes import main
    app.register_blueprint(main)

    return app
