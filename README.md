# COMP3005Project

This READMe is included within the repository for the Fall 2021 COMP 3005 Bookstore Project (Edward Akapo 101095403 &amp; Sarah Abdallah 101119716)

Please note: The created user interface operate as intended when the display resolution
is set to 1920 x 1080 and the sale is 100%

The deliverables for this project include both SQL (.sql) files and Python (.py) files
This application was developped within MySQL (in SQL) and VSCode (in Python)

1. Navigate to data.py and include your own password to access the connector to the database
2. Run the DDL (in DDL.sql) within MySQL to create the bookstore database
3. Use the relationsInsert.sql to insert "testing data" into the bookstore database (in MySQL)
4. Run in main.py
5. The first screen that appears will be the login screen for users and owners of the bookstore
   IF acting as an owner, select the sign in button
   IF acting as a userr, sign up with log-in information and then use this log-in information to sign in (email and password)
6. When finished with session, logout using the log-out button

Instruction on formatting of datatbase:

Unique iD's fromat examples

BasketId - "BA-10000"

Bookstore id - "BS-10000"

Phone number - "111-111-1111"

email - "lookinnabook@email.com"

Publisher ID - "PB-10000", only one publisher id added as of now so this is the id you need to use for adding more books

ISBN - "BK-10000"

User id - "US-10000"

Order number -  "OR-10000"

Tracking number - "TR-10000"


The dummy data inserted is not to replicate a proper simulation, thus if you run some functionality with some dummy data ID's it may give errors. For example things are inserted into book_orders but not inserted in other places thus tracking doesnt work for that dummy data.
Thus to test full simulation it is better to add new data via the GUI. you can use the inserted books also those are fine.


Format of GUI results

Search results are formatted as : (ISBN, book title, author , genre, price, amount left in inventory, Publisher id)
Basket results are formatted as: (ISBN, publisher id, book title , amount in basket, price , genre, author)
order history results are formatted as :(ID, Order number, tracking id, book title, amount , price , address month year)


ps. note that the code is functional, the book inventory amount increases and reduces with user actions, order history updates itself after every puchase, bank transfers update aswell...
