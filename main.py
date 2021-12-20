""" 
Acts as the controller 
main.py creates the connector and initializes a window for the user interfaces 
to appear on and sets the initial user interface 
"""
import data
import InitialUI
from tkinter import *
import UserUI
import OwnerUI


class Controller:

    def __init__(self) -> None:
        """Initializes a new window and sets it to the initial log-in screen 
        """
        self.connector = data.getConnector()
        self.activeUser = None
        self.isActive = None
        self.userName = None
        self.window = Tk()
        InitialUI.showUI(self.window, self)

    def print_test(self):
        self.clear_frame()

    def show_login(self):
        """Initializes the Initial UI page (login)
        """
        self.clear_frame()
        InitialUI.showUI(self.window, self)

    def show_User(self):
        """Initializes the User UI page 
        """
        self.clear_frame()
        UserUI.showUI(self.window, self)

    def show_Owner(self):
        """Initializes the Owner UI page 
        """
        self.clear_frame()
        OwnerUI.showUI(self.window, self)

    def clear_frame(self):
        """Clears the window and sets a new one
        """
        new_window = Tk()
        self.window.destroy()
        self.window = new_window

    def user_signUp(self, name,password,email,sa,ba):
        # creates a new user and signs them in
        print("user info:",name,password,email,sa,ba)
        result = data.signUpFunc(self.connector,name,email,password,ba,sa)
        if result == 0:
            print("Error!! that user alredy exists")
        else:
            self.user_login(email,password)
    
    def logout(self):
        self.show_login()
     
    def user_login(self, email,password):
        # takes email and passwords and attempts to login
        result = data.signInFunc(self.connector,email,password)
        if result:
            self.isActive = 1
            self.activeUser = result
            self.userName = result[2]
            print("SUCCESS!!! user logged in:",self.userName)
            print(self.activeUser)
            self.show_User()
        else:
            print("Error!!! with login")
    def fillBasket(self):
        #takes basket id and gets user basket information
        result = data.displayUserBasket(self.connector,self.activeUser[1])
        if result:
            print("User basket")
            print(result)
            return result
        else:
            print("Basket EMPTY!!")
            return []
    def fillOrderHistory(self):
        #takes user id and fils in all their orders
        result = data.getUserOrderHistory(self.connector,self.activeUser[0])
        if result:
            print("User history")
            print(result)
            return result
        else:
            print("History EMPTY!!")
            return[]

    def showInventory(self):
        #display books from the inventory
        result = data.updateInventory(self.connector)
        if result:
            print("Displaying store inventory")
            print(result)
            return result
        else:
            print("Inventory EMPTY!!!")
            return []

    def user_Search(self,title):
        #gets the search results and display
        title = title + "%"
        print("title is:",title)
        result = data.searchForBook(self.connector,title)
        if result:
            print("Displaying search results")
            print(result)
            return result
        else:
            print("Invalid Search!!!")
            return []
    
    def userAddBasket(self,isbn,amount):
        #adds the specified book into user basket
        result = data.addToBasket(self.connector,self.activeUser[1],isbn,amount)
        if result == 1:
            print("added")
        else:
            print("ERROR!! ISBN invalid in bookstore collection")
    def userRemoveBasket(self,isbn):
        #removes specified book from user basket
        result = data.removeFromBasket(self.connector,self.activeUser[1],isbn)
        if result == 1:
            print("Removed from basket")
        else:
            print("ERROR!! ISBN invalid in bookstore collection")
    def userBuy(self,sa,ba):
        if not sa or not ba:
            data.buyBooks(self.connector,self.activeUser[0], self.activeUser[1],self.activeUser[6],self.activeUser[5])
        else:
            data.buyBooks(self.connector,self.activeUser[0], self.activeUser[1],sa,ba)
    #def userTrack()
    def ownerSignIn(self):
        results = data.ownerLogin(self.connector)
        self.isActive = 1
        self.activeUser = results
        self.userName = results[2]
        self.show_Owner()
        print("Owner log in!!!!")

    def addBook(self,isbn,amount):
        data.addBook(self.connector,isbn,amount)
        print("Adding exisiting book")

    def addNewBook(self,title,pId,genre,author,price,percentage,seriesCode,amount):
        data.addNewBook(self.connector,title,pId,genre,author,price,percentage,seriesCode,amount)
        print("Adding new book")

    def removeBook(self, isbn):
        data.removeBook(self.connector, isbn)
        print("removing exisiting book")

    def increaseBook(self, isbn,amount):
        data.increaseAmount(self.connector, isbn,amount)
        print("Adding more to exisiting book")

    def getBankHistory(self):
        result = data.getTransactionHistory(self.connector)
        if result:
            print("Transactions gotten")
            return result
        else:
            print("Error with history")
            return[]

    def getReport(self,m1,m2,y1,y2):
        print("generating report")
        result = data.getSalesPerYear(self.connector,m1,m2,y1,y2)
        if result:
            format = ["Total sales made from "+str(m1)+" : "+str(y1)+" to "+str(m2)+" : "+str(y2)+"   =  $" + str(result)]
            print(format)
            return format
        else:
            return "invalid selection"

    def track(self,tID):
        location = "Location : Bookstore Warehouse"
        status = "Order Status : In Transit"
        result = data.track(self.connector,self.activeUser[0],tID)
        if result:
            print("info")
            print(result)
            format = []
            format.append(result[0])
            format.append([location,status])
            return format
        else:
            print("Error with history")
            return[]

        





def main():
    Controller()


if __name__ == "__main__":
    main()