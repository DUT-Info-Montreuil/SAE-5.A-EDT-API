from flask import jsonify
from services.main_service import Service

import connect_pg
from datetime import timedelta

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
    
    #Get stat of a teacher
    # TO DO: Changer de classe ?????
    def identify_course(self, id):
        """Identify a course by description, starttime, duree, course_type, personal_id, and rooms_id in JSON format"""
        # data = request.json
        #Rajouter condition, matière toussa
        query = "SELECT SUM(endtime-starttime) FROM university.courses WHERE personal_id = " + str(id)
        print(query)
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        if rows[0][0] is None:
            return {}
        connect_pg.disconnect(conn)
        return { "temps": rows[0][0].total_seconds()  / 60 }
    
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
        if description != '':
            sub_query = sub_query + """description = '""" + str(description) + """' """
        # @TO-DO: add other attributes
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