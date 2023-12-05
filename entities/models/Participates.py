from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Participates(db.Model):
    __tablename__ = 'university.participates'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('university.courses.id'), nullable=False)
    subgroup_id = db.Column(db.Integer, db.ForeignKey('university.subgroups.id'), nullable=False)