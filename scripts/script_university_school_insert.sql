-- \echo [INFO] Start of script Insertion for SAE 1.0
-- SOURCE script_university_delete.sql; -- or \i delete.sql; for some databases
-- \i script_university_school_create.sql; --create database
-- hashed by bcrypt in python

/* Script contain insert for each table
    -- university.personals(@id, last_name, first_name, mail, phone_number)
    -- university.roles(@id, name, description, personal_id)
    -- university.departments(@id, name, description, department_type)
    -- university.groups(@id, promotion, type, #department_id)
    -- university.subgroups(@id, name, #group_id)
    -- university.rooms(@id, code, capacity, has_computer, has_projector)
    -- university.specializations(@id, code, name, #department_id)
*/

/* Script miss for table
    -- university.courses(@id, description, starttime, duree, course_type, #personal_id, #rooms_id, #teaching_id)
    -- university.responsibles(@id, #personal_id, #resource_id)
    -- university.reminders(@id, name, description, #course_id)
    -- university.absents(@id, justified, #student_number, #course_id)
    -- university.participates(@id, #course_id, #subgroup_id)
*/

-- delete from university.users;

INSERT INTO university.personals (personal_code, last_name, first_name, mail, phone_number, user_id)
VALUES
    ('PB' ,'Bonnot', 'Philippe', 'p.bonnot@iut.univ-paris8.fr', '07.67.59.80.46', (SELECT id FROM university.users WHERE username = 'pbonnot')), -- username : pbonnot
    ('MyL' ,'Lamolle', 'Myriam', 'm.lamolle@iut.univ-paris8.fr', '06.68.99.99.67', (SELECT id FROM university.users WHERE username = 'mlamolle')), -- username : mlamolle
    ('PIB' ,'Boulanger', 'Max', 'm.boulanger@iut.univ-paris8.fr', '07.10.50.50.58', (SELECT id FROM university.users WHERE username = 'mboulanger')), -- username : mboulanger
    ('EMD' ,'Dafaoui', 'El Mouloudi', 'e.dafaoui@iut.univ-paris8.fr', '07.44.29.15.71', (SELECT id FROM university.users WHERE username = 'edafaoui')), -- username : edafaoui
    ('KF' ,'Flauraud', 'Khamphou', 'k.flauraud@iut.univ-paris8.fr', '06.94.48.00.99', (SELECT id FROM university.users WHERE username = 'kflauraud')), -- username : kflauraud
    ('HA' ,'Hassoun', 'Abdallah', 'a.hassoun@iut.univ-paris8.fr', '06.50.09.15.03', (SELECT id FROM university.users WHERE username = 'ahassoun')), -- username : ahassoun
    ('FE' ,'Filoche', 'Eddy', 'e.filoche@iut.univ-paris8.fr', '07.68.83.61.75', (SELECT id FROM university.users WHERE username = 'efiloche')), -- username : efiloche
    ('RK' ,'Kamal', 'Rachida', 'r.kamal@iut.univ-paris8.fr', '07.92.15.70.86', (SELECT id FROM university.users WHERE username = 'rkamal')), -- username : rkamal
    ('BK' ,'Bayoud', 'Khadija', 'k.bayoud@iut.univ-paris8.fr', '07.73.26.40.17', (SELECT id FROM university.users WHERE username = 'kbayoud')), -- username : kbayoud
    ('MarB' ,'Baboulall', 'Marielle', 'm.baboulall@iut.univ-paris8.fr', '06.16.61.84.81', (SELECT id FROM university.users WHERE username = 'mbaboulall')), -- username : mbaboulall    
    ('MK' ,'Kaiser', 'Marc', 'm.kaiser@iut.univ-paris8.fr', '07.58.46.23.15', (SELECT id FROM university.users WHERE username = 'mkaiser')), -- username : mkaiser
    ('AR' ,'Ricordeau', 'Anne', 'a.ricordeau@iut.univ-paris8.fr', '06.41.28.19.19', (SELECT id FROM university.users WHERE username = 'aricordeau')), -- username : aricordeau
    ('RG' ,'Georges', 'Rémi', 'r.georges@iut.univ-paris8.fr', '06.03.90.17.73', (SELECT id FROM university.users WHERE username = 'rgeorges')), -- username : rgeorges
    ('EoM' ,'Emonides', 'Mireille', 'm.emonides@iut.univ-paris8.fr', '06.26.10.43.02', (SELECT id FROM university.users WHERE username = 'memonides')), -- username : memonides        
    ('JHR' ,'Rety', 'Jean-Hugues', 'j.rety@iut.univ-paris8.fr', '07.86.87.03.82', (SELECT id FROM university.users WHERE username = 'jrety')), -- username : jrety
    ('MH' ,'Homps', 'Marc', 'm.homps@iut.univ-paris8.fr', '06.85.48.41.23', (SELECT id FROM university.users WHERE username = 'mhomps')), -- username : mhomps
    ('MS' ,'Simonot', 'Marianne', 'm.simonot@iut.univ-paris8.fr', '07.71.50.67.21', (SELECT id FROM university.users WHERE username = 'msimonot')), -- username : msimonot
    ('GD' ,'Delmas', 'Guylain', 'g.delmas@iut.univ-paris8.fr', '06.01.32.65.82', (SELECT id FROM university.users WHERE username = 'gdelmas')), -- username : gdelmas
    ('ArN' ,'Nauwynck', 'Nédra', 'n.nauwynck@iut.univ-paris8.fr', '06.72.53.57.70', (SELECT id FROM university.users WHERE username = 'nnauwynck')), -- username : nnauwynck
    ('VéC' ,'Clément-Comparot', 'Véronique', 'v.clement-comparot@iut.univ-paris8.fr', '07.45.74.93.97', (SELECT id FROM university.users WHERE username = 'vclementcomparot')), -- username : vclementcomparot
    ('LDuC' ,'Le Duc', 'Chan', 'c.leduc@iut.univ-paris8.fr', '07.98.45.05.76', (SELECT id FROM university.users WHERE username = 'cleduc')), -- username : cleduc
    ('ABo' ,'Bossard', 'Aurélien', 'a.bossard@iut.univ-paris8.fr', '07.19.29.79.65', (SELECT id FROM university.users WHERE username = 'abossard')), -- username : abossard
    ('MaC' ,'Cataldi', 'Mario', 'm.cataldi@iut.univ-paris8.fr', '07.79.24.19.54', (SELECT id FROM university.users WHERE username = 'mcataldi')), -- username : mcataldi
    ('AGo' ,'Golven', 'Amélie', 'a.golven@iut.univ-paris8.fr', '06.48.32.63.21', (SELECT id FROM university.users WHERE username = 'agolven')), -- username : agolven
    ('CBD' ,'Ballay-Dally', 'Charlotte', 'c.ballay_dally@iut.univ-paris8.fr', '06.79.06.77.84', (SELECT id FROM university.users WHERE username = 'cballaydally')), -- username : cballaydally
    ('GG' ,'Groff', 'Geoffrey', 'g.groff@iut.univ-paris8.fr', '07.40.01.70.39', (SELECT id FROM university.users WHERE username = 'ggroff')), -- username : ggroff
    ('CHi' ,'Chebbi', 'Imen', 'i.chebbi@iut.univ-paris8.fr', '07.33.33.28.19', (SELECT id FROM university.users WHERE username = 'ichebbi')), -- username : ichebbi
    ('ToJ' ,'Tobbelem', 'Jocelin', 'j.tobbelem@iut.univ-paris8.fr', '06.97.24.53.70', (SELECT id FROM university.users WHERE username = 'jtobbelem')), -- username : jtobbelem
    ('MoMe' ,'Mockel', 'Mehdi', 'm.mockel@iut.univ-paris8.fr', '06.45.07.64.29', (SELECT id FROM university.users WHERE username = 'mmockel')), -- username : mmockel
    ('MFr' ,'Mourel', 'Frédéric', 'f.mourel@iut.univ-paris8.fr', '06.69.18.17.81', (SELECT id FROM university.users WHERE username = 'fmourel')), -- username : fmourel
    ('NyV' ,'Nyzam', 'Valentin', 'v.nyzam@iut.univ-paris8.fr', '06.88.49.45.84', (SELECT id FROM university.users WHERE username = 'vnyzam')) -- username : vnyzam
;

-- university.roles(@id, name, description, personal_id)
INSERT INTO university.roles (name, description, personal_id)
VALUES 
    ('Directrice', 'Description of the role', (SELECT id FROM university.personals WHERE mail = 'm.lamolle@iut.univ-paris8.fr')),
    ('Cheffe de département INFO', '', (SELECT id FROM university.personals WHERE mail = 'a.ricordeau@iut.univ-paris8.fr')),
    ('Chef de département QLIO', '', (SELECT id FROM university.personals WHERE mail = 'e.dafaoui@iut.univ-paris8.fr')),
    ('Cheffe de département GACO', '', (SELECT id FROM university.personals WHERE mail = 'm.baboulall@iut.univ-paris8.fr')),
    ('Chef de département INFOCOM', '', (SELECT id FROM university.personals WHERE mail = 'm.kaiser@iut.univ-paris8.fr')),
    ('Directeur', '', (SELECT id FROM university.personals WHERE mail = 'm.boulanger@iut.univ-paris8.fr')),
    ('Responsable d''administration', '', (SELECT id FROM university.personals WHERE mail = 'k.flauraud@iut.univ-paris8.fr')),
    ('Responsable CCRI', '', (SELECT id FROM university.personals WHERE mail = 'a.hassoun@iut.univ-paris8.fr')),
    ('Responsable Hygiène et Sécurité', '', (SELECT id FROM university.personals WHERE mail = 'e.filoche@iut.univ-paris8.fr')),
    ('Chargé de mission', '', (SELECT id FROM university.personals WHERE mail = 'r.kamal@iut.univ-paris8.fr')),
    ('Secrétaire Informatique', '', (SELECT id FROM university.personals WHERE mail = 'k.bayoud@iut.univ-paris8.fr')),
    ('Directreur des études', '', (SELECT id FROM university.personals WHERE mail = 'p.bonnot@iut.univ-paris8.fr')),
    ('Responsable Apprentissage BUT', '', (SELECT id FROM university.personals WHERE mail = 'a.ricordeau@iut.univ-paris8.fr')),
    ('Responsable stage', '', (SELECT id FROM university.personals WHERE mail = 'r.georges@iut.univ-paris8.fr')),
    ('Responsable Contrat Apprentissage', '', (SELECT id FROM university.personals WHERE mail = 'm.emonides@iut.univ-paris8.fr')),

    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'm.homps@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'j.rety@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'm.lamolle@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'a.ricordeau@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'r.georges@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'g.delmas@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'n.nauwynck@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'p.bonnot@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'v.clement-comparot@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'c.leduc@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'a.bossard@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'm.cataldi@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'a.golven@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'c.ballay_dally@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'g.groff@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'i.chebbi@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'j.tobbelem@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'm.mockel@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'f.mourel@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'm.simonot@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'v.nyzam@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'r.kamal@iut.univ-paris8.fr'))
;

-- university.departments(@id, name, description, department_type)
INSERT into university.departments (name, description, degree_type,personal_id)
VALUES
    ('INFO', 'Informatique', 'BUT',(SELECT id FROM university.personals WHERE mail = 'a.ricordeau@iut.univ-paris8.fr')),
    ('QLIO', 'Qualité, Logistique Industrielle et Organisation', 'BUT',(SELECT id FROM university.personals WHERE mail = 'e.dafaoui@iut.univ-paris8.fr')),
    ('INFOCOM', 'Information et Communication', 'BUT',(SELECT id FROM university.personals WHERE mail = 'm.baboulall@iut.univ-paris8.fr')),
    ('GACO', 'Gestion des Administrations et Commerce', 'BUT',(SELECT id FROM university.personals WHERE mail = 'm.kaiser@iut.univ-paris8.fr'))
;

-- university.groups(@id, promotion, type, #department_id)
-- Insert group A for each promotion for Info department
INSERT INTO university.groups (promotion, type, department_id)
VALUES
    (1, 'A', 1),
    (2, 'A', 1),
    (3, 'A', 1)
;
-- Insert group A for each promotion for QLIO department
INSERT INTO university.groups (promotion, type, department_id)
VALUES
    (1, 'A', 2),
    (2, 'A', 2),
    (3, 'A', 2)
;
-- Insert group A for each promotion for INFOCOM department
INSERT INTO university.groups (promotion, type, department_id)
VALUES
    (1, 'A', 3),
    (2, 'A', 3),
    (3, 'A', 3)
;
-- Insert group A for each promotion for GACO department
INSERT INTO university.groups (promotion, type, department_id)
VALUES
    (2, 'A', 4),
    (1, 'A', 4),
    (3, 'A', 4)
;

-- Insert group B for each promotion for Info department
INSERT INTO university.groups (promotion, type, department_id)
VALUES
    (1, 'B', 1),
    (2, 'B', 1),
    (3, 'B', 1)
;
-- Insert group B for each promotion for QLIO department
INSERT INTO university.groups (promotion, type, department_id)
VALUES
    (1, 'B', 2),
    (2, 'B', 2),
    (3, 'B', 2)
;
-- Insert group B for each promotion for INFOCOM department
INSERT INTO university.groups (promotion, type, department_id)
VALUES
    (1, 'B', 3),
    (2, 'B', 3),
    (3, 'B', 3)
;
-- Insert group B for each promotion for GACO department
INSERT INTO university.groups (promotion, type, department_id)
VALUES
    (2, 'B', 4),
    (1, 'B', 4),
    (3, 'B', 4)
;

-- Insert group C for each promotion for Info department
INSERT INTO university.groups (promotion, type, department_id)
VALUES
    (1, 'C', 1),
    (2, 'C', 1),
    (3, 'C', 1)
;
-- Insert group C for each promotion for QLIO department
INSERT INTO university.groups (promotion, type, department_id)
VALUES
    (1, 'C', 2),
    (2, 'C', 2),
    (3, 'C', 2)
;
-- Insert group C for each promotion for INFOCOM department
INSERT INTO university.groups (promotion, type, department_id)
VALUES
    (1, 'C', 3),
    (2, 'C', 3),
    (3, 'C', 3)
;
-- Insert group C for each promotion for GACO department
INSERT INTO university.groups (promotion, type, department_id)
VALUES
    (2, 'C', 4),
    (1, 'C', 4),
    (3, 'C', 4)
;

-- Insert for promotion 2 and 3, groups App for each department
INSERT INTO university.groups (promotion, type, department_id)
VALUES
    -- (1, 'App', 1), -- 1st year Info in apprenticeship
    (2, 'APP', 1),
    (3, 'APP', 1),
    -- (1, 'App', 2), -- 1st year QLIO in apprenticeship
    (2, 'APP', 2),
    (3, 'APP', 2),
    -- (1, 'App', 3), -- 1st year INFOCOM in apprenticeship
    (3, 'APP', 3),
    (2, 'APP', 3),
    -- (1, 'App', 4), -- 1st year GACO in apprenticeship
    (2, 'App', 4),
    (3, 'App', 4)
;

-- university.subgroups(@id, name, #group_id)
-- For subgroup 1 for each group
INSERT INTO university.subgroups (name, group_id) SELECT type || '1', id FROM university.groups;
-- For subgroup 2 for each group
INSERT INTO university.subgroups (name, group_id) SELECT type || '2', id FROM university.groups;
-- For subgroup 3 for each group
INSERT INTO university.subgroups (name, group_id) SELECT type || '3', id FROM university.groups;
-- For subgroup app for each group
INSERT INTO university.subgroups (name, group_id) SELECT type || 'app', id FROM university.groups;

-- university.rooms(@id, code, capacity, has_computer, has_projector)
INSERT INTO university.rooms (code, capacity, has_computer, has_projector) VALUES
    ('A0-03 (Libre)', 0, 't', 'f'),
    ('A0-04 (musique)', 0, 't', 'f'),
    ('A0-05 (L)', 0, 'f', 'f'),
    ('A0-06 (Studio TV)', 0, 'f', 'f'),
    ('A1-01', 0, 't', 'f'),
    ('A2-01', 0, 't', 'f'),
    ('A2-03', 0, 't', 'f'),
    ('A2-04', 0, 't', 'f'),
    ('A2-05', 0, 't', 'f'),
    ('Amphi', 0, 'f', 't'),
    ('Amphi 2', 0, 'f', 't'),
    ('B0-01', 32, 'f', 'f'),
    ('B0-02', 32, 'f', 'f'),
    ('B0-03', 32, 'f', 'f'),
    ('B0-04', 32, 'f', 'f'),
    ('B0-05', 32, 'f', 'f'),
    ('B0-06', 32, 'f', 'f'),
    ('B0-07 (BE2IM)', 10, 'f', 'f'),
    ('B0-09 (salle réunion)', 0, 'f', 'f'),
    ('B1-09', 28, 't', 'f'),
    ('B1-10', 24, 't', 'f'),
    ('B1-13', 24, 't', 'f'),
    ('B1-14', 22, 't', 'f'),
    ('Bibliothèque', 0, 'f', 'f'),
    ('C0-01', 0, 'f', 'f'),
    ('C1-01', 0, 'f', 'f'),
    ('C1-02', 0, 'f', 'f'),
    ('C1-03', 0, 'f', 'f'),
    ('Conseil', 0, 'f', 'f'),
    ('D0-02', 0, 'f', 'f'),
    ('D0-03', 0, 'f', 'f'),
    ('D0-04', 0, 'f', 'f'),
    ('D0-05', 0, 'f', 'f'),
    ('D0-06', 0, 'f', 'f'),
    ('D0-07', 0, 'f', 'f'),
    ('D1-08', 0, 'f', 'f'),
    ('D1-10', 0, 'f', 'f'),
    ('D1-11 (Langues)', 0, 'f', 'f'),
    ('D1-12', 0, 'f', 'f'),
    ('D2-02', 0, 'f', 'f'),
    ('D2-03', 0, 'f', 'f'),
    ('D2-04', 0, 'f', 'f'),
    ('exterieur', 0, 'f', 'f'),
    ('EXTERIEUR', 0, 'f', 'f'),
    ('F1-01', 0, 'f', 'f'),
    ('F1-02', 0, 'f', 'f'),
    ('F1-03 (Langues)', 0, 'f', 'f'),
    ('F1-04', 0, 'f', 'f'),
    ('F1-05', 0, 'f', 'f'),
    ('F1-06', 0, 'f', 'f'),
    ('F1-07', 0, 'f', 'f'),
    ('F1-08', 0, 'f', 'f'),
    ('F1-09', 0, 'f', 'f'),
    ('F1-10', 0, 'f', 'f'),
    ('F1-14', 0, 'f', 'f'),
    ('F1-15', 0, 'f', 'f'),
    ('F2-01', 0, 'f', 'f'),
    ('F2-02', 0, 'f', 'f'),
    ('F2-03', 0, 'f', 'f'),
    ('F2-04', 0, 'f', 'f'),
    ('F2-05', 0, 'f', 'f'),
    ('F2-06', 0, 'f', 'f'),
    ('F2-07', 0, 'f', 'f'),
    ('F2-08', 0, 'f', 'f'),
    ('F2-09', 0, 'f', 'f'),
    ('F2-10', 0, 'f', 'f'),
    ('F2-14', 0, 'f', 'f'),
    ('F2-15', 0, 'f', 'f'),
    ('Halle', 0, 'f', 'f'),
    ('IUT', 0, 'f', 'f'),
    ('Lycée EC', 0, 'f', 'f'),
    ('LycéeVoillaume', 0, 'f', 'f'),
    ('Réunion 01', 0, 'f', 'f'),
    ('Salle Visio', 0, 'f', 'f'),
    ('St Denis ', 0, 'f', 'f'),
    ('StDenis', 0, 'f', 'f'),
    ('StDenis A429', 0, 'f', 'f'),
    ('Sur rdv', 0, 'f', 'f')
;

-- university.specializations(@id, code, name, #department_id)
-- Parcours - INFO
INSERT INTO university.specializations (code, name, department_id) 
VALUES
    ('INFO', 'Semestre de préparation au parcours',(SELECT id FROM university.departments WHERE name = 'INFO')),
    ('INFO_TC', 'TRONC COMMUN',(SELECT id FROM university.departments WHERE name = 'INFO')),
    ('INFO_A', 'Réalisation d’applications : conception, développement, validation',(SELECT id FROM university.departments WHERE name = 'INFO')),
    ('INFO_C', 'Administration, gestion et exploitation des données',(SELECT id FROM university.departments WHERE name = 'INFO'))
;

-- Parcours - QLIO
INSERT INTO university.specializations (code, name, department_id) 
VALUES
    ('QLIO', 'Semestre de préparation au parcours',(SELECT id FROM university.departments WHERE name = 'QLIO')),
    ('QLIO_TC', 'TRONC COMMUN',(SELECT id FROM university.departments WHERE name = 'QLIO')),
    ('QLIO_MP', 'Management de la production de biens et de services',(SELECT id FROM university.departments WHERE name = 'QLIO')),
    ('QLIO_PSC', 'Pilotage de la chaîne logistique globale',(SELECT id FROM university.departments WHERE name = 'QLIO'))
;

-- Parcours - INFOCOM
INSERT INTO university.specializations (code, name, department_id) 
VALUES
    ('INFOCOM', 'Semestre de préparation au parcours',(SELECT id FROM university.departments WHERE name = 'INFOCOM')),
    ('INFOCOM_TC', 'TRONC COMMUN',(SELECT id FROM university.departments WHERE name = 'INFOCOM')),
    ('INFOCOM_CO', 'Communication des organisations',(SELECT id FROM university.departments WHERE name = 'INFOCOM'))
;

-- Parcours - GACO
INSERT INTO university.specializations (code, name, department_id) 
VALUES
    ('GACO', 'Semestre de préparation au parcours',(SELECT id FROM university.departments WHERE name = 'GACO')),
    ('GACO_TC', 'TRONC COMMUN',(SELECT id FROM university.departments WHERE name = 'GACO')),
    ('GACO_MRPO', 'Management responsable de projet et entrepreneuriat',(SELECT id FROM university.departments WHERE name = 'GACO')),
    ('GACO_MFS', 'Management des fonctions supports',(SELECT id FROM university.departments WHERE name = 'GACO')),
    ('GACO_MCMO', 'Management commercial et marketing omni-canal',(SELECT id FROM university.departments WHERE name = 'GACO'))
;

-- university.teachings(@id, title, hour_number, semestre, sequence, teaching_type #specialization_id)
-- BUT INFO
INSERT INTO university.teachings (title, hour_number, semestre, sequence, teaching_type, specialization_id, color)
VALUES
    --Semestre 1 INFO
    --Ressources cœur de compétences (RCC)
    ('Initiation au développement', 0, 1, '01', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), 'FF0000'),
    ('Développement d’interfaces web', 0, 1, '02', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), 'FF0000'),
    ('Introduction à l’Architecture des Ordinateurs', 0, 1, '03', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), '00FF00'),
    ('Introduction aux Systèmes d’exploitation', 0, 1, '04', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), '0000FF'),
    ('Introduction aux bases de données SQL', 0, 1, '05', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), 'FFFF00'),
    --Ressources transversales (RT)
    ('Mathématiques Discrètes', 0, 1, '06', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), 'FF00FF'),
    ('Outils Mathématiques Fondamentaux', 0, 1, '07', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '00FFFF'),
    ('Gestion de projet et des organisations', 0, 1, '08', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '990000'),
    ('Économie durable et numérique', 0, 1, '09', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '009900'),
    ('Anglais Technique', 0, 1, '10', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '000099'),
    ('Bases de la Communication', 0, 1, '11', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '996633'),
    ('Projet professionnel et personnel', 0, 1, '12', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '330066'),
    -- SAE
    ('Implémentation d’un besoin client', 0, 1, '01', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO'), '663300'),
    ('Comparaison d’approches algorithmiques', 0, 1, '02', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO'), '336699'),
    ('Installation d’un poste pour le développement', 0, 1, '03', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO'), '660033'),
    ('Création d’une base de données', 0, 1, '04', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO'), '003366'),
    ('Recueil de besoins / Découverte de l’environnement économique et écologique', 0, 1, '05&06', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO'), '339966'),
    
    --Semestre 2 INFO
    --Ressources cœur de compétences (RCC)
    ('Développement orienté objets', 0, 2, '01', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), 'FF9900'),
    ('Développement d’applications avec IHM', 0, 2, '02', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), 'CC33FF'),
    ('Qualité de développement', 0, 2, '03', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), 'FFFF99'),
    ('Communication et fonctionnement bas niveau', 0, 2, '04', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), '66FF99'),
    ('Introduction aux services réseaux', 0, 2, '05', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), '9966CC'),
    ('Exploitation d’une base de données', 0, 2, '06', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), 'FF6666'),
    --Ressources transversales (RT)
    ('Graphes', 0, 2, '07', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), 'FF3366'),
    ('Outils numériques pour les statistiques descriptives', 0, 2, '08', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '3366FF'),
    ('Méthodes numériques', 0, 2, '09', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '66CCFF'),
    ('Gestion de projet et des organisations', 0, 2, '10', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '99FF33'),
    ('Droit des contrats et du numérique', 0, 2, '11', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '9933FF'),
    ('Anglais d’entreprise', 0, 2, '13', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '33FF99'),
    ('Communication avec le milieu professionnel', 0, 2, '14', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), 'FFCC00'),
    ('PPP : Métiers de l’informatique', 0, 2, '15', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), 'CCFF33'),
    -- SAE
    ('Développement d’une application', 0, 2, '01', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO'), 'FF0033'),
    ('Exploration algorithmique d’un problème', 0, 2, '02', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO'), '3300FF'),
    ('Installation de services réseau', 0, 2, '03', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO'), '00FF33'),
    ('Exploitation d’une base de données', 0, 2, '04', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO'), 'FF3300'),
    ('Gestion d’un projet', 0, 2, '05', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO'), '33FF00'),
    ('Organisation d’un travail d’équipe', 0, 2, '06', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO'), '0033FF'),
        
    --Semestre 3 INFO
    --Ressources cœur de compétences (RCC)
    ('Développement Web', 0, 3, '01', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), 'CC9966'),
    ('Développement efficace et Qualité', 0, 3, '02&04', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), '996633'),
    ('Programmation Système', 0, 3, '05', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), '663366'),
    ('Architecture des Réseaux', 0, 3, '06', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), '336699'),
    ('SQL et Programmation', 0, 3, '07', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), '9966CC'),
    --Ressources transversales (RT)
    ('Analyse', 0, 3, '03', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '669966'),
    ('Probabilités', 0, 3, '08', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '666699'),
    ('Cryptographie', 0, 3, '09', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '996666'),
    ('Management des Systèmes d’Information', 0, 3, '10', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '666699'),
    ('Droits des contrats et du numérique', 0, 3, '11', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '996666'),
    ('Anglais', 0, 3, '12', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '669999'),
    ('Anglais Apprentis', 0, 3, '12.app', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '999966'),
    ('Communication Professionnelle', 0, 3, '13', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '666699'),
    ('PPP', 0, 3, '14', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '996666'),
    ('Outils Mathématiques Fondamentaux', 0, 3, '15', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '669999'),
    ('Anglais pour les projets internationaux', 0, 3, '16', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '999966'),
    ('Anglais pour les projets internationaux [Apprentis - initiauxTDB]', 0, 3, '16.app', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '666699'),
    -- SAE

    --Semestre 4 INFO
    --TRONC COMMUN
    --Ressources cœur de compétences (RCC)
    ('Architecture Logicielle', 0, 4, '01', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO_TC'), 'FF3300'),
    ('Qualité Du Développement', 0, 4, '02', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO_TC'), '33FF00'),
    ('Qualité & Non-Relationnel', 0, 4, '03', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO_TC'), '0033FF'),
    --Ressources transversales (RT)
    ('Méthodes d’Optimisation', 0, 4, '04', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_TC'), 'FF00FF'),
    ('Anglais', 0, 4, '05', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_TC'), 'FFFF00'),
    ('Anglais Apprentis', 0, 4, '05.app', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_TC'), 'FF9900'),
    ('Comm. Interne', 0, 4, '06', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_TC'), 'FF3366'),
    ('PPP', 0, 4, '07', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_TC'), 'CC3366'),
    --Parcours A
    --Ressources cœur de compétences (RCC)
    ('Compléments Web', 0, 4, '10', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO_A'), 'CC9966'),
    ('Développement Mobile', 0, 4, '11', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO_A'), '996633'),
    --Ressources transversales (RT)
    ('Virtualisation', 0, 4, '08', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_A'), '996666'),
    ('Management Avancé de SI', 0, 4, '09', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_A'), '669999'),
    ('Automates', 0, 4, '12', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_A'), 'CC3300'),
    --Parcours C
    --Ressources cœur de compétences (RCC)
    ('Cryptographie et Sécurité', 0, 4, '08', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO_C'), '993366'),
    ('Réseau Avancé', 0, 4, '09', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO_C'), '336699'),
    --Ressources transversales (RT)
    ('Analyse et Visualisation', 0, 4, '10', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_C'), '996666'),
    ('Management Avancé de SI', 0, 4, '11', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_C'), '669999'),
    -- SAE
    ('Développement d’une application web', 0, 4, '01', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO_A'), 'FF3300'),
    ('Développement avec Base de Données', 0, 4, '01', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO_C'), '336699')
;

-- BUT QLIO
INSERT INTO university.teachings (title, hour_number, semestre, sequence, teaching_type, specialization_id, color)
VALUES
    -- SEMESTRE 1
    -- SAE
    ('Résolution de problèmes', 0, 1, '01', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO'), 'FF5733'),
    ('Immersion-Qualité', 0, 1, '02', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO'), '7FDBFF'),
    ('Exécution de gestion de stocks', 0, 1, '03', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO'), '85144b'),
    ('Immersion - Logistique', 0, 1, '04', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO'), 'B10DC9'),
    ('Organisation d’une situation de production', 0, 1, '05', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO'), 'FFDC00'),
    ('Immersion-Organisation', 0, 1, '06', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO'), '2ECC40'),
    ('Portfolio', 0, 1, '07', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO'), 'FF851B'),
    -- Ressources Transversales (RT)
    ('Anglais', 0, 1, '01', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO'), 'DDDDDD'),
    ('Expression et Communication', 0, 1, '02', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO'), '0074CC'),
    ('Base des mathématiques et des statistiques', 0, 1, '03', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO'), '2ECC40'),
    ('Connaissance technologique et socio-économique des entreprises', 0, 1, '04', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO'), 'FF4136'),
    ('outils numériques', 0, 1, '05', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO'), '001F3F'),
    ('PPP', 0, 1, '06', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO'), '39CCCC'),
    -- Ressources cœur de compétences (RCC)
    ('Outils, méthodes et communication pour la qualité', 0, 1, '07', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO'), 'FFD700'),
    ('Introduction aux Systèmes de Management de la Qualité', 0, 1, '08', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO'), 'FF851B'),
    ('Identification des Flux physiques et d’information', 0, 1, '09', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO'), 'FF5733'),
    ('Approvisionnements et exécution de planning', 0, 1, '10', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO'), '0074CC'),
    ('Organisation du système de production', 0, 1, '11', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO'), '2ECC40'),
    ('Organisation d’un projet', 0, 1, '12', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO'), '001F3F'),

    -- SEMESTRE 2
    -- Situations d’apprentissage et d’évaluation (SAE)
    ('Projet opérationnel', 0, 2, '01', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO'), 'FFDC00'),
    ('Audit d’un poste de travail', 0, 2, '02', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO'), 'B10DC9'),
    ('Exécution d’un planning de production', 0, 2, '03', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO'), 'FF4136'),
    ('Evolution de l’organisation d’un système de production', 0, 2, '04', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO'), '0074CC'),
    ('Portfolio S2', 0, 2, '05', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO'), 'FF851B'),
    ('Digitalisation des données techniques', 0, 2, '06', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO'), '39CCCC'),
    ('Intégration d’une démarche qualité de premier niveau dans un projet', 0, 2, '07', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO'), 'FF5733'),
    -- Ressources Transversales (RT)
    ('Anglais des affaires', 0, 2, '01', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO'), 'DDDDDD'),
    ('Expression - Communication', 0, 2, '02', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO'), '0074CC'),
    ('Statistiques', 0, 2, '03', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO'), '2ECC40'),
    ('Connaissance technologique et gestion de l’entreprise', 0, 2, '04', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO'), 'FF4136'),
    ('Algorithmique - Programmation et systèmes d’information', 0, 2, '05', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO'), '001F3F'),
    ('Projet personnel et professionnel', 0, 2, '06', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO'), '39CCCC'),
    -- Ressources cœur de compétences (RCC)
    ('Documentation et notions d’audit', 0, 2, '07', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO'), 'FFD700'),
    ('Mesure et surveillance de la conformité', 0, 2, '08', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO'), 'FF851B'),
    ('Digitalisation des données techniques', 0, 2, '09', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO'), 'FF5733'),
    ('Exécution d’un planning de production', 0, 2, '10', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO'), '0074CC'),
    ('Organisation d’un poste et d’un atelier', 0, 2, '11', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO'), '2ECC40'),
    ('Organisation des données techniques et économiques', 0, 2, '12', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO'), '001F3F'),

    -- SEMESTRE 3
    -- Situations d’apprentissage et d’évaluation (SAE)
    ('Déploiement des outils QLIO en tant que technicien', 0, 3, '01', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), 'FF5733'),
    ('Bilan et projection', 0, 3, '02', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO_MP'), '7FDBFF'),
    ('Projet gestion de production en tant que technicien', 0, 3, '03', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO_MP'), '85144b'),
    ('Dimensionnement d’un site logistique', 0, 3, '02', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO_PSC'), 'B10DC9'),
    ('Projet Supply chain en tant que technicien', 0, 3, '03', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO_PSC'), 'FFDC00'),
    -- Ressources Transversales (RT)
    ('Anglais des affaires', 0, 3, '01', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), 'DDDDDD'),
    ('Expression Communication', 0, 3, '02', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), '0074CC'),
    ('Communication', 0, 3, '02.app', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), '2ECC40'),
    ('Mathématiques', 0, 3, '03', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), 'FF4136'),
    ('Gestion de l’entreprise', 0, 3, '04', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), '001F3F'),
    ('Algorithmique et programmation avancées', 0, 3, '05', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), '39CCCC'),
    ('Projet Personnel et Professionnel', 0, 3, '06', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), 'FF851B'),
    ('Projet Personnel et Professionnel (APPRENTIS)', 0, 3, '06.app', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), 'FF5733'),
    -- Ressources cœur de compétences (RCC)
    ('Outils statistiques de pilotage d’un process', 0, 3, '07', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), 'FFD700'),
    ('Démarches d’amélioration', 0, 3, '08', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), 'FF851B'),
    ('Coordination approvisionnements - production', 0, 3, '09', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), 'FF5733'),
    ('Ordonnancement, lancement et pilotage', 0, 3, '10', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), '0074CC'),
    ('Amélioration d’un poste et d’un atelier', 0, 3, '11', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), '2ECC40'),
    ('Conduite d’un projet d’amélioration', 0, 3, '12', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), '001F3F'),
    ('Introduction au management', 0, 3, '13', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_MP'), 'FFDC00'),
    ('Activités d’un site logistique', 0, 3, '13', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_PSC'), 'B10DC9'),

    -- SEMESTRE 4
    -- Situations d’apprentissage et d’évaluation (SAE)
    ('Déploiement des outils QLIO en tant que technicien (APPRENTIS)', 0, 4, '01.app', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), 'FF5733'),
    ('Déploiement des outils QLIO en tant que technicien', 0, 4, '01', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), '7FDBFF'),
    ('Appréhender une unité de production', 0, 4, '02', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO_MP'), '85144b'),
    ('Projet gestion de production en tant que technicien', 0, 4, '03', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO_MP'), 'B10DC9'),
    ('Pilotage d’un réseau de distribution', 0, 4, '02', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO_PSC'), 'FFDC00'),
    ('Projet Supply Chain en tant que technicien', 0, 4, '03', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO_PSC'), '0074CC'),
    ('Stage', 0, 4, '04', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO'), '2ECC40'),
    -- Ressources Transversales (RT)
    ('Anglais professionnel et technique', 0, 4, '01', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), 'DDDDDD'),
    ('Expression Communication', 0, 4, '02', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), '0074CC'),
    ('Mathématiques et statistiques avancées', 0, 4, '03', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), '2ECC40'),
    ('Bases du contrôle de gestion industriel', 0, 4, '04', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), 'FF4136'),
    ('Base de données', 0, 4, '05', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), '001F3F'),
    ('Projet Personnel et Professionnel', 0, 4, '06', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), '39CCCC'),
    -- Ressources cœur de compétences (RCC)
    ('Amélioration de la performance', 0, 4, '07', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), 'FFD700'),
    ('Planification de la production et prévision de la demande à moyen et long terme', 0, 4, '08', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), 'FF851B'),
    ('Modélisation pour amélioration du système de production', 0, 4, '09', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC'), 'FF5733'),
    ('Réglementation et droit du travail', 0, 4, '10', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_MP'), '0074CC'),
    ('Prévision et planification de la distribution', 0, 4, '10', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_PSC'), '2ECC40'),
    ('Les fondamentaux de l’animation d’équipe', 0, 4, '11', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_MP'), '001F3F'),
    ('Mesure de la performance tout au long de la Supply Chain', 0, 4, '11', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_PSC'), 'FFDC00')
;


-- BUT GACO
INSERT INTO university.teachings (title, hour_number, semestre, sequence, teaching_type , specialization_id, color) 
VALUES
    -- SEMESTRE 1
    ('Gestion de projet', 0, 1, '08', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO'), 'FF5733'),
    ('Fondamentaux de la comptabilité', 0, 1, '05', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO'), '7FDBFF'),
    ('Langue vivante 1 - Anglais des affaires', 0, 1, '02', 'RT', (SELECT id FROM university.specializations WHERE code = 'GACO'), '85144b'),
    ('Fondamentaux de la comptabilité', 0, 1, '05.app', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO'), 'B10DC9'),
    ('Technologie de l’information et de la communication', 0, 1, '07', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO'), 'FFDC00'),
    ('Gestion de projet et management opérationnel', 0, 1, '08.app', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO'), '0074CC'),
    ('Economie', 0, 1, '09', 'RT', (SELECT id FROM university.specializations WHERE code = 'GACO'), '2ECC40'),
    ('FONDAMENTAUX DU MARKETING', 0, 1, '10', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO'), '001F3F'),
    -- SEMESTRE 2
    ('Organisations-Développement durable', 0, 2, '01', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO'), '39CCCC'),
    ('MARKETING D’ETUDES', 0, 2, '02', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO'), 'FF4136'),
    ('TRAITEMENT DE L’INFORMATION', 0, 2, '03', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO'), 'FF851B'),
    -- SEMESTRE 3
    ('MCMO', 0, 3, '01', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO_MCMO'), 'FF5733'),
    ('Projet Transverse MCMO', 0, 3, '02', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO_MCMO'), '7FDBFF'),
    ('LV1 - Anglais des affaires', 0, 3, '02.app', 'RT', (SELECT id FROM university.specializations WHERE code = 'GACO_TC'), '85144b'),
    ('Fondamentaux du marketing digital', 0, 3, '01.app', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO_TC'), 'B10DC9'),
    ('Nouvelles approches de l’entreprise', 0, 3, '01.app', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO_MRPO'), 'FFDC00')
;


-- BUT INFOCOM
INSERT INTO university.teachings (title, hour_number, semestre, sequence, teaching_type , specialization_id, color) 
VALUES
    -- SEMESTRE 1
    ('MEDIAS, USAGES ET MARCHES', 0, 1, '01', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), 'FF5733'),
    ('Cahier de tendances', 0, 1, '02', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), '7FDBFF'),
    ('PAO', 0, 1, '03', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), '85144b'),
    ('Outils numériques de visualisation et infographie', 0, 1, '04', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), 'B10DC9'),
    ('Etude des publics et marchés', 0, 1, '05', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), 'FFDC00'),
    ('RI Veille', 0, 1, '06', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), '0074CC'),
    ('SAE Etude des organisations', 0, 1, '07', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), '2ECC40'),
    ('Etude des organisations', 0, 1, '08', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), '001F3F'),
    ('PPP Semestre 1', 0, 1, '09', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), '39CCCC'),
    ('Traitement de données', 0, 1, '10', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), 'FF4136'),
    ('Espagnol', 0, 1, '11', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), 'FF851B'),
    ('Anglais S1', 0, 1, '12', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), 'FF5733'),
    ('Organisations professionnelles', 0, 1, '13', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), '7FDBFF'),
    ('Cours Bases Informatiques : DUT INFORMATION COMMUNICATION', 0, 1, '14', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), '85144b'),
    ('SHS-BUT1-S1', 0, 1, '15', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), 'B10DC9'),
    ('Economie Generale', 0, 1, '16', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), 'FFDC00'),
    ('Gestion de projet', 0, 1, '17', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), '0074CC'),
    ('Organisations professionnelles', 0, 1, '18', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), '2ECC40'),
    ('BUT1-S1-Théories de l’information et de la communication', 0, 1, '19', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), '001F3F'),

    -- SEMESTRE 2
    ('Atelier de création graphique', 0, 2, '01', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), '39CCCC'),
    ('Plan de communication', 0, 2, '02', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), 'FF4136'),
    ('PPP Semestre 2', 0, 2, '03', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), 'FF851B'),
    ('Espagnol S2', 0, 2, '04', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), 'FF5733'),
    ('Sémiologie de l’image / Semiologie et linguistique', 0, 2, '05', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), '7FDBFF'),
    ('Anglais S2', 0, 2, '06', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), '85144b'),
    ('Outils de communication spécifique', 0, 2, '07', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM'), 'B10DC9'),

    -- SEMESTRE 3
    ('COMMUNICATION INTERNE 2023', 0, 3, '01', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM_CO'), 'FF5733'),
    ('Théories INFOCOM - S3', 0, 3, '02', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM_CO'), '7FDBFF'),
    ('PPP Semestre 3', 0, 3, '03', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM_CO'), '85144b'),
    ('Anglais S3', 0, 3, '04', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM_CO'), 'B10DC9'),
    ('Stratégie de communication (Apprentis)', 0, 3, '05', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM_CO'), 'FFDC00'),
    ('Ecrire pour le web APPRENTIS', 0, 3, '06', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM_CO'), '0074CC'),
    ('Ecrire pour le web', 0, 3, '07', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM_CO'), '2ECC40'),
    ('ANGLAIS INFOCOM APPRENTIS', 0, 3, '08', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM_CO'), '001F3F'),
    ('Stratégie de communication', 0, 3, '09', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM_CO'), '39CCCC')
;

