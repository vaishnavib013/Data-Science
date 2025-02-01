/*
CREATE TABLE customer(
	customer_id SERIAL PRIMARY KEY,
	first_name VARCHAR(30) NOT NULL,
	last_name VARCHAR(30) NOT NULL,
	email VARCHAR(50),
	phone_number VARCHAR(14),
	address VARCHAR(60),
	city VARCHAR(20),
	state VARCHAR(20),
	zip_code INTEGER,
	plan_id INTEGER,
	last_call_date DATE
);
*/
--SELECT * FROM customer;

/*
INSERT INTO customer
(first_name,last_name,email,phone_number,address,city,state,zip_code,plan_id,last_call_date)
VALUES
	('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Elm St', 'Springfield', 'IL', '62701', 1, '2024-06-01'),
	('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Oak St', 'Springfield', 'IL', '62701', 2, '2024-05-15'), 
	('Alice', 'Johnson', 'alice.johnson@example.com', '555-123-4567', '789 Pine St', 'Shelbyville', 'IL', '62565', 3, '2024-04-20'),
	('Bob', 'Brown', 'bob.brown@example.com', '444-555-6666', '101 Maple St', 'Capital City', 'IL', '62702', 1, '2024-06-10'),
	('Charlie', 'Davis', 'charlie.davis@example.com', '333-444-5555', '202 Cedar St', 'Springfield', 'IL', '62701', 2, '2024-03-30'),
	('Diana', 'Evans', 'diana.evans@example.com', '222-333-4444', '303 Birch St', 'Shelbyville', 'IL', '62565', 3, '2024-06-20'), 
	('Ethan', 'Foster', 'ethan.foster@example.com', '111-222-3333', '404 Spruce St', 'Capital City', 'IL', '62702', 1, '2024-02-14'), 
	('Fiona', 'Garcia', 'fiona.garcia@example.com', '999-888-7777', '505 Ash St', 'Springfield', 'IL', '62701', 2, '2024-05-05'),
	('George', 'Harris', 'george.harris@example.com', '888-777-6666', '606 Walnut St', 'Shelbyville', 'IL', '62565', 3, '2024-01-25'), 
	('Hannah', 'Irvine', 'hannah.irvine@example.com', '777-666-5555', '707 Hickory St', 'Capital City', 'IL', '62702', 1, '2024-06-22');
*/

--SELECT * FROM customer;

--HERE RISK OF CHURN Means the subscribe plan to be dead!

/*SELECT *,
	CASE 
		WHEN last_call_date<current_date- INTERVAL '90 days' THEN 'HIGH RISK'
		WHEN last_call_date<current_date - INTERVAL '60 days' THEN 'MEDIUM RISK'
		ELSE 'low risk'
END 
FROM customer;
*/

SELECT *,
	CASE 
		WHEN last_call_date<current_date- INTERVAL '90 days' THEN 'HIGH RISK'
		WHEN last_call_date<current_date - INTERVAL '60 days' THEN 'MEDIUM RISK'
		ELSE 'low risk'
END AS CHURN_RISK
FROM customer;







