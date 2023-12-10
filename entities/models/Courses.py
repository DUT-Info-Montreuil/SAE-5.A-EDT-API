from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Courses(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    startTime = db.Column(db.TIMESTAMP, nullable=False)
    endtime = db.Column(db.TIMESTAMP, nullable=False)
    course_type = db.Column(db.String(255), nullable=False, CheckConstraint('course_type IN (\'Situations d’apprentissage et d’évaluation (SAÉ)\', \'Ressources transversales (RT)\', \'Ressources cœur de compétences (RCC)\')'))
    personal_id = db.Column(db.Integer, nullable=False)
    rooms_id = db.Column(db.Integer, nullable=False)
    teaching_id = db.Column(db.Integer, nullable=False)
