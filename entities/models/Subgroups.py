from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Subgroups(db.Model):
    __tablename__ = 'university.subgroups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), nullable=False)
    group_id = db.Column(db.Integer, nullable=False)