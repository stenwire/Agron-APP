from flask import Blueprint

farmer = Blueprint('farmer', __name__, url_prefix='/farmer')


@farmer.route('/')
def index():

    return '<h1>Welcome to farmer page</h1>'