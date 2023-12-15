
INSERT INTO university.personals (personal_code, last_name, first_name, mail, phone_number, user_username)
VALUES
    ('PB' ,'Bonnot', 'Philippe', 'p.bonnot@iut.univ-paris8.fr', '07.67.59.80.46', 'pbonnot'), -- username : pbonnot
    ('AR' ,'Ricordeau', 'Anne', 'a.ricordeau@iut.univ-paris8.fr', '06.41.28.19.19', 'aricordeau'), -- username : aricordeau
    ('MyL' ,'Lamolle', 'Myriam', 'm.lamolle@iut.univ-paris8.fr', '06.68.99.99.67', 'mlamolle'), -- username : mlamolle
    ('GD' ,'Delmas', 'Guylain', 'g.delmas@iut.univ-paris8.fr', '06.01.32.65.82', 'gdelmas'), -- username : gdelmas
    ('VéC' ,'Clément-Comparot', 'Véronique', 'v.clement-comparot@iut.univ-paris8.fr', '07.45.74.93.97', 'vclementcomparot'), -- username : vclementcomparot
    ('MaC' ,'Cataldi', 'Mario', 'm.cataldi@iut.univ-paris8.fr', '07.79.24.19.54', 'mcataldi'), -- username : mcataldi
    ('ABo' ,'Bossard', 'Aurélien', 'a.bossard@iut.univ-paris8.fr', '07.19.29.79.65', 'abossard'), -- username : abossard
    ('MS' ,'Simonot', 'Marianne', 'm.simonot@iut.univ-paris8.fr', '07.71.50.67.21', 'msimonot'), -- username : msimonot
    ('JHR' ,'Rety', 'Jean-Hugues', 'j.rety@iut.univ-paris8.fr', '07.86.87.03.82', 'jrety'), -- username : jrety
    ('ArN' ,'Nauwynck', 'Nédra', 'n.nauwynck@iut.univ-paris8.fr', '06.72.53.57.70', 'nnauwynck'), -- username : nnauwynck
    ('CBD' ,'Ballay-Dally', 'Charlotte', 'c.ballay_dally@iut.univ-paris8.fr', '06.79.06.77.84', 'cballaydally'), -- username : cballaydally
    ('MH' ,'Homps', 'Marc', 'm.homps@iut.univ-paris8.fr', '06.85.48.41.23', 'mhomps') -- username : mhomps
;

-- university.roles(@id, name, description, personal_id)
INSERT INTO university.roles (name, description, personal_id)
VALUES 
    ('Directrice', 'Description of the role', (SELECT id FROM personals WHERE mail = 'm.lamolle@iut.univ-paris8.fr')),
    ('Cheffe de département INFO', '', (SELECT id FROM personals WHERE mail = 'a.ricordeau@iut.univ-paris8.fr')),
    ('Directreur des études', '', (SELECT id FROM personals WHERE mail = 'p.bonnot@iut.univ-paris8.fr')),
    ('Responsable Apprentissage BUT', '', (SELECT id FROM personals WHERE mail = 'a.ricordeau@iut.univ-paris8.fr')),

    ('Professeur', '', (SELECT id FROM personals WHERE mail = 'm.homps@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM personals WHERE mail = 'j.rety@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM personals WHERE mail = 'm.lamolle@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM personals WHERE mail = 'a.ricordeau@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM personals WHERE mail = 'g.delmas@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM personals WHERE mail = 'n.nauwynck@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM personals WHERE mail = 'p.bonnot@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM personals WHERE mail = 'v.clement-comparot@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM personals WHERE mail = 'a.bossard@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM personals WHERE mail = 'm.cataldi@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM personals WHERE mail = 'c.ballay_dally@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM personals WHERE mail = 'm.simonot@iut.univ-paris8.fr')),
;

-- university.departments(@id, name, description, department_type)
INSERT into departments (name, description, degree_type,personal_id)
VALUES
    ('INFO', 'Informatique', 'BUT', (SELECT id FROM personals WHERE mail = 'a.ricordeau@iut.univ-paris8.fr')),  -- id : 1
    ('QLIO', 'Qualité, Logistique Industrielle et Organisation', 'BUT',(SELECT id FROM personals WHERE mail = 'e.dafaoui@iut.univ-paris8.fr')),
    ('INFOCOM', 'Information et Communication', 'BUT',(SELECT id FROM personals WHERE mail = 'm.baboulall@iut.univ-paris8.fr')),
    ('GACO', 'Gestion des Administrations et Commerce', 'BUT',(SELECT id FROM personals WHERE mail = 'm.kaiser@iut.univ-paris8.fr'))
;

-- university.groups(@id, promotion, type, #department_id)
-- ### region group for INFO ###
INSERT INTO university.groups (promotion, type, department_id)
VALUES
    -- promotion 1
    (1, 'A', 1),  -- id : 1
    (1, 'B', 1),  -- id : 2

    -- promotion 2
    (2, 'A', 1),  -- id : 3
    (2, 'App', 1) -- id : 4
;
-- ### endregion group for INFO###

-- For subgroup 1 for each group
INSERT INTO university.subgroups (name, group_id) 
    -- promotion 1
        -- groupe A
    ('A1', 1),  -- id : 1
    ('A2', 1),  -- id : 2
        -- groupe B
    ('B1', 2),  -- id : 3
    ('B2', 2),  -- id : 4

    -- promotion 2
        -- groupe A
    ('A1', 3),  -- id : 5 
    ('A2', 3),  -- id : 6
        -- groupe APP
    ('app-1', 5), -- id : 7
    ('app-2', 5)  -- id : 8
;

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
    ('INFO', 'Semestre de préparation au parcours',(SELECT id FROM departments WHERE name = 'INFO')),
    ('INFO_TC', 'TRONC COMMUN',(SELECT id FROM departments WHERE name = 'INFO')),
    ('INFO_A', 'Réalisation d’applications : conception, développement, validation',(SELECT id FROM departments WHERE name = 'INFO')),
    ('INFO_C', 'Administration, gestion et exploitation des données',(SELECT id FROM departments WHERE name = 'INFO'))
;

-- university.teachings(@id, title, hour_number, semestre, sequence, teaching_type #specialization_id)
-- BUT INFO
INSERT INTO university.teachings (title, hour_number, semestre, sequence, teaching_type , specialization_id)
VALUES
    --Semestre 1 INFO
    --Ressources cœur de compétences (RCC)
    ('Initiation au développement', 0, 1, '01', 'RCC',  (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Développement d’interfaces web', 0, 1, '02', 'RCC',  (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Introduction à l’Architecture des Ordinateurs', 0, 1, '03', 'RCC',  (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Introduction aux Systèmes d’exploitation', 0, 1, '04', 'RCC',  (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Introduction aux bases de données SQL', 0, 1, '05', 'RCC',  (SELECT id FROM specializations WHERE code = 'INFO')),
    --Ressources transversales (RT)
    ('Mathématiques Discrètes', 0, 1, '06', 'RT',  (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Outils Mathématiques Fondamentaux', 0, 1, '07', 'RT',  (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Gestion de projet et des organisations', 0, 1, '08', 'RT',  (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Économie durable et numérique', 0, 1, '09', 'RT',  (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Anglais Technique', 0, 1, '10', 'RT',  (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Bases de la Communication', 0, 1, '11', 'RT',  (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Projet professionnel et personnel', 0, 1, '12', 'RT',  (SELECT id FROM specializations WHERE code = 'INFO')),
    -- SAE
    ('Implémentation d’un besoin client', 0, 1, '01', 'SAE',  (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Comparaison d’approches algorithmiques', 0, 1, '02', 'SAE',  (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Installation d’un poste pour le développement', 0, 1, '03', 'SAE',  (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Création d’une base de données', 0, 1, '04', 'SAE',  (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Recueil de besoins / Découverte de l’environnement économique et écologique', 0, 1, '05&06', 'SAE', (SELECT id FROM specializations WHERE code = 'INFO')),
    
    --Semestre 2 INFO
    --Ressources cœur de compétences (RCC)
    ('Développement orienté objets', 0, 2, '01', 'RCC', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Développement d’applications avec IHM', 0, 2, '02', 'RCC', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Qualité de développement', 0, 2, '03', 'RCC', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Communication et fonctionnement bas niveau', 0, 2, '04', 'RCC', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Introduction aux services réseaux', 0, 2, '05', 'RCC', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Exploitation d’une base de données', 0, 2, '06', 'RCC', (SELECT id FROM specializations WHERE code = 'INFO')),
    --Ressources transversales (RT)
    ('Graphes', 0, 2, '07', 'RT', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Outils numériques pour les statistiques descriptives', 0, 2, '08', 'RT', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Méthodes numériques', 0, 2, '09', 'RT', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Gestion de projet et des organisations', 0, 2, '10', 'RT', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Droit des contrats et du numérique', 0, 2, '11', 'RT', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Anglais d’entreprise', 0, 2, '13', 'RT', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Communication avec le milieu professionnel', 0, 2, '14', 'RT', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('PPP : Métiers de l’informatique', 0, 2, '15', 'RT', (SELECT id FROM specializations WHERE code = 'INFO')),
    -- SAE
    ('Développement d’une application', 0, 2, '01', 'SAE', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Exploration algorithmique d’un problème', 0, 2, '02', 'SAE', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Installation de services réseau', 0, 2, '03', 'SAE', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Exploitation d’une base de données', 0, 2, '04', 'SAE', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Gestion d’un projet', 0, 2, '05', 'SAE', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Organisation d’un travail d’équipe', 0, 2, '06', 'SAE', (SELECT id FROM specializations WHERE code = 'INFO')),
        
    --Semestre 3 INFO
    --Ressources cœur de compétences (RCC)
    ('Développement Web', 0, 3, '01', 'RCC', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Développement efficace et Qualité', 0, 3, '02&04', 'RCC', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Programmation Système', 0, 3, '05', 'RCC', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Architecture des Réseaux', 0, 3, '06', 'RCC', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('SQL et Programmation', 0, 3, '07', 'RCC', (SELECT id FROM specializations WHERE code = 'INFO')),
    --Ressources transversales (RT)
    ('Analyse', 0, 3, '03', 'RT', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Probabilités', 0, 3, '08', 'RT', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Cryptographie', 0, 3, '09', 'RT', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Management des Systèmes d’Information', 0, 3, '10', 'RT', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Droits des contrats et du numérique', 0, 3, '11', 'RT', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Anglais', 0, 3, '12', 'RT', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Anglais Apprentis', 0, 3, '12.app', 'RT', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Communication Professionnelle', 0, 3, '13', 'RT', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('PPP', 0, 3, '14', 'RT', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Outils Mathématiques Fondamentaux', 0, 3, '15', 'RT', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Anglais pour les projets internationaux', 0, 3, '16', 'RT', (SELECT id FROM specializations WHERE code = 'INFO')),
    ('Anglais pour les projets internationaux [Apprentis - initiauxTDB]', 0, 3, '16.app', 'RT', (SELECT id FROM specializations WHERE code = 'INFO')),
    -- SAE

    --Semestre 4 INFO
    --TRONC COMMUN
    --Ressources cœur de compétences (RCC)
    ('Architecture Logicielle', 0, 4, '01', 'RCC', (SELECT id FROM specializations WHERE code = 'INFO_TC')),
    ('Qualité Du Développement', 0, 4, '02', 'RCC', (SELECT id FROM specializations WHERE code = 'INFO_TC')),
    ('Qualité & Non-Relationnel', 0, 4, '03', 'RCC', (SELECT id FROM specializations WHERE code = 'INFO_TC')),
    --Ressources transversales (RT)
    ('Méthodes d’Optimisation', 0, 4, '04', 'RT', (SELECT id FROM specializations WHERE code = 'INFO_TC')),
    ('Anglais', 0, 4, '05', 'RT', (SELECT id FROM specializations WHERE code = 'INFO_TC')),
    ('Anglais Apprentis', 0, 4, '05.app', 'RT', (SELECT id FROM specializations WHERE code = 'INFO_TC')),
    ('Comm. Interne', 0, 4, '06', 'RT', (SELECT id FROM specializations WHERE code = 'INFO_TC')),
    ('PPP', 0, 4, '07', 'RT', (SELECT id FROM specializations WHERE code = 'INFO_TC')),
    --Parcours A
    --Ressources cœur de compétences (RCC)
    ('Compléments Web', 0, 4, '10', 'RCC', (SELECT id FROM specializations WHERE code = 'INFO_A')),
    ('Développement Mobile', 0, 4, '11', 'RCC', (SELECT id FROM specializations WHERE code = 'INFO_A')),
    --Ressources transversales (RT)
    ('Virtualisation', 0, 4, '08', 'RT', (SELECT id FROM specializations WHERE code = 'INFO_A')),
    ('Management Avancé de SI', 0, 4, '09', 'RT', (SELECT id FROM specializations WHERE code = 'INFO_A')),
    ('Automates', 0, 4, '12', 'RT', (SELECT id FROM specializations WHERE code = 'INFO_A')),
    --Parcours C
    --Ressources cœur de compétences (RCC)
    ('Cryptographie et Sécurité', 0, 4, '08', 'RCC', (SELECT id FROM specializations WHERE code = 'INFO_C')),
    ('Réseau Avancé', 0, 4, '09', 'RCC', (SELECT id FROM specializations WHERE code = 'INFO_C')),
    --Ressources transversales (RT)
    ('Analyse et Visualisation', 0, 4, '10', 'RT', (SELECT id FROM specializations WHERE code = 'INFO_C')),
    ('Management Avancé de SI', 0, 4, '11', 'RT', (SELECT id FROM specializations WHERE code = 'INFO_C')),
    -- SAE
    ('Développement d’une application web', 0, 4, '01', 'SAE', (SELECT id FROM specializations WHERE code = 'INFO_A')),
    ('Développement avec Base de Données', 0, 4, '01', 'SAE', (SELECT id FROM specializations WHERE code = 'INFO_C'))
;