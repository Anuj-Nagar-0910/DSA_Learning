--sql
/*Select the dept_name and the total number of employees (num_employees) for each department, 
grouped by department name and ordered alphabetically.*/
select 
d.dept_name,
count(de.emp_no) as num_employees
from departments d
join dept_emp de
    on d.dept_no = de.dept_no
group by d.dept_name
order by d.dept_name asc
--

--sql
/*
Select the hire year (hire_year) and the total number of employees hired 
(total_employees) for each year, grouped by the year of hire.
*/
select
    year(hire_date) as hire_year,
    count(*) as total_employees
from employees
group by year(hire_date);
-- order by hire_year;
--

--sql
/*
Select the title of each job and its average salary (avg_salary), grouped by the job title.
*/
select
    t.title,
    avg(s.salary) as avg_salary
from titles t
join salaries s
    on t.emp_no = s.emp_no
group by t.title
--

--sql
/*Select all columns for employees who meet the specified name conditions using pattern matching.*/
select *
from employees
where first_name like 'A%'
    and last_name like '%n';
--

--sql
-- Retrieve the first name, last name, and the number of title changes (title_changes) of the employee with the highest number of title changes.
select
e.first_name,
e.last_name,
tc.title_changes
from employees e
join(
    select 
    emp_no,
    count(*) as title_changes
    from titles
    group by emp_no
    order by title_changes desc
    limit 1

) tc

on e.emp_no = tc.emp_no;
--

--sql
-- Retrieve the first name, last name, and the number of salary changes (salary_changes) of the employee with the highest count of salary changes.
select
e.first_name,
e.last_name,
sc.salary_changes
From employees e
join(
select
    emp_no,
    count(*) as salary_changes
    from salaries
    group by emp_no
    order by salary_changes desc
    limit 1
) sc
on e.emp_no = sc.emp_no
--

--sql
-- Retrieve the year and the maximum salary (max_salary) given in that year by grouping salaries by year.
select
    year(from_date) as year,
    max(salary) as max_salary
from salaries
group by year(from_date)
--

--sql
-- Retrieve the first name and last name of employees who have only one salary record in the salaries table, indicating no salary increments.
select
e.first_name,
e.last_name
from employees e
join salaries s
    on e.emp_no = s.emp_no
group by e.emp_no, e.first_name, e.last_name
having count(s.emp_no) = 1;
--

--sql
-- Retrieve the employee number, first name, last name, department name, current title, and current salary of all department managers where their salary is active (to_date = '9999-01-01').
SELECT
    e.emp_no,
    e.first_name,
    e.last_name,
    d.dept_name,
    t.title AS title,
    s.salary AS salary
FROM employees AS e
INNER JOIN dept_manager AS dm
    ON e.emp_no = dm.emp_no
INNER JOIN departments AS d
    ON dm.dept_no = d.dept_no
INNER JOIN titles AS t
    ON e.emp_no = t.emp_no
INNER JOIN salaries AS s
    ON e.emp_no = s.emp_no
WHERE 
  s.to_date = '9999-01-01';
--

--sql
-- Retrieve the department names where there are no employees assigned in the dept_emp table.
Select d.dept_name
from departments d
left join dept_emp de
    on d.dept_no = de.dept_no
where de.emp_no is null;
--

--sql
-- Retrieve the department name, total number of employees, and total salary expenditure for each department. Group the data by department name.
Select
    d.dept_name,
    Count( de.emp_no) as total_employees,
    sum(s.salary) as total_salary
from departments d
join dept_emp de
    on d.dept_no = de.dept_no
join salaries s
    on de.emp_no = s.emp_no
group by d.dept_name
--

--sql
-- Retrieve the employee number, first name, and last name of employees who are not assigned to the 'Sales' department.
SELECT DISTINCT
    e.emp_no,
    e.first_name,
    e.last_name
FROM employees AS e
INNER JOIN dept_emp AS de
    ON e.emp_no = de.emp_no
INNER JOIN departments AS d
    ON de.dept_no = d.dept_no
WHERE d.dept_name <> 'Sales';
--

--sql
/*
Problem Description
You are tasked with listing all employees who have worked in the 'Development' department for more than 3 years. This information is essential for tracking employee tenure in specific departments.
Task

Retrieve the first name and last name of employees who meet the tenure condition in the 'Development' department.
*/
SELECT
    e.first_name,
    e.last_name
FROM employees AS e
INNER JOIN dept_emp AS de
    ON e.emp_no = de.emp_no
INNER JOIN departments AS d
    ON de.dept_no = d.dept_no
WHERE d.dept_name = 'Development'
  AND DATEDIFF(de.to_date, de.from_date) > 365 * 3;
--

--sql
/*
Problem Description
You are required to calculate the total salary expenditure for each department within a specific period (from January 1, 1990, to December 31, 2000). This helps in analyzing historical salary budgets across departments.
Task
Retrieve the department name and the total salary expenditure for each department during the specified period.
*/
SELECT
    d.dept_name,
    SUM(s.salary) AS total_salary
FROM departments AS d
INNER JOIN dept_emp AS de
    ON d.dept_no = de.dept_no
INNER JOIN salaries AS s
    ON de.emp_no = s.emp_no
WHERE s.from_date >= '1990-01-01'
  AND s.to_date <= '2000-12-31'
GROUP BY d.dept_name;

--
