SELECT w.Id 
FROM weather w
INNER JOIN weather w2 on w.recordDate = dateadd(day, 1, w2.recordDate)
WHERE w.temperature > w2.temperature