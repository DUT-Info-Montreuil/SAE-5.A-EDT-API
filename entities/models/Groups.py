from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Groups(db.Model):
    __tablename__ = 'university.groups'
    id = db.Column(db.Integer, primary_key=True)
    promotion = db.Column(db.Integer)
    type = db.Column(db.String(5), nullable=False, CheckConstraint('type ~ \'^[A-Z]+$\' OR type = \'APP\''))
    department_id = db.Column(db.Integer, nullable=False)
