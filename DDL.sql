DROP DATABASE bookstore;
CREATE DATABASE bookstore; 
USE bookstore; 

create table Basket
(Basket_ID		varchar(8),
primary key (Basket_ID)
); 
 create table BookStore 
 (ID         varchar(8), 
 Store_Name  varchar(20), 
 Address     varchar(40), 
 Email       varchar(30), 
 Number      varchar(12), 
 primary key (ID) 
 ); 
 
 create table Publisher 
 (Publisher_ID  varchar(8), 
 Publisher_Name varchar(30), 
 Address   varchar(40), 
 Email     varchar(30), 
 Number   varchar(12), 
 primary key (Publisher_ID) 
 ); 
 
  create table Book 
 (ISBN  varchar(8), 
 Title  varchar(40), 
 Publisher_ID   varchar(8), 
 Genre     varchar(20), 
 Author_Name  varchar(30),
 Selling_Price  numeric(4,2), 
 Publisher_Percentage numeric(2), 
 Series_Code varchar(8), 
 primary key (ISBN), 
 foreign key (Publisher_ID) references Publisher(Publisher_ID)
	on delete set null
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
foreign key (Basket_ID) references Basket(Basket_ID)
	on delete set null
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
	on delete cascade
); 


create table Book_Orders
(ID 	      varchar(8), 
 Order_Number varchar(8), 
 ISBN         varchar(8),
 Price		  numeric(6,2),
 Amount       numeric(3), 
 primary key (ID, Order_Number, ISBN),
 foreign key(ID, Order_Number) references Orders(ID, Order_Number) on delete cascade,
 foreign key(ISBN) references Book(ISBN) on delete no action
 ); 

 
 create table Book_Bookstore
 (ID     varchar(8), 
 ISBN    varchar(8), 
 Amount  numeric(4), 
 primary key (ID, ISBN), 
 foreign key (ID) references BookStore(ID) on delete cascade,  
 foreign key(ISBN) references Book(ISBN) on delete cascade
 ); 
 
 
 create table Book_Basket 
 (Basket_ID   varchar(8), 
 ISBN  varchar(8), 
 Amount numeric(3), 
 primary key (Basket_ID, ISBN), 
 foreign key(Basket_ID) references Basket(Basket_ID) on delete cascade, 
 foreign key(ISBN) references Book(ISBN) on delete cascade 
 ); 
 
 create table Bank
(ID         varchar(8),
Reference_no	varchar(8),
 Bank_Name  varchar(20), 
 Address     varchar(40), 
 Email       varchar(30), 
 Number      varchar(12), 
 primary key (ID, Reference_no)
 ); 
 
  create table Bookstore_Bank 
 (BookStore_ID   varchar(8), 
 Bank_ID   varchar(8),
 Reference_no	varchar(8),
 Amount    numeric(8,2),
 Month    numeric(2),
 Year       numeric(4,0),
 primary key (BookStore_ID, Bank_ID,Reference_no), 
 foreign key(BookStore_ID) references BookStore(ID) on delete cascade, 
 foreign key(Bank_ID, Reference_no) references Bank(ID, Reference_no)
 ); 
 
  create table Publisher_Bank
 (Publisher_ID   varchar(8),
 Bank_ID   varchar(8),
 Reference_no	varchar(8),
 primary key (Publisher_ID, Bank_ID, Reference_no), 
 foreign key(Publisher_ID) references Publisher(Publisher_ID) on delete cascade, 
 foreign key(Bank_ID, Reference_no) references Bank(ID, Reference_no)
 ); 
 
 
 
 
 
 


	







