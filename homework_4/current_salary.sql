create  or replace view employee_position_salary as
select first_name, last_name, current_position, base_salary, hire_date,
round(base_salary * POWER (1.012, extract(year from AGE(CURRENT_DATE, hire_date))), 2) as current_salary
from employees;