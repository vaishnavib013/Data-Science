select customer_id,SUM(amount) from payment
WHERE staff_id=2 
GROUP BY customer_id
HAVING sum(amount)>100;

select * from payment;


SELECT amount AS rental_price FROM payment;


SELECT SUM(amount) AS net_revenue FROM payment;

SELECT COUNT(amount) AS num_transaction FROM payment;


SELECT COUNT(*) AS num_transaction FROM payment;

SELECT customer_id,SUM(amount)
FROM payment
GROUP BY customer_id;

SELECT customer_id,SUM(amount) AS total_spent
FROM payment
GROUP BY customer_id;

select customer_id,SUM(amount) 
FROM payment
GROUP BY customer_id
HAVING SUM(amount)>100;

select customer_id,SUM(amount) AS total_spent
FROM payment
GROUP BY customer_id
HAVING SUM(amount)>100;

/*select customer_id,SUM(amount) AS total_spent
FROM payment
GROUP BY customer_id
HAVING total_spent>100;*/

SELECT customer_id,amount
FROM payment
WHERE amount>2;


/*SELECT customer_id,amount AS new_name
FROM payment
WHERE new_name>2;

 this gives error as asliasing name cannot be given further*/ 

--JOINS

SELECT * FROM payment;

SELECT * FROM customer;

SELECT payment_id,payment.customer_id,first_name FROM payment
INNER JOIN customer
ON payment.customer_id=customer.customer_id;

SELECT payment_id,payment.customer_id,first_name FROM customer
INNER JOIN payment
ON payment.customer_id=customer.customer_id;

SELECT * FROM customer
FULL OUTER JOIN payment
ON customer.customer_id=payment.customer_id;

SELECT * FROM film;
SELECT * FROM inventory;

SELECT film.film_id,title,inventory_id,store_id
FROM film
LEFT JOIN inventory 
ON inventory.film_id=film.film_id;

SELECT film.film_id,title,inventory_id
FROM film
LEFT JOIN inventory 
ON inventory.film_id=film.film_id;

SELECT film.film_id,title,inventory_id,store_id
FROM film
LEFT JOIN inventory 
ON inventory.film_id=film.film_id
WHERE inventory.film_id IS null;

--RIGHT OUTER JOIN
SELECT film.film_id,title,inventory_id,store_id
FROM film
RIGHT JOIN inventory 
ON inventory.film_id=film.film_id;


SELECT film.film_id,title,inventory_id,store_id
FROM inventory
RIGHT JOIN film 
ON inventory.film_id=film.film_id;

SELECT film.film_id,title,inventory_id,store_id
FROM film
RIGHT JOIN inventory 
ON inventory.film_id=film.film_id
WHERE inventory.film_id IS null;

SELECT film.film_id,title,inventory_id,store_id
FROM inventory
RIGHT JOIN film 
ON inventory.film_id=film.film_id
WHERE inventory.film_id IS null;


