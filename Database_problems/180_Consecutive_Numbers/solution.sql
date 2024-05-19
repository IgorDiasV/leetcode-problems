SELECT DISTINCT num AS ConsecutiveNums 
FROM
    (SELECT 
            id,
            num,
            LAG(num) OVER(ORDER BY id) AS ant,
            LEAD(num) OVER(ORDER BY id) AS pos,
            LAG(id) OVER(ORDER BY id) AS antid,
            LEAD(id) OVER(ORDER BY id) AS posid
    FROM Logs) AS t
WHERE num = ant AND pos = num and (id -1) = antid and (id + 1) = posid