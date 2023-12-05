from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Reminders(db.Model):
    __tablename__ = 'university.reminders'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    description = db.Column(db.Text)
    course_id = db.Column(db.Integer, nullable=False)
