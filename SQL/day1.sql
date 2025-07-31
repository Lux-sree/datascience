-- create database
CREATE DATABASE database_may_25;
-- create table ---> studtable : studname,rollno
CREATE TABLE studenttable(stud_name varchar(30),rollno int);
-- select * from tablename --->to display table
SELECT * FROM studenttable;
-- insert into tablename values(valueset 1),(values2); 
insert into studenttable 
values("Anu",23);
insert into studenttable
values("Manuel",45),("Aravind",12),("Malini",36);
-- primary key--->to avod duplicatn and uniquely identify,done while creating a table
CREATE TABLE studenttable1(stud_name varchar(30),rollno int primary key);
insert into studenttable1
values("Manuel",45),("Aravind",12),("Malini",36);
select * from studenttable1;
-- each column:field
-- each row:record

-- decimal(10,2)--->datatype with 8 digits can be used and 2 digits after point
-- example:
create table employee(empid int primary key,name varchar(30),salary decimal(10,2),profession varchar(30));
insert into employee
values(101,"Ram",20000,"Supervisor"),
(102,"Seetha",25000,"Engineer"),
(103,"Rahul",30000,"Advocate"),
(104,"Vivek",34000,"Doctor");
select * from employee;

-- can get only required cols
select name,profession from employee; 
select NAME,SALARY from Employee;-- not case sensitive

-- can get all details of a specific person,uses condition
-- select colnames from tablename where condition;
select * from employee 
where salary>28000;

-- 1.display the details of employees their profession is doctor
select * from employee
where profession="doctor";
-- 2.display details of employees whose salary less than 25000
select * from employee
where salary<25000;
-- 3.display details of employee ram
select * from employee
where name="ram";
-- 4.display names of employees whose profession not advocate
select name from employee
where profession!="advocate";

-- LIKE -->for words and letters
-- 1. display the details of the persons their name start with 'r'
-- % matches any no of chars
-- _ matches 1 char
select * from employee
where name like 'r%';	-- dives ram and rahul
-- or
select * from employee
where name like 'r__';  -- gives ram only
-- 2.display the details of employees their profession end with r
select * from employee
where profession like '%r';
-- 3.display the details of employees names have a as second letter
select * from employee
where name like '_a%';

-- multiple conditions-->AND
-- 1.select the name and salary of the employees where salary greater than 25000 and lessthan 35000
select * from employee
where salary>25000 and salary<35000;
-- 2.display salary of all employees their salary greater than 25000 and profession is not doctor
select * from employee
where salary>25000 and profession!="doctor";  		-- --> "<>" can also be not equal to
-- 3.display the details of employees whose name start with r and salary less than 25000
select * from employee
where name like 'r%' and salary<25000;

-- multiple conditions-->OR
-- 1.display the details of employees their profession is either advocate or doctor
select * from employee
where profession="doctor" or profession="advocate";
-- 2.display the details of the employees whose name start with r or s
select * from employee
where name like 'r%' or name like 's%';

-- multiple conditions-->NOT
select * from employee
where not profession="advocate";  -- syntax: where not

-- SORT-->order by colname asc or desc
select * from employee
order by salary desc;  -- for ascending ,use asc
-- 1 display the details of an employee in alphabetical order of their name
select * from employee
order by name asc;
-- 2 display the details of the employees in the descending order of their empid
select * from employee
order by empid desc;
-- 3 display the details of the employee in alphabetical order of their profession
select * from employee
order by profession asc;









