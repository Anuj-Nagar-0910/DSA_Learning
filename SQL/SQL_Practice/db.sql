"""
select all columns from the employees table for
employees whose hire_date is 10 or more years before the current date.
"""
SELECT *
FROM employees
WHERE hire_date <= DATE_SUB(CURDATE(), INTERVAL 10 YEAR);

"""select all columns from the employees table for
employees whose salary falls between 40000 and 60000 inclusive.
"""
SELECT *
FROM employees 
WHERE salary BETWEEN 40000 AND 60000;

"""
select all columns from the employees table
for employees whose gender is 
not 'M' or 'F'.
"""
SELECT *
FROM employees
WHERE gender NOT IN ('M', 'F');

"""
Write a query to return the list of employees (emp_no):
1. have been employed by the company for the last 5 years.
2. earn a salary less than 40000.

in salaries table we have 
emp_no, salary, from_date, to_date
"""
SELECT emp_no
FROM salaries
WHERE salary < 40000
AND to_date >= DATE_SUB(CURDATE(), INTERVAL 5 YEAR);
"but this is not working"
SELECT emp_no
FROM salaries
WHERE salary < 40000
AND to_date >= DATE_SUB(CURDATE(), INTERVAL 5 YEAR);

"Write a query to return the list of employees:
have been assigned to a fepartment for more than 10 years
the assignment must still be active, meaning
they are either currently assigned to the department 
or have no end date.

dept_manager table has emp_no, dept_no, from_date, to_date
"
SELECT emp_no
FROM dept_manager
WHERE (to_date >= CURDATE() OR to_date IS NULL)
AND from_date <= DATE_SUB(CURDATE(), INTERVAL 10 YEAR);








