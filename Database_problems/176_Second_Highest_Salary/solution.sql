SELECT MAX(CASE 
                WHEN rank = 2 THEN salary
                ELSE NULL
           END)
FROM (SELECT salary, DENSE_RANK() OVER(ORDER BY salary DESC) rank FORM employee) AS t