create table departments(
	id SERIAL primary key,
	name VARCHAR(50) not null,
	abbreviation VARCHAR(10),
	manager_id INT references employees(id)
);