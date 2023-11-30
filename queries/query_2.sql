-- Find a student with a high GPA in a specific subject.
SELECT Student.name, AVG(Grade.score) AS average_score
FROM Student
JOIN Grade ON Student.student_id = Grade.student_id
WHERE Grade.subject_id = 1
GROUP BY Student.student_id
ORDER BY average_score DESC
LIMIT 1;

