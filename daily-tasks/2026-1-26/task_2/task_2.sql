-- Q. no. 1

select d.name as department, sum(e.salary) as total_expenditure
from employee e
join department d on e.departmentId=d.id
group by d.id;

-- Q. no. 2

select d.name as department, avg(e.salary) as average_salary
from employee e
join department d on e.departmentId=d.id
group by d.id;

-- Q. no. 3

select name
from employee 
where departmentId = (
	select departmentId 
    from employee
    where name='John'
);

-- Q. no. 4

select e.name
from employee e
join department d on e.departmentId=d.id
where d.name!='IT';

-- Q. no. 5

select d.name, sum(e.salary) as total_salary
from employee e
join department d on e.departmentId=d.id
group by d.name
order by total_salary desc
limit 1;

-- Q. no. 6

select name
from employee
where salary=(
	select max(e.salary)
    from employee e
    join department d on e.departmentId=d.id
    where d.name='HR'
    group by d.id
);

-- Q. no. 7

select e.name, coalesce(d.name, 'No Department') 
from employee e 
left join department d on d.id=e.departmentId;

-- Q. no. 8

select d.name
from employee e
join department d on e.departmentId=d.id
where e.salary > (
	select avg(salary)
    from employee
);

-- Q. no. 9

select d.name
from employee e
join department d on e.departmentId=d.id
group by e.salary, d.name
having count(*)>1;
