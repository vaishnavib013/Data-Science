/*CREATE TABLE student(
	grade_id SERIAL PRIMARY KEY,
	student_id INTEGER,
	course_id INTEGER,
	grade FLOAT,
	grade_date DATE
	);
*/

/*
INSERT INTO student
(student_id,course_id,grade,grade_date)
VALUES
(1, 101, 85.5, '2024-01-15'),
	(1, 102, 78.0, '2024-02-20'),
	(2, 101, 92.0, '2024-01-15'),
	(2, 103, 88.5, '2024-03-10'), 
	(3, 102, 74.0, '2024-02-20'), 
	(3, 103, 81.5, '2024-03-10'), 
	(4, 101, 67.0, '2024-01-15'), 
	(4, 104, 90.0, '2024-04-05'), 
	(5, 102, 85.0, '2024-02-20'), 
	(5, 104, 87.0, '2024-04-05');
*/

--SELECT * FROM student;


--THIS IS FOR ABOVE 60 (NOT IN ASSIGNMENT)
SELECT student_id,AVG(grade)
FROM student
GROUP BY student_id
HAVING AVG(grade)>60;

--THIS IS FOR BELOW PASSING 80 
SELECT student_id,AVG(grade)
FROM student
GROUP BY student_id
HAVING AVG(grade)<80;
