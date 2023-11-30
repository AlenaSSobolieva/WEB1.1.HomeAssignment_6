-- Find a list of courses the student is taking.
SELECT Subject.name AS course_name
FROM Student
JOIN Grade ON Student.student_id = Grade.student_id
JOIN Subject ON Grade.subject_id = Subject.subject_id
WHERE Student.name = 'Matthew Gardner';
