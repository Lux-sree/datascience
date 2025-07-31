create table student(adno int primary key,student_name varchar(30),class int,division varchar(10),fees decimal(10,2));
insert into student
values(111,'anna roy',11,'a',4500.00),
(222,'mohit sharma',11,'b',5500.00),
(333,'k p gupta',12,'b',4000.00),
(444,'rahul',10,'a',3500.00),
(555,'rohini s',12,'c',4000.00),
(666,'rohan sharma',11,'c',3000.00);
select * from student;

-- 1display the details of students studying in class 12
select * from student
where class=12;
-- 2.display name of students studying in 11 b
select * from student
where class=11 and division='b';
-- 3.display the details of students in the ascending order of their fees
select * from student
order by fees asc;
-- 4.display the name of students end with 'a'
select * from student
where student_name like '%a';
-- 5.display the name of students start with a
select * from student
where student_name like 'a%';
-- 6.display the details of student their fees between 3500 and 5000
select * from student
where fees between 3500 and 5000;  		-- ---used keyword between here and keyword and
-- 7.display the details of students not studying in 10
select * from student 
where not class=10;
-- 8.display the details of student studying in class 11 in the descending order of their fees
select * from student
where class=11
order by fees desc;
-- 9.Display all the students in the division B in the alphabetical order of their name
select * from student
where division='b'
order by student_name desc;
-- 10.Display the name of students their names have ‘o’ as second letter
select * from student
where student_name like '_o%';


-- AGGREGATE FUNCTIONS
-- count(),sum(),avg(),max(),min()
select count(*)
 from student;     				-- count of all rows from table
select count(student_name)
 from student;					-- count of student name
select count(student_name) as std_count 
from student;  					-- count of studentname and heading set as std_count
select avg(fees) as avg_fee
 from student;					-- avg of fees
select sum(fees) as fee_sum 
from student;					-- sum of fees
select max(fees) as max_fee 
from student;					-- max fee
select min(fees) as min_fee 
from student;					-- min fee

-- details of student paying max fee
select *  
from student
where fees=(select max(fees) from student);  -- nested
-- display the details of the student who paid lowest fees
select * from student
where fees=(select min(fees) from student);
-- display the details of student with fee above average fee
select * from student
where fees>(select avg(fees) from student);

-- GROUP BY HAVING
-- ----->where cannot be used here,instead use having to write condition
-- classwise count
select count(*),class 
from student 
group by class;
-- find total fee amount collected in each class
select sum(fees),class
from student
group by class;
-- display total fee amount collected in each class in ascending order of fee amount
select sum(fees) as amnt ,class
from student
group by class
order by amnt asc;
-- display the classes and total amnt collected if it is greater than 5000
select sum(fees) as amnt ,class
from student
group by class
having amnt>5000;


-- LIMIT -->first 3 values from table 
-- OFFSET --> skips the amount of values and shows the rest according to the limit
-- display details of three students paying high fees
select * from student 
order by fees desc
limit 3;   
-- -- display details of three students paying high fees,skipping first one
select * from student 
order by fees desc
limit 3 offset 1;  -- displays top 3,but if offset is one,avoids 1st and then displays the next 3 
-- display details of students paying highest fees,if more than 1 pay high fee------------>this cannot be done using limit

-- DISTINCT-->will provide values uniquely,no duplicate and show value
-- which all class's students payedfees,if atleast 1 student
select distinct class 
from student;

-- BETWEEN 
select * 
from student
where fees between 4000 and 5000;

-- IN(value1,value2...)
select * from student
where class in (11,12);

-- SELECT-->
-- WHERE,AND,OR,NOT
-- COUNT,MIN,MAX,AVG,SUM
-- GROUPBY,HAVING
-- LIMIT,OFFSET
-- BETWEEN,DISTINCT,IN



