from flask import Flask
from .main.routes import main
from .extensions import mongo
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

def create_app():
    app = Flask(__name__)

    app.config['MONGO_URI'] = os.getenv('DB_URL')
    
    mongo.init_app(app)

    app.register_blueprint(main)

    return app