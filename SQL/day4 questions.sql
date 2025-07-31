create table employeetab(empid int primary key,name varchar(30),department varchar(30),salary decimal(10,2),joindate date,managerid int);
insert into employeetab
values(101,'Alice','HR',60000,'2019-03-15',null),
(102,'Bob','IT',75000,'2020-07-10',104),
(103,'Charlie','IT',72000,'2021-01-20',104),
(104,'David','IT',90000,'2018-11-01',null),
(105,'Eva','Sales',65000,'2022-05-05',106),
(106,'Frank','Sales',80000,'2017-04-23',null),
(107,'Grace','HR',58000,'2023-02-14',101);
select * from employeetab;
-- 1.Find all employees who joined after January 1, 2020.
select * from employeetab
where joindate >'2020-01-01';
-- 2.List the departments along with the total number of employees in each department.
select department,count(*) as total_employees
from employeetab
group by department;
-- 3.Retrieve names of employees who earn more than the average salary in the IT department.
select name 
from employeetab
where salary>(select avg(salary) from employeetab where department='IT' );
-- 4.Find the names of employees who do not report to any manager.
select name
from employeetab
where managerid is null;   -- use is null
-- 5.Get the highest salary in each department.
select distinct department,max(salary)
from employeetab
group by department;
-- 6.Find employees who share the same manager.
select name,managerid
from employeetab
where managerid in (select managerid
from employeetab
where managerid is not null
group by managerid 
having count(*)>1);
-- OR
select managerid,group_concat(name) as employees      -- grouped things taken from diff rows printed in a single string form
from employeetab
where managerid is not null
group by managerid
having count(managerid) >1;

-- 7.List the employees along with their manager's name.
SELECT NAME,(SELECT NAME AS MANAGER FROM EMPLOYEETAB E2 WHERE E1.MANAGERID=E2.EMPID) FROM EMPLOYEETAB E1;

-- 8.Get the second highest salary in the company.
select distinct salary
from employeetab
order by salary desc
limit 1 offset 1;
-- 9.Find the average salary of employees grouped by year of joining.
select year(joindate),avg(salary) as average 
from employeetab
group by year(joindate)
order by year(joindate);
-- 10.Delete employees who joined before 2018.
set sql_safe_updates=0;
delete from employeetab
where year(joindate)<'2018';
set sql_safe_updates=1;
-- 11.List all employees with salaries between 60000 and 80000
select name,salary
from employeetab
where salary between 60000 and 80000;
-- 12.show the number of employees managed by each manager
select managerid,count(empid)
from employeetab
where managerid is not null
group by managerid;
-- 13.list employees who joined in 2022
select name
from employeetab
where year(joindate)=2022;
-- 14.find the total salary expense per department
select department,sum(salary) as total_salary
from employeetab
group by department;
-- 15.display the employee with the lowest salary
select  distinct salary,name
from employeetab
order by salary asc
limit 1 offset 1 ;
-- 16.count the no of employees in each dept having salary above 65000
select department,count(*)
from employeetab 
where salary>65000
group by department;
select * from employeetab;
-- 17.list departments having more than 1 employees
select distinct department,count(*)
from employeetab
group by department
having count(*)>1;
-- 18.display the average salary for each managers team
select avg(salary),department
from employeetab
group by department;
-- 19.find employees who donot report to anyone
select name
from employeetab
where managerid is null;





