delete from Basket;
delete from BookStore;
delete from Publisher;
delete from Users;
delete from Orders;
delete from Book_Orders;
delete from Book;
delete from Book_Bookstore;
delete from Book_Basket;
delete from Bank;
delete from Publisher_Bank;
delete from Bookstore_Bank;
insert into Basket values ("BA-10000");
insert into Basket values ("BA-10001");
insert into BookStore values("BS-10000","Look inna book", "bookstore address", "lookinnabook@email.com" ,"111-111-1111" );
insert into Publisher values("PB-10000", "Puffin studios", "publisher address", "puffin@email.com","111-111-1111");
insert into Book values("BK-10000", "Harry potter and the seven witches", "PB-10000", "Fantasy", "J.K.Bowling", 15.99, 12, "SC-10000");
insert into Book values("BK-10001", "Harry potter new world", "PB-10000", "Fantasy", "J.K.Bowling", 20.00, 15, "SC-10000");
insert into Users values("US-10000", "BA-10000", "Edward", "edward@email.com", "10000", "edward address", "edward address");
insert into Users values("US-10001", "BA-10001", "Edward2", "edward2@email.com", "10000", "edward address", "edward address");
insert into Orders values("US-10000", "OR-10000", "TR-10000", "Billing address", "shipping address", 1 ,1999);
insert into Orders values("US-10000", "OR-10003", "TR-10003", "Billing address", "shipping address", 2 ,1999);
insert into Orders values("US-10000", "OR-10001", "TR-10001", "Billing address", "shipping address", 3 ,1999);
insert into Orders values("US-10000", "OR-10002", "TR-10002", "Billing address", "shipping address", 4 ,1999);
insert into Orders values("US-10001", "OR-10005", "TR-10004", "Billing address", "shipping address", 4 ,1999);
insert into Book_Orders values("US-10000","OR-10000","BK-10000", 40,2);
insert into Book_Orders values("US-10000","OR-10001","BK-10001", 30,2);
insert into Book_Orders values("US-10000","OR-10001","BK-10000", 60,2);
insert into Book_Orders values("US-10000","OR-10002","BK-10000", 70,2);
insert into Book_Orders values("US-10000","OR-10003","BK-10001", 30,2);
insert into Book_Orders values("US-10001","OR-10005","BK-10000", 100,2);
insert into Book_Bookstore values("BS-10000","BK-10000",10);
insert into Book_Bookstore values("BS-10000","BK-10001",10);
insert into Book_Basket values("BA-10000","BK-10000",10);
insert into Book_Basket values("BA-10000","BK-10001",3);
insert into Bank values("BN-10000","RF-10000","access bank","oniru","accessbank@email.com","111-111-1111");
insert into Publisher_Bank values ("PB-10000","BN-10000","RF-10000");
insert into Bookstore_Bank values ("BS-10000","BN-10000","RF-10000",100,12,2020);
create view sales_by_year(order_number,month,year,total_sales) as
select Orders.Order_Number,Month,Year,sum(Price)
from Orders join Book_Orders on Orders.Order_number = Book_Orders.Order_number
group by Orders.Order_Number,Orders.Month,Orders.Year