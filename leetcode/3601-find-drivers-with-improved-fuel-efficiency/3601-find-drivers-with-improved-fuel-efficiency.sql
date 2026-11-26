with filter as (
    select driver_id from trips where month(trip_date) between 1 and 6
    intersect 
    select driver_id from trips where month(trip_date) between 7 and 12
)
, first_half as (
    select d.driver_id,d.driver_name,
avg(distance_km/fuel_consumed) over(partition by driver_id) as first_half_avg 
from drivers d inner join trips t 
on d.driver_id = t.driver_id and t.driver_id in (select driver_id from filter)
where month(trip_date) between 1 and 6
),
second_half as (
        select d.driver_id,d.driver_name,
avg(distance_km/fuel_consumed) over(partition by driver_id) as second_half_avg 
from drivers d inner join trips t 
on d.driver_id = t.driver_id and t.driver_id in (select driver_id from filter)
where month(trip_date) between 7 and 12
)
select distinct f.driver_id,f.driver_name,
round(first_half_avg,2) as first_half_avg,
round(second_half_avg,2) as second_half_avg,
CAST(second_half_avg - first_half_avg AS DECIMAL(10,2)) as efficiency_improvement
from first_half f join second_half s on f.driver_id = s.driver_id
where CAST(second_half_avg - first_half_avg AS DECIMAL(10,2)) > 0
order by efficiency_improvement desc ,f.driver_name
