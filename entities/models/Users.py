from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'university.users'
    username = db.Column(db.String(64), primary_key=True, unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)