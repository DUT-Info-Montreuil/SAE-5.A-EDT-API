# sqlAlchemyController.py

from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from datetime import timedelta
from config import config
import connect_pg

db = SQLAlchemy()

def initialize_app(app):
    params = config()
    connectString = f'postgresql://{ params["user"] }:{ params["password"] }@{ params["host"] }/{params["database"]}'
    app.config['SQLALCHEMY_DATABASE_URI'] = connectString
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return db

def getTable():
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

def get_table_objects(app):
    with app.app_context():
        db.reflect()
    try:
        return getTable()
    except KeyError:
        print("Tables are not created or not found")
        result = initialize_database()
        if(result) :
            # Reflect the existing tables in the database
            with app.app_context():
                db.reflect()
            return get_table_objects(app)

def reflect() : 
    with db.get_app().app_context():
        db.reflect()

def initialize_database():
    university_drop_bool, university_drop = connect_pg.execute_sql_script('scripts/script_university_drop.sql')
    university_create_bool, university_create = connect_pg.execute_sql_script('scripts/script_university_create.sql')
    university_user_insert_bool, university_user_insert = connect_pg.execute_sql_script('scripts/script_university_user_insert.sql')
    university_school_insert_bool, university_school_insert = connect_pg.execute_sql_script('scripts/script_university_school_insert.sql')
    university_student_insert_bool, university_student_insert = connect_pg.execute_sql_script('scripts/script_university_student_insert.sql')
    university_courses_insert_bool, university_courses_insert = connect_pg.execute_sql_script('scripts/script_university_courses_insert.sql')
    university_participate_insert_bool, university_participate_insert = connect_pg.execute_sql_script('scripts/script_university_participate_insert.sql')
    
    resultBool = university_drop_bool == university_create_bool == university_user_insert_bool == university_school_insert_bool == university_student_insert_bool == university_courses_insert_bool == university_participate_insert_bool

    resultString = { "university_drop " : university_drop ,  
                "university_create " : university_create ,  
                "university_user_insert " : university_user_insert ,  
                "university_school_insert " : university_school_insert ,  
                "university_student_insert " : university_student_insert ,  
                "university_courses_insert " : university_courses_insert ,  
                "university_participate_insert " : university_participate_insert }
    
    return resultBool, resultString

def drop_database():
    bool_result, string_result = connect_pg.execute_sql_script('scripts/script_university_drop.sql')
    return bool_result, { "university_drop": string_result }

def create_database():
    bool_result, string_result = connect_pg.execute_sql_script('scripts/script_university_create.sql')
    return bool_result, { "university_create": string_result }

def insert_university_user():
    bool_result, string_result = connect_pg.execute_sql_script('scripts/script_university_user_insert.sql')
    return bool_result, { "university_user_insert": string_result }

def insert_university_school():
    bool_result, string_result = connect_pg.execute_sql_script('scripts/script_university_school_insert.sql')
    return bool_result, { "university_school_insert": string_result }

def insert_university_student():
    bool_result, string_result = connect_pg.execute_sql_script('scripts/script_university_student_insert.sql')
    return bool_result, { "university_student_insert": string_result }

def insert_university_courses():
    bool_result, string_result = connect_pg.execute_sql_script('scripts/script_university_courses_insert.sql')
    return bool_result, { "university_courses_insert": string_result }

def insert_university_participate():
    bool_result, string_result = connect_pg.execute_sql_script('scripts/script_university_participate_insert.sql')
    return bool_result, { "university_participate_insert": string_result }