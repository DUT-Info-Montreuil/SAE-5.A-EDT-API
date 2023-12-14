# sql_alchemy_service.py
from services.university_service import university_service
from flask_sqlalchemy import SQLAlchemy
from configuration.config import config

db = SQLAlchemy()

def init_app(app):
    params = config()
    connectString = f'postgresql://{ params["user"] }:{ params["password"] }@{ params["host"] }/{params["database"]}'
    app.config['SQLALCHEMY_DATABASE_URI'] = connectString
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

def getTable(db):
    table_users = db.metadata.tables['users']
    table_students = db.metadata.tables['students']
    table_departments = db.metadata.tables['departments']
    table_groups = db.metadata.tables['groups']
    table_subgroups = db.metadata.tables['subgroups']
    table_personals = db.metadata.tables['personals']
    table_roles = db.metadata.tables['roles']
    table_courses = db.metadata.tables['courses']
    table_rooms = db.metadata.tables['rooms']
    table_reminders = db.metadata.tables['reminders']
    table_specializations = db.metadata.tables['specializations']
    table_teachings = db.metadata.tables['teachings']
    table_absents = db.metadata.tables['absents']
    table_participates = db.metadata.tables['participates']
    table_responsibles = db.metadata.tables['responsibles']
    
    return (
        table_users, table_students, table_departments, table_groups, table_subgroups, 
        table_personals, table_roles, table_courses, table_rooms, 
        table_reminders, table_specializations, table_teachings, 
        table_absents, table_participates, table_responsibles
    )

def get_table_objects(app, db): 
    with app.app_context():
        db.reflect()
    try:
        return getTable(db)
    except KeyError:
        print("Tables are not created or not found")
        _service = university_service()
        result_bool, resultString  = _service.initialize_database()
        if(result_bool) :
            # Reflect the existing tables in the database
            with app.app_context():
                db.reflect()
            return get_table_objects(app)

def reflect(db) : 
    with db.get_app().app_context():
        db.reflect()
