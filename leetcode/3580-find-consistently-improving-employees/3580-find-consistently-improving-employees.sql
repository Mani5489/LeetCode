with recent as (
    select employee_id,review_date,rating,row_number() over(partition by employee_id order by review_date desc) as rn
    from performance_reviews 
    where employee_id in (select employee_id from performance_reviews group by employee_id having count(employee_id) >=3 )
)
,recentIds as (
    select employee_id,review_date,rating from recent
    where rn <= 3
)
, ratings as (
select 
distinct
r1.employee_id,
rating as one,
lead(rating,1) over(partition by employee_id order by review_date) as two,
lead(rating,2) over(partition by employee_id order by review_date) as three
from recentIds r1
)
select 
r.employee_id,
e.name,
(three-one) as improvement_score 
from ratings r
join employees e
on r.employee_id = e.employee_id
where three is not null
and (one < two) and (two < three)
order by (three-one) desc,e.name