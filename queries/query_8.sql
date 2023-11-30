-- Find the average grade given by a certain teacher in his subjects.
SELECT AVG(Grade.score) AS average_score
FROM Grade
JOIN Subject ON Grade.subject_id = Subject.subject_id
WHERE Subject.teacher_id = 5;
