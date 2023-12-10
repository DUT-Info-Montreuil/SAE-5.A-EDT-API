from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Responsibles(db.Model):
    __tablename__ = 'responsibles'
    id = db.Column(db.Integer, primary_key=True)
    personal_id = db.Column(db.Integer, db.ForeignKey('personals.id'), nullable=False)
    teaching_id = db.Column(db.Integer, db.ForeignKey('teachings.id'), nullable=False)
