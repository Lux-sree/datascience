-- UPDATE -->updates the values in rows or cell
-- syntax:
-- update table_name 
-- set col1= 
-- where primary_key=
-- 
update student 
set fees=fees-500
where Adno=222;
select * from student;

-- update division of rohini as b
update student
set division='b'
where Adno=555;
-- update the name of anna roy as ann roy
update student
set student_name='ann roy'
where Adno='111';

-- update all students fees +500 ---->for all datas to be updated in a col-->can chng safe update mode
set sql_safe_updates=0; -- change safe update mode
update student
set fees=fees+500;
