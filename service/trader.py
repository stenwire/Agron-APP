from flask import Blueprint

trader = Blueprint('trader', __name__, url_prefix='/trader')


@trader.route('/')
def index():

    return '<h1>Welcome to trader page</h1>'