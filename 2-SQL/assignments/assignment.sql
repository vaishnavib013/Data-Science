/*CREATE TABLE product(
	product_id SERIAL PRIMARY KEY,
	product_name VARCHAR(30),
	category VARCHAR(30),
	quantity INTEGER,
	price FLOAT,
	supplier VARCHAR(40),
	last_restock_date DATE
	);
*/
/*
INSERT INTO product
(product_name,category,quantity,price,supplier,last_restock_date)
VALUES
	('Laptop', 'Electronics', 50, 799.99, 'TechSupplier Inc.', '2024-06-01'),
	('Smartphone', 'Electronics', 150, 499.99, 'MobileDistributors Ltd.', '2024-05-25'),
	('Desk Chair', 'Furniture', 80, 89.99, 'OfficeSupplies Co.', '2024-05-15'),
	('Notebook', 'Stationery', 200, 2.99, 'PaperGoods Inc.', '2024-06-10'),
	('Water Bottle', 'Accessories', 120, 9.99, 'Lifestyle Products', '2024-06-05'), 
	('Headphones', 'Electronics', 70, 149.99, 'TechSupplier Inc.', '2024-06-08'), 
	('Desk Lamp', 'Furniture', 60, 29.99, 'OfficeSupplies Co.', '2024-05-20'), 
	('Backpack', 'Accessories', 90, 49.99, 'TravelGear Ltd.', '2024-06-12'),
	('Pen', 'Stationery', 300, 1.49, 'PaperGoods Inc.', '2024-06-03'),
	('Monitor', 'Electronics', 40, 199.99, 'TechSupplier Inc.', '2024-06-15');

*/
--SELECT * FROM product;

SELECT product_name,MIN(quantity)
FROM product
GROUP BY product_name
HAVING MIN(quantity)<100;
