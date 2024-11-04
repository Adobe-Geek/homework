create table departments(
	department_id SERIAL primary key,
	department_name VARCHAR(50) not null,
	abbreviation VARCHAR(10),
	department_head VARCHAR(50)
);