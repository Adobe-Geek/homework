create table positions_history(
	id SERIAL primary key,
	employee_id INT references employees(id),
	position VARCHAR(30) references positions(id),,
	start_date DATE,
	end_date DATE
);
