from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Personals(db.Model):
    __tablename__ = 'personals'
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(32), nullable=False)
    first_name = db.Column(db.String(32), nullable=False)
    mail = db.Column(db.String(320), nullable=False)
    personal_code = db.Column(db.String(16), unique=True, nullable=False)
    user_username = db.Column(db.String(64), db.ForeignKey('users.username'), unique=True, nullable=False)
    phone_number = db.Column(db.Integer, unique=True, nullable=False)
