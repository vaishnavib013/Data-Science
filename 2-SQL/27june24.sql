SELeCT * FROM film;

--DISTINCT
SELECT DISTINCT(release_year) FROM film;

SELECT DISTINCT(rental_rate) FROM film;

SELECT DISTINCT(rating) FROM film;

--COUNT
SELECT CoUNT(category_id) FROM film_category;

--MAX()
SELECT max(amount) FROM payment;

--COUNT()
SELECT COUNT(*) FROM payment;
--OR BOTH THE QUERY GIVES SAME RESULT.
SELECT COUNT(amount) FROM payment;

--DISTINCT
SELECT amount FROM payment;

SELECT DISTINCT amount FROM payment;

SELECT COUNT(DISTINCT amount) FROM payment; 
--if here parenthesis is not given then it gets confuse then it will give error.

--where clause filter
SELECT * FROM film;

SELECT * FROM film
WHERE rental_rate>4;

SELECT * FROM film
WHERE rental_rate>4 AND replacement_cost>=19.99 
AND rating='R';

SELECT COUNT(title) FROM film;

SELECT COUNT(*) FROM film
WHERE rating='R' OR rating='PG-13';

SELECT COUNT(*) FROM film
WHERE rating!='R';

--Q1)
SELECT email FROM customer
WHERE first_name='Nancy'
AND last_name='Thomas';

--Q2)
SELECT description FROM film
WHERE title='Outlaw Hanky';












