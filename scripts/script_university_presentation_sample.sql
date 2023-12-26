

INSERT INTO university.users (username, password)
VALUES
    ('pbonnot', '$2b$12$NyUZ8nMD7n9cbV.yBUbNVOom1TDWUUviZgXku63jMqPMMNzDebBRe'), -- pwd : pbonnot
    ('aricordeau', '$2b$12$NyUZ8nMD7n9cbV.yBUbNVOom1TDWUUviZgXku63jMqPMMNzDebBRe'), -- pwd : pbonnot
    ('mlamolle', '$2b$12$NyUZ8nMD7n9cbV.yBUbNVOom1TDWUUviZgXku63jMqPMMNzDebBRe'), -- pwd : pbonnot
    ('gdelmas', '$2b$12$NyUZ8nMD7n9cbV.yBUbNVOom1TDWUUviZgXku63jMqPMMNzDebBRe'), -- pwd : pbonnot
    ('vclementcomparot', '$2b$12$NyUZ8nMD7n9cbV.yBUbNVOom1TDWUUviZgXku63jMqPMMNzDebBRe'), -- pwd : pbonnot
    ('mcataldi', '$2b$12$NyUZ8nMD7n9cbV.yBUbNVOom1TDWUUviZgXku63jMqPMMNzDebBRe'), -- pwd : pbonnot
    ('abossard', '$2b$12$NyUZ8nMD7n9cbV.yBUbNVOom1TDWUUviZgXku63jMqPMMNzDebBRe'), -- pwd : pbonnot
    ('msimonot', '$2b$12$NyUZ8nMD7n9cbV.yBUbNVOom1TDWUUviZgXku63jMqPMMNzDebBRe'), -- pwd : pbonnot
    ('jrety', '$2b$12$NyUZ8nMD7n9cbV.yBUbNVOom1TDWUUviZgXku63jMqPMMNzDebBRe'), -- pwd : pbonnot
    ('nnauwynck', '$2b$12$NyUZ8nMD7n9cbV.yBUbNVOom1TDWUUviZgXku63jMqPMMNzDebBRe'), -- pwd : pbonnot
    ('cballaydally', '$2b$12$NyUZ8nMD7n9cbV.yBUbNVOom1TDWUUviZgXku63jMqPMMNzDebBRe'), -- pwd : pbonnot
    ('mhomps', '$2b$12$NyUZ8nMD7n9cbV.yBUbNVOom1TDWUUviZgXku63jMqPMMNzDebBRe') -- pwd : pbonnot
;

INSERT INTO university.personals (personal_code, last_name, first_name, mail, phone_number, user_id)
VALUES
    ('PB' ,'Bonnot', 'Philippe', 'p.bonnot@iut.univ-paris8.fr', '07.67.59.80.46', (SELECT id FROM university.users WHERE username = 'pbonnot')), -- username : pbonnot
    ('AR' ,'Ricordeau', 'Anne', 'a.ricordeau@iut.univ-paris8.fr', '06.41.28.19.19', (SELECT id FROM university.users WHERE username = 'aricordeau')), -- username : aricordeau
    ('MyL' ,'Lamolle', 'Myriam', 'm.lamolle@iut.univ-paris8.fr', '06.68.99.99.67', (SELECT id FROM university.users WHERE username = 'mlamolle')), -- username : mlamolle
    ('GD' ,'Delmas', 'Guylain', 'g.delmas@iut.univ-paris8.fr', '06.01.32.65.82', (SELECT id FROM university.users WHERE username = 'gdelmas')), -- username : gdelmas
    ('VeC' ,'Clement-Comparot', 'Veronique', 'v.clement-comparot@iut.univ-paris8.fr', '07.45.74.93.97', (SELECT id FROM university.users WHERE username = 'vclementcomparot')), -- username : vclementcomparot
    ('MaC' ,'Cataldi', 'Mario', 'm.cataldi@iut.univ-paris8.fr', '07.79.24.19.54', (SELECT id FROM university.users WHERE username = 'mcataldi')), -- username : mcataldi
    ('ABo' ,'Bossard', 'Aurelien', 'a.bossard@iut.univ-paris8.fr', '07.19.29.79.65', (SELECT id FROM university.users WHERE username = 'abossard')), -- username : abossard
    ('MS' ,'Simonot', 'Marianne', 'm.simonot@iut.univ-paris8.fr', '07.71.50.67.21', (SELECT id FROM university.users WHERE username = 'msimonot')), -- username : msimonot
    ('JHR' ,'Rety', 'Jean-Hugues', 'j.rety@iut.univ-paris8.fr', '07.86.87.03.82', (SELECT id FROM university.users WHERE username = 'jrety')), -- username : jrety
    ('ArN' ,'Nauwynck', 'Nedra', 'n.nauwynck@iut.univ-paris8.fr', '06.72.53.57.70', (SELECT id FROM university.users WHERE username = 'nnauwynck')), -- username : nnauwynck
    ('CBD' ,'Ballay-Dally', 'Charlotte', 'c.ballay_dally@iut.univ-paris8.fr', '06.79.06.77.84', (SELECT id FROM university.users WHERE username = 'cballaydally')), -- username : cballaydally
    ('MH' ,'Homps', 'Marc', 'm.homps@iut.univ-paris8.fr', '06.85.48.41.23', (SELECT id FROM university.users WHERE username = 'mhomps')) -- username : mhomps
;

-- university.roles(@id, name, description, personal_id)
INSERT INTO university.roles (name, description, personal_id)
VALUES
    ('Directrice', 'Description of the role', (SELECT id FROM university.personals WHERE mail = 'm.lamolle@iut.univ-paris8.fr')),
    ('Cheffe de departement INFO', '', (SELECT id FROM university.personals WHERE mail = 'a.ricordeau@iut.univ-paris8.fr')),
    ('Directreur des etudes', '', (SELECT id FROM university.personals WHERE mail = 'p.bonnot@iut.univ-paris8.fr')),
    ('Responsable Apprentissage BUT', '', (SELECT id FROM university.personals WHERE mail = 'a.ricordeau@iut.univ-paris8.fr')),

    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'm.homps@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'j.rety@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'm.lamolle@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'a.ricordeau@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'g.delmas@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'n.nauwynck@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'p.bonnot@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'v.clement-comparot@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'a.bossard@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'm.cataldi@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'c.ballay_dally@iut.univ-paris8.fr')),
    ('Professeur', '', (SELECT id FROM university.personals WHERE mail = 'm.simonot@iut.univ-paris8.fr'))
;

-- university.departments(@id, name, description, department_type)
INSERT into university.departments (name, description, degree_type,personal_id)
VALUES
    ('INFO', 'Informatique', 'BUT', (SELECT id FROM university.personals WHERE mail = 'a.ricordeau@iut.univ-paris8.fr')),  -- id : 1
    ('QLIO', 'Qualite, Logistique Industrielle et Organisation', 'BUT',(SELECT id FROM university.personals WHERE mail = 'm.simonot@iut.univ-paris8.fr')),
    ('INFOCOM', 'Information et Communication', 'BUT',(SELECT id FROM university.personals WHERE mail = 'p.bonnot@iut.univ-paris8.fr')),
    ('GACO', 'Gestion des Administrations et Commerce', 'BUT',(SELECT id FROM university.personals WHERE mail = 'p.bonnot@iut.univ-paris8.fr'))
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
VALUES
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
    ('app-1', 4), -- id : 7
    ('app-2', 4)  -- id : 8
;
-- university.users(@username, password)
INSERT INTO university.users (username, password)
VALUES
	('hugo', '$2b$12$suR4RUnowOZPYUkJxAsb5OuaNO.xw2VDberXSoHuez1ZT9/xeH9cC'), -- pwd : hugohugohugo
	('mtoure', '$2b$12$n9o/jbKgDAJrpC1ejpfWcug6dRTh.wpEmXdv2o4nWJHtiQVYhFZAa'), -- pwd : Mehedi_Toure
	('hcohen', '$2b$12$7v3cwt6UnMwKbKwPWucXAeeGULIPpDL0qtzUbK2Sk7LRAvidh.uhi'), -- pwd : Hugo_COHENh1
	('aclaude', '$2b$12$4uT0.g7slJG8HR810FhP6uOpsS7iBdW5lBbW2M.JU076Dp4w1dqxq'), -- pwd : Aldric_CLAUD
	('achetouani', '$2b$12$foIsmgkwIiRDCpzl9FDcS.ox7crQ320ShFB1P79Iygny1PmdIlQ0q'), -- pwd : Adil_CHETOUA
	('bseydi', '$2b$12$3tWrEuOGAtwERwLjmZeUl.Q4LYjE.yl/m6f.77Bs1VwYX2rCXuP22'), -- pwd : Boulaye_SEYD
	('yhanma', '$2b$12$/Hu/tJQwfN5UYeTQTcQlYOHJsiFiTP4QSXlEtcJegSljsz1x2deje'), -- pwd : @~f=,6}n/%]v
	('bhanma', '$2b$12$0d8XHQR3kPq1Jm/hW2s05u5.PrLFriCynsXozbhW5sze9aMRzuQnW'), -- pwd : Z1:t}uv?"<Mh
	('cbrown1', '$2b$12$uJ8rbTensgrPrIB/YjnRUev7./v/rF336xpw/lyReONumpCLBM/r.') -- pwd : ;`#{-t&'AYY~
;

INSERT INTO university.students (id, last_name, first_name, mail, phone_number, user_id, department_id, group_id, subgroup_id)
VALUES
    (85800425, 'Mehedi', 'Toure', 'mtoure@iut.univ-paris8.fr', '07.12.34.56.78', (SELECT id FROM university.users WHERE username = 'mtoure'), 1, 1, 1), -- username : mtoure
    (32800138, 'Hugo', 'COHEN', 'hcohen@iut.univ-paris8.fr', '06.12.21.12.21', (SELECT id FROM university.users WHERE username = 'hcohen'), 1, 1, 2), -- username : hcohen
    (91736781, 'Aldric', 'CLAUDE', 'aclaude@iut.univ-paris8.fr', '07.11.11.11.11', (SELECT id FROM university.users WHERE username = 'aclaude'), 1, 2, 3), -- username : aclaude
    (00953322, 'Adil', 'CHETOUANI', 'achetouani@iut.univ-paris8.fr', '07.22.22.22.22', (SELECT id FROM university.users WHERE username = 'achetouani'), 1, 2, 4), -- username : achetouani
    (24992466, 'Boulaye', 'SEYDI', 'bseydi@iut.univ-paris8.fr', '07.01.10.01.10', (SELECT id FROM university.users WHERE username = 'bseydi'), 1, 3, 5), -- username : bbseydi
    (65857267, 'Yujiro', 'Hanma', 'yhanma@iut.univ-paris8.fr', '07.76.01.23.29', (SELECT id FROM university.users WHERE username = 'yhanma'), 1, 3, 6), -- username : yhanma
    (26211358, 'Baki', 'Hanma', 'bhanma@iut.univ-paris8.fr', '07.24.20.80.26', (SELECT id FROM university.users WHERE username = 'bhanma'), 1, 4, 7), -- username : bhanma
    (68294080, 'Christine', 'Brown', 'cbrown1@iut.univ-paris8.fr', '06.55.09.93.34', (SELECT id FROM university.users WHERE username = 'cbrown1'), 1, 4, 8) -- username : cbrown1
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
    ('B0-09 (salle reunion)', 0, 'f', 'f'),
    ('B1-09', 28, 't', 'f'),
    ('B1-10', 24, 't', 'f'),
    ('B1-13', 24, 't', 'f'),
    ('B1-14', 22, 't', 'f'),
    ('Bibliotheque', 0, 'f', 'f'),
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
    ('Lycee EC', 0, 'f', 'f'),
    ('LyceeVoillaume', 0, 'f', 'f'),
    ('Reunion 01', 0, 'f', 'f'),
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
    ('INFO', 'Semestre de preparation au parcours',(SELECT id FROM university.departments WHERE name = 'INFO')),
    ('INFO_TC', 'TRONC COMMUN',(SELECT id FROM university.departments WHERE name = 'INFO')),
    ('INFO_A', 'Realisation d applications : conception, developpement, validation',(SELECT id FROM university.departments WHERE name = 'INFO')),
    ('INFO_C', 'Administration, gestion et exploitation des donnees',(SELECT id FROM university.departments WHERE name = 'INFO'))
;

-- university.teachings(@id, title, hour_number, semestre, sequence, teaching_type #specialization_id)
-- BUT INFO
INSERT INTO university.teachings (title, hour_number, semester, sequence, teaching_type, specialization_id, teaching_color)
VALUES
    --Semestre 1 INFO
    --Ressources cœur de competences (RCC)
    ('Initiation au developpement', 0, 1, '01', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#FF0000'),
    ('Developpement d interfaces web', 0, 1, '02', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#FF0000'),
    ('Introduction a l Architecture des Ordinateurs', 0, 1, '03', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#FF0000'),
    ('Introduction aux Systemes d exploitation', 0, 1, '04', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#FF0000'),
    ('Introduction aux bases de donnees SQL', 0, 1, '05', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#FF0000'),
    --Ressources transversales (RT)
    ('Mathematiques Discretes', 0, 1, '06', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    ('Outils Mathematiques Fondamentaux', 0, 1, '07', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    ('Gestion de projet et des organisations', 0, 1, '08', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    ('economie durable et numerique', 0, 1, '09', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    ('Anglais Technique', 0, 1, '10', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    ('Bases de la Communication', 0, 1, '11', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    ('Projet professionnel et personnel', 0, 1, '12', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),

    -- SAE
    ('Implementation d un besoin client', 0, 1, '01', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#0000FF'),
    ('Comparaison d approches algorithmiques', 0, 1, '02', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#0000FF'),
    ('Installation d un poste pour le developpement', 0, 1, '03', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#0000FF'),
    ('Creation d une base de donnees', 0, 1, '04', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#0000FF'),
    ('Recueil de besoins / Decouverte de l environnement economique et ecologique', 0, 1, '05&06', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#0000FF'),

    --Semestre 2 INFO
    --Ressources cœur de competences (RCC)
    ('Developpement oriente objets', 0, 2, '01', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#FF0000'),
    ('Developpement d applications avec IHM', 0, 2, '02', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#FF0000'),
    ('Qualite de developpement', 0, 2, '03', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#FF0000'),
    ('Communication et fonctionnement bas niveau', 0, 2, '04', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#FF0000'),
    ('Introduction aux services reseaux', 0, 2, '05', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#FF0000'),
    ('Exploitation d une base de donnees', 0, 2, '06', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#FF0000'),
    --Ressources transversales (RT)
    ('Graphes', 0, 2, '07', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    ('Outils numeriques pour les statistiques descriptives', 0, 2, '08', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    ('Methodes numeriques', 0, 2, '09', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    ('Gestion de projet et des organisations', 0, 2, '10', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    ('Droit des contrats et du numerique', 0, 2, '11', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    ('Anglais d entreprise', 0, 2, '13', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    ('Communication avec le milieu professionnel', 0, 2, '14', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    ('PPP : Metiers de l informatique', 0, 2, '15', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    -- SAE
    ('Developpement d une application', 0, 2, '01', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#0000FF'),
    ('Exploration algorithmique d un probleme', 0, 2, '02', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#0000FF'),
    ('Installation de services reseau', 0, 2, '03', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#0000FF'),
    ('Exploitation d une base de donnees', 0, 2, '04', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#0000FF'),
    ('Gestion d un projet', 0, 2, '05', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#0000FF'),
    ('Organisation d un travail d equipe', 0, 2, '06', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#0000FF'),

    --Semestre 3 INFO
    --Ressources cœur de competences (RCC)
    ('Developpement Web', 0, 3, '01', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#FF0000'),
    ('Developpement efficace et Qualite', 0, 3, '02&04', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#FF0000'),
    ('Programmation Systeme', 0, 3, '05', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#FF0000'),
    ('Architecture des Reseaux', 0, 3, '06', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#FF0000'),
    ('SQL et Programmation', 0, 3, '07', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#FF0000'),
    --Ressources transversales (RT)
    ('Analyse', 0, 3, '03', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    ('Probabilites', 0, 3, '08', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    ('Cryptographie', 0, 3, '09', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    ('Management des Systemes d Information', 0, 3, '10', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    ('Droits des contrats et du numerique', 0, 3, '11', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    ('Anglais', 0, 3, '12', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    ('Anglais Apprentis', 0, 3, '12.app', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    ('Communication Professionnelle', 0, 3, '13', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    ('PPP', 0, 3, '14', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    ('Outils Mathematiques Fondamentaux', 0, 3, '15', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    ('Anglais pour les projets internationaux', 0, 3, '16', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    ('Anglais pour les projets internationaux [Apprentis - initiauxTDB]', 0, 3, '16.app', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO'), '#00FF00'),
    -- SAE

    --Semestre 4 INFO
    --TRONC COMMUN
    --Ressources cœur de competences (RCC)
    ('Architecture Logicielle', 0, 4, '01', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO_TC'), '#FF0000'),
    ('Qualite Du Developpement', 0, 4, '02', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO_TC'), '#FF0000'),
    ('Qualite & Non-Relationnel', 0, 4, '03', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO_TC'), '#FF0000'),
    --Ressources transversales (RT)
    ('Methodes d Optimisation', 0, 4, '04', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_TC'), '#00FF00'),
    ('Anglais', 0, 4, '05', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_TC'), '#00FF00'),
    ('Anglais Apprentis', 0, 4, '05.app', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_TC'), '#00FF00'),
    ('Comm. Interne', 0, 4, '06', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_TC'), '#00FF00'),
    ('PPP', 0, 4, '07', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_TC'), '#00FF00'),
    --Parcours A
    --Ressources cœur de competences (RCC)
    ('Complements Web', 0, 4, '10', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO_A'), '#FF0000'),
    ('Developpement Mobile', 0, 4, '11', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO_A'), '#FF0000'),
    --Ressources transversales (RT)
    ('Virtualisation', 0, 4, '08', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_A'), '#FF0000'),
    ('Management Avance de SI', 0, 4, '09', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_A'), '#FF0000'),
    ('Automates', 0, 4, '12', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_A'), '#FF0000'),
    --Parcours C
    --Ressources cœur de competences (RCC)
    ('Cryptographie et Securite', 0, 4, '08', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO_C'), '#FF0000'),
    ('Reseau Avance', 0, 4, '09', 'RCC', (SELECT id FROM university.specializations WHERE code = 'INFO_C'), '#FF0000'),
    --Ressources transversales (RT)
    ('Analyse et Visualisation', 0, 4, '10', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_C'), '#FF0000'),
    ('Management Avance de SI', 0, 4, '11', 'RT', (SELECT id FROM university.specializations WHERE code = 'INFO_C'), '#FF0000'),
    -- SAE
    ('Developpement d une application web', 0, 4, '01', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO_A'), '#FF0000'),
    ('Developpement avec Base de Donnees', 0, 4, '01', 'SAE', (SELECT id FROM university.specializations WHERE code = 'INFO_C'), '#FF0000')
;