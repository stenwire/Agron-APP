from flask import Blueprint

shop = Blueprint('shop', __name__, url_prefix='/shop')


@shop.route('/')
def index():

    return '<h1>Welcome to shop page</h1>'