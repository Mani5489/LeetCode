with src as (
    select num, 
    (row_number() over(order by id)- row_number() over(partition by num order by id)) as gap
    from Logs
)
select distinct num as ConsecutiveNums 
from src
group by num,gap
having count(*) >= 3