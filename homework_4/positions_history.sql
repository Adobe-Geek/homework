create table positions_history(
	id SERIAL primary key,
	position_id INT references positions(id),
	start_date DATE,
	end_date DATE
);