-- \echo [INFO] Start of script Insertion for SAE 1.0
-- SOURCE script_university_delete.sql; -- or \i delete.sql; for some databases
-- psql -U university_admin -d university

/* Script contain create for each table
    -- departments(@id, name, description, department_type)
    -- groups(@id, promotion, type, #department_id)
    -- subgroups(@id, name, #group_id)
    -- personals(@id, last_name, first_name, mail, phone_number)
    -- specializations(@id, code, name, #department_id)
    -- rooms(@id, code, capacity, has_computer, has_projector)
    -- teachings(@id, title, hour_number, semestre, sequence, description, teaching_type, #specialization_id)
    -- roles(@id, name, description, #personal_id)
    -- courses(@id, description, starttime, duree, course_type, #personal_id, #rooms_id, #teaching_id)
    -- students(@studentNumber, last_name, first_name, mail, phone_number, #department_id, #group_id, #subgroup_id)
    -- responsibles(@id, #personal_id, #resource_id)
    -- reminders(@id, name, description, #course_id)
    -- absents(@id, justified, #student_number, #course_id)
    -- participates(@id, #course_id, #subgroup_id)
*/

/* Script has insert for table
    -- departments(@id, name, description, department_type)
    -- groups(@id, promotion, type, #department_id)
    -- subgroups(@id, name, #group_id)
    -- personals(@id, last_name, first_name, mail, phone_number)
    -- specializations(@id, code, name, #department_id)
    -- rooms(@id, code, capacity, has_computer, has_projector)
    -- teachings(@id, title, hour_number, semestre, sequence, description, teaching_type, #specialization_id)
    -- roles(@id, name, description, #personal_id)
    -- students(@studentNumber, last_name, first_name, mail, phone_number, #department_id, #group_id, #subgroup_id)
   
*/

/* Script has no insert for table
    -- courses(@id, description, starttime, duree, course_type, #personal_id, #rooms_id, #teaching_id)
    -- responsibles(@id, #personal_id, #resource_id)
    -- reminders(@id, name, description, #course_id)
    -- absents(@id, justified, #student_number, #course_id)
    -- participates(@id, #course_id, #subgroup_id)
*/

/*  Need a connection to a SUPERUSER (maybe postgres)
    DROP DATABASE IF EXISTS university;
    CREATE DATABASE university;
    DROP USER IF EXISTS university_admin;
    CREATE USER university_admin WITH PASSWORD 'password';
    GRANT ALL PRIVILEGES ON DATABASE university TO university_admin;
    GRANT USAGE ON SCHEMA public TO university_admin;
    GRANT CREATE ON SCHEMA public TO university_admin;
    ALTER USER university_admin WITH SUPERUSER;

    Then
    -- psql -U university_admin -d university
    Password for user university_admin: password
    url : jdbc:postgresql://localhost:5432/university

*/


-- \echo '\nStart of create UNIVERSITY database\n' -- Start of create UNIVERSITY database
\i script_university_create.sql;
-- \echo '\nend of create UNIVERSITY database\n' -- End of create UNIVERSITY database

-- \echo '\nStart of insert UNIVERSITY database (design for montreuil)\n' --Start of insert UNIVERSITY database (design for montreuil)
\i script_university_school_insert.sql;
-- \echo '\nend of insert UNIVERSITY database\n' -- End of insert UNIVERSITY database

-- \echo '\nStart of insert UNIVERSITY student in database (design for montreuil)\n' -- Start of insert UNIVERSITY student in database (design for montreuil)
\i script_university_student_insert.sql;
-- \echo '\nEnd of insert UNIVERSITY student in database\n' -- End of insert UNIVERSITY student in database
