with Winter as (
    select 'Winter' as season,p.category as category ,
    sum(quantity) as total_quantity, sum(quantity * price) as total_revenue 
    from sales s join products p on s.product_id = p.product_id 
    where month(sale_date) in (12,1,2)
    group by category,season
),
Spring as (
    select 'Spring' as season,p.category as category ,
    sum(quantity) as total_quantity, sum(quantity * price) as total_revenue 
    from sales s join products p on s.product_id = p.product_id 
    where month(sale_date) in (3,4,5)
    group by category,season
),
Summer as (
    select 'Summer' as season,p.category as category ,
    sum(quantity) as total_quantity, sum(quantity * price) as total_revenue 
    from sales s join products p on s.product_id = p.product_id 
    where month(sale_date) in (6,7,8)
    group by category,season
),
Fall as (
    select 'Fall' as season,p.category as category ,
    sum(quantity) as total_quantity, sum(quantity * price) as total_revenue 
    from sales s join products p on s.product_id = p.product_id 
    where month(sale_date) in (9,10,11)
    group by category,season
), full as (
select * from Winter 
union all
select * from Spring 
union all
select * from Summer  
union all
select * from Fall 
)
, getTop as(
    select *, row_number() over(partition by season order by total_quantity desc,total_revenue desc,category) as rn
    from full
)
select season,category,total_quantity,total_revenue from getTop
where rn = 1