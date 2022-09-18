from flask import Blueprint

employ = Blueprint('employ', __name__, url_prefix='/employ')


@employ.route('/')
def index():

    return '<h1>Welcome to employ page</h1>'