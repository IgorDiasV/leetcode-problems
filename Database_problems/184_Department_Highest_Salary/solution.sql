SELECT Department,
       Employee,
       Salary 
FROM(
        SELECT d.name Department,
               e.name AS Employee ,
               e.salary, 
               Rank() OVER(partition by departmentID order by salary desc) as rank
        FROM Employee e 
             INNER JOIN Department d on d.id = e.departmentId
             ) as t
WHERE Rank = 1 