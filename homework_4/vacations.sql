create table vacations(
	vacation_id SERIAL primary key,
	employee_id INT references employees(employee_id),
	start_date DATE,
	end_date DATE,
	duration_days INT --(to improve further)
);