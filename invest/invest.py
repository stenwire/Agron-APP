from flask import Blueprint

invest = Blueprint('invest', __name__, url_prefix='/invest')


@invest.route('/')
def index():

    return '<h1>Welcome to invest page</h1>'