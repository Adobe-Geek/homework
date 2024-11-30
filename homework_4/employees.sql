create table employees(
	id SERIAL primary key,
	last_name VARCHAR(30) not null,
	first_name VARCHAR(30) not null,
	middle_name VARCHAR(30),
	passport VARCHAR(30) unique not null,
	birth_date DATE not null,
	birth_place VARCHAR(30),
	hire_date DATE,
	address VARCHAR(100),
	department_id INT references departments(id)
);