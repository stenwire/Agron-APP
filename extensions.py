from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_prefixed_env()

    db.init_app(app)

    return app