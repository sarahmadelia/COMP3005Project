create function report_sales_by_year(month1 numeric(2), year1 numeric(4,0), month2 numeric(2),year2 numeric(4,0))
	returns integer
    begin
    declare sales integer
		select sum(total_sales) into sales
        from sales_by_year
        where month >= month1 and year >= year1 and month <= month2 and year <= year2
	return sales
    end
-------------------------------------------------------------------------------------------