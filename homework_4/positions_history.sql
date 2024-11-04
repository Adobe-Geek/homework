create table positions_history(
	history_id SERIAL primary key,
	employee_id INT references employees(employee_id),
	position VARCHAR(30),
	start_date DATE,
	end_date DATE
);