SELECT t.request_at AS Day,
       ROUND(SUM(IIF(t.status = 'completed',0 ,1.0))/COUNT(*), 2) AS 'Cancellation Rate'
FROM Trips t 
INNER JOIN Users u1 on u1.users_id = t.client_id and u1.banned = 'No'
INNER JOIN Users u2 on u2.users_id = t.driver_id and u2.banned = 'No'
WHERE T.request_at between convert(date, '2013-10-01') and convert(date, '2013-10-03')
GROUP BY t.request_at