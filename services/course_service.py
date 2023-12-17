from flask import jsonify
from services.main_basic_service import *
from configuration import connect_pg
from datetime import timedelta

class course_service(Service):
    
    # university.courses(@id, description, starttime, endtime, course_type, #personal_id, #rooms_id, #teaching_id)
    
    # === region : Course ===
    def get_all_courses(self):
        courses = Course.query.all()
        course_list = []

        for course in courses:
            course_data = course.get_json()
            course_list.append(course_data)

        return course_list
    
    def get_course_by_id(self, course_id):
        course = Course.query.get(course_id)

        if course:
            course_data = course.get_json()
            return course_data
        else:
            return None
    
    def find_course(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        courses = Course.query.filter_by(**conditions)

        course_list = []

        for course in courses:
            course_list.append(course.get_json())

        return course_list
    
    def delete_course(self, course_id):
        course = Course.query.get(course_id)

        if course:
            db.session.delete(course)
            db.session.commit()
            return True
        else:
            return False
    
    def update_course(self, course_id, new_data):
        course = Course.query.get(course_id)

        if course:
            for key, value in new_data.items():
                setattr(course, key, value)

            db.session.commit()
            return True
        else:
            return False
    
    def add_course(self, course_data):
        new_course = Course(**course_data)

        try:
            db.session.add(new_course)
            db.session.commit()
            return new_course.get_json()
        except Exception as e:
            # Handle exceptions (e.g., integrity errors) appropriately
            db.session.rollback()
            return None
    # === endregion : Course ===