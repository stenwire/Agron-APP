from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # app.config.from_prefixed_env()
    app.config.from_pyfile('flask.cfg') # all config in 1-file

    db.init_app(app)

    migrate.init_app(app, db)

    return app


if __name__ == "__main__":
    app =create_app()
    app.run(debug=True)
