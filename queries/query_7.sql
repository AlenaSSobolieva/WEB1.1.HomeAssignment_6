-- Find the grades of students in a specific group in a specific subject.
SELECT Student.name, Grade.score
FROM Student
JOIN Grade ON Student.student_id = Grade.student_id
WHERE Student.group_id = 1
  AND Grade.subject_id = 2;
