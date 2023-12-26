
/* Script contain drop for each table
    -- university.departments(@id, name, description, department_type)
    -- university.groups(@id, promotion, type, #department_id)
    -- university.subgroups(@id, name, #group_id)
    -- university.personals(@id, last_name, first_name, mail, phone_number)
    -- university.specializations(@id, code, name, #department_id)
    -- university.rooms(@id, code, capacity, has_computer, has_projector)
    -- university.teachings(@id, title, hour_number, semestre, sequence, description, teaching_type, #specialization_id)
    -- university.roles(@id, name, description, #personal_id)
    -- university.courses(@id, description, starttime, duree, course_type, #personal_id, #rooms_id, #teaching_id)
    -- university.students(@student_number, last_name, first_name, mail, phone_number, #department_id, #group_id, #subgroup_id)
    -- university.responsibles(@id, #personal_id, #resource_id)
    -- university.reminders(@id, name, description, #course_id)
    -- university.absents(@id, justified, #student_number, #course_id)
    -- university.participates(@id, #course_id, #subgroup_id)
*/

-- DROP TABLE IF EXISTS university.absents CASCADE ;
-- DROP TABLE IF EXISTS university.participates CASCADE ;
-- DROP TABLE IF EXISTS university.responsibles CASCADE ;
-- DROP TABLE IF EXISTS university.reminders CASCADE ;
-- DROP TABLE IF EXISTS university.courses CASCADE ;
-- DROP TABLE IF EXISTS university.rooms CASCADE ;
-- DROP TABLE IF EXISTS university.teachings CASCADE ;
-- DROP TABLE IF EXISTS university.students CASCADE ;
-- DROP TABLE IF EXISTS university.subgroups CASCADE ;
-- DROP TABLE IF EXISTS university.groups CASCADE ;
-- DROP TABLE IF EXISTS university.roles CASCADE ;
-- DROP TABLE IF EXISTS university.specializations CASCADE ;
-- DROP TABLE IF EXISTS university.departments CASCADE ;
-- DROP TABLE IF EXISTS university.personals CASCADE ;

DROP SCHEMA IF EXISTS university cascade ;