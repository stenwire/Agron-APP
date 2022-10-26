from models import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(500), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    is_farmer = db.Column(db.Boolean, default=False)
    is_trader = db.Column(db.Boolean, default=False)
    is_investor = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Farmer {self.firstname}>'