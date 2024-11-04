create or replace view department_employees as
select e.first_name, e.last_name, e,current_position, d.name as department_name
from employees e
join departments d on e.department_id = d.department_id;

select * from department_employees where department_name = 'Sales';