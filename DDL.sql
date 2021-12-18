DROP DATABASE bookstore;
CREATE DATABASE bookstore; 
USE bookstore; 

create table Checkout_Basket
(Basket_ID		varchar(8),
primary key (Basket_ID)
); 
 create table BookStore 
 (ID         varchar(8), 
 Store_Name  varchar(20), 
 Address     varchar(40), 
 Email       varchar(30), 
 Number      varchar(20), 
 primary key (ID) 
 ); 
 
 create table Publisher 
 (Publisher_ID  varchar(8), 
 Publisher_Name varchar(30), 
 Address   varchar(40), 
 Email     varchar(30), 
 Number   varchar(20), 
 primary key (Publisher_ID) 
 ); 
 
  create table Book 
 (ISBN  varchar(8), 
 Title  varchar(40), 
 Publisher_ID   varchar(8), 
 Genre     varchar(20), 
 Author_Name  varchar(30),
 Selling_Price  numeric(4,2), 
 Publisher_Percentage int, 
 Series_Code int, 
 primary key (ISBN), 
 foreign key (Publisher_ID) references Publisher(Publisher_ID)
 ); 
 
create table Users 
(ID			         varchar(8), 
Basket_ID   	 	 varchar(8),
Username			 varchar(20),
Email			     varchar(30),
User_Password		 varchar(30),
Billing_Address      varchar(40),
Shipping_Address     varchar(40), 
primary key	(ID), 
foreign key (Basket_ID) references Checkout_Basket(Basket_ID)
); 

create table Orders 
(ID 	         varchar(8), 
Order_Number     varchar(8), 
Tracking_Number  varchar(8), 
Billing_Address  varchar(40), 
Shipping_Address varchar(40), 
Month            numeric(2),
Year             numeric(4,0),
primary key (ID, Order_Number), 
foreign key (ID) references Users(ID)
); 


create table Book_Orders
(ID 	      varchar(8), 
 Order_Number varchar(8), 
 ISBN         varchar(8), 
 Amount       numeric(3), 
 primary key (ID, Order_Number, ISBN),
 foreign key(ID, Order_Number) references Orders(ID, Order_Number),
 foreign key(ISBN) references Book(ISBN)
 ); 

 
 create table Book_Bookstore
 (ID     varchar(8), 
 ISBN    varchar(8), 
 Amount  numeric(3), 
 primary key (ID, ISBN), 
 foreign key (ID) references BookStore(ID) on delete cascade,  
 foreign key(ISBN) references Book(ISBN) on delete cascade
 ); 
 
 
 create table Book_Basket 
 (Basket_ID   varchar(8), 
 ISBN  varchar(8), 
 Amount numeric(3), 
 primary key (Basket_ID, ISBN), 
 foreign key(Basket_ID) references Checkout_Basket(Basket_ID), 
 foreign key(ISBN) references Book(ISBN) on delete cascade 
 ); 
 
 
 create table BankTransfers 
 (ID   varchar(8), 
 Publisher_ID   varchar(8), 
 Amount    numeric(4,2), 
 primary key (ID, Publisher_ID), 
 foreign key(ID) references BookStore(ID), 
 foreign key(Publisher_ID) references Publisher(Publisher_ID)
 ); 
 
 
 
 
 
 
 
 


	







