/*
===============================================================================
BIKE STORE DATABASE
===============================================================================

ER Diagram Summary

The Bike Store database is organized around customers, orders, stores, staff,
products, brands, categories, and stock inventory. It supports a retail bike
store workflow where customers place orders, staff process those orders, stores
hold inventory, and products are grouped by brand and category.

Main Tables

1. customers
   Stores customer details such as name, phone, email, and address.
   Primary key: customer_id

2. orders
   Stores order header information including customer, order status, order date,
   required date, shipped date, store, and staff member.
   Primary key: order_id
   Foreign keys:
   - customer_id references customers(customer_id)
   - store_id references stores(store_id)
   - staff_id references staffs(staff_id)

3. order_items
   Stores products included in each order, with quantity, list price, and
   discount.
   Composite primary key: order_id, item_id
   Foreign keys:
   - order_id references orders(order_id)
   - product_id references products(product_id)

4. stores
   Stores store details such as store name, contact information, and address.
   Primary key: store_id

5. staffs
   Stores employee details including name, email, phone, active status, assigned
   store, and manager.
   Primary key: staff_id
   Foreign keys:
   - store_id references stores(store_id)
   - manager_id references staffs(staff_id)

6. products
   Stores product details including product name, brand, category, model year,
   and list price.
   Primary key: product_id
   Foreign keys:
   - brand_id references brands(brand_id)
   - category_id references categories(category_id)

7. brands
   Stores bike brand names.
   Primary key: brand_id

8. categories
   Stores product category names.
   Primary key: category_id

9. stocks
   Stores product inventory quantity available at each store.
   Composite primary key: store_id, product_id
   Foreign keys:
   - store_id references stores(store_id)
   - product_id references products(product_id)

Common Query Paths

- Customer order history: customers -> orders -> order_items -> products
- Store sales: stores -> orders -> order_items
- Staff performance: staffs -> orders -> order_items
- Product catalog: products -> brands, categories
- Store inventory: stores -> stocks -> products
*/

--sql
/*
Problem 1: Staff Member With Most Orders

Problem Summary:
Identify the staff member who processed the most orders. Display the staff
member's full name and the total number of orders processed.

Lesson Learnt:
Use joins to connect transaction tables with master tables, then group by the
entity whose performance you want to measure.

Points To Revise:
- join between staffs and orders
- count aggregate
- group by staff columns
- order by aggregate result
- limit for top result
*/
select
    concat(s.first_name, ' ', s.last_name) as full_name,
    count(o.order_id) as total_orders
from staffs s
join orders o
    on s.staff_id = o.staff_id
group by s.staff_id, s.first_name, s.last_name
order by total_orders desc
limit 1;
--

--sql
/*
Problem 2: Customers With No Active Orders

Problem Summary:
Retrieve customer names and email addresses for customers who have placed at
least one order, but currently do not have any active orders. Active orders are
Pending or Processing, represented by order_status values 1 and 2.

Important Logic:
If a customer has two orders, where one is Completed and one is Processing,
that customer must not be counted. The check must happen at the customer level,
not only at the order-row level.

Lesson Learnt:
Use exists to prove order history and not exists to exclude customers who have
any active order. This avoids the null-related problems that can happen with
not in.

Points To Revise:
- exists and not exists
- correlated subqueries
- customer-level filtering
- avoiding row-level filtering mistakes
- active status filter: order_status in (1, 2)
*/
select
    c.first_name,
    c.last_name,
    c.email
from customers c
where exists (
    select 1
    from orders o
    where o.customer_id = c.customer_id
)
and not exists (
    select 1
    from orders o
    where o.customer_id = c.customer_id
      and o.order_status in (1, 2)
);
--

--sql
/*
Problem 3: Total Discount Per Product

Problem Summary:
Determine the total discount given for each product across all orders using:
quantity * list_price * discount / 100

Lesson Learnt:
For calculations based on ordered items, start from the transaction-detail table
order_items, then join products only to fetch the product name.

Points To Revise:
- aggregate calculations with sum
- joining order_items to products
- grouping by product
- sorting by calculated totals
- understanding where the business calculation lives
*/
select
    p.product_name,
    sum(oi.quantity * oi.list_price * oi.discount / 100) as total_discount
from order_items oi
join products p
    on oi.product_id = p.product_id
group by p.product_id, p.product_name
order by total_discount desc;
--

--sql
/*
Problem 4: Top 3 Statuses For The Busiest Store

Problem Summary:
Identify the store with the highest total number of orders, then show the top
3 most frequent order statuses for that store.

Lesson Learnt:
When the expected output belongs to only one store, first find the relevant
store in a subquery or CTE, then do the status count for that store only.

Points To Revise:
- common table expressions
- group by store_id
- order by count descending
- limit inside a CTE
- joining filtered results back to detail data
*/
with top_store as (
    select
        store_id
    from orders
    group by store_id
    order by count(order_id) desc
    limit 1
)
select
    s.store_name,
    o.order_status,
    count(o.order_id) as status_count
from stores s
join orders o
    on s.store_id = o.store_id
join top_store ts
    on o.store_id = ts.store_id
group by s.store_id, s.store_name, o.order_status
order by status_count desc
limit 3;
--

--sql
/*
Problem 5: Late Orders By Store

Problem Summary:
Find stores where orders were shipped later than the required date. Return the
store name and the count of late orders.

Lesson Learnt:
Date comparison can be done directly when both columns are date or datetime
types. Filter the late rows first, then group by store.

Points To Revise:
- date comparison
- where shipped_date > required_date
- joining stores and orders
- counting filtered rows
- sorting aggregate results
*/
select
    s.store_name,
    count(o.order_id) as late_orders
from stores s
join orders o
    on s.store_id = o.store_id
where o.shipped_date > o.required_date
group by s.store_id, s.store_name
order by late_orders desc;
--

--sql
/*
Problem 6: Store With Highest Product Returns

Problem Summary:
Identify the store with the highest number of product returns. In this data,
returns are represented by rejected orders, where order_status = 3.

Lesson Learnt:
When a status code represents a business meaning, filter by that code before
aggregating.

Points To Revise:
- status-code based filtering
- where order_status = 3
- group by store
- count rejected orders
- limit 1 for the highest result
*/
select
    s.store_name,
    count(o.order_id) as rejected_orders
from stores s
join orders o
    on s.store_id = o.store_id
where o.order_status = 3
group by s.store_id, s.store_name
order by rejected_orders desc
limit 1;
--

/*
===============================================================================
AIRLINE DATABASE
===============================================================================

ER Diagram Note

The table names shown in Airlines.png are written in lowercase, but in the
actual database the table names start with a capital letter. Use these exact
table names while writing queries:

- Airlines
- Airplanes
- Airports
- Bookings
- Crew
- Flight_Crew_Assignment
- Flights
- Passengers
*/

--sql
/*
Problem 1: Show Tables

Problem Summary:
Show all tables available in the current Airline database.

Lesson Learnt:
Before writing queries on a new database, check the exact table names because
case and spelling can matter depending on the database setup.

Points To Revise:
- show tables
- exact table names
- database metadata commands
*/
show tables;
--

--sql
/*
Problem 2: Flights With Airplane Details

Problem Summary:
Fetch all flight details along with associated airplane information. Return the
flight number, departure time, arrival time, departure airport, arrival airport,
status, airplane model, and seating capacity.

Lesson Learnt:
Use the foreign key airplane_id in Flights to connect each flight with its
airplane details from Airplanes.

Points To Revise:
- join Flights and Airplanes
- selecting columns from both tables
- using aliases
- foreign key: airplane_id
*/
select
    f.flight_number,
    f.departure_time,
    f.arrival_time,
    f.departure_airport,
    f.arrival_airport,
    f.status,
    a.model,
    a.seating_capacity
from Flights f
join Airplanes a
    on f.airplane_id = a.airplane_id;
--

--sql
/*
Problem 3: Flight Count By Departure Airport

Problem Summary:
Count the number of flights departing from each airport. Return the departure
airport and total number of departing flights.

Lesson Learnt:
Use group by when you need one result row per category.

Points To Revise:
- group by departure_airport
- count flight_id
- grouping without a join when all needed columns are in one table
*/
select
    f.departure_airport,
    count(f.flight_id) as total_flights
from Flights f
group by f.departure_airport;
--

--sql
/*
Problem 4: Boeing Airplanes With Capacity Greater Than 200

Problem Summary:
Fetch airplane model and seating capacity for airplanes manufactured by Boeing
with seating capacity greater than 200.

Lesson Learnt:
Use like when the manufacturer value may contain extra words around the brand
name, such as "Boeing Company".

Points To Revise:
- like with wildcard %
- filtering numeric columns
- where with multiple conditions
- exact table name: Airplanes
*/
select
    model,
    seating_capacity
from Airplanes
where manufacturer like '%Boeing%'
  and seating_capacity > 200;
--

--sql
/*
Problem 5: Crew Members Working For Emirates

Problem Summary:
Fetch all crew members working for Emirates.

Lesson Learnt:
Crew stores airline_id, while the airline name is stored in Airlines. Join both
tables to filter by airline name.

Points To Revise:
- join Crew and Airlines
- filtering by text value
- selecting crew details
- foreign key: airline_id
*/
select
    c.first_name,
    c.last_name,
    c.role
from Crew c
join Airlines a
    on c.airline_id = a.airline_id
where a.name = 'Emirates';
--

--sql
/*
Problem 6: Flights With Travel Time Greater Than 50 Hours

Problem Summary:
Fetch all flights where the travel time exceeds 50 hours.

Lesson Learnt:
Use timestampdiff to calculate the difference between departure_time and
arrival_time in hours.

Points To Revise:
- timestampdiff
- datetime calculations
- filtering calculated time differences
- selecting the calculated value as travel_hours
*/
select
    flight_id,
    flight_number,
    departure_time,
    arrival_time,
    timestampdiff(hour, departure_time, arrival_time) as travel_hours
from Flights
where timestampdiff(hour, departure_time, arrival_time) > 50;
--

--sql
/*
Problem 7: Flights With Available Seats

Problem Summary:
Fetch all flights where the number of booked passengers is less than the
airplane seating capacity, considering only scheduled flights.

Lesson Learnt:
Available seats are calculated by subtracting the number of bookings from the
airplane seating capacity. Use having to filter after counting bookings.

Why Grouping By flight_id Works Here:
flight_id uniquely identifies one flight. After joining Flights to Airplanes,
each flight_id points to one flight_number and one airplane seating_capacity.
So grouping by f.flight_id creates one group per flight, and count(b.booking_id)
counts bookings for that exact flight. In MySQL, this works when the selected
columns are functionally dependent on the grouped primary/unique key. In stricter
SQL settings, you may still be asked to include f.flight_number and
a.seating_capacity in the group by clause.

Points To Revise:
- left join
- filtering scheduled flights
- count with group by
- comparing aggregate values with having
- joining Flights, Airplanes, and Bookings
- calculating available seats
- some MySQL practice platforms allow grouping by the unique flight_id only
*/
select
    f.flight_number,
    a.seating_capacity - count(b.booking_id) as available_seats
from Flights f
join Airplanes a
    on f.airplane_id = a.airplane_id
left join Bookings b
    on f.flight_id = b.flight_id
where f.status = 'Scheduled'
group by
    f.flight_id
having available_seats > 0;
--
