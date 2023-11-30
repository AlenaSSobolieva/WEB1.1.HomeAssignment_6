-- Find the 5 students with the highest average scores in all subjects.
SELECT Student.name, AVG(Grade.score) AS average_score
FROM Student
JOIN Grade ON Student.student_id = Grade.student_id
GROUP BY Student.student_id
ORDER BY average_score DESC
LIMIT 5;
