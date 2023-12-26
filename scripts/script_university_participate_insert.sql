
-- Insert records with subgroup_id as 0
INSERT INTO university.participates (course_id, subgroup_id)
SELECT
    n AS course_id,
    1 AS subgroup_id
FROM
    generate_series(1, 5) n
;