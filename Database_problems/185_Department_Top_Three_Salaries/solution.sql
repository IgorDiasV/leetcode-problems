SELECT Department,
       Employee,
       Salary
FROM(
    SELECT 
        d.name as Department, 
        e.name as Employee, 
        e.Salary,
        DENSE_RANK() OVER(PARTITION BY d.name ORDER BY e.salary desc) as rank 
    FROM Employee e
    INNER JOIN Department d on e.departmentId  = d.id
) AS T
WHERE rank <=3