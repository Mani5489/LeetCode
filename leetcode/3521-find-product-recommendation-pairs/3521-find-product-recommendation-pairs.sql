select 
a.product_id as product1_id,
b.product_id as product2_id,
pf1.category  as product1_category,
pf2.category  as product2_category, 
count(*) as customer_count
from ProductPurchases a
join ProductPurchases b on a.user_id = b.user_id 
join ProductInfo pf1 on a.product_id = pf1.product_id
join ProductInfo pf2 on b.product_id = pf2.product_id
where b.product_id > a.product_id
group by a.product_id,b.product_id
having customer_count >= 3
order by customer_count desc,product1_id ,product2_id 