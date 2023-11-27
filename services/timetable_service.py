from services.main_service import Service

import connect_pg
import datetime 

class timetable_service(Service):

    #@todo invalid date exception, + rajouter exception au contrat
    def get_timetable_by_room(self, data):
        room_name = data.get('room_name', '')
        week_date_start = data.get('week_date_start', '')
        week_date_end = data.get('week_date_end', '')

        if room_name == '' or week_date_start == '' or week_date_end == '':
            return "Null arguments"
            
        query = "SELECT id FROM university.rooms WHERE code = '" + str(room_name) + "'"
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)

        if len(rows) == 0: 
            return "Room does not exist"

        room_id = rows[0][0]

        week_date_start = datetime.datetime.strptime(week_date_start,"%Y-%m-%d")
        week_date_end = datetime.datetime.strptime(week_date_end,"%Y-%m-%d")

        query = """SELECT courses.description, course_type, personals.last_name, personals.first_name, teachings.title, TO_CHAR(starttime, 'yyyy-mm-dd HH24:MI:SS'), duree 
                    FROM university.courses 
                    INNER JOIN university.teachings ON university.courses.teaching_id = university.teachings.id
                    INNER JOIN university.personals ON university.courses.personal_id = university.personals.id
                    WHERE rooms_id =""" +  str(room_id) + """ AND
                    starttime >= '""" + str(week_date_start) + """' AND starttime <= '""" + str(week_date_end) + """'"""
        #utiliser model?
        rows = connect_pg.get_query(conn, query)
        returnStatement = []
        for row in rows:
            row = row + (room_name,)
            returnStatement.append(self.get_student_statement(row))
        connect_pg.disconnect(conn)
        return returnStatement
    
    def get_timetable_by_teacher(self, data):
        # rajouter try catch si teacher n'existe pas
        personnal_id = data.get('personnal_id', '')
        week_date_start = data.get('week_date_start', '')
        week_date_end = data.get('week_date_end', '')

        if personnal_id == '' or week_date_start == '' or week_date_end == '':
            return "Null arguments"
        

        week_date_start = datetime.datetime.strptime(week_date_start,"%Y-%m-%d")
        week_date_end = datetime.datetime.strptime(week_date_end,"%Y-%m-%d")

        query = """SELECT courses.description, course_type, personals.last_name, personals.first_name, teachings.title, TO_CHAR(starttime, 'yyyy-mm-dd HH24:MI:SS'), duree, rooms.code 
                    FROM university.courses 
                    INNER JOIN university.teachings ON university.courses.teaching_id = university.teachings.id
                    INNER JOIN university.personals ON university.courses.personal_id = university.personals.id
                    INNER JOIN university.rooms ON university.courses.rooms_id = university.rooms.id
                    WHERE university.personals.id =""" +  str(personnal_id) + """ AND
                    starttime >= '""" + str(week_date_start) + """' AND starttime <= '""" + str(week_date_end) + """'"""
        print(query)

        #utiliser model?
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)

        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_student_statement(row))
        connect_pg.disconnect(conn)
        return returnStatement
    
    def get_timetable_by_prom(self, data):
        # rajouter try catch si teacher n'existe pas
        promotion_id = data.get('promotion_id', '')
        department_id = data.get('department_id', '')
        week_date_start = data.get('week_date_start', '')
        week_date_end = data.get('week_date_end', '')

        if promotion_id == '' or department_id == '' or week_date_start == '' or week_date_end == '':
            return "Null arguments"
        

        week_date_start = datetime.datetime.strptime(week_date_start,"%Y-%m-%d")
        week_date_end = datetime.datetime.strptime(week_date_end,"%Y-%m-%d")

        query = """SELECT courses.description, course_type, personals.last_name, personals.first_name, teachings.title, TO_CHAR(starttime, 'yyyy-mm-dd HH24:MI:SS'), duree, rooms.code
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
        print(query)

        #utiliser model?
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
            'personal_last_name': row[2],
            'personal_first_name': row[3],
            'teachings.title': row[4],      # r1-01 développement web, sae, c'est les ressources
            'starttime': row[5],         # Le nom de famille de l'étudiant
            'duree':  str(row[6]),        # Le prénom de l'étudiant
            'room_name':  row[7]
        }