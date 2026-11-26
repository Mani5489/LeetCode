with src as(
    select salary,dense_rank() over(order by salary desc) as rn
    from Employee
)
select max(salary) as SecondHighestSalary  from src where rn = 2