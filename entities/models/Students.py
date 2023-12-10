from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Students(db.Model):
    __tablename__ = 'students'
    student_number = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    first_name = db.Column(db.String(32), nullable=False)
    mail = db.Column(db.String(320), nullable=False)
    phone_number = db.Column(db.Integer, unique=True, nullable=False)
    user_username = db.Column(db.String(64), db.ForeignKey('users.username'), nullable=False)
    department_id = db.Column(db.Integer, nullable=False)
    group_id = db.Column(db.Integer, nullable=False)
    subgroup_id = db.Column(db.Integer, nullable=False)
