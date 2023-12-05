from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Absents(db.Model):
    __tablename__ = 'university.absents'
    id = db.Column(db.Integer, primary_key=True)
    justified = db.Column(db.Boolean, default=True)
    student_number = db.Column(db.Integer, db.ForeignKey('university.students.student_number'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('university.courses.id'), nullable=False)