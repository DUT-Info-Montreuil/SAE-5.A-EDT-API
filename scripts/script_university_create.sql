-- \echo [INFO] Start of script for SAE 1.0

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
    -- students(@student_number, last_name, first_name, mail, phone_number, #department_id, #group_id, #subgroup_id)
    -- responsibles(@id, #personal_id, #resource_id)
    -- reminders(@id, name, description, #course_id)
    -- absents(@id, justified, #student_number, #course_id)
    -- participates(@id, #course_id, #subgroup_id)
*/
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

-- User
-- \echo [INFO] Create the uses table
CREATE TABLE users(
    -- PRIMARY KEY
    username varchar(64) UNIQUE NOT NULL,
    CONSTRAINT pk_university_users PRIMARY KEY (username),
    -- ATTRIBUTE
    password varchar(255) NOT NULL
) ;

-- Student
-- \echo [INFO] Create the students table
CREATE TABLE students(
	-- PRIMARY KEY
    student_number numstudent UNIQUE NOT NULL,  -- domain numstudent,
    CONSTRAINT pk_university_students PRIMARY KEY (student_number),  -- primary key constraint
    CONSTRAINT ck_university_student_student_number CHECK (student_number IS NOT NULL),
    -- ATTRIBUTE
    last_name varchar(32) NOT NULL,
    first_name varchar(32) NOT NULL,
    mail email NOT NULL,
    phone_number numphone UNIQUE NOT NULL,  -- domain numphone,
    -- password varchar(255) NOT NULL,

    -- FOREIGN KEY (users)
    user_username varchar(64) UNIQUE NOT NULL,
    -- FOREIGN KEY (departments)
    department_id INT NOT NULL,
    -- FOREIGN KEY (groups)
    group_id INT NOT NULL,
    -- FOREIGN KEY (subgroups)
    subgroup_id INT NOT NULL
) ;

-- Department
-- \echo [INFO] Create the departments table
CREATE TABLE departments(
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
-- \echo [INFO] Create the groups table
CREATE TABLE groups(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_groups PRIMARY KEY CONSTRAINT ck_university_group_id CHECK(id > 0), 
    -- ATTRIBUTE
	promotion integer, -- 1st, 2nd or 3rd of school year
    type varchar(5) NOT NULL CHECK (type ~ '^[A-Z]+$' OR type = 'APP'), -- A,B,C... or APP

	-- FOREIGN KEY (departments)
    department_id INT NOT NULL
) ;

-- SubGroup
-- \echo [INFO] Create the subgroups table
CREATE TABLE subgroups(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_subgroups PRIMARY KEY CONSTRAINT ck_university_subgroup_id CHECK(id > 0), 
    -- ATTRIBUTE
	name varchar(16) NOT NULL ,-- CHECK (name ~ '^[A-Z]\d+$' OR name = 'app'), -- app,1,2...

	-- FOREIGN KEY (groups)
    group_id INT NOT NULL
) ;

-- Personal
-- \echo [INFO] Create the personals table
CREATE TABLE personals(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_personals PRIMARY KEY CONSTRAINT ck_university_personal_id CHECK(id > 0), 
    -- ATTRIBUTE
	last_name varchar(32) NOT NULL,
	first_name varchar(32) NOT NULL,
	mail email NOT NULL ,
    personal_code varchar(16) UNIQUE NOT NULL,

    -- FOREIGN KEY (users)
    user_username varchar(64) UNIQUE NOT NULL,
	phone_number numphone UNIQUE NOT NULL	-- domaine numphone
) ;

-- \echo [INFO] Create the roles table
CREATE TABLE roles(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_roles PRIMARY KEY CONSTRAINT ck_university_roles_id CHECK(id > 0), 
    -- ATTRIBUTE
	name varchar(64) NOT NULL,
	description varchar(128) ,

    -- FOREIGN KEY (personals)
    personal_id INT NOT NULL
) ;

-- Course
-- \echo [INFO] Create the courses table
CREATE TABLE courses(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_courses PRIMARY KEY CONSTRAINT ck_university_course_id CHECK(id > 0), 
    -- ATTRIBUTE
	description TEXT,
	startTime timestamp NOT NULL,
	endtime timestamp NOT NULL,
	course_type courses_types NOT NULL,

    -- FOREIGN KEY (personals)
    personal_id INT NOT NULL,
    -- FOREIGN KEY (rooms)
    rooms_id INT NOT NULL,
    -- FOREIGN KEY (teachings)
    teaching_id INT NOT NULL
) ;

-- rooms
-- \echo [INFO] Create the rooms table
CREATE TABLE rooms(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_rooms PRIMARY KEY CONSTRAINT ck_university_rooms_id CHECK(id > 0), 
    -- ATTRIBUTE
	code varchar(32) NOT NULL UNIQUE,
	capacity INTEGER NOT NULL,
	has_computer boolean default true,
	has_projector boolean default true
) ;

-- reminders
-- \echo [INFO] Create the reminders table
CREATE TABLE reminders(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_reminders PRIMARY KEY CONSTRAINT ck_university_reminders_id CHECK(id > 0), 
    -- ATTRIBUTE
	name varchar(32) NOT NULL,
	description TEXT,

	-- FOREIGN KEY (courses)
    course_id INT NOT NULL
) ;

-- specializations
CREATE TABLE specializations (
    id SERIAL constraint pk_university_specializations PRIMARY KEY CONSTRAINT ck_university_specialization_id CHECK(id > 0), 
    code VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL DEFAULT 'Semestre de préparation au parcours',
    -- FOREIGN KEY (departments)
    department_id INT NOT NULL
);

-- teachings
CREATE TABLE teachings (
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

-- \echo [INFO] Create the absents table
CREATE TABLE absents(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_absents PRIMARY KEY CONSTRAINT ck_university_absents_id CHECK(id > 0), 
    -- ATTRIBUTE
    justified boolean default true,

    -- FOREIGN KEY (students)
    student_number numstudent NOT NULL,
    constraint fk_university_absents_students foreign key (student_number) 
    references students (student_number) on delete restrict on update cascade,
    
    -- FOREIGN KEY (courses)
    course_id INT NOT NULL,
    constraint fk_university_absents_courses foreign key (course_id) 
    references courses (id) on delete restrict on update cascade
) ;

-- \echo [INFO] Create the participates table
CREATE TABLE participates(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_participates PRIMARY KEY CONSTRAINT ck_university_participates_id CHECK(id > 0), 
    -- FOREIGN KEY (courses)
    course_id INT NOT NULL,
    constraint fk_university_participates_courses foreign key (course_id) 
    references courses (id) on delete restrict on update cascade,
    
    -- FOREIGN KEY (groups)
    subgroup_id INT NOT NULL,
    constraint fk_university_participates_subgroups foreign key (subgroup_id) 
    references subgroups (id) on delete restrict on update cascade
) ;

-- \echo [INFO] Create the responsibles table
CREATE TABLE responsibles(
    -- PRIMARY KEY
    id SERIAL constraint pk_university_responsibles PRIMARY KEY CONSTRAINT ck_university_responsibles_id CHECK(id > 0), 
    
    -- FOREIGN KEY (personals)
    personal_id INT NOT NULL,
    constraint fk_university_responsibles_personals foreign key (personal_id) 
    references personals (id) on delete restrict on update cascade,
    
    -- FOREIGN KEY (teachings)
    teaching_id INT NOT NULL,
    constraint fk_university_responsibles_teachings foreign key (teaching_id)
    references teachings (id) on delete restrict on update cascade
) ;


/*
    FOREIGN KEY
*/
-- For the table 'reminders'
-- \echo [INFO] Alter table reminders
ALTER TABLE reminders
ADD CONSTRAINT fk_university_reminders_courses
FOREIGN KEY (course_id) REFERENCES courses(id)
ON DELETE RESTRICT ON UPDATE CASCADE;

-- For the table 'courses'
-- \echo [INFO] Alter table courses
ALTER TABLE courses
ADD CONSTRAINT fk_university_courses_personals
FOREIGN KEY (personal_id) REFERENCES personals(id)
ON DELETE RESTRICT ON UPDATE CASCADE;

ALTER TABLE courses
ADD CONSTRAINT fk_university_courses_rooms
FOREIGN KEY (rooms_id) REFERENCES rooms(id)
ON DELETE RESTRICT ON UPDATE CASCADE;

ALTER TABLE courses
ADD CONSTRAINT fk_university_courses_teachings
FOREIGN KEY (teaching_id) REFERENCES teachings(id)
ON DELETE RESTRICT ON UPDATE CASCADE;

-- For the table 'subgroups'
-- \echo [INFO] Alter table subgroups
ALTER TABLE subgroups
ADD CONSTRAINT fk_university_subgroups_groups
FOREIGN KEY (group_id) REFERENCES groups(id)
ON DELETE RESTRICT ON UPDATE CASCADE;

-- For the table 'groups'
-- \echo [INFO] Alter table groups
ALTER TABLE groups
ADD CONSTRAINT fk_university_groups_departments
FOREIGN KEY (department_id) REFERENCES departments(id)
ON DELETE RESTRICT ON UPDATE CASCADE;

-- For the table 'departments'
-- \echo [INFO] Alter table departments
ALTER TABLE departments
ADD CONSTRAINT fk_university_departments_personals
FOREIGN KEY (personal_id) REFERENCES personals(id)
ON DELETE RESTRICT ON UPDATE CASCADE;

-- For the table 'students'
-- \echo [INFO] Alter table students
ALTER TABLE students
ADD CONSTRAINT fk_university_students_departments
FOREIGN KEY (department_id) REFERENCES departments(id)
ON DELETE RESTRICT ON UPDATE CASCADE;

ALTER TABLE students
ADD CONSTRAINT fk_university_students_groups
FOREIGN KEY (group_id) REFERENCES groups(id)
ON DELETE RESTRICT ON UPDATE CASCADE;

ALTER TABLE students
ADD CONSTRAINT fk_university_students_subgroups
FOREIGN KEY (subgroup_id) REFERENCES subgroups(id)
ON DELETE RESTRICT ON UPDATE CASCADE;

ALTER TABLE students
ADD CONSTRAINT fk_university_students_users
FOREIGN KEY (user_username) REFERENCES users(username)
ON DELETE RESTRICT ON UPDATE CASCADE;

ALTER TABLE personals
ADD CONSTRAINT fk_university_personals_users
FOREIGN KEY (user_username) REFERENCES users(username)
ON DELETE RESTRICT ON UPDATE CASCADE;

-- For the table 'roles'
-- \echo [INFO] Alter table roles
ALTER TABLE roles
ADD CONSTRAINT fk_university_roles_personals
FOREIGN KEY (personal_id) REFERENCES personals(id)
ON DELETE RESTRICT ON UPDATE CASCADE;

-- For the table 'specializations'
-- \echo [INFO] Alter table specializations
ALTER TABLE specializations
ADD CONSTRAINT fk_university_specializations_departments
FOREIGN KEY (department_id) REFERENCES departments(id)
ON DELETE RESTRICT ON UPDATE CASCADE;

-- For the table 'specializations'
-- \echo [INFO] Alter table specializations
ALTER TABLE teachings
ADD CONSTRAINT fk_university_teachings_specializations
FOREIGN KEY (specialization_id) REFERENCES specializations(id)
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
    BEFORE INSERT ON groups
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
    BEFORE INSERT ON subgroups
    FOR EACH ROW
EXECUTE FUNCTION make_type_lowercase();


CREATE OR REPLACE FUNCTION check_student_foreign_keys()
RETURNS TRIGGER AS $$
BEGIN
    -- Vérifier le département
    IF NEW.department_id IS NOT NULL AND NEW.group_id IS NOT NULL AND NEW.subgroup_id IS NOT NULL THEN
        IF NOT EXISTS (
            SELECT 1
            FROM subgroups AS subgroups
            JOIN groups AS groups ON subgroups.group_id = groups.id
            JOIN departments AS departments ON groups.department_id = departments.id
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
    BEFORE INSERT OR UPDATE ON students
    FOR EACH ROW
EXECUTE FUNCTION check_student_foreign_keys();

-- CREATE OR REPLACE FUNCTION check_student_email_unique()
-- RETURNS TRIGGER AS $$
-- DECLARE
--     counter INTEGER := 1;
--     new_email text := NEW.mail;
--     base_username text;
--     domain text;
-- BEGIN
--     -- Split the email into username and domain
--     base_username := split_part(new_email, '@', 1);
--     domain := split_part(new_email, '@', 2);

--     -- Check the student email
--     WHILE (SELECT 1 FROM students WHERE mail = new_email) LOOP
--         -- If duplicate found, modify the username
--         new_email := base_username || counter || '@' || domain;
--         RAISE NOTICE 'Email already exists. Modifying to: %', new_email;
--         counter := counter + 1;
--     END LOOP;

--     -- Set the modified email back to NEW.email
--     NEW.mail := new_email;

--     RETURN NEW;
-- END;
-- $$ LANGUAGE plpgsql;

-- -- Create the trigger
-- CREATE TRIGGER check_student_email_trigger
--     BEFORE INSERT OR UPDATE ON students
--     FOR EACH ROW
-- EXECUTE FUNCTION check_student_email_unique();
