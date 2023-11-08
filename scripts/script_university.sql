-- \echo [INFO] Start of script Insertion for SAE 1.0
-- SOURCE script_university_delete.sql; -- or \i delete.sql; for some databases

/* Script contain create for each table
    -- university.personals(@id, last_name, first_name, mail, phone_number)
    -- university.roles(@id, name, description, personal_id)
    -- university.departments(@id, name, description, department_type)
    -- university.groups(@id, promotion, type, #department_id)
    -- university.subgroups(@id, name, #group_id)
    -- university.rooms(@id, code, capacity, has_computer, has_projector)
    -- university.specializations(@id, code, name, #department_id)
    -- university.courses(@id, description, starttime, duree, course_type, #personal_id, #rooms_id, #teaching_id)
    -- university.responsibles(@id, #personal_id, #resource_id)
    -- university.reminders(@id, name, description, #course_id)
    -- university.absents(@id, justified, #student_id, #course_id)
    -- university.participates(@id, #course_id, #subgroup_id)
*/

/* Script has insert for table
    -- university.courses(@id, description, starttime, duree, course_type, #personal_id, #rooms_id, #teaching_id)
    -- university.responsibles(@id, #personal_id, #resource_id)
    -- university.reminders(@id, name, description, #course_id)
    -- university.absents(@id, justified, #student_id, #course_id)
    -- university.participates(@id, #course_id, #subgroup_id)
*/

/* Script has no insert for table
    -- university.courses(@id, description, starttime, duree, course_type, #personal_id, #rooms_id, #teaching_id)
    -- university.responsibles(@id, #personal_id, #resource_id)
    -- university.reminders(@id, name, description, #course_id)
    -- university.absents(@id, justified, #student_id, #course_id)
    -- university.participates(@id, #course_id, #subgroup_id)
*/
DROP DATABASE IF EXISTS university;
CREATE DATABASE university;
DROP USER IF EXISTS university_admin;
CREATE USER university_admin WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE university TO university_admin;


\echo 'Start of create UNIVERSITY database'; -- Start of create UNIVERSITY database
\i script_university_school_create.sql;
\echo 'end of create UNIVERSITY database'; -- End of create UNIVERSITY database

\echo 'Start of insert UNIVERSITY database (design for montreuil)'; --Start of insert UNIVERSITY database (design for montreuil)
\i script_university_school_insert.sql;
\echo 'end of insert UNIVERSITY database'; -- End of insert UNIVERSITY database

\echo 'Start of insert UNIVERSITY student in database (design for montreuil)'; -- Start of insert UNIVERSITY student in database (design for montreuil)
\i script_university_student_insertsql;
\echo 'End of insert UNIVERSITY student in database'; -- End of insert UNIVERSITY student in database
