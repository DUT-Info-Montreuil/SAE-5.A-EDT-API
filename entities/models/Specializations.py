from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Specializations(db.Model):
    __tablename__ = 'specializations'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(255), nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False, default='Semestre de préparation au parcours')
    department_id = db.Column(db.Integer, nullable=False)
