delete from Basket;
delete from BookStore;
delete from Publisher;
delete from Book;
delete from Users;
delete from Orders;
delete from Book_Orders;
delete from Book_Bookstore;
delete from Book_Basket;
delete from BankTransfers;
insert into Basket values ("BA-10000");
insert into BookStore values("BS-10000","Look inna book", "bookstore address", "lookinnabook@email.com" ,"111-111-1111" );
insert into Publisher values("PB-10000", "Puffin studios", "publisher address", "puffin@email.com","111-111-1111");
insert into Book values("BK-10000", "Harry potter and the seven witches", "PB-10000", "Fantasy", "J.K.Bowling", 15.99, 12, "SC-10000");
insert int Users values("US-10000", "BA-10000")