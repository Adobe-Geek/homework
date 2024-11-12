create or replace view department_employees as
select e.first_name, e.last_name, d.name as department_name,
p.title as position_title
from employees e
join departments d on e.department_id = d.id
join positions p on p.employee_id = e.id;

select * from department_employees where department_name = 'Sales';