from flask_sqlalchemy import SQLAlchemy
from ..extensions import create_app
# from home import create_app

app = create_app()
db = SQLAlchemy(app)