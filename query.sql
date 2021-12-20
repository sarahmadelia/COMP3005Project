select ID from Users
where email = ${"%s"} and User_Password = ${"%s"} 

------------------------------------------------------------------
select * from BookStore
------------------------------------------------------------------
select * from Book_Basket
where Basket_ID = "BA-10000"
----------------------------------------------------------------------------
select * from Book_Orders
where ID = "US-10000"
-------------------------------------------------------------------------
select * from Orders
where Order_Number = "OR-10001"
----------------------------------------------------------------------------
Update Book_Basket
set amount = amount + "1"
where Basket_ID = "BA-10000" and ISBN = "BK-10001"
--------------------------------------------------------------------------
insert into Book_Basket values ()
-------------------------------------------
delete from Book_basket where Basket_ID = "BA-10000" and ISBN = "3"
------------------------------------------------------------------
select Amount from Book_BookStore
where ISBN = "BK-10001"
-----------------------------------------------------
Update Book_BookStore
set amount = amount - "1"
where ISBN = "Bk-10000"
---------------------------------------------------------
insert into Orders values("US-10000", "OR-10001", "TR-10001", "Billing address", "shipping address", 3 ,1999);
---------------------------------------
insert into Book_Orders values("US-10000","OR-10001","BK-10001", 2);
--------------------------------
insert into Bank values("BN-10000","RF-10000","access bank","oniru","accessbank@email.com","111-111-1111");
----------------------------------------------------
insert into Publisher_Bank values ("PB-10000","BN-10000","RF-10000");
--------------------------------------------------
insert into Bookstore_Bank values ("BS-10000","BN-10000","RF-10000",100,12,2020);
-------------------------------------------------------------------------
create view sales_by_year(order_number,month,year,total_sales) as
select Orders.Order_Number,Month,Year,sum(Price)
from Orders join Book_Orders on Orders.Order_number = Book_Orders.Order_number
group by Orders.Order_Number,Orders.Month,Orders.Year
-----------------------------------------------------------------------------
select sum(total_sales)
from sales_by_year
where month >= 1 and year >= 1999 and month <= 12 and year <= 2021
--------------------------------------------------------------------------
select Book_Basket.ISBN, Book.Publisher_ID,Book_Basket.Amount, Book.Selling_price, Book.Publisher_percentage
from Book_Basket join Book_Bookstore on (Book_Basket.ISBN = Book_Bookstore.ISBN ) join Book on (Book.ISBN = Book_Bookstore.ISBN)
where Book_Basket.Basket_ID = "BA-10000" and Book_Basket.Amount <= Book_Bookstore.Amount
--------------------------------------------------------------------------------------------
select Book.ISBN, Publisher_ID, Title, Book_Basket.Amount, Selling_Price, Genre, Author_Name
from Book_Basket join Book on (Book_Basket.ISBN = Book.ISBN)
where Book_Basket.Basket_ID = "BA-10000"
----------------------------------------------------------------------------
select * 
from Book join Book_Bookstore on (Book.ISBN = Book_Bookstore.ISBN)
where Book.Title like "%H%"
------------------------------------------
select Bookstore_Bank.Reference_no, Publisher_ID, month,year,amount,Bookstore_Bank.Bank_ID from 
Bookstore_Bank join Publisher_Bank on (Bookstore_Bank.Reference_no = Publisher_Bank.Reference_no)
---------------------------------------------------------------------------------------------
select count(*)
from Book_Bookstore join Book on Book.ISBN = Book_Bookstore.ISBN
where Title = "Harry potter new world" and Author_name = "J.K.Bowling" and Publisher_ID = "PB-10000"