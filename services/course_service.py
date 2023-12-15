from flask import jsonify
from services.main_service import Service
import connect_pg
from datetime import timedelta
import datetime 

class course_service(Service):
    
    # university.courses(@id, description, starttime, endtime, course_type, #personal_id, #rooms_id, #teaching_id)
    
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

        query = """SELECT courses.description, course_type, personals.personal_code, teachings.title, TO_CHAR(starttime, 'yyyy-mm-dd"T"HH24:MI'), TO_CHAR(endtime, 'yyyy-mm-dd"T"HH24:MI'), rooms.code 
                    FROM university.courses 
                    INNER JOIN university.teachings ON university.courses.teaching_id = university.teachings.id
                    INNER JOIN university.personals ON university.courses.personal_id = university.personals.id
                    INNER JOIN university.rooms ON university.courses.rooms_id = university.rooms.id
                    WHERE university.rooms.id =""" +  str(room_id) + """ AND
                    starttime >= '""" + str(week_date_start) + """' AND starttime <= '""" + str(week_date_end) + """'"""
        return self.execute_query_and_get_statement_timetable(query)
    
    def get_timetable_by_teacher(self, data):
        personal_id = data.get('personal_id', '')
        week_date_start = data.get('week_date_start', '')
        week_date_end = data.get('week_date_end', '')

        if personal_id == '' or week_date_start == '' or week_date_end == '':
            return "Null arguments"

        week_date_start = datetime.datetime.strptime(week_date_start,"%Y-%m-%d")
        week_date_end = datetime.datetime.strptime(week_date_end,"%Y-%m-%d")

        query = """SELECT courses.description, course_type, personals.personal_code, teachings.title, TO_CHAR(starttime, 'yyyy-mm-dd"T"HH24:MI'), TO_CHAR(endtime, 'yyyy-mm-dd"T"HH24:MI'), rooms.code 
                    FROM university.courses 
                    INNER JOIN university.teachings ON university.courses.teaching_id = university.teachings.id
                    INNER JOIN university.personals ON university.courses.personal_id = university.personals.id
                    INNER JOIN university.rooms ON university.courses.rooms_id = university.rooms.id
                    WHERE university.personals.id =""" +  str(personal_id) + """ AND
                    starttime >= '""" + str(week_date_start) + """' AND starttime <= '""" + str(week_date_end) + """'"""
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

        query = """SELECT courses.description, course_type, personals.personal_code, teachings.title, TO_CHAR(starttime, 'yyyy-mm-dd"T"HH24:MI'), TO_CHAR(endtime, 'yyyy-mm-dd"T"HH24:MI'), rooms.code
                FROM university.courses

                INNER JOIN university.personals ON university.courses.personal_id = university.personals.id
                INNER JOIN university.teachings ON university.courses.teaching_id = university.teachings.id
                INNER JOIN university.rooms ON university.courses.rooms_id = university.rooms.id

                INNER JOIN university.participates ON university.courses.id = university.participates.course_id
                INNER JOIN university.subgroups ON university.participates.subgroup_id = university.subgroups.id
                INNER JOIN university.groups ON university.subgroups.id = university.groups.id

                WHERE university.groups.promotion =""" +  str(promotion) + """ AND
                university.groups.department_id =""" + str(department_id) + """ AND
                starttime >= '""" + str(week_date_start) + """' AND starttime <= '""" + str(week_date_end) + """'"""

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

        query = """SELECT courses.description, course_type, personals.personal_code, teachings.title, TO_CHAR(starttime, 'yyyy-mm-dd"T"HH24:MI'), TO_CHAR(endtime, 'yyyy-mm-dd"T"HH24:MI'), rooms.code
                FROM university.courses

                INNER JOIN university.personals ON university.courses.personal_id = university.personals.id
                INNER JOIN university.teachings ON university.courses.teaching_id = university.teachings.id
                INNER JOIN university.rooms ON university.courses.rooms_id = university.rooms.id

                INNER JOIN university.participates ON university.courses.id = university.participates.course_id
                INNER JOIN university.students ON university.participates.subgroup_id = university.students.subgroup_id

                WHERE university.students.student_number = '""" +  str(student_id) + """' AND
                starttime >= '""" + str(week_date_start) + """' AND starttime <= '""" + str(week_date_end) + """'"""
        print(query)
        return self.execute_query_and_get_statement(query)
    
    # ----------------------------------------------------------
    # Add / Delete / Update
    # ----------------------------------------------------------

    def add_course(self, data):
        description = data.get('description', '')
        starttime = data.get('starttime', '')
        endtime = data.get('endtime', '')
        course_type = data.get('course_type', '')
        personal_id = data.get('personal_id', '')
        rooms_id = data.get('rooms_id', '')
        teaching_id = data.get('teaching_id', '')

        if description == '' or starttime == '' or endtime == '' or course_type == '' or personal_id == '' or rooms_id == '' or teaching_id == '':
            return {}
    
        query = """INSERT INTO university.courses (description, starttime, endtime, course_type, personal_id, rooms_id, teaching_id) 
                VALUES ('%(description)s', '%(starttime)s', '%(duree)s', '%(course_type)s', %(personal_id)s, %(rooms_id)s, %(teaching_id)s)"""
    
        conn = self.get_connection()
        new_course_id = connect_pg.execute_commands(conn, (query,))
        connect_pg.disconnect(conn)
    
        return new_course_id
        # print(data)
        # return "slt"
    
    def delete_course_by_id(self, id):
        """ Delete a course by ID in JSON format """
        query = "DELETE FROM university.courses WHERE id = %(id)s RETURNING id" %  {'id': id}
        conn = self.get_connection()
        row = connect_pg.execute_commands(conn, (query,))
        connect_pg.disconnect(conn)
        return row
    
    def update_course(self, id, data):
        sub_query = ''
        description = data.get('description', '')
        starttime = data.get('starttime', '')
        endtime = data.get('endtime', '')
        course_type = data.get('course_type', '')
        personal_id = data.get('personal_id', '')
        rooms_id = data.get('rooms_id', '')
        teaching_id = data.get('teaching_id', '')

        if description != '':
            sub_query = sub_query + """description = '""" + str(description) + """' """
        if starttime != '':
            sub_query = sub_query + """starttime = TO_CHAR('""" + str(starttime) + """', 'yyyy-mm-dd"T"HH24:MI') """
        if endtime != '':
            sub_query = sub_query + """endtime = TO_CHAR('""" + str(endtime) + """', 'yyyy-mm-dd"T"HH24:MI') """
        if course_type != '':
            sub_query = sub_query + """course_type = '""" + str(course_type) + """' """
        if personal_id != '':
            sub_query = sub_query + """personal_id = """ + str(personal_id) + """ """
        if rooms_id != '':
            sub_query = sub_query + """rooms_id = """ + str(rooms_id) + """ """
        if teaching_id != '':
            sub_query = sub_query + """teaching_id = """ + str(teaching_id) + """ """
       
        if sub_query == '':
            return jsonify({"message": "Invalid arguments"}), 403
        
        query = """UPDATE university.courses SET """ + sub_query + """ WHERE id = """ + str(id)
        try:
            conn = self.get_connection()
            connect_pg.execute_commands(conn, (query,))
            connect_pg.disconnect(conn)
            return jsonify({"message": "Course " + str(id) + " updated sucessfully"}), 200
        except Exception as e:
            return  jsonify({"message": e}), 400
        

        return True

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
            'personal_id': row[5],     # L'ID du personnel associé au cours
            'rooms_id': row[6],        # L'ID de la salle associée au cours
            'teaching_id': row[7]      # L'ID de l'enseignement associé au cours
        }
    
    def get_course_statement_timetable(self, row):
        return {
            'description': row[0],
            'course_type': row[1],
            'personal_code': row[2],   # Nom abrégé du professeur
            'teaching_title': row[3],  # Nom de la matière    
            'starttime': row[4],        
            'endtime':  row[5],        
            'room_name':  row[6]       # Nom de la salle
        }