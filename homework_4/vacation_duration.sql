create or replace view employee_vacation_summary as 
select e.employee_id, e.first_name, e.last_name, v.start_date, v.end_date, (v.end_date - v.start_date + 1) as duration_days,
SUM(v.end_date - v.start_date + 1) over (partition by e.employee_id) as total_vacation_days
from employees e
join vacations v on e.employee_id = v.employee_id;

