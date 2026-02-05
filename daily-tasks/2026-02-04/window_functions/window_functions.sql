-- based on employees

-- Q.NO.1
select 
	department, 
    name,
    rank() over(partition by department order by salary desc) as rank_salary
from employees;

-- Q.NO.2
select 
	name,
    salary,
    avg(salary) over(partition by department) as avg_sal
from employees;

-- Q.NO.3
select
	row_number() over(order by hire_date) as row_no,
	name,
    hire_date
from employees;

-- Q.NO.4
select
	department,
	name,
    salary - avg(salary) over(partition by department) as diff_from_avg
from employees;

-- Q.NO.5
select
	department,
	name,
    salary
from (
	select 
		department,
        name,
        salary,
        rank() over(partition by department order by salary desc) as salary_rank 
	from employees
) ranked
where salary_rank = 1;

-- based on orders

-- Q.NO.6
select
	customer_id,
    sum(amount) over(partition by customer_id order by order_date) as running_total
from orders;

-- Q.NO.7
select 
	customer_id, 
    order_id,
    lag(amount) over(partition by customer_id order by order_date) as prev_amount
from orders;

-- Q.NO.8
select
	customer_id,
    total_order_amount,
    rank() over(order by total_order_amount) as customer_rank
from (
	select
		customer_id,
		sum(amount) as total_order_amount
    from orders
    group by customer_id
) totals;

-- Q.NO.9
select 
	customer_id, 
    order_id,
    lead(order_date) over(partition by customer_id order by order_date) as next_order_date
from orders;

-- Q.NO.10
select
	customer_id,
    order_date,
    sum(amount) over(partition by customer_id order by order_date) as cum_amount
from orders;

select * from orders;