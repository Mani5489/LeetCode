with src as(
    select score,dense_rank() over(order by score desc) as rn
    from Scores
)
select score,rn as 'rank' from src