-- select * from emp where ename ~* '^A.*i$';  
-- select * from emp where length(ename) <> 6;
--create table student ( sid int generated always as identity ( start with 10 increment by 10),sname varchar);

--select * from emp;

--delete from emp where eid = '102';
--select concat (ename,salary) from  emp;
--select round (4729.29742,-6);
--select count(salary) from emp;
--select ename, sum(salary) from emp where ename  = 'sparsh' group by ename;
--select ename, sum(salary) from emp where ename ='Prakash' group by ename;
-- select ename , sum(salary) from emp group by ename order by sum(salary) desc;

-- ################################
--create table employee (eid int primary key, fname varchar(20), LNAME VARCHAR (20)
--					  , managerid int, foreign key(managerid) references employee(eid) on delete cascade);

-- insert into  employee(eid,fname,lname, managerid) 
-- values (1,'Prakash','yadava',1),
-- (2,'Sparsh','Agarwal',2),(3,'Archisman','Bhattacharya',2),
-- (4,'Jishnu','Srivastava',2),(5,'Prakul','Singh',1),
-- (6,'Aditya','xyz',3);

--select * from employee;

-- select e.fname ||' '||e.lname emp,
-- m.fname||' '||m.lname manager
-- from employee e INNER JOIN employee m ON
-- m.eid = e.managerid order by manager;

-- ######## subquery(nested query)

--select * from emp;

-- select ename , salary from emp
-- where salary> (select salary from emp where ename = 'Aryaman') order by salary desc;

-- select * from emp;
-- end;
-- Begin ;
-- update emp set salary = 32000 where eid = 103;
-- rollback;
-- commit;


--##################################
-- create index empindex on emp(eid);
--select * from emp;

--create unique index on emp(eid);

--drop index empindex ;

--##### task01
-- create table stu( sid int primary key, sname varchar(20),saddress varchar(20),
-- 					scontact int, sage int);
					
-- insert into stu values (1, 'sparsh', 'abc', 1234, 22),
-- (2,'prakash','abc',2638,21),(3,'Jishnu','xyz',2357,21),
-- (4,'Archisman','pqr',1023,20),(5,'Prakul','xyz',1652,20),
-- (6,'Aryaman','abc',5483,20);

-- insert into stu values (7,'aditya','pqr',5472,21),
-- (8,'sneha','abc',4260,21),(9,'sanchita','abc',7267,22),
-- (10,'Dayeem','xyz',1111,22);

--select sname,saddress from stu order by sid ;




-- print records from student with alphabet containg letter a or b or c 
-- hint - '%[^a-c]%' the sign up arrow inside 

-- fabric language to connect two pc
--create table sdetail (sid int primary key, branch varchar(20), grade varchar(20));
-- insert into sdetail values( 1,'cse','O'),
-- (2,'cse','O'),(3,'ece','A'),(4,'mechanical','B'),
-- (5,'ece','C'), (6,'cse','A'),(7,'ece','O'),
-- (8,'cse','C'),(9,'ece','D'),(10,'cse','D');
                            
-- select * from sdetail;
--select s.sname, ss.grade from stu s inner join sdetail ss on s.sid = ss.sid where s.sage>20;

--select sid as code from stu;
--select * from stu where saddress ~* '.*[a-s].*';



-- ###############################################################
-- ############################DAY 2##############################
-- ###############################################################

-- -- \l all db name  \d table_name - table details
-- create table teachers (id bigserial primary key, fname varchar (30), 
-- 					   lname varchar (30),
-- 					  school varchar(30),hire_date date,salary numeric );
					 
-- create table test_data( id serial, name text);
					  
-- insert into test_data(name) select 'xyz' from generate_series(1,50);

--explain select * from test_data limit 10;
--select count(*) from test_data;
--select * from test_data limit 10;

-- insert into teachers values (1, 'prakash','yadava','dps','2023-01-04','50000'),
-- (2, 'Sparsh','Agarwal','shps','2023-01-04','50000'),
-- (3,'Jishnu','Srivastava','grm','2023-01-10',30000),
-- (4,'Archisman','bhatacharya','dps','2023-01-06',30000),
-- (5,'Aditya','dutta','grm','2023-01-10',35000),
-- (6,'Aryman','pandey','shps','2023-01-04',40000);

-- insert into teachers values (7,'Arithro','Dutta','shps','2010-03-14',25000),
-- (8,'Sneha','Tivari','grm','2001-06-13',45000),
-- (9,'Sanchita','tiwari','dps','2005-10-14',30000);

-- select * from teachers where school ='dps';
--select * from teachers where school <> 'dps'; -- <> is not equal too

--select * from emp where salary > 20000;
--select * from emp where salary  <40000;
--select * from emp where salary between 30000 and 50000
--select * from emp where salary In (30000,35000,40000);

--select * from stu;
--select * from stu where sname like 'Ar%';
--select * from stu where sname  not like 'Ar%' and sname not like 's%';
--select * from stu where sname ilike 'S%';


--select * from teachers;
--select fname, lname , hire_date from teachers order by hire_date desc;

--select  fname , lname, hire_date, school from teachers order by hire_date desc, school;

--select * from teachers where school ='dps' and (salary<45000 or salary>35000);

-- problem list teachers at school 'dps' ordered from new hire to old hire
--select  * from teachers where school like '%grm%' order by hire_date desc, fname ;
-- ###############################################################

--select * from color2;
--create table color2 (cid int primary key, cname varchar(50));
--insert into color2 select * from color where cid in (select cid from color)

-- ###############################################################
-- problem 1 write a query that lists the school alphabetical order along with teachers ordered by last name A-Z
-- problem 2  write a query that finds the one teacher whose fname starts with the letter 'S' and who earns more than 40000
-- problem 3 teachers hired since jan 1 2010 ordered by highest paid to lowest

-- sol1 
--select * from teachers;
--select  * from teachers order by school, fname;

-- sol2
--select * from teachers where fname like 'S%' and salary > 30000;

-- sol3 
--select * from teachers where hire_date > '2005-01-01' order by salary desc;
-- ##################################################################
--select * from teachers

-- update teachers 
-- set salary = c.salary
-- from (values (1,20000),
--     (2, 50000)) as c(id,salary ) 
-- where teachers.id = c.id;	

-- update teachers te = c.hire_date from (values (1, to_date('2005-01-15', 'YYYYMMDD')), 
-- (2, to_date('2006-01-11', 'YYYYMMDD'))) as c(id, hire_date) where teachers.id = c.id;set hire_da	
-- ##################################################################

--create table emp_data(name varchar(30), address text );
--insert into emp_data values('sparsh','pune'),('prakash','Gorkhpur'),('Jishnu','Gurugram'),('Prakul','Lucknow');

--copy emp_data to '/Users/sparshagarwal/Desktop/emp1.rtf' with (format csv, header, delimiter '|');

--copy emp_data from '/Users/sparshagarwal/Desktop/emp1.rtf' with (format csv, header , delimiter '|');

--select * from emp_data;
--copy emp_data to '/tmp/emp2.rtf' with (format csv, header, delimiter '|');

-- ##################################################################

-- problem 
--create table licenses(license_id varchar(30), fname varchar(30), lname varchar(30),constraint license_key primary key (license_id));

-- create table registrations ( registration_id varchar(20), registration_date date, license_id varchar(30) references licenses(license_id),
-- 						   constraint registration_key primary key (registration_id, license_id));

-- -- insert into licenses values('T229901','Prakash','Chadda');

-- insert into registrations values( 'A203391','2015-10-28','T229901');
--select * from registrations;

-- check constraint - It evaluates whether data added to a column meets the expanded criteria

-- create table check_constraint_demo(userid serial, user_role varchar(20), salary int, constraint userid_key primary key(userid),
-- 								  constraint check_role_in_list check(user_role in ('Admin','Staffs')), 
-- 								   constraint check_salary_not_zero check(salary>0));

--select * from check_constraint_demo;
--insert into check_constraint_demo values(101, 'Admin',100000);
--insert into check_constraint_demo values(102, 'Staffs',500000000);
--drop table check_constraint_demo;

-- ##################################################################













