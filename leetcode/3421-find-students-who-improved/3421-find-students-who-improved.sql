with leads as (
    select distinct student_id,subject,
    first_value(score) over(partition by student_id,subject order by exam_date rows between unbounded preceding and unbounded following) as first_score,
    last_value(score) over(partition by student_id,subject order by exam_date rows between unbounded
preceding and unbounded following 
    ) as latest_score
    from Scores
),
grouped as (
   select student_id,subject,max(first_score) as first_score,max(latest_score) as latest_score from leads
   group by student_id,subject
)
select student_id,subject,first_score,latest_score from grouped
where first_score is not null and latest_score is not null
and latest_score > first_score
