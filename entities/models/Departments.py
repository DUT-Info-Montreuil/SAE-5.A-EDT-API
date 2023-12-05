from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Departments(db.Model):
    __tablename__ = 'university.departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, unique=True)
    description = db.Column(db.String(128))
    degree_type = db.Column(db.String(50), nullable=False, CheckConstraint('degree_type IN (\'Licence_PRO\', \'BUT\')'))
    personal_id = db.Column(db.Integer, nullable=False)
