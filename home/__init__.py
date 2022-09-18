# from flask import Flask
# from .views.main import main
# from .views.farmer import farmer
# from .views.invest import invest
# from .views.shop import shop
# from .auth.auth import auth

# from ..extensions import db

# def create_app():
#     app = Flask(__name__)

#     app.register_blueprint(main)
#     app.register_blueprint(farmer)
#     app.register_blueprint(invest)
#     app.register_blueprint(shop)
#     app.register_blueprint(auth)

#     app.config.from_prefixed_env()

#     db.init_app(app)

#     return app
# # from .config import create_app

# # app = create_app()
from flask import Blueprint

main = Blueprint('main', __name__)


@main.route('/')
def index():

    return '<h1>Welcome to main page</h1>'