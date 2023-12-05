from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Teachings(db.Model):
    __tablename__ = 'university.teachings'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    hour_number = db.Column(db.Integer)
    semestre = db.Column(db.Integer, nullable=False)
    sequence = db.Column(db.String(8), nullable=False)
    description = db.Column(db.Text)
    teaching_type = db.Column(db.String(255), default='RCC')
    specialization_id = db.Column(db.Integer, nullable=False)
