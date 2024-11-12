create table vacations(
	id SERIAL primary key,
	employee_id INT references employees(id),
	start_date DATE,
	end_date DATE
);
