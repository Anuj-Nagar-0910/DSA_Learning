# SQL Practice Summary Notes

These notes summarize all queries written in `practice.sql`, the SQL concepts used, and the mistakes that led to incorrect output before reaching the accepted queries.

## Quick Concept Index

| Concept | Where Used | Why It Matters |
|---|---|---|
| `INNER JOIN` | All multi-table queries | Combines only matching rows from related tables. |
| `DISTINCT` | Non-Sales employees query | Removes duplicate employee rows caused by multiple department assignments. |
| `DATEDIFF` | Development tenure query | Measures assignment duration in days. |
| `SUM` | Salary expenditure, Zomato spending | Adds numeric values within each group. |
| `GROUP BY` | Salary expenditure, Zomato spending | Creates one result row per department or user. |
| `HAVING` | Zomato spending query | Filters after aggregation. |
| Subquery | Zomato spending query | Calculates the average spending value used by the outer query. |
| `CREATE VIEW` | High-rated restaurants | Saves filtered restaurants as a reusable virtual table. |

## 1. Current Salary Of Department Managers

### Task

Retrieve the employee number, first name, last name, department name, current title, and current salary of all department managers where their salary is active.

### Final Query

```sql
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
```

### What We Used

- `INNER JOIN` to combine employee, manager, department, title, and salary data.
- Table aliases such as `e`, `dm`, `d`, `t`, and `s` to keep the query readable.
- `WHERE s.to_date = '9999-01-01'` to keep active salary rows.
- Column aliases `current_title` and `current_salary` for clearer output.

### Key Learning

The salary history is stored in `salaries`, so active salary must be checked there. The prompt specifically mentioned salary active with `to_date = '9999-01-01'`, so the accepted query filters `salaries.to_date`.

### Shortcoming To Remember

Tables like `titles` and `dept_manager` also contain history. If a prompt asks for current manager and current title explicitly, it may also require `dm.to_date = '9999-01-01'` and `t.to_date = '9999-01-01'`. But for this prompt, the checked condition was active salary.

## 2. Employees Not Assigned To Sales

### Task

Retrieve the employee number, first name, and last name of employees who are not assigned to the `Sales` department.

### Final Query

```sql
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
```

### What We Used

- `INNER JOIN` between `employees`, `dept_emp`, and `departments`.
- `WHERE d.dept_name <> 'Sales'` to keep department assignment rows that are not Sales.
- `DISTINCT` to avoid duplicate employees in the result.

### Why This Worked

The expected result treated the task as: list employees from assignment rows where the department is not `Sales`. Since one employee can have multiple rows in `dept_emp`, the same employee may appear more than once. `DISTINCT` fixes that by returning each employee only once.

### What Failed Before

```sql
WHERE NOT EXISTS (...)
```

This was logically stricter. It means an employee must have no Sales assignment at all. That can exclude employees who have both Sales and non-Sales records. The expected result did not use that interpretation.

```sql
WHERE de.to_date = '9999-01-01'
```

This assumed the task meant current department only. The prompt did not say current, so this condition changed the result.

### Critical Lesson

Read the expected output behavior carefully. In this problem, the checker expected row-level non-Sales assignments, not a historical exclusion of every employee who ever worked in Sales.

## 3. Employees Who Worked In Development For More Than 3 Years

### Task

Retrieve the first name and last name of employees who have worked in the `Development` department for more than 3 years.

### Final Query

```sql
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
```

### What We Used

- `INNER JOIN` to connect employees to department assignments and department names.
- `WHERE d.dept_name = 'Development'` to keep only Development assignments.
- `DATEDIFF(de.to_date, de.from_date)` to measure the assignment length in days.
- `> 365 * 3` to check for more than 3 years.

### Why This Worked

The tenure in a department is stored in `dept_emp`, using `from_date` and `to_date`. `DATEDIFF` directly measures the number of days between those dates. The prompt asks for more than 3 years, so the accepted condition checks that the duration is greater than `365 * 3`.

### What Failed Before

```sql
TIMESTAMPDIFF(YEAR, de.from_date, de.to_date) > 3
```

This counts completed calendar-year boundaries, which may not match the expected day-based calculation.

```sql
SELECT DISTINCT e.first_name, e.last_name
```

This was wrong because the prompt asks for employees but outputs only names. Two different employees can share the same first name and last name. `DISTINCT` would collapse them into one row and reduce the expected count.

### Critical Lesson

Do not use `DISTINCT` blindly. If the selected columns are not unique identifiers, `DISTINCT` can hide valid rows.

## 4. Department Salary Expenditure From 1990 To 2000

### Task

Retrieve the department name and total salary expenditure for each department during the period from January 1, 1990 to December 31, 2000.

### Final Query

```sql
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
```

### What We Used

- `INNER JOIN` to connect departments to employees and employees to salary records.
- `SUM(s.salary)` to calculate total salary.
- `GROUP BY d.dept_name` to produce one total per department.
- Date filtering on both `s.from_date` and `s.to_date`.
- Alias `total_salary` to match the expected output column.

### Why This Worked

The expected result counted salary records fully contained inside the requested period. That requires both:

```sql
s.from_date >= '1990-01-01'
s.to_date <= '2000-12-31'
```

This prevents salary records that extend beyond December 31, 2000 from being counted.

### What Failed Before

```sql
WHERE s.from_date BETWEEN '1990-01-01' AND '2000-12-31'
```

This only checked when the salary record started. It also included salary records that started before the end date but continued after the requested period. That caused totals to be too high.

### Critical Lesson

For period-based questions, check whether the prompt expects records that start inside the period, overlap with the period, or are fully contained inside the period. Here, the expected result required full containment.

## 5. High-Spending Users At High-Rated Restaurants

### Task

Create a view to list restaurants with a rating greater than 4. Then retrieve `user_id` and total spending for users who have spent more than the average spending at high-rated restaurants.

### Final Query

```sql
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
```

### What We Used

- `CREATE VIEW` to create `high_rated_restaurants`.
- `INNER JOIN` to keep only orders from high-rated restaurants.
- `SUM(o.total_price)` to calculate each user's total spending.
- `GROUP BY o.user_id` to produce one row per user.
- `HAVING` to filter after calculating `SUM`.
- A subquery to calculate the average order spending at high-rated restaurants.
- `AVG(o2.total_price)` inside the subquery.

### Why This Worked

The expected output contains only:

```sql
user_id, total_spending
```

So the outer query must group only by `user_id`. The filter compares:

```sql
each user's SUM(total_price)
>
average order total_price at high-rated restaurants
```

That is why the subquery uses:

```sql
AVG(o2.total_price)
```

### What Failed Before

Adding `rating` to the output:

```sql
SELECT o.user_id, hrr.rating, SUM(o.total_price)
GROUP BY o.user_id, hrr.rating
```

This created a different result shape than expected. It also split a user's spending by rating, making totals smaller and removing many users from the result.

Calculating average user-level totals:

```sql
SELECT AVG(user_total_spending)
FROM (
    SELECT user_id, SUM(total_price) AS user_total_spending
    ...
) AS user_spending
```

This compared each user against the average total per user. The expected result compared each user against average order spending, so this returned too few rows.

### Critical Lesson

`HAVING` filters grouped results. The subquery must calculate the exact threshold described by the expected output. Average order spending and average user spending are different numbers.

## Revision Checklist

- Use `WHERE` before grouping to filter raw rows.
- Use `HAVING` after grouping to filter aggregate values.
- Use `DISTINCT` only when duplicate rows are truly unwanted and selected columns are safe to deduplicate.
- When a table stores history, check whether the prompt asks for active/current rows.
- For date ranges, decide whether records must start inside, overlap, or be fully contained inside the range.
- Match the expected output columns exactly. Extra columns can force extra `GROUP BY` columns and change the result.
- When using a subquery as a threshold, confirm whether the average is per row, per order, per user, or per group.
