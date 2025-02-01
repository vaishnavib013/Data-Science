/*CREATE TABLE acount(
	user_id SERIAL PRIMARY KEY,
	username VARCHAR(50) UNIQUE NOT NULL,
	password VARCHAR(50) NOT NULL,
	email VARCHAR(50) UNIQUE NOT NULL,
	create_on TIMESTAMP NOT NULL,
	last_login TIMESTAMP);*/


/*CREATE TABLE job(
	job_id SERIAL PRIMARY KEY,
	jab_name VARCHAR(200) UNIQUE NOT NULL);*/

/*CREATE TABLE account_job(
	user_id INTEGER REFERENCES acount(user_id)
	);
*/

/*CREATE TABLE account_job1(
	user_id INTEGER REFERENCES acount(user_id),
	job_id INTEGER REFERENCES job(job_id),
	hire_date TIMESTAMP
);
*/

--SELECT * FROM acount;

/*INSERT INTO acount(username,password,email,create_on)
VALUES
('Jose12','password1','jose1@gmail.com',CURRENT_TIMESTAMP);*/

--SELECT * FROM acount;

/*INSERT INTO job(jab_name)
VALUES
('Astronaut');

insert into job(jab_name)
values
('President');*/
--SELECT * FROM job;

/*INSERT INTO account_job1(user_id,job_id,hire_date)
VALUES
(1,1,CURRENT_TIMESTAMP);*/
--SELECT * FROM account_job1;

/*INSERT INTO account_job1(user_id,job_id,hire_date)
VALUES
(10,10,CURRENT_TIMESTAMP);
SELECT * FROM account_job1;
--it gives error becoz using serial the 10 no does not appeanrs there
*/

/*insert into acount(username,password,email,create_on)
values
('Vaishnavi','helloworld','abc@gmail.com',CURRENT_TIMESTAMP);*/

--SELECT * FROM acount;

/*insert into job(jab_name)
values
('DATASCIENTIST');*/
--SELECT * FROM job;

/*SELECT * FROM acount;

UPDATE acount 
SET last_login=CURRENT_TIMESTAMP;

SELECT * FROM acount;

--UPDATE acount 
--SET last_login=CURRENT_TIMESTAMP;

UPDATE acount
SET last_login=CURRENT_TIMESTAMP;
*/

--SELECT * from  account_job1;
/*UPDATE account_job1
SET hire_date=acount.create_on
FROM acount
WHERE account_job1.user_id=acount.user_id;
*/
SELECT * FROM account_job1;


