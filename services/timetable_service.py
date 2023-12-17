from services.main_service import Service

from configuration import connect_pg
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
                    INNER JOIN university.teachings ON courses.teaching_id = teachings.id
                    INNER JOIN university.personals ON courses.personal_id = personals.id
                    INNER JOIN university.rooms ON courses.rooms_id = rooms.id
                    WHERE rooms.id =""" +  str(room_id) + """ AND
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
                    INNER JOIN university.teachings ON courses.teaching_id = teachings.id
                    INNER JOIN university.personals ON courses.personal_id = personals.id
                    INNER JOIN university.rooms ON courses.rooms_id = rooms.id
                    WHERE personals.id =""" +  str(personnal_id) + """ AND
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

                INNER JOIN university.personals ON courses.personal_id = personals.id
                INNER JOIN university.teachings ON courses.teaching_id = teachings.id
                INNER JOIN university.rooms ON courses.rooms_id = rooms.id

                INNER JOIN university.participates ON courses.id = participates.course_id
                INNER JOIN university.subgroups ON participates.subgroup_id = subgroups.id
                INNER JOIN university.groups ON subgroups.id = groups.id

                WHERE groups.promotion =""" +  str(promotion_id) + """ AND
                groups.department_id =""" + str(department_id) + """ AND
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

                INNER JOIN university.personals ON courses.personal_id = personals.id
                INNER JOIN university.teachings ON courses.teaching_id = teachings.id
                INNER JOIN university.rooms ON courses.rooms_id = rooms.id

                INNER JOIN university.participates ON courses.id = participates.course_id
                INNER JOIN university.students ON participates.subgroup_id = students.subgroup_id

                WHERE students.student_number = '""" +  str(student_id) + """' AND
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
            'description': row[0],    # juste une description
            'course_type': row[1],   # Type de cours, Contrôle, Tp, Td, Cours normal/amphi
            'personal_code': row[2],
            'teaching_title': row[3],      # r1-01 développement web, sae, c'est les ressources
            'starttime': row[4],         # Le nom de famille de l'étudiant
            'endtime':  row[5],        # Le prénom de l'étudiant
            'room_name':  row[6]
        }