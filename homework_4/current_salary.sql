create or replace view employee_position_salary as
select
    employees.first_name,
    employees.last_name,
    employees.hire_date,
    positions.base_salary,
    ROUND(
        positions.base_salary * POWER(1.012, extract(year from AGE (CURRENT_DATE, employees.hire_date))), 2
    ) AS current_salary
from
    employees
join
    positions on employees.id = positions.employee_id;