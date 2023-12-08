from services.main_service import Service

import connect_pg
import datetime 

class timetable_service(Service):

    #@todo invalid date exception, + rajouter exception au contrat
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
        return self.execute_query_and_get_statement(query)

    
    def get_timetable_by_teacher(self, data):
        personnal_id = data.get('personnal_id', '')
        week_date_start = data.get('week_date_start', '')
        week_date_end = data.get('week_date_end', '')

        if personnal_id == '' or week_date_start == '' or week_date_end == '':
            return "Null arguments"

        week_date_start = datetime.datetime.strptime(week_date_start,"%Y-%m-%d")
        week_date_end = datetime.datetime.strptime(week_date_end,"%Y-%m-%d")

        query = """SELECT courses.description, course_type, personals.personal_code, teachings.title, TO_CHAR(starttime, 'yyyy-mm-dd"T"HH24:MI'), TO_CHAR(endtime, 'yyyy-mm-dd"T"HH24:MI'), rooms.code 

                    FROM university.courses 
                    INNER JOIN university.teachings ON university.courses.teaching_id = university.teachings.id
                    INNER JOIN university.personals ON university.courses.personal_id = university.personals.id
                    INNER JOIN university.rooms ON university.courses.rooms_id = university.rooms.id
                    WHERE university.personals.id =""" +  str(personnal_id) + """ AND
                    starttime >= '""" + str(week_date_start) + """' AND starttime <= '""" + str(week_date_end) + """'"""
        return self.execute_query_and_get_statement(query)
    
    def get_timetable_by_prom(self, data):
        promotion_id = data.get('promotion_id', '')
        department_id = data.get('department_id', '')
        week_date_start = data.get('week_date_start', '')
        week_date_end = data.get('week_date_end', '')

        if promotion_id == '' or department_id == '' or week_date_start == '' or week_date_end == '':
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

                WHERE university.groups.promotion =""" +  str(promotion_id) + """ AND
                university.groups.department_id =""" + str(department_id) + """ AND
                starttime >= '""" + str(week_date_start) + """' AND starttime <= '""" + str(week_date_end) + """'"""

        return self.execute_query_and_get_statement(query)

    def get_timetable_by_student(self, data):
        student_id = data.get('student_id', '')
        week_date_start = data.get('week_date_start', '')
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



    def execute_query_and_get_statement(self, query):
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)

        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_student_statement(row))
        connect_pg.disconnect(conn)
        return returnStatement

    def get_student_statement(self, row):
        return {
            'description': row[0],  
            'course_type': row[1],  
            'personal_code': row[2],
            'teaching_title': row[3],      
            'starttime': row[4],      
            'endttime':  row[5],       
            'room_name':  row[6]
        }