with src as (
   select id,temperature,
   lag(temperature) over(order by recordDate asc) as prev_temp,
   recordDate,
   lag(recordDate) over(order by recordDate) as prev_rec
   from Weather 
)
select id from src
where temperature > prev_temp and datediff(recordDate,prev_rec)  = 1

