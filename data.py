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
def getUserBasket(id):
    try:
        mycursor.execute("select * from Book_Basket where Basket_ID = '%s'" % id)
        basketInfo = mycursor.fetchall()
        return basketInfo
    except Exception as e:
        print(e)

def displayUserBasket(id):
    basketInfo = getUserBasket(id)
    format = []
    for x in basketInfo:
        bookInfo = getBookInfo(x[1])
        print(bookInfo)
        print("---------")
        format.append((bookInfo[0],x[2]))
    print(len(basketInfo))
    print(format)


def calculateTotalPrice(x1,x2):
    f1 = float(x1)
    f2 = float(x2)
    return round(f1*f2, 2)

def getBookInfo(id):
    try:
        mycursor.execute("select * from Book where ISBN = '%s'" % id)
        bookInfo = mycursor.fetchall()
        return bookInfo
    except Exception as e:
        print(e)
        
#format information for sending
def getUserOrderHistory(id):
    try:
        mycursor.execute("select * from Orders where ID = '%s'" % id)
        orderInfo = mycursor.fetchall()
        return orderInfo
    except Exception as e:
        print(e)

# print("Test for displaying user basket and user order history on login")
# print("basket:")
# #print(displayUserBasket("BA-10000"))
# print("orders:")
# print(getUserOrderHistory("US-10000"))

#
#
#------------searching and adding to basket

def getInfoByTitle(title):
    try:
        mycursor.execute("select * from Book where Title = '%s'" % title)
        book = mycursor.fetchall()
        return book
    except Exception as e:
        print(e)

#make this search bookstore for book, if it exists display the info and amount
def searchForBook(title):
    bookInfo = getInfoByTitle(title)
    format = []
    for x in bookInfo:
        format.append((x, findAmountInCollection(x[0])))
    print(format)

def findAmountInCollection(isbn):
    try:
        mycursor.execute("select Amount from Book_BookStore where ISBN = '%s' " %isbn)
        amount = mycursor.fetchall()
        return amount[0]
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
# print("Test for displaying user basket and user order history on login")
# print("basket:")
# print(displayUserBasket("BA-10000"))
# print("orders:")
# print(getUserOrderHistory("US-10000"))
#addToBasket("BA-10000","BK-10000","10")
#removeFromBasket("BA-10000","BK-10000")

#searchForBook("Harry potter new world")
#
#---------- buying books

#checks the Book collection if it has the amount of books we need, else reply error

def buyBooks(id, basketID, sa,ba):
    print("buying..............")
    #create new order info
    today = datetime.today()
    month = today.month
    year = today.year
    newOrderId = generateRandID("OR")
    newTrackingInfo = generateRandID("TR")
    addNewOrder(id,newOrderId,newTrackingInfo,ba,sa,month,year)
    basket = getUserBasket(basketID)
    Removed = []
    for x in basket:
        #check if bookstore has correct amount
        print("book id is: ",x[1],"amount is:", x[2])
        if(checkCollection(x[1],x[2])):
            #remove amount from bookstore 
            reduceBookStoreAmount(x[1],x[2])
            #add to book_orders
            addNewBook_Order(id,newOrderId,x[1],x[2])
            #create new reference number
            #add to publisher_bank and bookstore_bank
            ref = generateRandID("RF")
            bookInfo = getBookInfo(x[1])
            storeId = "BS-10000"
            bankId = "BN-10000"
            #price*amount*percentage
            amount = (x[2] * bookInfo[0][5] * bookInfo[0][6])/100
            print("amount is :", amount)
            addBankTransfer(ref,month,year,bookInfo[0][2],bankId,storeId,amount)
            Removed.append(x)
    for x in Removed:
        removeFromBasket(x[0],x[1])
    print("buying operations complete")
        


   
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
        mycursor.execute("insert into BankTransfers values ('%s', '%s', '%s' ,%d ,%d ,%d) ;" % (storeId,bankId,referenceNo,amount,month,year))
        mydb.commit()
        print("added tuple to bank transfer")
    except Exception as e:
        print(e) 
    return  0    

def checkCollection(isbn,amount):
    num = findAmountInCollection(isbn)
    if amount <= num[0]:
        return 1
    else:
        return 0

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


def addNewBook_Order(id, oId,isbn,amount):
    try:
        mycursor.execute("insert into Book_Orders values('%s','%s','%s',%d);" % (id,oId,isbn,amount))
        mydb.commit()
        print("inserted new book order into book_order")
    except Exception as e:
        print(e)    
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
buyBooks("US-10000","BA-10000","bill","ship")
#print(getBankID())