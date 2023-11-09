-- \echo [INFO] Start of script Insertion for SAE 1.0
-- SOURCE script_university_delete.sql; -- or \i delete.sql; for some databases
-- \i script_university_school_create.sql; --create database

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

-- university.personals(@id, last_name, first_name, mail, phone_number)
INSERT INTO university.personals (last_name, first_name, mail, phone_number)
VALUES
    ('Lamolle', 'Myriam', 'm.lamolle@iut.univ-paris8.fr','06.68.99.99.67'),
    ('Boulanger', 'Max', 'm.boulanger@iut.univ-paris8.fr', '07.10.50.50.58'),
    ('Dafaoui', 'El Mouloudi', 'e.dafaoui@iut.univ-paris8.fr','07.44.29.15.71'),
    ('Flauraud', 'Khamphou', 'k.flauraud@iut.univ-paris8.fr', '06.94.48.00.99'),
    ('Hassoun', 'Abdallah', 'a.hassoun@iut.univ-paris8.fr','06.50.09.15.03'),
    ('Filoche', 'Eddy', 'e.filoche@iut.univ-paris8.fr', '07.68.83.61.75'),
    ('Kamal', 'Rachida', 'r.kamal@iut.univ-paris8.fr', '07.92.15.70.86'),
    ('Bayoud', 'Khadija', 'k.bayoud@iut.univ-paris8.fr', '07.73.26.40.17'),
    ('Baboulall', 'Marielle', 'm.baboulall@iut.univ-paris8.fr', '06.16.61.84.81'),
    ('Kaiser', 'Marc', 'm.kaiser@iut.univ-paris8.fr', '07.58.46.23.15'),
    ('Bonnot', 'Philippe', 'p.bonnot@iut.univ-paris8.fr','07.67.59.80.46'),
    ('Ricordeau', 'Anne', 'a.ricordeau@iut.univ-paris8.fr','06.41.28.19.19'),
    ('Georges', 'Rémi', 'r.georges@iut.univ-paris8.fr','06.03.90.17.73'),
    ('Emonides', 'Mireille', 'm.emonides@iut.univ-paris8.fr','06.26.10.43.02'),
    ('Rety', 'Jean-Hugues', 'j.rety@iut.univ-paris8.fr', '07.86.87.03.82'),
    ('Homps', 'Marc', 'm.homps@iut.univ-paris8.fr', '06.85.48.41.23'),
    ('Simonot', 'Marianne', 'm.simonot@iut.univ-paris8.fr', '07.71.50.67.21'),
    ('Delmas', 'Guylain', 'g.delmas@iut.univ-paris8.fr', '06.01.32.65.82'),
    ('Nauwynck', 'Nédra', 'n.nauwynck@iut.univ-paris8.fr', '06.72.53.57.70'),
    ('Clément-Comparot', 'Véronique', 'v.clement-comparot@iut.univ-paris8.fr', '07.45.74.93.97'),
    ('Le Duc', 'Chan', 'c.leDuc@iut.univ-paris8.fr', '07.98.45.05.76'),
    ('Bossard', 'Aurélien', 'a.bossard@iut.univ-paris8.fr', '07.19.29.79.65'),
    ('Cataldi', 'Mario', 'm.cataldi@iut.univ-paris8.fr', '07.79.24.19.54'),
    ('Golven', 'Amélie', 'a.golven@iut.univ-paris8.fr', '06.48.32.63.21'),
    ('Ballay-Dally', 'Charlotte', 'c.ballay_dally@iut.univ-paris8.fr', '06.79.06.77.84'),
    ('Groff', 'Geoffrey', 'g.groff@iut.univ-paris8.fr', '07.40.01.70.39'),
    ('Chebbi', 'Imen', 'i.chebbi@iut.univ-paris8.fr', '07.33.33.28.19'),
    ('Tobbelem', 'Jocelin', 'j.tobbelem@iut.univ-paris8.fr', '06.97.24.53.70'),
    ('Mockel', 'Mehdi', 'm.mockel@iut.univ-paris8.fr', '06.45.07.64.29'),
    ('Mourel', 'Frédéric', 'f.mourel@iut.univ-paris8.fr', '06.69.18.17.81'),
    ('Nyzam', 'Valentin', 'v.nyzam@iut.univ-paris8.fr', '06.88.49.45.84')
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
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'c.leDuc@iut.univ-paris8.fr')),
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
    ('INFO', 'Informatique','BUT',(SELECT id FROM university.personals WHERE mail = 'a.ricordeau@iut.univ-paris8.fr')),
    ('QLIO', 'Qualité, Logistique Industrielle et Organisation','BUT',(SELECT id FROM university.personals WHERE mail = 'e.dafaoui@iut.univ-paris8.fr')),
    ('INFOCOM', 'Information et Communication','BUT',(SELECT id FROM university.personals WHERE mail = 'm.baboulall@iut.univ-paris8.fr')),
    ('GACO', 'Gestion des Administrations et Commerce','BUT',(SELECT id FROM university.personals WHERE mail = 'm.kaiser@iut.univ-paris8.fr'))
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
INSERT INTO university.subgroups (name, group_id) SELECT '1', id FROM university.groups;
-- For subgroup 2 for each group
INSERT INTO university.subgroups (name, group_id) SELECT '2', id FROM university.groups;
-- For subgroup 3 for each group
INSERT INTO university.subgroups (name, group_id) SELECT '3', id FROM university.groups;
-- For subgroup app for each group
INSERT INTO university.subgroups (name, group_id) SELECT 'App', id FROM university.groups;

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
    ('INFO','Semestre de préparation au parcours',(SELECT id FROM university.departments WHERE name = 'INFO')),
    ('INFO_TC','TRONC COMMUN',(SELECT id FROM university.departments WHERE name = 'INFO')),
    ('INFO_A','Réalisation d’applications : conception, développement, validation',(SELECT id FROM university.departments WHERE name = 'INFO')),
    ('INFO_C','Administration, gestion et exploitation des données',(SELECT id FROM university.departments WHERE name = 'INFO'))
;

-- Parcours - QLIO
INSERT INTO university.specializations (code, name, department_id) 
VALUES
    ('QLIO','Semestre de préparation au parcours',(SELECT id FROM university.departments WHERE name = 'QLIO')),
    ('QLIO_TC','TRONC COMMUN',(SELECT id FROM university.departments WHERE name = 'QLIO')),
    ('QLIO_MP','Management de la production de biens et de services',(SELECT id FROM university.departments WHERE name = 'QLIO')),
    ('QLIO_PSC','Pilotage de la chaîne logistique globale',(SELECT id FROM university.departments WHERE name = 'QLIO'))
;

-- Parcours - INFOCOM
INSERT INTO university.specializations (code, name, department_id) 
VALUES
    ('INFOCOM','Semestre de préparation au parcours',(SELECT id FROM university.departments WHERE name = 'INFOCOM')),
    ('INFOCOM_TC','TRONC COMMUN',(SELECT id FROM university.departments WHERE name = 'INFOCOM')),
    ('INFOCOM_CO','Communication des organisations',(SELECT id FROM university.departments WHERE name = 'INFOCOM'))
;

-- Parcours - GACO
INSERT INTO university.specializations (code, name, department_id) 
VALUES
    ('GACO','Semestre de préparation au parcours',(SELECT id FROM university.departments WHERE name = 'GACO')),
    ('GACO_TC','TRONC COMMUN',(SELECT id FROM university.departments WHERE name = 'GACO')),
    ('GACO_MRPO','Management responsable de projet et entrepreneuriat',(SELECT id FROM university.departments WHERE name = 'GACO')),
    ('GACO_MFS','Management des fonctions supports',(SELECT id FROM university.departments WHERE name = 'GACO')),
    ('GACO_MCMO','Management commercial et marketing omni-canal',(SELECT id FROM university.departments WHERE name = 'GACO'))
;

-- university.teachings(@id, title, hour_number, semestre, sequence, teaching_type #specialization_id)
-- BUT INFO
INSERT INTO university.teachings (title, hour_number, semestre, sequence, teaching_type , specialization_id)
VALUES
    --Semestre 1 INFO
    --Ressources cœur de compétences (RCC)
    ('Initiation au développement', 0, 1, '01', 'RCC',  (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Développement d’interfaces web', 0, 1, '02', 'RCC',  (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Introduction à l’Architecture des Ordinateurs', 0, 1, '03', 'RCC',  (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Introduction aux Systèmes d’exploitation', 0, 1, '04', 'RCC',  (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Introduction aux bases de données SQL', 0, 1, '05', 'RCC',  (SELECT id FROM university.specializations WHERE code = 'INFO')),
    --Ressources transversales (RT)
    ('Mathématiques Discrètes', 0, 1, '06', 'RT',  (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Outils Mathématiques Fondamentaux', 0, 1, '07', 'RT',  (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Gestion de projet et des organisations', 0, 1, '08', 'RT',  (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Économie durable et numérique', 0, 1, '09', 'RT',  (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Anglais Technique', 0, 1, '10', 'RT',  (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Bases de la Communication', 0, 1, '11', 'RT',  (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Projet professionnel et personnel', 0, 1, '12', 'RT',  (SELECT id FROM university.specializations WHERE code = 'INFO')),
    -- SAE
    ('Implémentation d’un besoin client', 0, 1, '01', 'SAE',  (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Comparaison d’approches algorithmiques', 0, 1, '02', 'SAE',  (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Installation d’un poste pour le développement', 0, 1, '03', 'SAE',  (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Création d’une base de données', 0, 1, '04', 'SAE',  (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Recueil de besoins / Découverte de l’environnement économique et écologique', 0, 1, '05&06', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    
    --Semestre 2 INFO
    --Ressources cœur de compétences (RCC)
    ('Développement orienté objets', 0, 2, '01', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Développement d’applications avec IHM', 0, 2, '02', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Qualité de développement', 0, 2, '03', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Communication et fonctionnement bas niveau', 0, 2, '04', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Introduction aux services réseaux', 0, 2, '05', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Exploitation d’une base de données', 0, 2, '06', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    --Ressources transversales (RT)
    ('Graphes', 0, 2, '07', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Outils numériques pour les statistiques descriptives', 0, 2, '08', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Méthodes numériques', 0, 2, '09', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Gestion de projet et des organisations', 0, 2, '10', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Droit des contrats et du numérique', 0, 2, '11', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Anglais d’entreprise', 0, 2, '13', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Communication avec le milieu professionnel', 0, 2, '14', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('PPP : Métiers de l’informatique', 0, 2, '15', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    -- SAE
    ('Développement d’une application', 0, 2, '01', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Exploration algorithmique d’un problème', 0, 2, '02', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Installation de services réseau', 0, 2, '03', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Exploitation d’une base de données', 0, 2, '04', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Gestion d’un projet', 0, 2, '05', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Organisation d’un travail d’équipe', 0, 2, '06', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    
    --Semestre 3 INFO
    --Ressources cœur de compétences (RCC)
    ('Développement Web', 0, 3, '01', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Développement efficace et Qualité', 0, 3, '02&04', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Programmation Système', 0, 3, '05', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Architecture des Réseaux', 0, 3, '06', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('SQL et Programmation', 0, 3, '07', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    --Ressources transversales (RT)
    ('Analyse', 0, 3, '03', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Probabilités', 0, 3, '08', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Cryptographie', 0, 3, '09', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Management des Systèmes d’Information', 0, 3, '10', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Droits des contrats et du numérique', 0, 3, '11', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Anglais', 0, 3, '12', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Anglais Apprentis', 0, 3, '12.app', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Communication Professionnelle', 0, 3, '13', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('PPP', 0, 3, '14', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Outils Mathématiques Fondamentaux', 0, 3, '15', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Anglais pour les projets internationaux', 0, 3, '16', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    ('Anglais pour les projets internationaux [Apprentis - initiauxTDB]', 0, 3, '16.app', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO')),
    -- SAE

    --Semestre 4 INFO
    --TRONC COMMUN
    --Ressources cœur de compétences (RCC)
    ('Architecture Logicielle', 0, 4, '01', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO_TC')),
    ('Qualité Du Développement', 0, 4, '02', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO_TC')),
    ('Qualité & Non-Relationnel', 0, 4, '03', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO_TC')),
    --Ressources transversales (RT)
    ('Méthodes d’Optimisation', 0, 4, '04', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_TC')),
    ('Anglais', 0, 4, '05', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_TC')),
    ('Anglais Apprentis', 0, 4, '05.app', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_TC')),
    ('Comm. Interne', 0, 4, '06', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_TC')),
    ('PPP', 0, 4, '07', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_TC')),
    --Parcours A
    --Ressources cœur de compétences (RCC)
    ('Compléments Web', 0, 4, '10', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO_A')),
    ('Développement Mobile', 0, 4, '11', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO_A')),
    --Ressources transversales (RT)
    ('Virtualisation', 0, 4, '08', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_A')),
    ('Management Avancé de SI', 0, 4, '09', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_A')),
    ('Automates', 0, 4, '12', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_A')),
    --Parcours C
    --Ressources cœur de compétences (RCC)
    ('Cryptographie et Sécurité', 0, 4, '08', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO_C')),
    ('Réseau Avancé', 0, 4, '09', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO_C')),
    --Ressources transversales (RT)
    ('Analyse et Visualisation', 0, 4, '10', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_C')),
    ('Management Avancé de SI', 0, 4, '11', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_C')),
    -- SAE
    ('Développement d’une application web', 0, 4, '01', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO_A')),
    ('Développement avec Base de Données', 0, 4, '01', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO_C'))
;

-- BUT QLIO
INSERT INTO university.teachings (title, hour_number, semestre, sequence, teaching_type , specialization_id)
VALUES
    -- SEMESTRE 1
    -- SAE
    ('Résolution de problèmes', 0, 1, '01', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Immersion-Qualité', 0, 1, '02', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Exécution de gestion de stocks', 0, 1, '03', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Immersion - Logistique', 0, 1, '04', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Organisation d’une situation de production', 0, 1, '05', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Immersion-Organisation', 0, 1, '06', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Portfolio', 0, 1, '07', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    -- Ressources Transversales (RT)
    ('Anglais', 0, 1, '01', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Expression et Communication', 0, 1, '02', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Base des mathématiques et des statistiques', 0, 1, '03', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Connaissance technologique et socio-économique des entreprises', 0, 1, '04', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('outils numériques', 0, 1, '05', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('PPP', 0, 1, '06', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    -- Ressources cœur de compétences (RCC)
    ('Outils, méthodes et communication pour la qualité', 0, 1, '07', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Introduction aux Systèmes de Management de la Qualité', 0, 1, '08', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Identification des Flux physiques et d’information', 0, 1, '09', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Approvisionnements et exécution de planning', 0, 1, '10', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Organisation du système de production', 0, 1, '11', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Organisation d’un projet', 0, 1, '12', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    
    -- SEMESTRE 2
    -- Situations d’apprentissage et d’évaluation (SAE)
    ('Projet opérationnel', 0, 2, '01', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Audit d’un poste de travail', 0, 2, '02', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Exécution d’un planning de production', 0, 2, '03', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Evolution de l’organisation d’un système de production', 0, 2, '04', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Portfolio S2', 0, 2, '05', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Digitalisation des données techniques', 0, 2, '06', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Intégration d’une démarche qualité de premier niveau dans un projet', 0, 2, '07', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    -- Ressources Transversales (RT)
    ('Anglais des affaires', 0, 2, '01', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Expression - Communication', 0, 2, '02', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Statistiques', 0, 2, '03', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Connaissance technologique et gestion de l’entreprise', 0, 2, '04', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Algorithmique - Programmation et systèmes d’information', 0, 2, '05', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Projet personnel et professionnel', 0, 2, '06', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    -- Ressources cœur de compétences (RCC)
    ('Documentation et notions d’audit', 0, 2, '07', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Mesure et surveillance de la conformité', 0, 2, '08', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Digitalisation des données techniques', 0, 2, '09', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Exécution d’un planning de production', 0, 2, '10', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Organisation d’un poste et d’un atelier', 0, 2, '11', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    ('Organisation des données techniques et économiques', 0, 2, '12', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO')),

    -- SEMESTRE 3
    -- Situations d’apprentissage et d’évaluation (SAE)
    ('Déploiement des outils QLIO en tant que technicien', 0, 3, '01', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    ('Bilan et projection', 0, 3, '02', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO_MP')),
    ('Projet gestion de production en tant que technicien', 0, 3, '03', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO_MP')),
    ('Dimensionnement d’un site logistique', 0, 3, '02', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO_PSC')),
    ('Projet Supply chain en tant que technicien', 0, 3, '03', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO_PSC')),
    -- Ressources Transversales (RT)
    ('Anglais des affaires', 0, 3, '01', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    ('Expression Communication', 0, 3, '02', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    ('Communication', 0, 3, '02.app', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    ('Mathématiques', 0, 3, '03', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    ('Gestion de l’entreprise', 0, 3, '04', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    ('Algorithmique et programmation avancées', 0, 3, '05', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    ('Projet Personnel et Professionnel', 0, 3, '06', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    ('Projet Personnel et Professionnel (APPRENTIS)', 0, 3, '06.app', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    -- Ressources cœur de compétences (RCC)
    ('Outils statistiques de pilotage d’un process', 0, 3, '07', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    ('Démarches d’amélioration', 0, 3, '08', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    ('Coordination approvisionnements - production', 0, 3, '09', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    ('Ordonnancement, lancement et pilotage', 0, 3, '10', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    ('Amélioration d’un poste et d’un atelier', 0, 3, '11', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    ('Conduite d’un projet d’amélioration', 0, 3, '12', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    ('Introduction au management', 0, 3, '13', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_MP')),
    ('Activités d’un site logistique', 0, 3, '13', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_PSC')),

    -- SEMESTRE 4
    -- Situations d’apprentissage et d’évaluation (SAE)
    ('Déploiement des outils QLIO en tant que technicien (APPRENTIS)', 0, 4, '01.app', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    ('Déploiement des outils QLIO en tant que technicien', 0, 4, '01', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    ('Appréhender une unité de production', 0, 4, '02', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO_MP')),
    ('Projet gestion de production en tant que technicien', 0, 4, '03', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO_MP')),
    ('Pilotage d’un réseau de distribution', 0, 4, '02', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO_PSC')),
    ('Projet Supply Chain en tant que technicien', 0, 4, '03', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO_PSC')),
    ('Stage', 0, 4, '04', 'SAE', (SELECT id FROM university.specializations WHERE code = 'QLIO')),
    -- Ressources Transversales (RT)
    ('Anglais professionnel et technique', 0, 4, '01', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    ('Expression Communication', 0, 4, '02', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    ('Mathématiques et statistiques avancées', 0, 4, '03', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    ('Bases du contrôle de gestion industriel', 0, 4, '04', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    ('Base de données', 0, 4, '05', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    ('Projet Personnel et Professionnel', 0, 4, '06', 'RT', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    -- Ressources cœur de compétences (RCC)
    ('Amélioration de la performance', 0, 4, '07', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    ('Planification de la production et prévision de la demande à moyen et long terme', 0, 4, '08', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    ('Modélisation pour amélioration du système de production', 0, 4, '09', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_TC')),
    ('Réglementation et droit du travail', 0, 4, '10', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_MP')),
    ('Prévision et planification de la distribution', 0, 4, '10', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_PSC')),
    ('Les fondamentaux de l’animation d’équipe', 0, 4, '11', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_MP')),
    ('Mesure de la performance tout au long de la Supply Chain', 0, 4, '11', 'RCC', (SELECT id FROM university.specializations WHERE code = 'QLIO_PSC'));
;

-- BUT GACO
INSERT INTO university.teachings (title, hour_number, semestre, sequence, teaching_type , specialization_id) 
VALUES
    -- SEMESTRE 1
    ('Gestion de projet', 0, 1, '08', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO')),
    ('Fondamentaux de la comptabilité', 0, 1, '05', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO')),
    ('Langue vivante 1 - Anglais des affaires', 0, 1, '02', 'RT', (SELECT id FROM university.specializations WHERE code = 'GACO')),
    ('Fondamentaux de la comptabilité', 0, 1, '05.app', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO')),
    ('Technologie de l’information et de la communication', 0, 1, '07', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO')),
    ('Gestion de projet et management opérationnel', 0, 1, '08.app', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO')),
    ('Economie', 0, 1, '09', 'RT', (SELECT id FROM university.specializations WHERE code = 'GACO')),
    ('FONDAMENTAUX DU MARKETING', 0, 1, '10', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO')),
    -- SEMESTRE 2
    ('Organisations-Développement durable', 0, 2, '01', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO')),
    ('MARKETING D’ETUDES', 0, 2, '02', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO')),
    ('TRAITEMENT DE L’INFORMATION', 0, 2, '03', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO')),
    -- SEMESTRE 3
    ('MCMO', 0, 3, '01', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO_MCMO')),
    ('Projet Transverse MCMO', 0, 3, '02', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO_MCMO')),
    ('LV1 - Anglais des affaires', 0, 3, '02.app', 'RT', (SELECT id FROM university.specializations WHERE code = 'GACO_TC')),
    ('Fondamentaux du marketing digital', 0, 3, '01.app', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO_TC')),
    ('Nouvelles approches de l’entreprise', 0, 3, '01.app', 'RCC', (SELECT id FROM university.specializations WHERE code = 'GACO_MRPO'))
    -- SEMESTRE 4
;

-- BUT INFOCOM
INSERT INTO university.teachings (title, hour_number, semestre, sequence, teaching_type , specialization_id) 
VALUES
    -- SEMESTRE 1
    ('MEDIAS, USAGES ET MARCHES', 0, 1, '01', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),
    ('Cahier de tendances', 0, 1, '02', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),
    ('PAO', 0, 1, '03', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),
    ('Outils numériques de visualisation et infographie', 0, 1, '04', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),
    ('Etude des publics et marchés', 0, 1, '05', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),
    ('RI Veille', 0, 1, '06', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),
    ('SAE Etude des organisations', 0, 1, '07', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),
    ('Etude des organisations', 0, 1, '08', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),
    ('PPP Semestre 1', 0, 1, '09', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),
    ('Traitement de données', 0, 1, '10', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),
    ('Espagnol', 0, 1, '11', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),
    ('Anglais S1', 0, 1, '12', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),
    ('Organisations professionnelles', 0, 1, '13', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),
    ('Cours Bases Informatiques : DUT INFORMATION COMMUNICATION', 0, 1, '14', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),
    ('SHS-BUT1-S1', 0, 1, '15', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),
    ('Economie Generale', 0, 1, '16', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),
    ('Gestion de projet', 0, 1, '17', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),
    ('Organisations professionnelles', 0, 1, '18', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),
    ('BUT1-S1-Théories de l’information et de la communication', 0, 1, '19', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),

    -- SEMESTRE 2
    ('Atelier de création graphique', 0, 2, '01', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),
    ('Plan de communication', 0, 2, '02', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),
    ('PPP Semestre 2', 0, 2, '03', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),
    ('Espagnol S2', 0, 2, '04', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),
    ('Sémiologie de l’image / Semiologie et linguistique', 0, 2, '05', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),
    ('Anglais S2', 0, 2, '06', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),
    ('Outils de communication spécifique', 0, 2, '07', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM')),

    -- SEMESTRE 3
    ('COMMUNICATION INTERNE 2023', 0, 3, '01', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM_CO')),
    ('Théories INFOCOM - S3', 0, 3, '02', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM_CO')),
    ('PPP Semestre 3', 0, 3, '03', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM_CO')),
    ('Anglais S3', 0, 3, '04', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM_CO')),
    ('Stratégie de communication (Apprentis)', 0, 3, '05', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM_CO')),
    ('Ecrire pour le web APPRENTIS', 0, 3, '06', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM_CO')),
    ('Ecrire pour le web', 0, 3, '07', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM_CO')),
    ('ANGLAIS INFOCOM APPRENTIS', 0, 3, '08', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM_CO')),
    ('Stratégie de communication', 0, 3, '09', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFOCOM_CO'))
;
