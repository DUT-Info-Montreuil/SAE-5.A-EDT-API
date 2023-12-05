from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Rooms(db.Model):
    __tablename__ = 'university.rooms'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(32), nullable=False, unique=True)
    capacity = db.Column(db.Integer, nullable=False)
    has_computer = db.Column(db.Boolean, default=True)
    has_projector = db.Column(db.Boolean, default=True)