-- JOIN --

create table customer(cid int primary key,name varchar(30),location varchar(30),pid int);
describe customer;
create table prod(pid int primary key,item varchar(30),price decimal(10,2));
describe prod;
insert into customer
values(101,'Vishal','Aluva',301),
(102,'Nirmal','Ern',303),
(103,'Muhammed','Thrissur',304),
(104,'Azeem','Kozhikode',305),
(105,'Naveen','Malappuram',311);
insert into prod
values(301,'Washing machine',15000),
(302,'TV',30000),
(303,'Mixi',3000),
(304,'Oven',5000),
(305,'Fridge',16000),
(306,'Radio',2000),
(307,'Flask',1000);
select * from customer;
select * from prod;

-- pid is the foreign key in customer table,as it is the primary key from the prod table
-- INNER JOIN: done only if a common field present in both table
-- if any observation has no matching value,its not displayed
select name,item,price
from customer 
inner join prod
on customer.pid=prod.pid;
-- LEFT JOIN: 1st given table's whole data will be there,adjacent data from 2nd table also given
-- if no adjacent data in 2nd,then null occur
-- RIGHT JOIN: opposite of left join
select * from customer
left join prod
on customer.pid=prod.pid;
select * from customer
right join prod
on customer.pid=prod.pid;

-- SELF JOIN--->used to fetch data from a single table itself
-- outside eg:
-- SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, A.City
-- FROM Customers A, Customers B
-- WHERE A.CustomerID <> B.CustomerID
-- AND A.City = B.City 
-- ORDER BY A.City;               -- obtain 2 peoples name from same city in a row
