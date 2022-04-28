# Write your MySQL query statement below
select name as 'Employee'
from Employee e
where e.salary  > (
select e2.salary       
    from Employee e2
    where e.managerId   = e2.id
)