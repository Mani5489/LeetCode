with src as (
select 
e.employee_id ,
e.employee_name ,
e.department ,
sum(duration_hours) as hoursWeek
from employees e
left join meetings m on e.employee_id = m.employee_id 
group by yearweek(m.meeting_date,1),
e.employee_id ,
e.employee_name ,
e.department
) 
select employee_id,employee_name,department,count(hoursWeek) as meeting_heavy_weeks 
from src 
where hoursWeek > 20 
group by employee_id,employee_name,department
having count(hoursWeek) >= 2
order by count(hoursWeek) desc ,employee_name 