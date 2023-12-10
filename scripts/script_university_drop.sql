
/* Script contain drop for each table
    -- departments(@id, name, description, department_type)
    -- groups(@id, promotion, type, #department_id)
    -- subgroups(@id, name, #group_id)
    -- personals(@id, last_name, first_name, mail, phone_number)
    -- specializations(@id, code, name, #department_id)
    -- rooms(@id, code, capacity, has_computer, has_projector)
    -- teachings(@id, title, hour_number, semestre, sequence, description, teaching_type, #specialization_id)
    -- roles(@id, name, description, #personal_id)
    -- courses(@id, description, starttime, duree, course_type, #personal_id, #rooms_id, #teaching_id)
    -- students(@student_number, last_name, first_name, mail, phone_number, #department_id, #group_id, #subgroup_id)
    -- responsibles(@id, #personal_id, #resource_id)
    -- reminders(@id, name, description, #course_id)
    -- absents(@id, justified, #student_number, #course_id)
    -- participates(@id, #course_id, #subgroup_id)
*/

-- DROP TABLE IF EXISTS absents CASCADE ;
-- DROP TABLE IF EXISTS participates CASCADE ;
-- DROP TABLE IF EXISTS responsibles CASCADE ;
-- DROP TABLE IF EXISTS reminders CASCADE ;
-- DROP TABLE IF EXISTS courses CASCADE ;
-- DROP TABLE IF EXISTS rooms CASCADE ;
-- DROP TABLE IF EXISTS teachings CASCADE ;
-- DROP TABLE IF EXISTS students CASCADE ;
-- DROP TABLE IF EXISTS subgroups CASCADE ;
-- DROP TABLE IF EXISTS groups CASCADE ;
-- DROP TABLE IF EXISTS roles CASCADE ;
-- DROP TABLE IF EXISTS specializations CASCADE ;
-- DROP TABLE IF EXISTS departments CASCADE ;
-- DROP TABLE IF EXISTS personals CASCADE ;

drop table if exists roles cascade;

drop table if exists reminders cascade;

drop table if exists absents cascade;

drop table if exists students cascade;

drop table if exists participates cascade;

drop table if exists subgroups cascade;

drop table if exists groups cascade;

drop table if exists courses cascade;

drop table if exists rooms cascade;

drop table if exists responsibles cascade;

drop table if exists teachings cascade;

drop table if exists specializations cascade;

drop table if exists departments cascade;

drop table if exists personals cascade;

drop table if exists users cascade;