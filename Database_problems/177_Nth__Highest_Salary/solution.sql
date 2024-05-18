create function getNthHighestSalary(@n int) returns int
as 
begin
    declare @aux int

    select @aux =max(case 
                        when rank = @n then salary
                        else null
                        end
                    ) 
    from
    (select distinct salary, dense_rank() over(order by salary desc) rank
     from employee
    ) as t
    return @aux
end