from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_bootstrap import Bootstrap

db = SQLAlchemy()

def create_app(config_name):


    # Initializing application
    app = Flask(__name__)

    # Initializing flask extensions
    db.init_app(app)

    # Initializing Flask Extensions
    bootstrap = Bootstrap(app)

    return app