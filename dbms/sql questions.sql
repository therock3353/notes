--  joins
--      1. INNER JOIN
--      2. OUTER JOIN - Left Outer Join
--                      Right Outer Join
--  Pets Table:
--     ID	NAME	AGE	OWNER_ID
--      1	Fido	7	1
--      2	Missy	3	1
--      3	Sissy	10	2
--      4	Copper	1	3
--      5	Hopper	2	0
--
--  Pets Owners Table
--      ID	NAME	PHONE_NUMBER
--      1	Johnny	4567823
--      2	Olly	7486513
--      3	Ilenia	3481365
--      4	Luise	1685364
--
--  Inner Join:
SELECT pets.name AS pet_name, owners.name AS owner
  FROM pets
  JOIN owners
  ON pets.owner_id = owners.id;

--      PET_NAME	OWNER
--      Fido	    Johnny
--      Missy	    Johnny
--      Sissy	    Olly
--      Copper	    Ilenia

--  Left Outer Join
SELECT pets.name AS pet_name, owners.name AS owner
  FROM pets
  LEFT JOIN owners
  ON pets.owner_id = owners.id;

--      PET_NAME	OWNER
--      Fido	    Johnny
--      Missy	    Johnny
--      Sissy	    Olly
--      Copper	    Ilenia
--      Hopper	    NULL    <======= this row is also included because of left outer join
--                                   all rows from left/first table in join (which is Pets in this case)
--                                   are included.
--
--
--
-- 1) SQL Query to find the second highest salary of Employee
-- 2) SQL Query to find Max Salary from each department
-- 3) How do you find all employees who are also managers
-- 4) There is a table which contains two columns Student and Marks, you need to find all the students,
--     whose marks are greater than average marks i.e. list of above-average students.
-- 5) Write SQL Query to find duplicate rows in a database? and then write SQL query to delete them

-- ==========================================================================================
-- ==========================================================================================
-- ==========================================================================================


