# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# local imports

db = SQLAlchemy()



def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_name)
    app.config.from_pyfile('config.py')

    db.init_app(app)


    from app import models


    return app
