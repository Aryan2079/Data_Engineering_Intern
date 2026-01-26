-- Q. no. 1

create table Department(
	id serial primary key, 
    name varchar(50)
);

create table Employee(
	id serial primary key,
    name varchar(50),
    departmentId int references department(id),
    salary int, 
    active boolean
);

insert into Department(name)
values
('IT'),
('Admin'),
('HR'),
('Health'),
('Accounts');

insert into Employee(name, departmentId, salary, active)
values
('John', (select id from Department where name='IT'), 2000, true),
('Sean', (select id from Department where name='IT'), 4000, true),
('Eric', (select id from Department where name='Admin'), 2000, true),
('Nancy', (select id from Department where name='Admin'), 2000, true),
('Lee', (select id from Department where name='HR'), 3000, true),
('Steven', (select id from Department where name='Accounts'), 2000, true),
('Matt', (select id from Department where name='IT'), 5000, true),
('Sarah', (select id from Department where name='IT'), 2000, false);

-- Q. no. 2

select * 
from employee
order by salary desc;

-- Q. no. 3

select distinct(salary) as distinct_salary
from employee;

-- Q. no. 4

select count(id)
from employee
where active is true;

-- Q. no. 5

set sql_safe_updates = 0;
update employee
set departmentID = (
	select id 
    from department 
    where name='HR'
)
where name='Nancy';

-- Q. no. 6

select * 
from employee
order by salary desc
limit 2;

-- Q. no. 7

select e.name, d.name as department
from employee e
join department d on d.id=e.departmentId;

-- Q. no. 8

select d.name as department, count(e.id) as employee_count
from employee e
join department d on e.departmentId=d.id
group by d.name
order by employee_count desc
limit 1;

-- Q. no. 9

select d.name
from employee e
right join department d on e.departmentId=d.id
where e.id is null;

-- Q. no. 10

select distinct e1.name as employee_name, e1.salary as salary
from employee e1
join employee e2 
	on e1.salary=e2.salary
    and e1.id != e2.id
order by e1.salary, e1.name;


  