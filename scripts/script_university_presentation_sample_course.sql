
--INFO Course for promotion 1 
-- For the date 2023-12-15 09:00:00 (YYYY/MM/DD %H:%M)
INSERT INTO university.courses (starttime, endtime, course_type, rooms_id, teaching_id,personal_id)
VALUES
	('2023-12-15 09:00:00', '2023-12-15 10:05:00', 'TP', 
		(SELECT id FROM university.rooms WHERE code = 'A2-05'),
		(SELECT id FROM university.teachings WHERE title = 'Introduction aux Systemes d exploitation' and semestre = 1),
		(SELECT id FROM university.personals WHERE mail = 'g.delmas@iut.univ-paris8.fr')),
	('2023-12-15 09:00:00', '2023-12-15 10:05:00', 'TP', 
		(SELECT id FROM university.rooms WHERE code = 'A2-03'),
		(SELECT id FROM university.teachings WHERE title = 'Anglais Technique' and semestre = 1),
		(SELECT id FROM university.personals WHERE mail = 'c.ballay_dally@iut.univ-paris8.fr')),
	('2023-12-15 09:00:00', '2023-12-15 10:05:00', 'TD', 
		(SELECT id FROM university.rooms WHERE code = 'A2-04'),
		(SELECT id FROM university.teachings WHERE title = 'Projet professionnel et personnel' and semestre = 1),
		(SELECT id FROM university.personals WHERE mail = 'v.clement-comparot@iut.univ-paris8.fr')),
	('2023-12-15 09:00:00', '2023-12-15 10:05:00', 'TD', 
		(SELECT id FROM university.rooms WHERE code = 'A2-03'),
		(SELECT id FROM university.teachings WHERE title = 'Introduction a l Architecture des Ordinateurs' and semestre = 1),
		(SELECT id FROM university.personals WHERE mail = 'g.delmas@iut.univ-paris8.fr'))
;

-- For the date 2023-12-15 10:00:00 (YYYY/MM/DD %H:%M)
INSERT INTO university.courses (starttime, endtime, course_type, rooms_id, teaching_id,personal_id)
VALUES
	('2023-12-15 10:00:00', '2023-12-15 12:15:00', 'TD', 
		(SELECT id FROM university.rooms WHERE code = 'B1-09'),
		(SELECT id FROM university.teachings WHERE title = 'Introduction aux bases de donnees SQL' and semestre = 1),
		(SELECT id FROM university.personals WHERE mail = 'm.cataldi@iut.univ-paris8.fr')),
	('2023-12-15 10:00:00', '2023-12-15 12:15:00', 'TP', 
		(SELECT id FROM university.rooms WHERE code = 'B1-14'),
		(SELECT id FROM university.teachings WHERE title = 'Introduction aux bases de donnees SQL' and semestre = 1),
		(SELECT id FROM university.personals WHERE mail = 'm.lamolle@iut.univ-paris8.fr')),
	('2023-12-15 10:00:00', '2023-12-15 12:15:00', 'TP', 
		(SELECT id FROM university.rooms WHERE code = 'B1-14'),
		(SELECT id FROM university.teachings WHERE title = 'Developpement d interfaces web' and semestre = 1),
		(SELECT id FROM university.personals WHERE mail = 'a.bossard@iut.univ-paris8.fr')),
	('2023-12-15 10:00:00', '2023-12-15 12:15:00', 'TP', 
		(SELECT id FROM university.rooms WHERE code = 'F1-02'),
		(SELECT id FROM university.teachings WHERE title = 'Initiation au developpement' and semestre = 1),
		(SELECT id FROM university.personals WHERE mail = 'm.simonot@iut.univ-paris8.fr'))
;

-- For the date 2023-12-15 11:00:00 (YYYY/MM/DD %H:%M)
INSERT INTO university.courses (starttime, endtime, course_type, rooms_id, teaching_id,personal_id)
VALUES
	('2023-12-15 11:00:00', '2023-12-15 12:05:00', 'cours', 
		(SELECT id FROM university.rooms WHERE code = 'Amphi'),
		(SELECT id FROM university.teachings WHERE title = 'economie durable et numerique' and semestre = 1),
		(SELECT id FROM university.personals WHERE mail = 'v.clement-comparot@iut.univ-paris8.fr'))
;

-- For the date 2023-12-15 12:00:00 (YYYY/MM/DD %H:%M)
INSERT INTO university.courses (starttime, endtime, course_type, rooms_id, teaching_id,personal_id)
VALUES
	('2023-12-15 13:00:00', '2023-12-15 14:15:00', 'TD', 
		(SELECT id FROM university.rooms WHERE code = 'D0-02'),
		(SELECT id FROM university.teachings WHERE title = 'Gestion de projet et des organisations' and semestre = 1),
		(SELECT id FROM university.personals WHERE mail = 'v.clement-comparot@iut.univ-paris8.fr')),
	('2023-12-15 13:00:00', '2023-12-15 14:15:00', 'TD', 
		(SELECT id FROM university.rooms WHERE code = 'D0-02'),
		(SELECT id FROM university.teachings WHERE title = 'Introduction a l Architecture des Ordinateurs' and semestre = 1),
		(SELECT id FROM university.personals WHERE mail = 'a.bossard@iut.univ-paris8.fr')),
	('2023-12-15 13:00:00', '2023-12-15 14:15:00', 'TP', 
		(SELECT id FROM university.rooms WHERE code = 'B1-10'),
		(SELECT id FROM university.teachings WHERE title = 'Mathematiques Discretes' and semestre = 1),
		(SELECT id FROM university.personals WHERE mail = 'm.homps@iut.univ-paris8.fr')),
	('2023-12-15 13:00:00', '2023-12-15 14:15:00', 'TD', 
		(SELECT id FROM university.rooms WHERE code = 'B1-14'),
		(SELECT id FROM university.teachings WHERE title = 'Projet professionnel et personnel' and semestre = 1),
		(SELECT id FROM university.personals WHERE mail = 'v.clement-comparot@iut.univ-paris8.fr'))
;

-- For the date 2023-12-15 14:00:00 (YYYY/MM/DD %H:%M)
INSERT INTO university.courses (starttime, endtime, course_type, rooms_id, teaching_id,personal_id)
VALUES
	('2023-12-15 15:00:00', '2023-12-15 16:00:00', 'cours', 
		(SELECT id FROM university.rooms WHERE code = 'F2-03'),
		(SELECT id FROM university.teachings WHERE title = 'Introduction a l Architecture des Ordinateurs' and semestre = 1),
		(SELECT id FROM university.personals WHERE mail = 'g.delmas@iut.univ-paris8.fr'))
;

-- For the date 2023-12-15 16:00:00 (YYYY/MM/DD %H:%M)
INSERT INTO university.courses (starttime, endtime, course_type, rooms_id, teaching_id,personal_id)
VALUES
	('2023-12-15 16:00:00', '2023-12-15 17:00:00', 'cours', 
		(SELECT id FROM university.rooms WHERE code = 'F2-02'),
		(SELECT id FROM university.teachings WHERE title = 'Introduction aux Systemes d exploitation' and semestre = 1),
		(SELECT id FROM university.personals WHERE mail = 'g.delmas@iut.univ-paris8.fr'))
;

-- For the date 2023-12-15 17:00:00 (YYYY/MM/DD %H:%M)
INSERT INTO university.courses (starttime, endtime, course_type, rooms_id, teaching_id,personal_id)
VALUES
	('2023-12-15 17:00:00', '2023-12-15 18:00:00', 'TD', 
		(SELECT id FROM university.rooms WHERE code = 'B1-10'),
		(SELECT id FROM university.teachings WHERE title = 'Outils Mathematiques Fondamentaux' and semestre = 1),
		(SELECT id FROM university.personals WHERE mail = 'a.ricordeau@iut.univ-paris8.fr')),
	('2023-12-15 17:00:00', '2023-12-15 18:00:00', 'TP', 
		(SELECT id FROM university.rooms WHERE code = 'A2-03'),
		(SELECT id FROM university.teachings WHERE title = 'economie durable et numerique' and semestre = 1),
		(SELECT id FROM university.personals WHERE mail = 'v.clement-comparot@iut.univ-paris8.fr')),
	('2023-12-15 17:00:00', '2023-12-15 18:00:00', 'TP', 
		(SELECT id FROM university.rooms WHERE code = 'A2-04'),
		(SELECT id FROM university.teachings WHERE title = 'Introduction aux Systemes d exploitation' and semestre = 1),
		(SELECT id FROM university.personals WHERE mail = 'n.nauwynck@iut.univ-paris8.fr')),
	('2023-12-15 17:00:00', '2023-12-15 18:00:00', 'TP', 
		(SELECT id FROM university.rooms WHERE code = 'A2-03'),
		(SELECT id FROM university.teachings WHERE title = 'Mathematiques Discretes' and semestre = 1),
		(SELECT id FROM university.personals WHERE mail = 'm.homps@iut.univ-paris8.fr'))
;

-- For the date 2023-12-15 18:00:00 (YYYY/MM/DD %H:%M)
INSERT INTO university.courses (starttime, endtime, course_type, rooms_id, teaching_id,personal_id)
VALUES
	('2023-12-15 18:00:00', '2023-12-15 20:05:00', 'TD', 
		(SELECT id FROM university.rooms WHERE code = 'B1-13'),
		(SELECT id FROM university.teachings WHERE title = 'Bases de la Communication' and semestre = 1),
		(SELECT id FROM university.personals WHERE mail = 'v.clement-comparot@iut.univ-paris8.fr')),
	('2023-12-15 18:00:00', '2023-12-15 20:05:00', 'TP', 
		(SELECT id FROM university.rooms WHERE code = 'B1-14'),
		(SELECT id FROM university.teachings WHERE title = 'Gestion de projet et des organisations' and semestre = 1),
		(SELECT id FROM university.personals WHERE mail = 'v.clement-comparot@iut.univ-paris8.fr')),
	('2023-12-15 18:00:00', '2023-12-15 20:05:00', 'TP', 
		(SELECT id FROM university.rooms WHERE code = 'F2-01'),
		(SELECT id FROM university.teachings WHERE title = 'economie durable et numerique' and semestre = 1),
		(SELECT id FROM university.personals WHERE mail = 'v.clement-comparot@iut.univ-paris8.fr')),
	('2023-12-15 18:00:00', '2023-12-15 20:05:00', 'TD', 
		(SELECT id FROM university.rooms WHERE code = 'A2-04'),
		(SELECT id FROM university.teachings WHERE title = 'Anglais Technique' and semestre = 1),
		(SELECT id FROM university.personals WHERE mail = 'c.ballay_dally@iut.univ-paris8.fr'))
;

-- INFO Course for promotion 3 
-- For the date 2023-12-15 09:00:00 (YYYY/MM/DD %H:%M)
INSERT INTO university.courses (starttime, endtime, course_type, rooms_id, teaching_id,personal_id)
VALUES
	('2023-12-15 09:00:00', '2023-12-15 10:30:00', 'cours', 
		(SELECT id FROM university.rooms WHERE code = 'F1-03 (Langues)'),
		(SELECT id FROM university.teachings WHERE title = 'Anglais' and semestre = 3),
		(SELECT id FROM university.personals WHERE mail = 'c.ballay_dally@iut.univ-paris8.fr'))
;

-- For the date 2023-12-15 10:00:00 (YYYY/MM/DD %H:%M)
INSERT INTO university.courses (starttime, endtime, course_type, rooms_id, teaching_id,personal_id)
VALUES
	('2023-12-15 10:00:00', '2023-12-15 12:15:00', 'cours', 
		(SELECT id FROM university.rooms WHERE code = 'A1-01'),
		(SELECT id FROM university.teachings WHERE title = 'SQL et Programmation' and semestre = 3),
		(SELECT id FROM university.personals WHERE mail = 'm.lamolle@iut.univ-paris8.fr'))
;

-- For the date 2023-12-15 11:00:00 (YYYY/MM/DD %H:%M)
INSERT INTO university.courses (starttime, endtime, course_type, rooms_id, teaching_id,personal_id)
VALUES
	('2023-12-15 11:00:00', '2023-12-15 12:05:00', 'TP', 
		(SELECT id FROM university.rooms WHERE code = 'F2-03'),
		(SELECT id FROM university.teachings WHERE title = 'Management des Systemes d Information' and semestre = 3),
		(SELECT id FROM university.personals WHERE mail = 'v.clement-comparot@iut.univ-paris8.fr')),
	('2023-12-15 11:00:00', '2023-12-15 12:05:00', 'TP', 
		(SELECT id FROM university.rooms WHERE code = 'A2-01'),
		(SELECT id FROM university.teachings WHERE title = 'Outils Mathematiques Fondamentaux' and semestre = 3),
		(SELECT id FROM university.personals WHERE mail = 'a.ricordeau@iut.univ-paris8.fr')),
	('2023-12-15 11:00:00', '2023-12-15 12:05:00', 'TD', 
		(SELECT id FROM university.rooms WHERE code = 'B1-10'),
		(SELECT id FROM university.teachings WHERE title = 'Outils Mathematiques Fondamentaux' and semestre = 3),
		(SELECT id FROM university.personals WHERE mail = 'a.ricordeau@iut.univ-paris8.fr')),
	('2023-12-15 11:00:00', '2023-12-15 12:05:00', 'TD', 
		(SELECT id FROM university.rooms WHERE code = 'B1-13'),
		(SELECT id FROM university.teachings WHERE title = 'Communication Professionnelle' and semestre = 3),
		(SELECT id FROM university.personals WHERE mail = 'v.clement-comparot@iut.univ-paris8.fr'))
;

-- For the date 2023-12-15 12:00:00 (YYYY/MM/DD %H:%M)
INSERT INTO university.courses (starttime, endtime, course_type, rooms_id, teaching_id,personal_id)
VALUES
	('2023-12-15 13:00:00', '2023-12-15 14:05:00', 'cours', 
		(SELECT id FROM university.rooms WHERE code = 'D1-10'),
		(SELECT id FROM university.teachings WHERE title = 'SQL et Programmation' and semestre = 3),
		(SELECT id FROM university.personals WHERE mail = 'm.cataldi@iut.univ-paris8.fr'))
;

-- For the date 2023-12-15 14:00:00 (YYYY/MM/DD %H:%M)
INSERT INTO university.courses (starttime, endtime, course_type, rooms_id, teaching_id,personal_id)
VALUES
	('2023-12-15 15:00:00', '2023-12-15 16:15:00', 'TP', 
		(SELECT id FROM university.rooms WHERE code = 'B0-03'),
		(SELECT id FROM university.teachings WHERE title = 'Anglais' and semestre = 3),
		(SELECT id FROM university.personals WHERE mail = 'c.ballay_dally@iut.univ-paris8.fr')),
	('2023-12-15 15:00:00', '2023-12-15 16:15:00', 'TD', 
		(SELECT id FROM university.rooms WHERE code = 'A1-01'),
		(SELECT id FROM university.teachings WHERE title = 'Developpement efficace et Qualite' and semestre = 3),
		(SELECT id FROM university.personals WHERE mail = 'j.rety@iut.univ-paris8.fr')),
	('2023-12-15 15:00:00', '2023-12-15 16:15:00', 'TD', 
		(SELECT id FROM university.rooms WHERE code = 'B0-03'),
		(SELECT id FROM university.teachings WHERE title = 'Outils Mathematiques Fondamentaux' and semestre = 3),
		(SELECT id FROM university.personals WHERE mail = 'p.bonnot@iut.univ-paris8.fr')),
	('2023-12-15 15:00:00', '2023-12-15 16:15:00', 'TP', 
		(SELECT id FROM university.rooms WHERE code = 'F1-02'),
		(SELECT id FROM university.teachings WHERE title = 'Management des Systemes d Information' and semestre = 3),
		(SELECT id FROM university.personals WHERE mail = 'v.clement-comparot@iut.univ-paris8.fr'))
;

-- For the date 2023-12-15 16:00:00 (YYYY/MM/DD %H:%M)
INSERT INTO university.courses (starttime, endtime, course_type, rooms_id, teaching_id,personal_id)
VALUES
	('2023-12-15 16:00:00', '2023-12-15 17:00:00', 'cours', 
		(SELECT id FROM university.rooms WHERE code = 'F1-03 (Langues)'),
		(SELECT id FROM university.teachings WHERE title = 'Cryptographie' and semestre = 3),
		(SELECT id FROM university.personals WHERE mail = 'm.homps@iut.univ-paris8.fr'))
;

-- For the date 2023-12-15 17:00:00 (YYYY/MM/DD %H:%M)
INSERT INTO university.courses (starttime, endtime, course_type, rooms_id, teaching_id,personal_id)
VALUES
	('2023-12-15 17:00:00', '2023-12-15 18:30:00', 'TD', 
		(SELECT id FROM university.rooms WHERE code = 'B1-09'),
		(SELECT id FROM university.teachings WHERE title = 'Developpement efficace et Qualite' and semestre = 3),
		(SELECT id FROM university.personals WHERE mail = 'p.bonnot@iut.univ-paris8.fr')),
	('2023-12-15 17:00:00', '2023-12-15 18:30:00', 'TP', 
		(SELECT id FROM university.rooms WHERE code = 'B1-10'),
		(SELECT id FROM university.teachings WHERE title = 'Outils Mathematiques Fondamentaux' and semestre = 3),
		(SELECT id FROM university.personals WHERE mail = 'p.bonnot@iut.univ-paris8.fr')),
	('2023-12-15 17:00:00', '2023-12-15 18:30:00', 'TP', 
		(SELECT id FROM university.rooms WHERE code = 'A2-03'),
		(SELECT id FROM university.teachings WHERE title = 'Developpement efficace et Qualite' and semestre = 3),
		(SELECT id FROM university.personals WHERE mail = 'j.rety@iut.univ-paris8.fr')),
	('2023-12-15 17:00:00', '2023-12-15 18:30:00', 'TD', 
		(SELECT id FROM university.rooms WHERE code = 'B0-03'),
		(SELECT id FROM university.teachings WHERE title = 'Probabilites' and semestre = 3),
		(SELECT id FROM university.personals WHERE mail = 'a.ricordeau@iut.univ-paris8.fr'))
;

-- For the date 2023-12-15 18:00:00 (YYYY/MM/DD %H:%M)
INSERT INTO university.courses (starttime, endtime, course_type, rooms_id, teaching_id,personal_id)
VALUES
	('2023-12-15 18:00:00', '2023-12-15 19:30:00', 'TP', 
		(SELECT id FROM university.rooms WHERE code = 'D1-11 (Langues)'),
		(SELECT id FROM university.teachings WHERE title = 'Architecture des Reseaux' and semestre = 3),
		(SELECT id FROM university.personals WHERE mail = 'g.delmas@iut.univ-paris8.fr')),
	('2023-12-15 18:00:00', '2023-12-15 19:30:00', 'TD', 
		(SELECT id FROM university.rooms WHERE code = 'B0-01'),
		(SELECT id FROM university.teachings WHERE title = 'Programmation Systeme' and semestre = 3),
		(SELECT id FROM university.personals WHERE mail = 'g.delmas@iut.univ-paris8.fr')),
	('2023-12-15 18:00:00', '2023-12-15 19:30:00', 'TD', 
		(SELECT id FROM university.rooms WHERE code = 'Salle Visio'),
		(SELECT id FROM university.teachings WHERE title = 'Developpement efficace et Qualite' and semestre = 3),
		(SELECT id FROM university.personals WHERE mail = 'm.simonot@iut.univ-paris8.fr')),
	('2023-12-15 18:00:00', '2023-12-15 19:30:00', 'TD', 
		(SELECT id FROM university.rooms WHERE code = 'Salle Visio'),
		(SELECT id FROM university.teachings WHERE title = 'SQL et Programmation' and semestre = 3),
		(SELECT id FROM university.personals WHERE mail = 'm.cataldi@iut.univ-paris8.fr'))
;
