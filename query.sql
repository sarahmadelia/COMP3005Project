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