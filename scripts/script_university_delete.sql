-- Delete all records from absents
DELETE FROM absents;
-- Delete all records from participates
DELETE FROM participates;
-- Delete all records from responsibles
DELETE FROM responsibles;
-- Delete all records from reminders
DELETE FROM reminders;
-- Delete all records from courses
DELETE FROM courses;
-- Delete all records from rooms
DELETE FROM rooms;
-- Delete all records from 
DELETE FROM teachings;
-- Delete all records from students
DELETE FROM students;
-- Delete all records from subgroups
DELETE FROM subgroups;
-- Delete all records from groups
DELETE FROM groups;
-- Delete all records from roles
DELETE FROM roles;
-- Delete all records from specializations
DELETE FROM specializations;
-- Delete all records from departments
DELETE FROM departments;
-- Delete all records from personals
DELETE FROM personals;

-- ALTER SEQUENCE students_id_seq RESTART WITH 1;
ALTER SEQUENCE departments_id_seq RESTART WITH 1;
ALTER SEQUENCE groups_id_seq RESTART WITH 1;
ALTER SEQUENCE subgroups_id_seq RESTART WITH 1;
ALTER SEQUENCE personals_id_seq RESTART WITH 1;
ALTER SEQUENCE roles_id_seq RESTART WITH 1;
ALTER SEQUENCE courses_id_seq RESTART WITH 1;
ALTER SEQUENCE rooms_id_seq RESTART WITH 1;
ALTER SEQUENCE teachings_id_seq RESTART WITH 1;
ALTER SEQUENCE specializations_id_seq RESTART WITH 1;
ALTER SEQUENCE reminders_id_seq RESTART WITH 1;
ALTER SEQUENCE absents_id_seq RESTART WITH 1;
ALTER SEQUENCE participates_id_seq RESTART WITH 1;
ALTER SEQUENCE responsibles_id_seq RESTART WITH 1;

