/*
CREATE TABLE patient(
	patient_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	date_of_birth DATE,
	gender VARCHAR(10),
	phone_number VARCHAR(15),
	email VARCHAR(50),
	address VARCHAR(50),
	city VARCHAR(50),
	state VARCHAR(50),
	zip_code INTEGER,
	medical_history VARCHAR(50),
	last_visit_date DATE
);


INSERT INTO patient(first_name,last_name,date_of_birth,gender,phone_number,email,address,city,state,zip_code,medical_history,last_visit_date)
VALUES
	('John', 'Doe', '1980-01-15', 'Male', '123-456-7890', 'john.doe@example.com', '123 Elm St', 'Springfield', 'IL', '62701', 'Hypertension', '2024-06-01'),
	('Jane', 'Smith', '1990-02-20', 'Female', '987-654-3210', 'jane.smith@example.com', '456 Oak St', 'Springfield', 'IL', '62701', 'Diabetes', '2024-05-25'), 
	('Alice', 'Johnson', '1975-03-30', 'Female', '555-123-4567', 'alice.johnson@example.com', '789 Pine St', 'Shelbyville', 'IL', '62565', 'Asthma', '2024-06-10'),
	('Bob', 'Brown', '1965-04-10', 'Male', '444-555-6666', 'bob.brown@example.com', '101 Maple St', 'Capital City', 'IL', '62702', 'High Cholesterol', '2024-05-15'), 
	('Charlie', 'Davis', '1985-05-20', 'Male', '333-444-5555', 'charlie.davis@example.com', '202 Cedar St', 'Springfield', 'IL', '62701', 'Allergies', '2024-06-05'), 
	('Diana', 'Evans', '2000-06-25', 'Female', '222-333-4444', 'diana.evans@example.com', '303 Birch St', 'Shelbyville', 'IL', '62565', 'Migraine', '2024-06-20'), 
	('Ethan', 'Foster', '1970-07-15', 'Male', '111-222-3333', 'ethan.foster@example.com', '404 Spruce St', 'Capital City', 'IL', '62702', 'Arthritis', '2024-06-12'), 
	('Fiona', 'Garcia', '1995-08-10', 'Female', '999-888-7777', 'fiona.garcia@example.com', '505 Ash St', 'Springfield', 'IL', '62701', 'Depression', '2024-05-30'),
	('George', 'Harris', '1988-09-05', 'Male', '888-777-6666', 'george.harris@example.com', '606 Walnut St', 'Shelbyville', 'IL', '62565', 'Hypertension', '2024-04-25'), 
	('Hannah', 'Irvine', '1992-10-12', 'Female', '777-666-5555', 'hannah.irvine@example.com', '707 Hickory St', 'Capital City', 'IL', '62702', 'Diabetes', '2024-06-22');

SELECT * FROM patient;
*/
--DROP TABLE patient;

SELECT * FROM patient
WHERE last_visit_date>current_date-INTERVAL '50 days';