delimiter $$
create trigger fill_books 
before update on Book_Bookstore
For each row
begin 
	if new.amount < 10 Then
		set new.amount = new.amount +  (select sum(amount) from Book_Orders join Orders on Orders.Order_number = Book_Orders.Order_number where month = 12);
	end if;
end;$$
delimiter ;
