--SHOW TIMEZONE;

/*CREATE TABLE timezones(
	ts TIMESTAMP WITHOUT TIME ZONE,
	tz TIMESTAMP WITH TIME ZONE
)
*/

/*INSERT INTO TIMEZONES VALUES(
	TIMESTAMP WITHOUT TIME ZONE '2023-03-07 10:50',
	TIMESTAMP WITH TIME ZONE '2023-03-07 10:50'
)
*/

--SELECT * FROM timezones;

/*SELECT now()::date;
SELECT CURRENT_DATE
*/
--SELECT TO_CHAR(CURRENT_DATE,'dd/mm/yy')

--SELECT TO_CHAR(CURRENT_DATE,'DDD')

--SELECT TO_CHAR(CURRENT_DATE,'WW')

--SELECT AGE(date'1800-01-01')

--SELECT AGE(date '1992/11/13',date'1800/01/01')

--SELECT EXTRACT(DAY FROM date'1992/11/13')AS DAY

--SELECT EXTRACT(MONTH FROM date'1992/11/13')AS MONTH

--SELECT EXTRACT(YEAR FROM date'1992/11/13')AS YEAR

--SELECT DATE_TRUNC('year',date'1992/11/13')

--quesries
/*SELECT AGE(birth_date),*FROM employees
WHERE (
	EXTRACT(YEAR FROM AGE(birth_date))
)>60;
*/

/*SELECT COUNT(birth_date) FROM employees
WHERE birth_date<now()-interval '61 years'
*/
/*SELECT COUNT(emp_no)FROM employees
where EXTRACT(MONTH FROM hire_date)=2;*/

/*SELECT COUNT(emp_no)FROM employees
where EXTRACT(MONTH FROM birth_date)=11;
*/
--SELECT MAX(AGE(birth_date)) FROM employees;

--SELECT MAX(salary) FROM salaries;

/*SELECT *,
	MAX(salary) 
	FROM salaries;

this gives error
*/
/*SELECT *,
	MAX(salary) OVER() 
	FROM salaries;

SELECT *,
	MAX(salary) OVER() 
	FROM salaries
	LIMIT 100;

SELECT *,
	MAX(salary) OVER() 
	FROM salaries
	WHERE salary<70000;
*/

--PARTITION
/*SELECT *,
	AVG(salary) OVER()
FROM salaries;
*/

/*SELECT *,
	d.dept_name,
	AVG(salary) OVER()
FROM salaries
JOIN dept_emp AS de using (emp_no)
JOIN departments AS d USING (dept_no)
*/
/*SELECT *,
	d.dept_name,
	AVG(salary) OVER(
	PARTITION BY d.dept_name
	)
FROM salaries
JOIN dept_emp AS de using (emp_no)
JOIN departments AS d USING (dept_no)
*/

/*SELECT *,
	AVG(salary) OVER(
	PARTITION BY d.dept_name
	)
FROM salaries
JOIN dept_emp AS de using (emp_no)
*/
JOIN departments AS d USING (dept_no)