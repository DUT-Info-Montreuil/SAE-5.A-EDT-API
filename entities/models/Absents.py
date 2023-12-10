from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Absents(db.Model):
    __tablename__ = 'absents'
    id = db.Column(db.Integer, primary_key=True)
    justified = db.Column(db.Boolean, default=True)
    student_number = db.Column(db.Integer, db.ForeignKey('students.student_number'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    
from sqlAlchemyModel import db, table_users
# Dynamically create the model User based on the reflected table (table in the db)
class User(db.Model):
    __table__ = table_users