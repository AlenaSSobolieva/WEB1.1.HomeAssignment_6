-- A list of courses taught to a student by a specific teacher.
SELECT Subject.name AS course_name
FROM Student
JOIN Grade ON Student.student_id = Grade.student_id
JOIN Subject ON Grade.subject_id = Subject.subject_id
WHERE Student.name = '[STUDENT_NAME]'
  AND Subject.teacher_id = [SPECIFIC_TEACHER_ID];
