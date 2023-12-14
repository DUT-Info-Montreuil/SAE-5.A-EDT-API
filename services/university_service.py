from services.main_service import Service

from configuration import connect_pg

class university_service(Service):
    def initialize_database(db):
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