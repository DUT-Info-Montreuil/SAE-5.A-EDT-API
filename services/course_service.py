from flask import jsonify
from services.main_service import Service

from services.sql_alchemy_service import db
from entities.models.models import Course,Participates,RoomsCourses,PersonalsCourses

from configuration import connect_pg
from datetime import timedelta
import datetime 

class course_service(Service):
    
    # university.courses(@id, description, starttime, endtime, course_type, #personal_id, #teaching_id)
    
    # ----------------------------------------------------------
    # Recuperer data
    # ----------------------------------------------------------

    def get_courses(self):
        query = "SELECT * FROM university.courses"
        return self.execute_query_and_get_statement(query)
        
    def get_course_by_id(self, id):
        query = "SELECT * FROM university.courses WHERE id = " + str(id)
        returnStatement = self.execute_query_and_get_statement(query)
        if len(returnStatement) == 1:
            return returnStatement
        else:
            return {}
    
    # ----------------------------------------------------------
    # Recuperer timetable
    # ----------------------------------------------------------

    def get_timetable_by_room(self, data):
        room_id = data.get('room_id', '')
        week_date_start = data.get('week_date_start', '')
        week_date_end = data.get('week_date_end', '')

        if room_id == '' or week_date_start == '' or week_date_end == '':
            return "Null arguments"

        week_date_start = datetime.datetime.strptime(week_date_start,"%Y-%m-%d")
        week_date_end = datetime.datetime.strptime(week_date_end,"%Y-%m-%d")
        
        

        query = """SELECT courses.id, courses.description, course_type,  json_agg(DISTINCT jsonb_build_object('code', personals.personal_code, 'id',personals.id)),
                   json_agg(DISTINCT jsonb_build_object('title', teachings.title, 'color', teachings.color, 'id', teachings.id)),
                    TO_CHAR(starttime, 'yyyy-mm-dd"T"HH24:MI'), TO_CHAR(endtime, 'yyyy-mm-dd"T"HH24:MI'), json_agg(DISTINCT jsonb_build_object('code', rooms.code, 'id', teachings.id)),
                    json_agg(DISTINCT jsonb_build_object('name', subgroups.name, 'id', subgroups.id)), university.groups.promotion, departments.name

                    FROM university.courses 
                    INNER JOIN university.teachings ON university.courses.teaching_id = university.teachings.id

                    LEFT JOIN university.personals_courses ON university.personals_courses.course_id = university.courses.id
                    LEFT JOIN university.personals ON university.personals_courses.personal_id = university.personals.id

                    LEFT JOIN university.rooms_courses ON university.rooms_courses.course_id = university.courses.id
                    LEFT JOIN university.rooms ON university.rooms_courses.rooms_id = university.rooms.id

                    LEFT JOIN university.participates ON university.courses.id = university.participates.course_id
                    LEFT JOIN university.subgroups ON university.participates.subgroup_id = university.subgroups.id
                    LEFT JOIN university.groups ON university.subgroups.group_id = university.groups.id
                    LEFT JOIN university.departments ON university.groups.department_id = university.departments.id

                    WHERE university.rooms_courses.rooms_id =""" +  str(room_id) + """ AND
                    starttime >= '""" + str(week_date_start) + """' AND starttime <= '""" + str(week_date_end) + """'
                    
                    GROUP BY courses.id, courses.description, course_type, courses.starttime, courses.endtime, university.groups.promotion, departments.name"""
        return self.execute_query_and_get_statement_timetable(query)
    
    def get_timetable_by_teacher(self, data):
        personal_id = data.get('personal_id', '')
        week_date_start = data.get('week_date_start', '')
        week_date_end = data.get('week_date_end', '')

        if personal_id == '' or week_date_start == '' or week_date_end == '':
            return "Null arguments"

        week_date_start = datetime.datetime.strptime(week_date_start,"%Y-%m-%d")
        week_date_end = datetime.datetime.strptime(week_date_end,"%Y-%m-%d")

        query = """SELECT courses.id, courses.description, course_type,  json_agg(DISTINCT jsonb_build_object('code', personals.personal_code, 'id',personals.id)),
                   json_agg(DISTINCT jsonb_build_object('title', teachings.title, 'color', teachings.color, 'id', teachings.id)),
                    TO_CHAR(starttime, 'yyyy-mm-dd"T"HH24:MI'), TO_CHAR(endtime, 'yyyy-mm-dd"T"HH24:MI'), json_agg(DISTINCT jsonb_build_object('code', rooms.code, 'id', teachings.id)),
                    json_agg(DISTINCT jsonb_build_object('name', subgroups.name, 'id', subgroups.id)), university.groups.promotion, departments.name

                    FROM university.courses 
                    INNER JOIN university.teachings ON university.courses.teaching_id = university.teachings.id

                    LEFT JOIN university.personals_courses ON university.personals_courses.course_id = university.courses.id
                    LEFT JOIN university.personals ON university.personals_courses.personal_id = university.personals.id

                    LEFT JOIN university.rooms_courses ON university.rooms_courses.course_id = university.courses.id
                    LEFT JOIN university.rooms ON university.rooms_courses.rooms_id = university.rooms.id

                    LEFT JOIN university.participates ON university.courses.id = university.participates.course_id
                    LEFT JOIN university.subgroups ON university.participates.subgroup_id = university.subgroups.id
                    LEFT JOIN university.groups ON university.subgroups.group_id = university.groups.id
                    LEFT JOIN university.departments ON university.groups.department_id = university.departments.id
                    
                    WHERE university.personals.id =""" +  str(personal_id) + """ AND
                    starttime >= '""" + str(week_date_start) + """' AND starttime <= '""" + str(week_date_end) + """'
                    
                    GROUP BY courses.id, courses.description, course_type, courses.starttime, courses.endtime, university.groups.promotion, departments.name"""
        return self.execute_query_and_get_statement_timetable(query)
    
    def get_timetable_by_department(self, data):
        promotion = data.get('promotion', '')
        department_id = data.get('department_id', '')
        week_date_start = data.get('week_date_start', '')
        week_date_end = data.get('week_date_end', '')

        if promotion == '' or department_id == '' or week_date_start == '' or week_date_end == '':
            return "Null arguments"
        
        week_date_start = datetime.datetime.strptime(week_date_start,"%Y-%m-%d")
        week_date_end = datetime.datetime.strptime(week_date_end,"%Y-%m-%d")

        query = """SELECT courses.id, courses.description, course_type,  json_agg(DISTINCT jsonb_build_object('code', personals.personal_code, 'id',personals.id)),
                json_agg(DISTINCT jsonb_build_object('title', teachings.title, 'color', teachings.color, 'id', teachings.id)),
                TO_CHAR(starttime, 'yyyy-mm-dd"T"HH24:MI'), TO_CHAR(endtime, 'yyyy-mm-dd"T"HH24:MI'), json_agg(DISTINCT jsonb_build_object('code', rooms.code, 'id', teachings.id)),
                json_agg(DISTINCT jsonb_build_object('name', subgroups.name, 'id', subgroups.id)), university.groups.promotion, departments.name
                
                FROM university.courses

                INNER JOIN university.teachings ON university.courses.teaching_id = university.teachings.id

                LEFT JOIN university.personals_courses ON university.personals_courses.course_id = university.courses.id
                LEFT JOIN university.personals ON university.personals_courses.personal_id = university.personals.id

                LEFT JOIN university.rooms_courses ON university.rooms_courses.course_id = university.courses.id
                LEFT JOIN university.rooms ON university.rooms_courses.rooms_id = university.rooms.id

                LEFT JOIN university.participates ON university.courses.id = university.participates.course_id
                LEFT JOIN university.subgroups ON university.participates.subgroup_id = university.subgroups.id
                LEFT JOIN university.groups ON university.subgroups.id = university.groups.id
                LEFT JOIN university.departments ON university.groups.department_id = university.departments.id

                WHERE university.groups.promotion =""" +  str(promotion) + """ AND
                university.groups.department_id =""" + str(department_id) + """ AND
                starttime >= '""" + str(week_date_start) + """' AND starttime <= '""" + str(week_date_end) + """'
                
                GROUP BY courses.id, courses.description, course_type, courses.starttime, courses.endtime, university.groups.promotion, departments.name"""

        return self.execute_query_and_get_statement_timetable(query)
    
    # Get by teachers id also ?
    # To adapt with the new student id
    def get_timetable_by_student(self, data):
        student_id = data.get('student_id', '') 
        week_date_start = data.get('week_date_start', '') #Format : YYYY-MM-DD
        week_date_end = data.get('week_date_end', '')

        if student_id == '' or week_date_start == '' or week_date_end == '':
            return "Null arguments"

        week_date_start = datetime.datetime.strptime(week_date_start,"%Y-%m-%d")
        week_date_end = datetime.datetime.strptime(week_date_end,"%Y-%m-%d")

        query = """SELECT courses.id, courses.description, course_type,  json_agg(DISTINCT jsonb_build_object('code', personals.personal_code, 'id',personals.id)),
                json_agg(DISTINCT jsonb_build_object('title', teachings.title, 'color', teachings.color, 'id', teachings.id)),
                TO_CHAR(starttime, 'yyyy-mm-dd"T"HH24:MI'), TO_CHAR(endtime, 'yyyy-mm-dd"T"HH24:MI'), json_agg(DISTINCT jsonb_build_object('code', rooms.code, 'id', teachings.id)),
                json_agg(DISTINCT jsonb_build_object('name', subgroups.name, 'id', subgroups.id)), university.groups.promotion, departments.name
                FROM university.courses

                INNER JOIN university.teachings ON university.courses.teaching_id = university.teachings.id

                LEFT JOIN university.personals_courses ON university.personals_courses.course_id = university.courses.id
                LEFT JOIN university.personals ON university.personals_courses.personal_id = university.personals.id

                LEFT JOIN university.rooms_courses ON university.rooms_courses.course_id = university.courses.id
                LEFT JOIN university.rooms ON university.rooms_courses.rooms_id = university.rooms.id

                LEFT JOIN university.participates ON university.courses.id = university.participates.course_id
                INNER JOIN university.students ON university.participates.subgroup_id = university.students.subgroup_id
                LEFT JOIN university.subgroups ON university.participates.subgroup_id = university.subgroups.id
                LEFT JOIN university.groups ON university.subgroups.group_id = university.groups.id
                LEFT JOIN university.departments ON university.groups.department_id = university.departments.id

                WHERE university.students.id =""" +  str(student_id) + """ AND
                starttime >= '""" + str(week_date_start) + """' AND starttime <= '""" + str(week_date_end) + """'
                
                GROUP BY courses.id, courses.description, course_type, courses.starttime, courses.endtime, university.groups.promotion, departments.name"""  
        return self.execute_query_and_get_statement(query)
    
    # ----------------------------------------------------------
    # Add / Delete / Update
    # ----------------------------------------------------------

    def add_course(self, data):
        description = data.get('description', '')
        starttime = data.get('starttime', '')
        endtime = data.get('endtime', '')
        course_type = data.get('course_type', '')
        teaching_id = data.get('teaching_id', '')

        if description == '' or starttime == '' or endtime == '' or course_type == '' or teaching_id == '':
            return {'error': 'Missing data'}, 400
        
        course = Course(
            description=description,
            starttime=starttime,
            endtime=endtime,
            course_type=course_type,
            teaching_id=teaching_id
        )

        rooms = data.get('rooms', [])
        personals = data.get('personals', [])
        subgroups = data.get('subgroups', [])

        try:
            with db.session.begin_nested():
                db.session.add(course)
                db.session.flush() 

                for room_id in rooms:
                    rooms_courses = RoomsCourses(course_id=course.id, rooms_id=room_id['id'])
                    db.session.add(rooms_courses)
                for personal_id in personals:
                    personals_courses = PersonalsCourses(course_id=course.id, personal_id=personal_id['id'])
                    db.session.add(personals_courses)

                for subgroup_id in subgroups:
                    participates = Participates(course_id=course.id, subgroup_id=subgroup_id['id'])
                    db.session.add(participates)

            db.session.commit()
            return {'message': f'Course s : {course.id} sucessfully added!'}, 200
        
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500 
        finally:
            db.session.close()

    def delete_course_by_id(self, id):
        try:

            db.session.query(RoomsCourses).filter(RoomsCourses.course_id == id).delete()
            db.session.query(Participates).filter(Participates.course_id == id).delete()
            db.session.query(PersonalsCourses).filter(PersonalsCourses.course_id == id).delete()
            db.session.query(Course).filter(Course.id == id).delete()
            
            db.session.commit()
            return {'message': f'Course : {id} sucessfully deleted!'}, 200
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500 
        finally:
            db.session.close()

    
    def update_course(self, id, data):
        try:
            course_data = {
            'description': data.get('description', None),
            'starttime': data.get('starttime', None),
            'endtime': data.get('endtime', None),
            'course_type': data.get('course_type', None),
            'teaching_id': data.get('teaching_id', None)
            }

            # Remove None values from the dictionary
            course_data = {k: v for k, v in course_data.items() if v is not None}

            if 'rooms' in data:
                # Delete existing room-course relationships for this course
                RoomsCourses.query.filter(RoomsCourses.course_id == id).delete()

                # Create new room-course relationships
                for room in data['rooms']:
                    new_room_course = RoomsCourses(course_id=id, rooms_id=room['id'])
                    db.session.add(new_room_course)

            if 'personals' in data:
                # Delete existing personal-course relationships for this course
                PersonalsCourses.query.filter(PersonalsCourses.course_id == id).delete()

                # Create new personal-course relationships
                for personal in data['personals']:
                    new_personal_course = PersonalsCourses(course_id=id, personal_id=personal['id'])
                    db.session.add(new_personal_course)

            if 'subGroups' in data:
                # Delete existing subgroup-course relationships for this course
                Participates.query.filter(Participates.course_id == id).delete()

                # Create new subgroup-course relationships
                for subgroup in data['subGroups']:
                    new_subgroup_course = Participates(course_id=id, subgroup_id=subgroup['id'])
                    db.session.add(new_subgroup_course)

            if course_data:
                db.session.query(Course).filter(Course.id == id).update(course_data)
                    

            db.session.commit()
            return {'message': f'Course : {id} sucessfully updated!'}, 200
        
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500 
        finally:
            db.session.close()



    # ----------------------------------------------------------
    # Utilitaires
    # ----------------------------------------------------------

    def execute_query_and_get_statement(self, query):
            conn = self.get_connection()
            rows = connect_pg.get_query(conn, query)
            if rows is None:
                return {}
            returnStatement = []
            for row in rows:
                returnStatement.append(self.get_course_statement(row))
            connect_pg.disconnect(conn)
            return returnStatement
    
    def execute_query_and_get_statement_timetable(self, query):
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)

        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_course_statement_timetable(row))
        connect_pg.disconnect(conn)
        return returnStatement
    
    
    def get_course_statement(self, row):
        """ Formats course data in JSON """
        return {
            'id': row[0],              # L'ID du cours
            'description': row[1],     # La description du cours
            'starttime': row[2],       # L'heure de début du cours
            'endtime': row[3],         # L'heure de la fin du cours
            'course_type': row[4],     # Le type de cours
            'teaching_id': row[5]      # L'ID de l'enseignement associé au cours
        }
    
    def get_course_statement_timetable(self, row):
        return {
            'id': row[0],              
            'description': row[1],
            'course_type': row[2],
            'personals': row[3],   # Nom abrégé du professeur
            'teaching': row[4],  # Nom de la matière    
            'starttime': row[5],        
            'endtime':  row[6],        
            'rooms':  row[7],       # Nom de la salle
            'subgroups': row[8],
            'promotion': row[9],
            'department': row[10]
        }