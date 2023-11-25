from services.main_service import Service

import connect_pg
import datetime 

class timetable_service(Service):

    #@todo invalid date exception, + rajouter exception au contrat
    def get_timetable_by_room(self, data):
        room_name = data.get('room_name', '')
        week_date = data.get('week_date', '') #needs to be monday

        if room_name == '' or week_date == '':
            return "Null arguments"
            
        query = "SELECT id FROM university.rooms WHERE code = '" + str(room_name) + "'"
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)

        if len(rows) == 0: 
            return "Room does not exist"

        room_id = rows[0][0]

        monday = datetime.datetime.strptime(week_date,"%Y-%m-%d")
        friday = monday + datetime.timedelta(days=5)

        query = """SELECT courses.description, course_type, personals.last_name, personals.first_name, teachings.title, TO_CHAR(starttime, 'yyyy-mm-dd HH24:MI:SS'), duree 
                    FROM university.courses 
                    INNER JOIN university.teachings ON university.courses.teaching_id = university.teachings.id
                    INNER JOIN university.personals ON university.courses.personal_id = university.personals.id
                    WHERE rooms_id =""" +  str(room_id) + """ AND
                    starttime >= '""" + str(monday) + """' AND starttime <= '""" + str(friday) + """'"""
        print(query)
        #utiliser model?
        rows = connect_pg.get_query(conn, query)
        returnStatement = []
        for row in rows:
            row = row + (room_name,)
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