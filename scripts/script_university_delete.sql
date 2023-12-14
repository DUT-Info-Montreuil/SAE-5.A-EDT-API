-- Delete all records from university.absents
DELETE FROM university.absents;
-- Delete all records from university.participates
DELETE FROM university.participates;
-- Delete all records from university.responsibles
DELETE FROM university.responsibles;
-- Delete all records from university.reminders
DELETE FROM university.reminders;
-- Delete all records from university.courses
DELETE FROM university.courses;
-- Delete all records from university.rooms
DELETE FROM university.rooms;
-- Delete all records from university.
DELETE FROM university.teachings;
-- Delete all records from university.students
DELETE FROM university.students;
-- Delete all records from university.subgroups
DELETE FROM university.subgroups;
-- Delete all records from university.groups
DELETE FROM university.groups;
-- Delete all records from university.roles
DELETE FROM university.roles;
-- Delete all records from university.specializations
DELETE FROM university.specializations;
-- Delete all records from university.departments
DELETE FROM university.departments;
-- Delete all records from university.personals
DELETE FROM university.personals;

-- ALTER SEQUENCE university_students_id_seq RESTART WITH 1;
ALTER SEQUENCE university_departments_id_seq RESTART WITH 1;
ALTER SEQUENCE university_groups_id_seq RESTART WITH 1;
ALTER SEQUENCE university_subgroups_id_seq RESTART WITH 1;
ALTER SEQUENCE university_personals_id_seq RESTART WITH 1;
ALTER SEQUENCE university_roles_id_seq RESTART WITH 1;
ALTER SEQUENCE university_courses_id_seq RESTART WITH 1;
ALTER SEQUENCE university_rooms_id_seq RESTART WITH 1;
ALTER SEQUENCE university_teachings_id_seq RESTART WITH 1;
ALTER SEQUENCE university_specializations_id_seq RESTART WITH 1;
ALTER SEQUENCE university_reminders_id_seq RESTART WITH 1;
ALTER SEQUENCE university_absents_id_seq RESTART WITH 1;
ALTER SEQUENCE university_participates_id_seq RESTART WITH 1;
ALTER SEQUENCE university_responsibles_id_seq RESTART WITH 1;

