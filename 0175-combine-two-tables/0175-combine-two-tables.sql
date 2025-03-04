# Write your MySQL query statement below
SELECT firstName, lastName, city, state FROM Person t1 LEFT JOIN Address t2 on t1.personId = t2.personId