from logging import NullHandler
import mysql.connector
import random
import string
from datetime import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tamilore",
    database="bookstore"
)

def generateRandID(str):
    letters = string.digits
    numbers = ( ''.join(random.choice(letters) for i in range(5)))
    return str + "-" + numbers


#
#
#
#--------------login page functionality

mycursor = mydb.cursor()
# print("Orders are:")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x[5],x[6])

def createNewBasket():
    basketID = generateRandID('BA')
    try:
        mycursor.execute("insert into Basket values ('%s')"%basketID)
        mydb.commit()
        print(mycursor.rowcount, "new baseket created")
        return basketID
    except Exception as e:
        print(e)

#sign up
#may want to include functions to make sure email & username are always unique
def signUpFunc(name,email,password,ba,sa):
    #check if they are a current user
    user = signInFunc(email,password)
    if user:
        print("ERROR!!! : User already exists")
        return user
    else:
        basketID = createNewBasket()
        userID = generateRandID('US')
        userInfo = (userID,basketID,name,email,password,ba,sa)
        print(userInfo)
        try:
            mycursor.execute("insert into Users values ('%s', '%s', '%s','%s', '%s', '%s', '%s') " % userInfo )
            mydb.commit()
            print(mycursor.rowcount, "new user created" , name)
            return userInfo
        except Exception as e:
            print(e)


#sign in
def signInFunc(email,password):
    try:
        query = ("select * from Users "
        "where email = ('%s') and User_Password = ('%s')")
        mycursor.execute(query%(email, password))
        userInfo = mycursor.fetchall()
        if not userInfo:
            print("ERROR!!! : no user with that info exists")
            return None
        else:
            print("User", userInfo[0][2]," has logged in")
            return userInfo[0]
    except Exception as e:
        print(e)

#owner login
def ownerLogin():
    try:
        mycursor.execute("select * from BookStore")
        ownerInfo = mycursor.fetchall()
        return ownerInfo[0]
    except Exception as e:
        print(e)

# signUpFunc("Edward","edward4@email.com","10000","edward address","edward address")
# print(ownerLogin())

#
#
#--------------------User Page Functionality

#at this point the front end knows the active user so it should be able to send User ID, Basket ID...

#format information for sending

#
#
#-------displaying info funcitons

def displayUserBasket(basketId):
    try:
        sql = ("select * "
                "from Book_Basket join Book on (Book_Basket.ISBN = Book.ISBN) "
                "where Book_Basket.Basket_ID = '%s'")
        mycursor.execute(sql % basketId)
        bookInfo = mycursor.fetchall()
        print("displaying user basket")
        return bookInfo
    except Exception as e:
        print(e)

        
#format information for sending
def getUserOrderHistory(id):
    sql = ("select * "
            "from Orders join Book_Orders on (Orders.ID = Book_Orders.ID  and Orders.Order_Number = Book_Orders.Order_Number) join Book on Book.ISBN = Book_Orders.ISBN "
            "where Orders.ID = '%s'")
    try:
        mycursor.execute(sql % id)
        orderInfo = mycursor.fetchall()
        print("displaying user order history")
        return orderInfo
    except Exception as e:
        print(e)


#
#
#------------searching and adding to basket

def searchForBook(title):
    try:
        sql = ("select * "
                "from Book join Book_Bookstore on (Book.ISBN = Book_Bookstore.ISBN) "
                "where Book.Title like '%s'")
        mycursor.execute(sql % title)
        book = mycursor.fetchall()
        print("displaying user book search")
        print(book)
        for x in book:
            print(x)
    except Exception as e:
        print(e)   

def checkBookInBasket(basketId,isbn):
    try:
        mycursor.execute("select * from Book_Basket where Basket_ID = '%s' and ISBN = '%s'" % (basketId,isbn))
        book = mycursor.fetchall()
        if book :
            return book
        else:
            return None
    except Exception as e:
        print(e)   


def addToBasket(basketId ,isbn, amount):
    #check if book is aready in basket
    book = checkBookInBasket(basketId,isbn)
    if book:
    #update amount
        try:
            mycursor.execute("Update Book_Basket set amount = amount + '%s' where Basket_ID = '%s' and ISBN = '%s'"% (amount,basketId,isbn))
            mydb.commit()
            print("increased amount")
        except Exception as e:
            print(e) 
    else:
    #add book to basket
        try:
            mycursor.execute("insert into Book_Basket values ('%s' ,'%s' ,'%s')"% (basketId,isbn,amount))
            mydb.commit()
            print(mycursor.rowcount, "new book added to basket created")
        except Exception as e:
            print(e)

def removeFromBasket(basketId, isbn):
        try:
            mycursor.execute("delete from Book_basket where Basket_ID = '%s' and ISBN = '%s' "% (basketId,isbn))
            mydb.commit()
            print("removed book from basket")
        except Exception as e:
            print(e)     

#
#---------- buying books

#checks the Book collection if it has the amount of books we need, else reply error
        
def getValidBooksFromBasket(basketId):
    try:
        

        sql = ("select Book_Basket.ISBN, Book.Publisher_ID,Book_Basket.Amount, Book.Selling_price, Book.Publisher_percentage "
                "from Book_Basket join Book_Bookstore on (Book_Basket.ISBN = Book_Bookstore.ISBN ) join Book on (Book.ISBN = Book_Bookstore.ISBN) "
                "where Book_Basket.Basket_ID = '%s' and Book_Basket.Amount <= Book_Bookstore.Amount")
        mycursor.execute(sql%basketId)
        results = mycursor.fetchall()
        for x in results:
            print(x)
        return results
    except Exception as e:
        print(e) 

def buyBooks(id,basketId,sa,ba):
    print("buying process starting....................")
    books = getValidBooksFromBasket(basketId)
    if books:
        today = datetime.today()
        month = today.month
        year = today.year
        newOrderId = generateRandID("OR")
        newTrackingInfo = generateRandID("TR")
        # add new order
        addNewOrder(id,newOrderId,newTrackingInfo,ba,sa,month,year)
        # add to book orders
        for x in books:
            ref = generateRandID("RF")
            storeId = "BS-10000"
            bankId = "BN-10000"
            pubAmount = (x[2] * x[3] * x[4])/100
            totalPrice = (x[2] * x[3]) - pubAmount
            reduceBookStoreAmount(x[0],x[2])
            addNewBook_Order(id,newOrderId,x[0],totalPrice,x[2])
            addBankTransfer(ref,month,year,x[1],bankId,storeId,pubAmount)
            removeFromBasket(basketId,x[0])
        print("buying complete")



def addBankTransfer(referenceNo,month,year,publisherId,bankId,storeId,amount):
    #add ref to bank
    addToBank(bankId,referenceNo)
    #add to Publisher bank
    addToPubBank(bankId,publisherId,referenceNo)
    #add to Bookstore bank
    addToBookBank(storeId,bankId,referenceNo,amount,month,year)


def addToBank(bankId,referenceNo):
    address = "oniru"
    name ="access bank"
    email = "accessbank@email.com"
    number = "111-111-1111"

    try:
        mycursor.execute("insert into Bank values ('%s', '%s','%s', '%s','%s', '%s') ;" % (bankId,referenceNo,name,address,email,number))
        mydb.commit()
        print("added tuple to bank")
    except Exception as e:
        print(e) 
    return  0

def addToPubBank(bankId,publisherId,referenceNo):
    try:
        mycursor.execute("insert into Publisher_Bank values ('%s', '%s' ,'%s') ;" % (publisherId,bankId,referenceNo))
        mydb.commit()
        print("added tuple to publisher bank")
    except Exception as e:
        print(e) 
    return  0

def addToBookBank(storeId,bankId,referenceNo,amount,month,year):
    try:
        mycursor.execute("insert into Bookstore_Bank values ('%s', '%s', '%s' ,%d ,%d ,%d) ;" % (storeId,bankId,referenceNo,amount,month,year))
        mydb.commit()
        print("added tuple to bank transfer")
    except Exception as e:
        print(e) 
    return  0    


def reduceBookStoreAmount(isbn,amount):
    try:
        mycursor.execute("Update Book_BookStore set amount = amount - '%s' where ISBN = '%s'"% (amount,isbn))
        mydb.commit()
        print("reduced amount of book from bookstore")
    except Exception as e:
        print(e)     

def addNewOrder(id,oNum,tNum,ba,sa,month,year):
    #get month and year 
    try:
        mycursor.execute("insert into Orders values ('%s','%s','%s','%s','%s',%d,%d)" % (id,oNum,tNum,ba,sa,month,year))
        mydb.commit()
        print(mycursor.rowcount, "new order created")
    except Exception as e:
        print(e)  


def addNewBook_Order(id, oId,isbn,price,amount):
    try:
        mycursor.execute("insert into Book_Orders values('%s','%s','%s',%d,%d);" % (id,oId,isbn,price,amount))
        mydb.commit()
        print("inserted new book order into book_order")
    except Exception as e:
        print(e)    



#
#
#-----------Owner page functions
def createView():
    view = ("create view sales_by_year(order_number,month,year,total_sales) as "
            "select Orders.Order_Number,Month,Year,sum(Price) "
            "from Orders join Book_Orders on Orders.Order_number = Book_Orders.Order_number "
            "group by Orders.Order_Number,Orders.Month,Orders.Year")
    try:
        mycursor.execute(view)
        mydb.commit()
        print("Created new view")
    except Exception as e:
        print(e)

def createTrigger():
    trigger = ("delimiter $$"
                "create trigger fill_books "
                "before update on Book_Bookstore"
                "For each row"
                "begin "
	            "if new.amount < 10 Then"
		        "set new.amount = new.amount +  (select sum(amount) from Book_Orders join Orders on Orders.Order_number = Book_Orders.Order_number where month = 12);"
	            "end if;"
                "end;$$"
                "delimiter ;")
    try:
        mycursor.execute(trigger)
        mydb.commit()
        print("Created new trigger")
    except Exception as e:
        print(e)  

def getSalesPerYear(m1,m2,y1,y2):
    sum = ("select sum(total_sales) "
        "from sales_by_year "
        "where month >= %d and year >= %d and month <= %d and year <= %d")
    try:
        mycursor.execute(sum % (m1,m2,y1,y2))
        val = mycursor.fetchall()
        return val[0][0]
    except Exception as e:
        print(e)    
  

def updateInventory():
    try:
        sql = ("select * "
                "from Book_Bookstore join Book on (Book_Bookstore.ISBN = Book.ISBN)")
        mycursor.execute(sql)
        bookInfo = mycursor.fetchall()
        return bookInfo
    except Exception as e:
        print(e)

#when user adds a totally new book
def addNewBook(title,pId,genre,author,price,percentage,seriesCode,amount):
    #insert into Book
    isbn = generateRandID("BK")
    try:
        mycursor.execute("insert into Book values ('%s','%s','%s','%s','%s', %d,%d,'%s')"%(isbn,title,pId,genre,author,price,percentage,seriesCode))
        mydb.commit()
    except Exception as e:
        print(e) 

    #insert into Book_Bookstore
    id = "BS-10000"
    try:
        mycursor.execute("insert into Book_Bookstore values ('%s','%s',%d)"%(id,isbn,amount))
        mydb.commit()
    except Exception as e:
        print(e)     

#when user adds book that already exists
def addBook(isbn,amount):
    id = "BS-10000"
    try:
        mycursor.execute("insert into Book_Bookstore values ('%s','%s',%d)"%(id,isbn,amount))
        mydb.commit()
    except Exception as e:
        print(e)     

def removeBook(isbn):
    try:
        mycursor.execute("delete from Book_Bookstore where ISBN = '%s'" % isbn)
        mydb.commit()
    except Exception as e:
        print(e)

def increaseAmount(isbn,amount):
    try:
        mycursor.execute("Update Book_Bookstore set amount = amount + %d where ISBN = '%s'" % (amount,isbn))
        mydb.commit()
    except Exception as e:
        print(e)

#def getTransferHistory()

#buyBook("BK-10000","BA-10000","10","23")
#reduceBookStoreAmount("BK-10000","10")
# def moveToOrders():

# def addToBookOrder():

# def 
#addNewOrder("US-10000", "OR-10006", "TR-10001", "Billing address", "shipping address")
#addNewBook_Order("US-10000","OR-10003","BK-10001", 10)
#print(getBookStoreID())
#bookInfo = getBookInfo("BK-10001")
#print(bookInfo[0][5] * bookInfo[0][6])
#print(getUserBasket("BA-10000"))
#buyBooks("US-10000","BA-10000","bill","ship")
#print(getBankID())
#addNewBook()
#removeBook("BK-10000")
# print(updateInventory())
#addBook("BK-10000",10)
#print(searchForBook("Harry potter and the seven witches"))
#createView()
#print(getSalesPerYear(1,12,1999,2021))
# print("Test for displaying user basket and user order history on login")

# print("basket:")
# print(displayUserBasket("BA-10000"))
# print("orders:")
# print(getUserOrderHistory("US-10000"))
# addToBasket("BA-10000","BK-10000","10")
#getValidBooksFromBasket("BA-10000")
# searchForBook("Harry %")
# buyBooks("US-10000","BA-10000","bill","ship")
# print(updateInventory())
# createView()
# print(getSalesPerYear(1,12,1999,2021))