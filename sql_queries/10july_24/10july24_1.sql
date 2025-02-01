--update job set jab_name=job_name;

--UPDATE
--SELECT *  FROM job;
/*INSERT INTO job (jab_name)
VALUES ('Cowboy');

SELECT * FROM job;
*/

/*DELETE FROM job
WHERE jab_name='Cowboy'
RETURNING job_id,jab_name;
*/
--SELECT * FROM job;

--ALTER

/*CREATE TABLE information(
	info_id SERIAL PRIMARY KEY,
	title VARCHAR(500) NOT NULL,
	person VARCHAR(50) NOT NULL UNIQUE
);
*/
/*ALTER TABLE information
RENAME to new_info;
*/
--SELECT * FROM information;--error

--SELECT * FROM new_info;

/*ALTER TABLE new_info
RENAME COLUMN person TO people;
*/
/*
INSERT INTO new_info
VALUES
	('SOME NEW TITLE'); */

/*ALTER TABLE new_info
	ALTER COLUMN people DROP NOT NULL;
*/

/*INSERT INTO new_info(title)
VALUES('SOME NEW TITLE');

SELECT * FROM new_info;
*/

--SELECT * FROM new_info;

/*ALTER TABLE new_info
DROP COLUMN people;

SELECT * FROM new_info;*/

/*ALTER TABLE new_info
DROP COLUMN if exists people;

SELECT * FROM new_info*/

/*
CREATE TABLE employees(
	emp_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	birthdate DATE CHECK (birthdate > '1900-01-01'),
	hire_date DATE CHECK(hire_date > birthdate),
	salary INTEGER CHECK (salary >0)
	);
*/

/*INSERT INTO employees(first_name,last_name,birthdate,hire_date,salary)
VALUES
('Jose','Portilla','1899-11-03','2010-01-01',100);
*/
/*INSERT INTO employees(first_name,last_name,birthdate,hire_date,salary)
VALUES
('Jose','Portilla','1990-11-03','2010-01-01',100);
*/

--select * from employees;

/*INSERT INTO employees(first_name,last_name,birthdate,hire_date,salary)
VALUES
('Sammy','SMITH','1990-11-03','2010-01-01',-100);
it gives error*/

/*INSERT INTO employees(first_name,last_name,birthdate,hire_date,salary)
VALUES
('Sammy','SMITH','1990-11-03','2010-01-01',100);
*/

--check ends


--case expression

select * from employees;