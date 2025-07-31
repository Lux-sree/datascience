create table products(itemno int primary key,iname varchar(15),price decimal(10,2),quantity int); 
describe products;

insert into products
values(101,'soap',50,100),
(102,'powder',100,50),
(103,'face cream',150,25),
(104,'pen',50,200),
(105,'soap box',20,100);

-- 3.display all items info
select * from products;
-- 4.display itemname and price values
select iname ,price from products;
-- 5.display soap info
select * from products
where iname='soap';
-- 6.Display the item information whose name starts with letter 's'.
 select * from products
 where iname like 's%';
 -- 7.Display item table information in ascending order based upon item name. 
select * from products
order by iname;
-- 8.Display item name and price in descending order based upon price. 
select iname, price from products
order by price desc;
-- 9.Display item name, whose price is in between 50 to 100. 
select iname from products
where price between 50 and 100;
-- 10.Add new column totalprice with number (10, 2).alter
alter table products
add totalprice decimal(10,2);
select * from products;
-- 11.Insert value in total price by Price*Quantity
set sql_safe_updates=0;
update products
set totalprice=price*quantity;
set sql_safe_updates=1;
-- 12.Increase price of soap as 60
update products
set price=60
where itemno=101;
-- 13.Increase price of all items by 5
set sql_safe_updates=0;
update products
set price=price+5;
set sql_safe_updates=1;
-- 14.Display the item with highest price
select max(price) as higest_price
from products;
-- 15.Remove powder information. 
delete from products
where itemno=102; 
-- 16. Remove totalprice column.
alter table products
drop totalprice;
select * from products;
-- 17.Display the itemname which is less in quantity
select min(quantity) as less_quanity
from products;
-- 19.Specify the product in the table its price is highest
select * from products
where price=(select max(price) from products);





 

