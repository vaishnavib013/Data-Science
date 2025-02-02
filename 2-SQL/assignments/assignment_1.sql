/*CREATE TABLE machine(
	log_id SERIAL PRIMARY KEY,
	machine_id INTEGER,
	production_date DATE,
	production_shift VARCHAR(15),
	products_produced INTEGER,
	defects INTEGER,
	runtime FLOAT);
*/

--SELECT * FROM machine;

/*INSERT INTO machine
	(machine_id,production_date,production_shift,products_produced,defects,runtime)
	VALUES(1,'2024-06-01','Morning', 500, 5, 8.0);
*/	
--SELECT * FROM machine;

/*INSERT INTO machine
	(machine_id,production_date,production_shift,products_produced,defects,runtime)
	VALUES
	(1, '2024-06-01', 'Evening', 450, 3, 7.5), 
	(2, '2024-06-01', 'Morning', 480, 2, 7.8),
	(2, '2024-06-01', 'Evening', 470, 4, 8.1), 
	(3, '2024-06-01', 'Morning', 510, 6, 8.2), 
	(3, '2024-06-01', 'Evening', 520, 1, 7.9), 
	(1, '2024-06-02', 'Morning', 490, 3, 8.0)
	;
*/
--SELECT * FROM machine;
	
/*INSERT INTO machine
	(machine_id,production_date,production_shift,products_produced,defects,runtime)
	VALUES
	(1, '2024-06-02', 'Evening', 460, 2, 7.6), 
	(2, '2024-06-02', 'Morning', 475, 1, 7.9), 
	(2, '2024-06-02', 'Evening', 465, 5, 8.3), 
	(3, '2024-06-02', 'Morning', 505, 4, 8.0), 
	(3, '2024-06-02', 'Evening', 515, 3, 8.2)
	;

*/
--SELECT * FROM machine;

SELECT machine_id,max(defects),AVG(runtime)
FROM machine
GROUP BY machine_id;