-- Q.NO.1
select department, count(*)
from employees
group by department;

-- Q.NO.2
select department, avg(salary)
from employees
group by department;

-- Q.NO.3
select max(salary) as max_salary
from employees;

-- Q.NO.4
select sum(salary) as salary_expence
from employees
group by department;

-- Q.NO.5
select department
from employees
group by department
having count(emp_id) > 2;

-- Q.NO.6
select min(amount) as min_amt, max(amount) as max_amt
from orders;

-- Q.NO.7
select customer_id, sum(amount)
from orders
group by customer_id;

-- Q.NO.8
select customer_id
from orders
group by customer_id
having sum(amount) > 500;

-- Q.NO.9
select region, sum(revenue)
from sales
group by region;

-- Q.NO.10
select salesperson, avg(revenue)
from sales
group by salesperson
having avg(revenue) > 400;