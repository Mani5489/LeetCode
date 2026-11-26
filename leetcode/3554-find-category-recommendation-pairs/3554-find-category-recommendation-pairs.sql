with categoryPairs as (
    select 
    distinct
    pp.user_id as user_id,
    p1.category as category
    from ProductInfo p1 
    join ProductPurchases pp on p1.product_id = pp.product_id  
)
select 
c1.category as category1, 
c2.category as category2,
count(distinct c1.user_id) as customer_count 
from categoryPairs c1
join categoryPairs c2
on c1.user_id = c2.user_id
where c1.category < c2.category
group by c1.category,c2.category
having count(distinct c1.user_id) >= 3
order by count(distinct c1.user_id) desc,c1.category,c2.category

