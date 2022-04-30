# Write your MySQL query statement below
select name, sum(amount) as balance
from Users u join Transactions t on u.account = t.account
group by name
having sum(amount) > 10000