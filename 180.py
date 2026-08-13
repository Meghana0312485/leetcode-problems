
select distinct l1.num as ConsecutiveNums
from Logs l1
where (l1.id + 1, l1.num) in (select id, num from Logs)
  and (l1.id + 2, l1.num) in (select id, num from Logs);