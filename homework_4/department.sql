create table departments(
	id SERIAL primary key,
	name VARCHAR(50) not null,
	abbreviation VARCHAR(10),
	manager VARCHAR(50)
);