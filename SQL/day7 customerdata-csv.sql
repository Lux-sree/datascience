select * from customerdata;
describe customerdata;
-- 1.Find the number of persons from india
select count(*) from customerdata
where country='india';
-- Display the details of person from us
select * from customerdata
where country='us';
-- 3.Display the fname,lname and age of all persons they are from china.The data should display in the ascending order of age
select fname,lname,age from customerdata
where country='china'
order by age asc;
-- 4..Display the details of maximum aged person ireland
select * from customerdata
where age=(select max(age) from customerdata);
-- 5.Display the profession of minimum aged person from india
select profession,age from customerdata
where age=(select min(age) from customerdata where country='india');
-- 6.Display the details of all the person their age is greater than 70
select * from customerdata
where age>70;
-- 7.Display the fname and profession of the persons their age is greater than 50 and their country is china
select fname,profession from customerdata
where age>50 and country='china';
-- 8..Display the details of the person their profession is Pilot
select * from customerdata
where profession='pilot';
-- 9.Display the details of all the Teachers from uk
select * from customerdata
where profession='teacher' and country='uk';
-- 10.Display the fname and lname of the persons they are Accountant from india
select fname,lname from customerdata
where profession='accountant' and country='india';
-- 11.Display the details of maximum aged 2 Musicians from india
select * from customerdata
where profession = 'musician' 
order by age desc
limit 2;

-- 12.Display the fname, profession and age of all Teachers in the decreasing order of the age.
select fname,profession,age from customerdata
where profession='teacher'
order by age desc;
-- 13.Display the fname of maximum aged person, he is a Musician from india
select fname,age,profession from customerdata
where (profession='musician' and country='India') and age=(select max(age) from customerdata where profession='musician' and country='India'); 
-- 14.Display the fname of minimum aged Dancer from india
select fname from customerdata 
where (profession='dancer' and country='india') and age=(select min(age) from customerdata where profession='dancer' and country='india');
