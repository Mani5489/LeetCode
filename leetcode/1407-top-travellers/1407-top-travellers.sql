with src as (
    select u.name,coalesce(sum(r.distance) over(partition by u.id),0) as travelled_distance 
    from Users u left join Rides r on u.id = r.user_id
)
select distinct name,travelled_distance 
from src
order by travelled_distance desc ,name asc