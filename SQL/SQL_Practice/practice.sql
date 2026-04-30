/*
Retrieve the employee number, first name, last name, department name,
current title, and current salary of all department managers where
their salary is active.
*/
SELECT
    e.emp_no,
    e.first_name,
    e.last_name,
    d.dept_name,
    t.title AS current_title,
    s.salary AS current_salary
FROM employees AS e
INNER JOIN dept_manager AS dm
    ON e.emp_no = dm.emp_no
INNER JOIN departments AS d
    ON dm.dept_no = d.dept_no
INNER JOIN titles AS t
    ON e.emp_no = t.emp_no
INNER JOIN salaries AS s
    ON e.emp_no = s.emp_no
WHERE s.to_date = '9999-01-01';

/*
Retrieve the employee number, first name, and last name of employees
who are not assigned to the Sales department.

Explanation:
- Start from the employees table because the final output needs employee details.
- Join dept_emp to find each employee's department assignment records.
- Join departments to get the department name for each assignment.
- Filter with dept_name <> 'Sales' to keep only assignment rows that are not
  for the Sales department.
- Use DISTINCT because an employee can have multiple department assignment
  records, and the output should list each employee only once.
*/
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

/*
Retrieve the first name and last name of employees who have worked in
the Development department for more than 3 years.

Explanation:
- Join employees with dept_emp to read department assignment dates.
- Join departments to filter only the Development department.
- Use DATEDIFF to calculate how many days the employee worked in that
  department assignment.
- Do not use DISTINCT here because two different employees can have the same
  first name and last name, and the prompt asks for employees.

Crucial change:
- The working query does not use DISTINCT.
- DISTINCT is incorrect here because the output columns are only first_name
  and last_name. If two different employees have the same full name, DISTINCT
  would collapse them into one row, which gives fewer rows than expected.

Why this works correctly:
- dept_emp stores the actual department assignment period using from_date and
  to_date.
- DATEDIFF(de.to_date, de.from_date) calculates the length of that specific
  Development assignment in days.
- The condition > 365 * 3 keeps only assignments longer than 3 years.
- The SELECT list follows the prompt exactly by returning only first_name and
  last_name.
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

/*
Retrieve the department name and total salary expenditure for each department
from January 1, 1990, to December 31, 2000.

Explanation:
- departments gives the department name.
- dept_emp connects employees to departments.
- salaries stores each employee's salary history.
- Filter salary records whose full salary period falls inside the requested
  date range.
- SUM(s.salary) calculates the total salary expenditure per department.
- GROUP BY d.dept_name returns one total for each department.

Critical changes that made this query work:
- The date filter checks both salary dates:
    s.from_date >= '1990-01-01'
    s.to_date <= '2000-12-31'
- This means the salary record must be fully contained inside the requested
  period.
- Filtering only with s.from_date BETWEEN '1990-01-01' AND '2000-12-31'
  is not enough. That version also includes salary records that started before
  the end date but continued after December 31, 2000, which increases the
  total incorrectly.
- The prompt asks for salary expenditure "during the specified period", so the
  expected result is based on salary records whose start and end dates both fit
  inside that period.
- The alias is total_salary because the expected output column is named
  total_salary.

Why this exact structure works:
- departments is needed for dept_name.
- dept_emp is needed because salaries do not store dept_no directly.
- salaries is joined through emp_no to get each employee's salary records.
- SUM(s.salary) adds the matching salary values for each department.
- GROUP BY d.dept_name gives one row per department.
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

/*
Create a view to list restaurants with a rating greater than 4.

Then retrieve user_id and total spending for users who have spent more than
the average spending at high-rated restaurants.

Explanation:
- The view stores only restaurants whose rating is greater than 4.
- Orders contains user_id, restaurant_id, and total_price, so it is the table
  used to calculate user spending.
- Join Orders with high_rated_restaurants to keep only orders placed at
  high-rated restaurants.
- Group by user_id to calculate each user's total spending at high-rated
  restaurants.
- HAVING compares each user's total spending against the average order
  spending at high-rated restaurants.
- The final output should only contain user_id and total_spending.

What SQL concepts are used here:
- View:
  high_rated_restaurants is created with CREATE VIEW. It acts like a saved
  virtual table containing only restaurants where rating > 4.
- INNER JOIN:
  Orders is joined with high_rated_restaurants using restaurant_id. This keeps
  only orders whose restaurant exists in the high-rated restaurant view.
- Aggregate function:
  SUM(o.total_price) calculates total spending per user.
- GROUP BY:
  GROUP BY o.user_id groups all matching high-rated restaurant orders for the
  same user into one row.
- HAVING:
  HAVING is used because the condition is applied after aggregation. We need
  to filter users based on SUM(o.total_price), which cannot be done with WHERE.
- Subquery:
  The subquery calculates AVG(o2.total_price), the average order spending at
  high-rated restaurants. The outer query compares each user's total spending
  against this value.

Why this worked:
- The expected output has only user_id and total_spending, so the SELECT list
  must contain only those two columns.
- The comparison is:
    each user's SUM(total_price) > average order total_price at high-rated
    restaurants.
- Because the subquery uses AVG(o2.total_price), it calculates the average
  spending per order, which matches the expected result.

Why the other version was incorrect:
- Adding rating to SELECT changed the result shape to user_id, rating, and
  total_spending, but the expected output does not include rating.
- Grouping by both user_id and rating split one user's spending into separate
  groups by rating. That made totals smaller and removed many users from the
  result.
- Calculating the average from user-level totals compared each user against
  the average total per user, which is a different condition from the expected
  average order spending.
*/
CREATE VIEW high_rated_restaurants AS
SELECT
    restaurant_id,
    name,
    rating
FROM Restaurants
WHERE rating > 4;

SELECT
    o.user_id,
    SUM(o.total_price) AS total_spending
FROM Orders AS o
INNER JOIN high_rated_restaurants AS hrr
    ON o.restaurant_id = hrr.restaurant_id
GROUP BY o.user_id
HAVING SUM(o.total_price) > (
    SELECT AVG(o2.total_price)
    FROM Orders AS o2
    INNER JOIN high_rated_restaurants AS hrr2
        ON o2.restaurant_id = hrr2.restaurant_id
);
