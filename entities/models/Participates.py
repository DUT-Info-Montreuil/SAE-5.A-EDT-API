from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Participates(db.Model):
    __tablename__ = 'participates'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    subgroup_id = db.Column(db.Integer, db.ForeignKey('subgroups.id'), nullable=False)