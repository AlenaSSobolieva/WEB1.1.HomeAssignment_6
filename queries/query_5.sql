-- Find what courses a specific teacher teaches.
SELECT Subject.name AS course_name
FROM Subject
WHERE Subject.teacher_id = 1;
