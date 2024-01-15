from flask import jsonify
from services.main_service import Service

from services.sql_alchemy_service import db
from sqlalchemy import and_, cast, Date
from entities.models.models import Course,Participates,RoomsCourses,PersonalsCourses,Subgroup, Group, Personal, Room

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

    # @to-do: refactor all timetable functions
    # les seuls elements unique sont les subquery, les query sont les mêmes partout
    def get_timetable_by_room(self, data):
        room_id = data.get('room_id', '')
        week_date_start = data.get('week_date_start', '')
        week_date_end = data.get('week_date_end', '')

        if room_id == '' or week_date_start == '' or week_date_end == '':
            return "Null arguments"

        week_date_start = datetime.datetime.strptime(week_date_start,"%Y-%m-%d")
        week_date_end = datetime.datetime.strptime(week_date_end,"%Y-%m-%d")
        
        query = """SELECT courses.id FROM university.courses
                
                LEFT JOIN university.rooms_courses ON university.rooms_courses.course_id = university.courses.id
                LEFT JOIN university.rooms ON university.rooms_courses.rooms_id = university.rooms.id
                
                WHERE university.rooms_courses.rooms_id =""" +  str(room_id) + """ AND
                starttime >= '""" + str(week_date_start) + """' AND starttime <= '""" + str(week_date_end) + """'"""
        
        values = self.execute_subquery_and_get_statement(query)
        if values is None:
            return {}
        return self.timetable_query(values)
    
    def get_timetable_by_teacher(self, data):
        personal_id = data.get('personal_id', '')
        week_date_start = data.get('week_date_start', '')
        week_date_end = data.get('week_date_end', '')

        if personal_id == '' or week_date_start == '' or week_date_end == '':
            return "Null arguments"

        week_date_start = datetime.datetime.strptime(week_date_start,"%Y-%m-%d")
        week_date_end = datetime.datetime.strptime(week_date_end,"%Y-%m-%d")

        query = """SELECT courses.id FROM university.courses
                
                LEFT JOIN university.personals_courses ON university.personals_courses.course_id = university.courses.id
                LEFT JOIN university.personals ON university.personals_courses.personal_id = university.personals.id
                
                WHERE university.personals.id =""" +  str(personal_id) + """ AND
                starttime >= '""" + str(week_date_start) + """' AND starttime <= '""" + str(week_date_end) + """'"""
        
        values = self.execute_subquery_and_get_statement(query)
        if values is None:
            return {}
        return self.timetable_query(values)
    
    def get_timetable_by_department(self, data):
        promotion = data.get('promotion', '')
        department_id = data.get('department_id', '')
        week_date_start = data.get('week_date_start', '')
        week_date_end = data.get('week_date_end', '')

        if promotion == '' or department_id == '' or week_date_start == '' or week_date_end == '':
            return "Null arguments"
        
        week_date_start = datetime.datetime.strptime(week_date_start,"%Y-%m-%d")
        week_date_end = datetime.datetime.strptime(week_date_end,"%Y-%m-%d")

        query = """SELECT courses.id FROM university.courses
                
                LEFT JOIN university.participates ON university.courses.id = university.participates.course_id
                LEFT JOIN university.subgroups ON university.participates.subgroup_id = university.subgroups.id
                LEFT JOIN university.groups ON university.subgroups.id = university.groups.id
                LEFT JOIN university.departments ON university.groups.department_id = university.departments.id
                
                WHERE university.groups.promotion =""" +  str(promotion) + """ AND
                university.groups.department_id =""" + str(department_id) + """ AND
                starttime >= '""" + str(week_date_start) + """' AND starttime <= '""" + str(week_date_end) + """'"""
        
        values = self.execute_subquery_and_get_statement(query)
        if values is None:
            return {}
        return self.timetable_query(values)
    
    def get_timetable_by_student(self, data):
        student_id = data.get('student_id', '') 
        week_date_start = data.get('week_date_start', '') #Format : YYYY-MM-DD
        week_date_end = data.get('week_date_end', '')

        if student_id == '' or week_date_start == '' or week_date_end == '':
            return "Null arguments"

        week_date_start = datetime.datetime.strptime(week_date_start,"%Y-%m-%d")
        week_date_end = datetime.datetime.strptime(week_date_end,"%Y-%m-%d")

        query = """SELECT courses.id FROM university.courses
                
                LEFT JOIN university.participates ON university.courses.id = university.participates.course_id
                LEFT JOIN university.students ON university.participates.subgroup_id = university.students.subgroup_id
                LEFT JOIN university.subgroups ON university.participates.subgroup_id = university.subgroups.id
                
                WHERE students.id = """ +  str(student_id) + """ AND
                starttime >= '""" + str(week_date_start) + """' AND starttime <= '""" + str(week_date_end) + """'"""
        
        values = self.execute_subquery_and_get_statement(query)
        if values is None:
            return {}
        return self.timetable_query(values)

    def timetable_query(self, values):
        if values is None:
            return {}

        query = """SELECT courses.id, courses.description, course_type,  json_agg(DISTINCT jsonb_build_object('personal_code', personals.personal_code, 'id',personals.id)),
                jsonb_build_object('title', teachings.title, 'color', teachings.color, 'id', teachings.id),
                TO_CHAR(starttime, 'yyyy-mm-dd"T"HH24:MI'), TO_CHAR(endtime, 'yyyy-mm-dd"T"HH24:MI'), json_agg(DISTINCT jsonb_build_object('code', rooms.code, 'id', rooms.id)),
                json_agg(DISTINCT jsonb_build_object('name', subgroups.name, 'id', subgroups.id, 'department', departments.name, 'promotion', university.groups.promotion, 'group_id', groups.id))
                
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

                WHERE university.courses.id  IN (""" +  str(values) + """)
                GROUP BY courses.id, courses.description, course_type, teachings.title, teachings.color, teachings.id, courses.starttime, courses.endtime"""
        
        return self.execute_query_and_get_statement_timetable(query)

    
    # ----------------------------------------------------------
    # Copy courses
    # ----------------------------------------------------------

    def copy_courses_by_day(self, data):
        promotion = data.get('promotion', '')
        department_id = data.get('department_id', '')
        day_to_copy = data.get('day_to_copy', '')
        day_to_paste = data.get('day_to_paste', '')

        if promotion == '' or department_id == '' or day_to_copy == '' or day_to_paste == '':
            return

        day_to_copy = datetime.datetime.strptime(day_to_copy,"%Y-%m-%d")
        nextday_to_copy = day_to_copy + datetime.timedelta(days=1)

        # Query the courses
        rows = db.session.query(
            Course.description,
            Course.starttime,
            Course.endtime,
            Course.course_type,
            Course.teaching_id,
            Course.id.label('course_id'),
            Participates.subgroup_id,
            Subgroup.name,
            Group.id.label('group_id'),
            Group.promotion,
            Group.type,
            Group.department_id
        ).join(
            Participates, Course.id == Participates.course_id
        ).join(
            Subgroup, Participates.subgroup_id == Subgroup.id
        ).join(
            Group, Subgroup.group_id == Group.id
        ).filter(
            and_(
                Group.promotion == promotion,
                Group.department_id == department_id,
                cast(Course.starttime, Date) >= day_to_copy,
                cast(Course.starttime, Date) < nextday_to_copy
            )
        ).all()

        if not rows:
            return {}

        day_to_paste = datetime.datetime.strptime(day_to_paste, '%Y-%m-%d')
        try:
            for row in rows:
                # Calculate the new start and end times
                new_starttime = datetime.datetime.combine(day_to_paste, row.starttime.time())
                new_endtime = datetime.datetime.combine(day_to_paste, row.endtime.time())

                # Create the new course
                new_course = Course(
                    description=row.description,
                    starttime=new_starttime,
                    endtime=new_endtime,
                    course_type=row.course_type,
                    teaching_id=row.teaching_id
                )

                # Add the new course to the session
                db.session.add(new_course)
                db.session.flush()

                # Copy personals
                personals = db.session.query(Personal).join(PersonalsCourses).filter(PersonalsCourses.course_id == row.course_id).all()
                for personal in personals:
                    new_personals_courses = PersonalsCourses(course_id=new_course.id, personal_id=personal.id)
                    db.session.add(new_personals_courses)

                # Copy rooms
                rooms = db.session.query(Room).join(RoomsCourses).filter(RoomsCourses.course_id == row.course_id).all()
                for room in rooms:
                    new_rooms_courses = RoomsCourses(course_id=new_course.id, rooms_id=room.id)
                    db.session.add(new_rooms_courses)

                # Copy participants
                participants = db.session.query(Participates).filter(Participates.course_id == row.course_id).all()
                for participant in participants:
                    new_participant = Participates(course_id=new_course.id, subgroup_id=participant.subgroup_id)
                    db.session.add(new_participant)

                db.session.commit()
                return {'message': f'Course {new_course.id} successfully added!'}, 200
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500 
        finally:
            db.session.close()

    # Must be monday
    def copy_courses_by_week(self, data):
        promotion = data.get('promotion', '')
        department_id = data.get('department_id', '')
        week_to_copy_start = data.get('week_to_copy_start', '')
        week_to_paste_start = data.get('week_to_paste_start', '')

        if promotion == '' or department_id == '' or week_to_copy_start == '' or week_to_paste_start == '':
            return

        week_to_copy_start = datetime.datetime.strptime(week_to_copy_start,"%Y-%m-%d")
        week_to_copy_end = week_to_copy_start + datetime.timedelta(days=7)

        week_to_paste_start = datetime.datetime.strptime(week_to_paste_start, '%Y-%m-%d')

        # Query the courses
        rows = db.session.query(
            Course.description,
            Course.starttime,
            Course.endtime,
            Course.course_type,
            Course.teaching_id,
            Course.id.label('course_id'),
            Participates.subgroup_id,
            Subgroup.name,
            Group.id.label('group_id'),
            Group.promotion,
            Group.type,
            Group.department_id
        ).join(
            Participates, Course.id == Participates.course_id
        ).join(
            Subgroup, Participates.subgroup_id == Subgroup.id
        ).join(
            Group, Subgroup.group_id == Group.id
        ).filter(
            and_(
                Group.promotion == promotion,
                Group.department_id == department_id,
                cast(Course.starttime, Date) >= week_to_copy_start,
                cast(Course.starttime, Date) < week_to_copy_end
            )
        ).all()

        if not rows:
            return {}

        try:
            for row in rows:
                # Calculate the new start and end times
                days_difference = (row.starttime.date() - week_to_copy_start.date()).days
                new_starttime = datetime.datetime.combine(week_to_paste_start + datetime.timedelta(days=days_difference), row.starttime.time())
                new_endtime = datetime.datetime.combine(week_to_paste_start + datetime.timedelta(days=days_difference), row.endtime.time())

                # Create the new course
                new_course = Course(
                    description=row.description,
                    starttime=new_starttime,
                    endtime=new_endtime,
                    course_type=row.course_type,
                    teaching_id=row.teaching_id
                )

                # Add the new course to the session
                db.session.add(new_course)
                db.session.flush()

                # Copy personals
                personals = db.session.query(Personal).join(PersonalsCourses).filter(PersonalsCourses.course_id == row.course_id).all()
                for personal in personals:
                    new_personals_courses = PersonalsCourses(course_id=new_course.id, personal_id=personal.id)
                    db.session.add(new_personals_courses)

                # Copy rooms
                rooms = db.session.query(Room).join(RoomsCourses).filter(RoomsCourses.course_id == row.course_id).all()
                for room in rooms:
                    new_rooms_courses = RoomsCourses(course_id=new_course.id, rooms_id=room.id)
                    db.session.add(new_rooms_courses)

                # Copy participants
                participants = db.session.query(Participates).filter(Participates.course_id == row.course_id).all()
                for participant in participants:
                    new_participant = Participates(course_id=new_course.id, subgroup_id=participant.subgroup_id)
                    db.session.add(new_participant)

                db.session.commit()
                return {'message': f'Course {new_course.id} successfully added!'}, 200
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500 
        finally:
            db.session.close()
            
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

            if 'subgroups' in data:
                # Delete existing subgroup-course relationships for this course
                Participates.query.filter(Participates.course_id == id).delete()

                # Create new subgroup-course relationships
                for subgroup in data['subgroups']:
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

    def student_or_personal(self, data): 
        username = data.get('username', '') 

        if username == '':
            return {'error': 'Null arguments'}

        query = """SELECT 
            CASE 
                WHEN students.id IS NOT NULL THEN 'student'
                WHEN personals.id IS NOT NULL THEN 'personal'
                ELSE 'unknown'
            END as user_type,
            COALESCE(students.id, personals.id) as id
        FROM 
            university.users
        LEFT JOIN 
            university.students ON users.id = students.user_id
        LEFT JOIN 
            university.personals ON users.id = personals.user_id
        WHERE 
            users.username = '""" + username + """';"""
        
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        print(rows)
        if not rows:
            return None
        elif rows[0][0] == 'student':
            data.update({'student_id': rows[0][1]})
            return self.get_timetable_by_student(data)
        elif rows[0][0] == 'personal':
            data.update({'personal_id': rows[0][1]})
            return self.get_timetable_by_teacher(data)
    
    def execute_subquery_and_get_statement(self,query):
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        if not rows:
            return None
       
        values = [str(t[0]) for t in rows]
        return ', '.join(values)
    
    def execute_query_and_get_statement(self, query):
            conn = self.get_connection()
            rows = connect_pg.get_query(conn, query)
            if not rows:
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
    
    #@todo: filter at the level of the query ?
    #@todo: use sqlalchemy on the whole class to avoid using this function
    def filter_none(self, value):
        if isinstance(value, dict):
            new_dict = {k: self.filter_none(v) for k, v in value.items() if v is not None}
            return new_dict if new_dict else None
        elif isinstance(value, list):
            new_list = [self.filter_none(v) for v in value]
            return new_list if any(new_list) else None
        else:
            return value
     
    def get_course_statement_timetable(self, row):
        course_data = {
            'id': row[0],              
            'description': row[1],
            'course_type': row[2],
            'personals': self.filter_none(row[3]), 
            'teaching': self.filter_none(row[4]),  
            'starttime': row[5],        
            'endtime':  row[6],        
            'rooms':  self.filter_none(row[7]),       
            'subgroups': self.filter_none(row[8])
        }
        return {k: v for k, v in course_data.items() if v is not None}
