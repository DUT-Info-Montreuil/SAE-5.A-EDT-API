
INSERT INTO university.courses (starttime, endtime, course_type, teaching_id)
VALUES
	('2023-12-09 08:00:00', '2023-12-09 11:00:00', 'Projet', 12),
	('2023-12-09 11:00:00', '2023-12-09 13:00:00', 'cours', 10),
	('2023-12-09 13:00:00', '2023-12-09 14:00:00', 'cours', 7),
	('2023-12-09 14:00:00', '2023-12-09 17:00:00', 'rattrapage', 4)
;
INSERT INTO university.courses (starttime, endtime, course_type, teaching_id)
VALUES
	('2023-12-09 08:00:00', '2023-12-09 10:00:00', 'cours', 15),
	('2023-12-09 10:00:00', '2023-12-09 13:00:00', 'TP', 18),
	('2023-12-09 13:00:00', '2023-12-09 14:00:00', 'controles', 8),
	('2023-12-09 14:00:00', '2023-12-09 17:00:00', 'cours', 7)
;

INSERT INTO university.courses (starttime, endtime, course_type, teaching_id)
VALUES
	('2023-12-09 08:00:00', '2023-12-09 10:00:00', 'TD', 10),
	('2023-12-09 10:00:00', '2023-12-09 12:00:00', 'controles', 14),
	('2023-12-09 12:00:00', '2023-12-09 14:00:00', 'controles', 18),
	('2023-12-09 14:00:00', '2023-12-09 15:00:00', 'TP', 20),
	('2023-12-09 15:00:00', '2023-12-09 17:00:00', 'controles', 19)
;

INSERT INTO university.courses (starttime, endtime, course_type, teaching_id)
VALUES
	('2023-12-09 08:00:00', '2023-12-09 10:00:00', 'TD', 4),
	('2023-12-09 10:00:00', '2023-12-09 12:00:00', 'controles', 17),
	('2023-12-09 12:00:00', '2023-12-09 14:00:00', 'TP', 11),
	('2023-12-09 14:00:00', '2023-12-09 16:00:00', 'TP', 19)
;

INSERT INTO university.courses (starttime, endtime, course_type, teaching_id)
VALUES
	('2023-12-09 08:00:00', '2023-12-09 11:00:00', 'Projet', 16),
	('2023-12-09 11:00:00', '2023-12-09 14:00:00', 'controles', 8),
	('2023-12-09 14:00:00', '2023-12-09 15:00:00', 'rattrapage', 11),
	('2023-12-09 15:00:00', '2023-12-09 17:00:00', 'cours', 19)
;

INSERT INTO university.courses (starttime, endtime, course_type, teaching_id)
VALUES
	('2023-12-09 08:00:00', '2023-12-09 11:00:00', 'cours', 8),
	('2023-12-09 11:00:00', '2023-12-09 13:00:00', 'Projet', 12),
	('2023-12-09 13:00:00', '2023-12-09 16:00:00', 'TD', 17)
;

INSERT INTO university.courses (starttime, endtime, course_type, teaching_id)
VALUES
	('2023-12-09 08:00:00', '2023-12-09 09:00:00', 'rattrapage', 13),
	('2023-12-09 09:00:00', '2023-12-09 11:00:00', 'TP', 13),
	('2023-12-09 11:00:00', '2023-12-09 13:00:00', 'TP', 6),
	('2023-12-09 13:00:00', '2023-12-09 14:00:00', 'TD', 9),
	('2023-12-09 14:00:00', '2023-12-09 17:00:00', 'cours', 9)
;

INSERT INTO university.rooms_courses (course_id, rooms_id)
VALUES
    (1, 1),
    (1, 2), 
    (3, 2), 
	(3, 1),
    (4, 4)
;

INSERT INTO university.personals_courses (course_id, personal_id)
VALUES
    (2, 1),
    (2, 2), 
    (4, 2), 
	(4, 1),
    (6, 4)
;