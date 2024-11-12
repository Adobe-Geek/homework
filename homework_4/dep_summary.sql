create  or replace view department_summary as 
select d.id, d.name as department_name, d.manager,
count(e.id) as employee_count
from departments d
left join employees e on d.id = e.department_id
group  by d.id, d.name, d.manager;

select * from department_summary;