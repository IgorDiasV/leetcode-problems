 select round(count(distinct a.player_id)*1.0/count(distinct t.player_id), 2) fraction
 from 
 (SELECT player_id, min(event_date) first_login
  from activity
  group by player_id
  ) as t
  left join activity a on t.player_id = a.player_id  and 
          t.first_login = DATEADD(day, -1, a.event_date)