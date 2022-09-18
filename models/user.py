from models import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    secondname = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(500), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f'<Farmer {self.firstname}>'