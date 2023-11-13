-- \echo [INFO] Start of script for SAE 1.0

/* Script contain create for each table
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
DROP SCHEMA IF EXISTS university cascade ;

-- \echo [INFO] Create schema university
CREATE SCHEMA university;

-- \echo [INFO] Create the numphone domain with regex
DROP DOMAIN IF EXISTS numstudent ;
CREATE DOMAIN numstudent as varchar(8) check (value ~* E'\\d{8}');

-- \echo [INFO] Create the numphone domain with regex
DROP DOMAIN IF EXISTS numphone ;
CREATE DOMAIN numphone as varchar(14) check (value ~* E'0\\d{1}\.\\d{2}\.\\d{2}\.\\d{2}\.\\d{2}');

-- \echo [INFO] Create the email domain with regex
DROP DOMAIN IF EXISTS email ;
CREATE DOMAIN email AS varchar(64)
CHECK (value ~* E'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\s*$');

-- \echo [INFO] Create the courses_types domain with regex
DROP DOMAIN IF EXISTS courses_types ;
CREATE DOMAIN courses_types as varchar(32) check (value ~* '^(controles|TD|TP|cours|rattrapage|Projet)$');

DROP DOMAIN IF EXISTS teachings_types ;
CREATE DOMAIN teachings_types as varchar(32) check (value ~* '^(SAE|RT|RCC|Portfolio)$');
-- \echo [INFO] Create ALL table
-- Student
-- \echo [INFO] Create the university.students table
CREATE TABLE university.students(
	-- PRIMARY KEY
    student_number numstudent UNIQUE NOT NULL,  -- domain numstudent,
    CONSTRAINT pk_university_students PRIMARY KEY (student_number),  -- primary key constraint
    CONSTRAINT ck_university_student_student_number CHECK (student_number IS NOT NULL),
    -- ATTRIBUTE
    last_name varchar(32) NOT NULL,
    first_name varchar(32) NOT NULL,
    mail email NOT NULL,
    phone_number numphone UNIQUE NOT NULL,  -- domain numphone,
    password varchar(255) NOT NULL,
    -- FOREIGN KEY (departments)
    department_id INT NOT NULL,
    -- FOREIGN KEY (groups)
    group_id INT NOT NULL,
    -- FOREIGN KEY (subgroups)
    subgroup_id INT NOT NULL
) ;

-- Department
-- \echo [INFO] Create the university.departments table
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

-- Group
-- \echo [INFO] Create the university.groups table
CREATE TABLE university.groups(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_groups PRIMARY KEY CONSTRAINT ck_university_group_id CHECK(id > 0), 
    -- ATTRIBUTE
	promotion integer, -- 1st, 2nd or 3rd of school year
    type varchar(5) NOT NULL CHECK (type ~ '^[A-Z]+$' OR type = 'APP'), -- A,B,C... or APP

	-- FOREIGN KEY (departments)
    department_id INT NOT NULL
) ;

-- SubGroup
-- \echo [INFO] Create the university.subgroups table
CREATE TABLE university.subgroups(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_subgroups PRIMARY KEY CONSTRAINT ck_university_subgroup_id CHECK(id > 0), 
    -- ATTRIBUTE
	name varchar(5) NOT NULL CHECK (name ~ '^\d+$' OR name = 'app'), -- app,1,2...

	-- FOREIGN KEY (groups)
    group_id INT NOT NULL
) ;

-- Personal
-- \echo [INFO] Create the university.personals table
CREATE TABLE university.personals(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_personals PRIMARY KEY CONSTRAINT ck_university_personal_id CHECK(id > 0), 
    -- ATTRIBUTE
	last_name varchar(32) NOT NULL,
	first_name varchar(32) NOT NULL,
	mail email NOT NULL ,
    password varchar(255) NOT NULL,
	phone_number numphone UNIQUE NOT NULL	-- domaine numphone
) ;

-- \echo [INFO] Create the university.roles table
CREATE TABLE university.roles(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_roles PRIMARY KEY CONSTRAINT ck_university_roles_id CHECK(id > 0), 
    -- ATTRIBUTE
	name varchar(64) NOT NULL,
	description varchar(128) ,

    -- FOREIGN KEY (personals)
    personal_id INT NOT NULL
) ;

-- Course
-- \echo [INFO] Create the university.courses table
CREATE TABLE university.courses(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_courses PRIMARY KEY CONSTRAINT ck_university_course_id CHECK(id > 0), 
    -- ATTRIBUTE
	description TEXT NOT NULL,
	startTime timestamp NOT NULL,
	duree time NOT NULL,
	course_type courses_types NOT NULL,

    -- FOREIGN KEY (personals)
    personal_id INT NOT NULL,
    -- FOREIGN KEY (rooms)
    rooms_id INT NOT NULL,
    -- FOREIGN KEY (teachings)
    teaching_id INT NOT NULL
) ;

-- rooms
-- \echo [INFO] Create the university.rooms table
CREATE TABLE university.rooms(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_rooms PRIMARY KEY CONSTRAINT ck_university_rooms_id CHECK(id > 0), 
    -- ATTRIBUTE
	code varchar(32) NOT NULL UNIQUE,
	capacity INTEGER NOT NULL,
	has_computer boolean default true,
	has_projector boolean default true
) ;

-- reminders
-- \echo [INFO] Create the university.reminders table
CREATE TABLE university.reminders(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_reminders PRIMARY KEY CONSTRAINT ck_university_reminders_id CHECK(id > 0), 
    -- ATTRIBUTE
	name varchar(32) NOT NULL,
	description TEXT,

	-- FOREIGN KEY (courses)
    course_id INT NOT NULL
) ;

-- specializations
CREATE TABLE university.specializations (
    id SERIAL constraint pk_university_specializations PRIMARY KEY CONSTRAINT ck_university_specialization_id CHECK(id > 0), 
    code VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL DEFAULT 'Semestre de préparation au parcours',
    -- FOREIGN KEY (departments)
    department_id INT NOT NULL
);

-- teachings
CREATE TABLE university.teachings (
    id SERIAL constraint pk_university_teachings PRIMARY KEY CONSTRAINT ck_university_teaching_id CHECK(id > 0), 
    title VARCHAR(255),
    hour_number INTEGER,
    semestre INT NOT NULL, -- exemple : 5 for R5.X
    sequence VARCHAR(8) NOT NULL, -- exemple : "2" for RX.2 or "MP.09" for RX.MP.09
    description TEXT,

    --Situations d’apprentissage et d’évaluation (SAÉ)
    --Ressources transversales (RT)
    --Ressources cœur de compétences (RCC)
    teaching_type teachings_types DEFAULT 'RCC',
    
    -- -- FOREIGN KEY (departments)
    -- department_id INT NOT NULL,
    -- FOREIGN KEY (departments)
    specialization_id INT NOT NULL
);

-- Link table N to N
-- \echo [INFO] Create ALL link table N to N

-- \echo [INFO] Create the university.absents table
CREATE TABLE university.absents(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_absents PRIMARY KEY CONSTRAINT ck_university_absents_id CHECK(id > 0), 
    -- ATTRIBUTE
    justified boolean default true,

    -- FOREIGN KEY (students)
    student_number numstudent NOT NULL,
    constraint fk_university_absents_students foreign key (student_number) 
    references university.students (student_number) on delete restrict on update cascade,
    
    -- FOREIGN KEY (courses)
    course_id INT NOT NULL,
    constraint fk_university_absents_courses foreign key (course_id) 
    references university.courses (id) on delete restrict on update cascade
) ;

-- \echo [INFO] Create the university.participates table
CREATE TABLE university.participates(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_participates PRIMARY KEY CONSTRAINT ck_university_participates_id CHECK(id > 0), 
    -- FOREIGN KEY (courses)
    course_id INT NOT NULL,
    constraint fk_university_participates_courses foreign key (course_id) 
    references university.courses (id) on delete restrict on update cascade,
    
    -- FOREIGN KEY (groups)
    subgroup_id INT NOT NULL,
    constraint fk_university_participates_subgroups foreign key (subgroup_id) 
    references university.subgroups (id) on delete restrict on update cascade
) ;

-- \echo [INFO] Create the university.responsibles table
CREATE TABLE university.responsibles(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_responsibles PRIMARY KEY CONSTRAINT ck_university_responsibles_id CHECK(id > 0), 
    
    -- FOREIGN KEY (personals)
    personal_id INT NOT NULL,
    constraint fk_university_responsibles_personals foreign key (personal_id) 
    references university.personals (id) on delete restrict on update cascade,
    
    -- FOREIGN KEY (teachings)
    teaching_id INT NOT NULL,
    constraint fk_university_responsibles_teachings foreign key (teaching_id)
    references university.teachings (id) on delete restrict on update cascade
) ;


/*
    FOREIGN KEY
*/
-- For the table 'reminders'
-- \echo [INFO] Alter table reminders
ALTER TABLE university.reminders
ADD CONSTRAINT fk_university_reminders_courses
FOREIGN KEY (course_id) REFERENCES university.courses(id)
ON DELETE RESTRICT ON UPDATE CASCADE;

-- For the table 'courses'
-- \echo [INFO] Alter table courses
ALTER TABLE university.courses
ADD CONSTRAINT fk_university_courses_personals
FOREIGN KEY (personal_id) REFERENCES university.personals(id)
ON DELETE RESTRICT ON UPDATE CASCADE;

ALTER TABLE university.courses
ADD CONSTRAINT fk_university_courses_rooms
FOREIGN KEY (rooms_id) REFERENCES university.rooms(id)
ON DELETE RESTRICT ON UPDATE CASCADE;

ALTER TABLE university.courses
ADD CONSTRAINT fk_university_courses_teachings
FOREIGN KEY (teaching_id) REFERENCES university.teachings(id)
ON DELETE RESTRICT ON UPDATE CASCADE;

-- For the table 'subgroups'
-- \echo [INFO] Alter table subgroups
ALTER TABLE university.subgroups
ADD CONSTRAINT fk_university_subgroups_groups
FOREIGN KEY (group_id) REFERENCES university.groups(id)
ON DELETE RESTRICT ON UPDATE CASCADE;

-- For the table 'groups'
-- \echo [INFO] Alter table groups
ALTER TABLE university.groups
ADD CONSTRAINT fk_university_groups_departments
FOREIGN KEY (department_id) REFERENCES university.departments(id)
ON DELETE RESTRICT ON UPDATE CASCADE;

-- For the table 'departments'
-- \echo [INFO] Alter table departments
ALTER TABLE university.departments
ADD CONSTRAINT fk_university_departments_personals
FOREIGN KEY (personal_id) REFERENCES university.personals(id)
ON DELETE RESTRICT ON UPDATE CASCADE;

-- For the table 'students'
-- \echo [INFO] Alter table students
ALTER TABLE university.students
ADD CONSTRAINT fk_university_students_departments
FOREIGN KEY (department_id) REFERENCES university.departments(id)
ON DELETE RESTRICT ON UPDATE CASCADE;

ALTER TABLE university.students
ADD CONSTRAINT fk_university_students_groups
FOREIGN KEY (group_id) REFERENCES university.groups(id)
ON DELETE RESTRICT ON UPDATE CASCADE;

ALTER TABLE university.students
ADD CONSTRAINT fk_university_students_subgroups
FOREIGN KEY (subgroup_id) REFERENCES university.subgroups(id)
ON DELETE RESTRICT ON UPDATE CASCADE;

-- For the table 'roles'
-- \echo [INFO] Alter table roles
ALTER TABLE university.roles
ADD CONSTRAINT fk_university_roles_personals
FOREIGN KEY (personal_id) REFERENCES university.personals(id)
ON DELETE RESTRICT ON UPDATE CASCADE;

-- For the table 'specializations'
-- \echo [INFO] Alter table specializations
ALTER TABLE university.specializations
ADD CONSTRAINT fk_university_specializations_departments
FOREIGN KEY (department_id) REFERENCES university.departments(id)
ON DELETE RESTRICT ON UPDATE CASCADE;

-- For the table 'specializations'
-- \echo [INFO] Alter table specializations
ALTER TABLE university.teachings
ADD CONSTRAINT fk_university_teachings_specializations
FOREIGN KEY (specialization_id) REFERENCES university.specializations(id)
ON DELETE RESTRICT ON UPDATE CASCADE;

---- TRIGGER ----

-- Create a trigger to make the 'type' column uppercase before insertion
CREATE OR REPLACE FUNCTION make_type_uppercase()
    RETURNS TRIGGER AS $$
    BEGIN
        NEW.type = UPPER(NEW.type);
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
    -- Create the trigger
    CREATE TRIGGER uppercase_type_trigger
    BEFORE INSERT ON university.groups
    FOR EACH ROW
EXECUTE FUNCTION make_type_uppercase();

-- Create a trigger to make the 'name' column lowercase before insertion
CREATE OR REPLACE FUNCTION make_type_lowercase()
    RETURNS TRIGGER AS $$
    BEGIN
        NEW.name = LOWER(NEW.name);
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;

-- Create the trigger
CREATE TRIGGER lowercase_name_trigger
    BEFORE INSERT ON university.subgroups
    FOR EACH ROW
EXECUTE FUNCTION make_type_lowercase();


CREATE OR REPLACE FUNCTION check_student_foreign_keys()
RETURNS TRIGGER AS $$
BEGIN
    -- Vérifier le département
    IF NEW.department_id IS NOT NULL AND NEW.group_id IS NOT NULL AND NEW.subgroup_id IS NOT NULL THEN
        IF NOT EXISTS (
            SELECT 1
            FROM university.subgroups AS subgroups
            JOIN university.groups AS groups ON subgroups.group_id = groups.id
            JOIN university.departments AS departments ON groups.department_id = departments.id
            WHERE subgroups.id = NEW.subgroup_id
            AND groups.id = NEW.group_id
            AND departments.id = NEW.department_id
        ) THEN
            RAISE EXCEPTION 'Contrainte de clé étrangère violation : Les clés étrangères (student_number=%, department_id=%, group_id=%, subgroup_id=%) ne correspondent pas', NEW.student_number, NEW.department_id, NEW.group_id, NEW.subgroup_id;
        END IF;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Créer le trigger
CREATE TRIGGER check_student_keys_trigger
    BEFORE INSERT OR UPDATE ON university.students
    FOR EACH ROW
EXECUTE FUNCTION check_student_foreign_keys();
