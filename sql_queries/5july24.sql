SELECT * FROM payment;
--customer_id,staff_id are category_columns
SELECT customer_id,staff_id,SUM(amount) FROM payment
GROUP BY customer_id,staff_id;

SELECT staff_id,customer_id ,SUM(amount) FROM payment
GROUP BY staff_id,customer_id;

SELECT staff_id,customer_id ,SUM(amount) FROM payment
GROUP BY staff_id,customer_id 
ORDER BY staff_id;

SELECT staff_id,customer_id ,SUM(amount) FROM payment
GROUP BY staff_id,customer_id 
ORDER BY staff_id,customer_id;

SELECT staff_id,customer_id ,SUM(amount) FROM payment
GROUP BY staff_id,customer_id 
ORDER BY SUM(amount);

SELECT * FROM payment;

SELECT DATE(payment_date),SUM(amount) FROM payment
GROUP BY DATE(payment_date);

SELECT DATE(payment_date),SUM(amount) FROM payment
GROUP BY DATE(payment_date)
ORDER BY SUM(amount);

SELECT DATE(payment_date),SUM(amount) FROM payment
GROUP BY DATE(payment_date)
ORDER BY SUM(amount) DESC;

SELECT staff_id,COUNT(amount) FROM payment
GROUP BY staff_id;

SELECT rating,AVG(replacement_cost) FROM film
GROUP BY rating;
--or
SELECT rating,ROUND(AVG(replacement_cost),2) FROM film
GROUP BY rating;

SELECT customer_id,SUM(amount) FROM payment
GROUP BY customer_id
ORDER BY SUM(amount) DESC
limit 5;

SELECT customer_id from payment
GROUP BY customer_id
ORDER BY SUM(amount);

SELECT customer_id,count(*) FROM payment
GROUP BY customer_id
HAVING COUNT(*)>=40;

SELECT customer_id,SUM(amount) from payment
WHERE customer_id NOT IN (184,87,477)
GROUP BY customer_id;

SELECT customer_id,SUM(amount) FROM payment
GROUP BY customer_id
HAVING SUM(amount)>100;
