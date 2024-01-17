DROP SCHEMA IF EXISTS university cascade ;
CREATE SCHEMA university;

DROP DOMAIN IF EXISTS numstudent CASCADE ;
CREATE DOMAIN numstudent as varchar(8) check (value ~* E'\\d{8}');

DROP DOMAIN IF EXISTS courses_types CASCADE ;
CREATE DOMAIN courses_types as varchar(32) check (value ~* '^(controles|TD|TP|cours|rattrapage|Projet)$');

DROP DOMAIN IF EXISTS roles_types CASCADE ;
CREATE DOMAIN roles_types as varchar(32) check (value ~* '^(TEACHER|TEACHER_RESPONSIBLE|ADMIN)$');

DROP DOMAIN IF EXISTS teachings_types CASCADE ;
CREATE DOMAIN teachings_types as varchar(32) check (value ~* '^(SAE|RT|RCC|Portfolio)$');

CREATE TABLE university.users(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_users PRIMARY KEY CONSTRAINT ck_university_users_id CHECK(id > 0),
    username varchar(64) UNIQUE NOT NULL,
    -- ATTRIBUTE
    password varchar(255) NOT NULL
) ;

CREATE TABLE university.students(
	-- PRIMARY KEY
    id SERIAL constraint pk_university_student PRIMARY KEY CONSTRAINT ck_university_student_id CHECK(id > 0),
    -- ATTRIBUTE
    last_name varchar(32) NOT NULL,
    first_name varchar(32) NOT NULL,
    -- FOREIGN KEY (users)
    user_id INT UNIQUE NOT NULL,
    -- FOREIGN KEY (departments)
    department_id INT NOT NULL,
    -- FOREIGN KEY (groups)
    group_id INT NOT NULL,
    -- FOREIGN KEY (subgroups)
    subgroup_id INT NOT NULL
) ;

CREATE TABLE university.departments(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_departments PRIMARY KEY CONSTRAINT ck_university_department_id CHECK(id > 0),
    -- ATTRIBUTE
	name varchar(32) NOT NULL UNIQUE,
	description varchar(128) ,
	degree_type VARCHAR(50) NOT NULL CHECK (degree_type IN ('Licence_PRO', 'BUT')),
    
    -- FOREIGN KEY (personals)
    personal_id INT NOT NULL
) ;


CREATE TABLE university.groups(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_groups PRIMARY KEY CONSTRAINT ck_university_group_id CHECK(id > 0),
    -- ATTRIBUTE
	promotion integer, -- 1st, 2nd or 3rd of school year
    type varchar(5) NOT NULL, --CHECK (type ~ '^[A-Z]+$' OR type = 'APP'), -- A,B,C... or APP

	-- FOREIGN KEY (departments)
    department_id INT NOT NULL
) ;


CREATE TABLE university.subgroups(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_subgroups PRIMARY KEY CONSTRAINT ck_university_subgroup_id CHECK(id > 0),
    -- ATTRIBUTE
	name varchar(16) NOT NULL,

	-- FOREIGN KEY (groups)
    group_id INT NOT NULL
) ;


CREATE TABLE university.personals(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_personals PRIMARY KEY CONSTRAINT ck_university_personal_id CHECK(id > 0),
    -- ATTRIBUTE
	last_name varchar(32) NOT NULL,
	first_name varchar(32) NOT NULL,
    personal_code varchar(16) UNIQUE NOT NULL,
    roles roles_types NOT NULL DEFAULT 'TEACHER',

    -- FOREIGN KEY (users)
    user_id integer UNIQUE NOT NULL
) ;

CREATE TABLE university.courses(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_courses PRIMARY KEY CONSTRAINT ck_university_course_id CHECK(id > 0),
    -- ATTRIBUTE
	description TEXT,
	startTime timestamp NOT NULL,
	endtime timestamp NOT NULL,
	course_type courses_types NOT NULL,
    -- FOREIGN KEY (teachings)
    teaching_id INT NOT NULL
) ;


CREATE TABLE university.rooms(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_rooms PRIMARY KEY CONSTRAINT ck_university_rooms_id CHECK(id > 0),
    -- ATTRIBUTE
	code varchar(32) NOT NULL UNIQUE,
	capacity INTEGER NOT NULL,
	has_computer boolean default true,
	has_projector boolean default true
) ;

CREATE TABLE university.rooms_courses (
    -- PRIMARY KEY
    id SERIAL constraint pk_university_rooms_courses PRIMARY KEY CONSTRAINT ck_university_rooms_courses_id CHECK(id > 0),
    -- FOREIGN KEY (courses)
    course_id INT NOT NULL,
    constraint fk_university_rooms_courses_courses foreign key (course_id)
    references university.courses (id) on delete cascade on update cascade,

    -- FOREIGN KEY (groups)
    rooms_id INT NOT NULL,
    constraint fk_university_rooms_courses_rooms foreign key (rooms_id)
    references university.rooms (id) on delete cascade on update cascade
) ;

CREATE TABLE university.personals_courses (
    -- PRIMARY KEY
    id SERIAL constraint pk_university_personals_courses PRIMARY KEY CONSTRAINT ck_university_personals_courses_id CHECK(id > 0),
    -- FOREIGN KEY (courses)
    course_id INT NOT NULL,
    constraint fk_university_rooms_courses_courses foreign key (course_id)
    references university.courses (id) on delete cascade on update cascade,

    -- FOREIGN KEY (groups)
    personal_id INT NOT NULL,
    constraint fk_university_personal_courses_personal foreign key (personal_id)
    references university.personals (id) on delete cascade on update cascade
) ;

CREATE TABLE university.reminders(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_reminders PRIMARY KEY CONSTRAINT ck_university_reminders_id CHECK(id > 0),
    -- ATTRIBUTE
	name varchar(32) NOT NULL,
	description TEXT,

	-- FOREIGN KEY (courses)
    course_id INT NOT NULL
) ;


CREATE TABLE university.specializations (
    id SERIAL constraint pk_university_specializations PRIMARY KEY CONSTRAINT ck_university_specialization_id CHECK(id > 0),
    code VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL DEFAULT 'Semestre de préparation au parcours',
    -- FOREIGN KEY (departments)
    department_id INT NOT NULL
);


CREATE TABLE university.teachings (
    id SERIAL constraint pk_university_teachings PRIMARY KEY CONSTRAINT ck_university_teaching_id CHECK(id > 0),
    title VARCHAR(255),
    hour_number INTEGER,
    semestre INT NOT NULL, -- exemple : 5 for R5.X
    sequence VARCHAR(8) NOT NULL, -- exemple : "2" for RX.2 or "MP.09" for RX.MP.09
    description TEXT,
    color VARCHAR(7),

    --Situations d’apprentissage et d’évaluation (SAÉ)
    --Ressources transversales (RT)
    --Ressources cœur de compétences (RCC)
    teaching_type teachings_types DEFAULT 'RCC',

    -- FOREIGN KEY (departments)
    specialization_id INT NOT NULL
);


CREATE TABLE university.absents(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_absents PRIMARY KEY CONSTRAINT ck_university_absents_id CHECK(id > 0),
    -- ATTRIBUTE
    justified boolean default true,

    -- FOREIGN KEY (students)
    student_number INT NOT NULL,
    constraint fk_university_absents_students foreign key (student_number)
    references university.students(id) on delete cascade on update cascade,

    -- FOREIGN KEY (courses)
    course_id INT NOT NULL,
    constraint fk_university_absents_courses foreign key (course_id)
    references university.courses (id) on delete cascade on update cascade
) ;

CREATE TABLE university.participates(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_participates PRIMARY KEY CONSTRAINT ck_university_participates_id CHECK(id > 0),
    -- FOREIGN KEY (courses)
    course_id INT NOT NULL,
    constraint fk_university_participates_courses foreign key (course_id)
    references university.courses (id) on delete cascade on update cascade,

    -- FOREIGN KEY (groups)
    subgroup_id INT NOT NULL,
    constraint fk_university_participates_subgroups foreign key (subgroup_id)
    references university.subgroups (id) on delete cascade on update cascade
) ;

CREATE TABLE university.responsibles(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_responsibles PRIMARY KEY CONSTRAINT ck_university_responsibles_id CHECK(id > 0),

    -- FOREIGN KEY (personals)
    personal_id INT NOT NULL,
    constraint fk_university_responsibles_personals foreign key (personal_id)
    references university.personals (id) on delete cascade on update cascade,

    -- FOREIGN KEY (teachings)
    teaching_id INT NOT NULL,
    constraint fk_university_responsibles_teachings foreign key (teaching_id)
    references university.teachings (id) on delete cascade on update cascade
) ;


/*
    FOREIGN KEY
*/
ALTER TABLE university.reminders
ADD CONSTRAINT fk_university_reminders_courses
FOREIGN KEY (course_id) REFERENCES university.courses(id)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE university.courses
ADD CONSTRAINT fk_university_courses_teachings
FOREIGN KEY (teaching_id) REFERENCES university.teachings(id)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE university.subgroups
ADD CONSTRAINT fk_university_subgroups_groups
FOREIGN KEY (group_id) REFERENCES university.groups(id)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE university.groups
ADD CONSTRAINT fk_university_groups_departments
FOREIGN KEY (department_id) REFERENCES university.departments(id)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE university.departments
ADD CONSTRAINT fk_university_departments_personals
FOREIGN KEY (personal_id) REFERENCES university.personals(id)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE university.students
ADD CONSTRAINT fk_university_students_departments
FOREIGN KEY (department_id) REFERENCES university.departments(id)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE university.students
ADD CONSTRAINT fk_university_students_groups
FOREIGN KEY (group_id) REFERENCES university.groups(id)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE university.students
ADD CONSTRAINT fk_university_students_subgroups
FOREIGN KEY (subgroup_id) REFERENCES university.subgroups(id)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE university.students
ADD CONSTRAINT fk_university_students_users
FOREIGN KEY (user_id) REFERENCES university.users(id)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE university.personals
ADD CONSTRAINT fk_university_personals_users
FOREIGN KEY (user_id) REFERENCES university.users(id)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE university.specializations
ADD CONSTRAINT fk_university_specializations_departments
FOREIGN KEY (department_id) REFERENCES university.departments(id)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE university.teachings
ADD CONSTRAINT fk_university_teachings_specializations
FOREIGN KEY (specialization_id) REFERENCES university.specializations(id)
ON DELETE CASCADE ON UPDATE CASCADE;
