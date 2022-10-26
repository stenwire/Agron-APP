from datetime import datetime
from ..extension import db

class Users(db.Model):
    # __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(500), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    register_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_farmer = db.Column(db.Boolean, default=False, nullable=False)
    is_trader = db.Column(db.Boolean, default=False, nullable=False)
    is_investor = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f'<User: {self.firstname}, ID: {self.id}>'

    def is_farmer(self):
        return f'{self.is_farmer}'

    def is_trader(self):
        return f'{self.is_trader}'

    def is_investor(self):
        return f'{self.is_investor}'
