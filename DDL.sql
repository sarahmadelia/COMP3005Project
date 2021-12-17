CREATE DATABASE bookstore; 
USE bookstore; 
create table Users 
(ID			         int, 
Basket_ID   	 	 int,
Username			 varchar(20),
Email			     varchar(30),
User_Password		 varchar(30),
Billing_Address      varchar(40),
Shipping_Address     varchar(40), 
primary key	(ID), 
foreign key (Basket_ID) references Checkout_Basket
); 

create table Orders 
(ID 	         int, 
Order_Number     int, 
Tracking_Number  int, 
Billing_Address  varchar(40), 
Shipping_Address varchar(40), 
Order_Month            int,
Order_Year             int,
primary key (ID, Order_Number), 
foreign key (ID) references Users
); 

create table Checkout_Basket
(Basket_ID		int,
primary key (Basket_ID)
); 

create table Book_Orders
(ID 	      int, 
 Order_Number int, 
 ISBN         int, 
 Amount       int, 
 primary key (ID, Order_Number, ISBN),
 foreign key(ID) references Users, 
 foreign key(Order_Number) references Orders, 
 foreign key(ISBN) references Book 
 ); 

 
 create table Book_Bookstore
 (ID     int, 
 ISBN    int, 
 Amount  int, 
 primary key (ID, ISBN), 
 foreign key (ID) references BookStore on delete cascade,  
 foreign key(ISBN) references Book on delete cascade
 ); 
 
 
 create table Book_Basket 
 (Basket_ID   int, 
 ISBN  int, 
 Amount int, 
 primary key (Basket_ID, ISBN), 
 foreign key(Basket_ID) references Checkout_Basket, 
 foreign key(ISBN) references Book on delete cascade 
 ); 
 
 create table Book 
 (ISBN  int, 
 Title  varchar(40), 
 Publisher_ID   int, 
 Genre     varchar(20), 
 Author_Name  varchar(30),
 Selling_Price  numeric(4,2), 
 Publisher_Percentage int, 
 Series_Code int, 
 primary key (ISBN), 
 foreign key (Publisher_ID) references Publisher
 ); 
 
 create table BookStore 
 (ID         int, 
 Store_Name  varchar(20), 
 Address     varchar(40), 
 Email       varchar(30), 
 Number      varchar(20), 
 primary key (ID) 
 ); 
 
 
 create table Publisher 
 (Publisher_ID  int, 
 Publisher_Name varchar(30), 
 Address   varchar(40), 
 Email     varchar(30), 
 Number   varchar(20), 
 primary key (Publisher_ID) 
 ); 
 
 create table BankTransfers 
 (ID   int, 
 Publisher_ID   int, 
 Amount    int, 
 primary key (ID, Publisher_ID), 
 foreign key(ID) references BookStore, 
 foreign key(Publisher_ID) references Publisher
 ); 
 
 
 
 
 
 
 
 


	







