from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Responsibles(db.Model):
    __tablename__ = 'university.responsibles'
    id = db.Column(db.Integer, primary_key=True)
    personal_id = db.Column(db.Integer, db.ForeignKey('university.personals.id'), nullable=False)
    teaching_id = db.Column(db.Integer, db.ForeignKey('university.teachings.id'), nullable=False)
