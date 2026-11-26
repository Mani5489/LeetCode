with rankUser as (
    select user_id,activity_type,lead(activity_type) over(partition by user_id order by activity_date) as lead_activity_type
    from UserActivity
)
,filteredUser as (
    select distinct user_id from rankUser where activity_type = 'free_trial' and lead_activity_type = 'paid'
)
, freeTrial as (
select
user_id, 
sum(activity_duration) over(partition by user_id,activity_type order by activity_type) as trial_avg_duration,
count(user_id) over(partition by user_id,activity_type order by activity_type) as trial_avg_duration_count 
from UserActivity 
where user_id in (select user_id from filteredUser)
and activity_type = 'free_trial'
)
, paidTrial as (
select
user_id, 
sum(activity_duration) over(partition by user_id,activity_type order by activity_type) as paid_avg_duration,  
count(user_id) over(partition by user_id,activity_type order by activity_type) as paid_avg_duration_count
from UserActivity 
where user_id in (select user_id from filteredUser)
and activity_type = 'paid'
)
select 
f.user_id as user_id,
round(avg(trial_avg_duration)/trial_avg_duration_count,2) as trial_avg_duration,
round(avg(paid_avg_duration)/paid_avg_duration_count,2) as paid_avg_duration
from freeTrial f inner join paidTrial p on f.user_id = p.user_id
group by f.user_id