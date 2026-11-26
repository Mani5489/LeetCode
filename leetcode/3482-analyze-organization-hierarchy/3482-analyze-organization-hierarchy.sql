with recursive dlevels as (
    select e1.*,1 as rank_level from Employees e1 where manager_id is null
    union all
    select e1.*,e2.rank_level+ 1 as rank_level from Employees e1 inner join dlevels e2 on e1.manager_id = e2.employee_id 
),
levels as (
select employee_id, employee_name, manager_id,salary,dense_rank() over(order by rank_level) as ranks from dlevels
),
subordinate_map as (
    SELECT 
        employee_id AS manager_id, 
        employee_id AS subordinate_id,
        salary as salary 
    FROM Employees
    UNION ALL
    SELECT 
        m.manager_id, 
        e.employee_id AS subordinate_id,
        e.salary as salary 
    FROM subordinate_map m
    INNER JOIN Employees e ON m.subordinate_id = e.manager_id 
)
, tandb as (
    select manager_id,count(subordinate_id)-1 as team_size,sum(salary) as budget 
    from subordinate_map 
    group by manager_id
) 
select 
t.employee_id as employee_id,
t.employee_name as employee_name,
t.ranks as level,
l.team_size as team_size,
l.budget as budget
from tandb l
inner join levels t on t.employee_id = l.manager_id
order by t.ranks, l.budget desc,t.employee_name