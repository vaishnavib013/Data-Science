/*1.	Write a SQL statement to create a simple table countries, including columns country_id,country_name and region_id which already exist.*/


--create table countries(country_id int Primary key,country_name varchar(20),region_id int);

--create table sales(sale_id SERIAL PRIMARY KEY,product_id INT ,quantity_sold INT,sale_date DATE,total_price INT);

--create table products(product_id SERIAL PRIMARY KEY,product_name varchar(30),category varchar(30),unit_price int );
--Insert into sales(product_id,quantity_sold,sale_date,total_price) values (1,10,'13-03-2024',50),(2,20,'2024-06-25',120),(3,25,'2024-07-15',150);;

--SELECT * FROM sales where total_price >100;

--insert into products(product_name,category,unit_price) values('pencil','general',50),('fridge','Electronics',100);
--select * from products where category='Electronics';

/*select product_name,category from products
order by category asc;
*/
--select round(total_price,2) from sales;