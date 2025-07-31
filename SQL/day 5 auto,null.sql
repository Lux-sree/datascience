-- auto increment of primary key,
-- not null -->will never accept null value
-- primary key is always not accepting null
create table personTable(Personid int auto_increment primary key ,fname varchar(20) not null,lname varchar(20),age int);
describe persontable;
-- to enter only 2 values
insert into persontable(fname,lname) 
values('Anu','T');
insert into persontable(fname,lname,age)
values('Anna','T',34);
select * from persontable;
insert into persontable(fname,age)
values('Ann',42);