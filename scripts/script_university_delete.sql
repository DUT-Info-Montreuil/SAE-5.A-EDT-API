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
-- Delete all records from university.resource
-- DELETE FROM university.resource;
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

ALTER SEQUENCE university.students_id_seq RESTART WITH 1;
ALTER SEQUENCE university.departments_id_seq RESTART WITH 1;
ALTER SEQUENCE university.groups_id_seq RESTART WITH 1;
ALTER SEQUENCE university.subgroups_id_seq RESTART WITH 1;
ALTER SEQUENCE university.personals_id_seq RESTART WITH 1;
ALTER SEQUENCE university.roles_id_seq RESTART WITH 1;
ALTER SEQUENCE university.courses_id_seq RESTART WITH 1;
ALTER SEQUENCE university.rooms_id_seq RESTART WITH 1;
ALTER SEQUENCE university.teachings_id_seq RESTART WITH 1;
ALTER SEQUENCE university.specializations_id_seq RESTART WITH 1;
ALTER SEQUENCE university.reminders_id_seq RESTART WITH 1;
ALTER SEQUENCE university.absents_id_seq RESTART WITH 1;
ALTER SEQUENCE university.participates_id_seq RESTART WITH 1;
ALTER SEQUENCE university.responsibles_id_seq RESTART WITH 1;

