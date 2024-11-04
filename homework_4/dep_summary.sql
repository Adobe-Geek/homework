create  or replace view department_summary as 
select d.department_id, d.department_name as department_name, d.department_head,
count(e.employee_id) as employee_count
from departments d
left join employees e on d.department_id = e.department_id
group  by d.department_id, d.department_name, d.department_head;

select * from department_summary;