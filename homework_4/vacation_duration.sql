create or replace view employee_vacation_summary as 
select e.id, e.first_name, e.last_name, v.start_date, v.end_date,
SUM(v.end_date - v.start_date + 1) over (partition by e.id) as total_vacation_days
from employees e
join vacations v on e.id = v.employee_id;