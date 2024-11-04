create table employees(
	employee_id SERIAL primary key,
	last_name VARCHAR(30) not null,
	first_name VARCHAR(30) not null,
	middle_name VARCHAR(30),
	passport VARCHAR(30) unique not null,
	birth_date DATE not null,
	birth_place VARCHAR(30),
	address VARCHAR(100),
	current_position VARCHAR(50),
	base_salary DECIMAL(10, 2),
	department_id INT references departments(department_id)
);
