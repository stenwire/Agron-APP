from models import db

class Trader(db.Model):
    __tablename__ = "trader"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    secondname = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(500), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    user_id = db.Column(db.Integer)

    def __repr__(self):
        return f'<Farmer {self.firstname}>'