import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import data
from main import Controller

WIDTH = 2000
HEIGHT = 1500


def showUI(window, controller: Controller):

    def user_search():
        result = controller.user_Search(search1_entry.get())
        #clear box
        lb1.delete(0,END)
        lb1.insert(END,*result)

    def user_logout():
            controller.logout()
    def user_addBasket():
        controller.userAddBasket(add_entry.get(),
                                amount_entry.get())
        basket_lbx.delete(0,END)
        basket = controller.fillBasket()
        basket_lbx.insert(END, *basket)
        

    def user_removeBasket():
        controller.userRemoveBasket(add_entry.get())
        basket_lbx.delete(0,END)
        basket = controller.fillBasket()
        basket_lbx.insert(END, *basket)
    
    def user_buy():
        controller.userBuy(ship.get(),
                            bill.get())
        lb1.delete(0,END)                    
        intialList = controller.showInventory()
        lb1.insert(END, *intialList)

        order_lbx.delete(0,END)
        history = controller.fillOrderHistory()
        order_lbx.insert(END, *history)
        
        basket_lbx.delete(0,END)
        basket = controller.fillBasket()
        basket_lbx.insert(END, *basket)
    def track():
        results = controller.track(track_entry.get())
        trackstatus.delete(0,END)
        trackstatus.insert(END,*results)
    
    """Search Books"""

    welcome_lbl = Label(window, text="Welcome User    :"+controller.activeUser[2])
    welcome_lbl.grid(column=0, row=0)

    search1_entry = Entry(window, width=50)
    search1_entry.grid(column=1, row=0)

    track_button = Button(window, text="Search", command= user_search)
    track_button.grid(column=2, row=0)

    """Search Results"""

    lb1 = Listbox(window, height=25, width=150)

    # grabs the names of all the bookstores from the sql database
    intialList = controller.showInventory()
    # inputs all the names at the end of listbox
    lb1.insert(END, *intialList)

    lb1.grid(column=0, row=2, columnspan=2)

    """Order History Display"""

    order_lbl = Label(window, text='Order history')
    order_lbl.grid(column=0, row=3)

    order_lbx = Listbox(window, width=150, height=20)
    order_lbx.grid(column=0, row=4, columnspan=4)
    history = controller.fillOrderHistory()
    order_lbx.insert(END, *history)

    #shipping and billing
    
    ship = Entry(window, width=50)
    ship.grid(column=5, row=4)
    ship.insert(0,"enter shipping address")

    bill = Entry(window, width=50)
    bill.grid(column=5, row=5)
    bill.insert(0,"enter billing address")

    """Log out """
    logout = Button(window, text="   Logout   ", command=user_logout)
    logout.grid(column=6, row=0,)
    """Display Basket= Add items, remove items, buy items"""

    basket_lbl = Label(window, text='Basket')
    basket_lbl.grid(column=3, row=2)


    basket_lbx = Listbox(window, width=110, height=20)
    basket_lbx.grid(column=4, row=2, columnspan=2)

    basket = controller.fillBasket()
    basket_lbx.insert(END, *basket)

    add_btn = Button(window, text='Add to basket', command=user_addBasket)
    add_btn.grid(column=5, row=0)
    add_entry = Entry(window, width=50)
    add_entry.grid(column=4, row=0)

    remove_btn = Button(window, text='Remove from basket', command=user_removeBasket)
    remove_btn.grid(column=5, row=1)

    amount_entry = ttk.Combobox(
        window, values=[str(i) for i in range(1, 10)])
    amount_entry.grid(column=4, row=1)

    add_label = Label(window, text="ISBN :")
    add_label.grid(column=3, row=0)
    amount_label = Label(window, text="Amount :")
    amount_label.grid(column=3, row=1)

    filler1 = Label(window, text= "   ")
    filler1. grid(column=3, row=4)

    buy_btn = Button(window, text='    Buy   ', command=user_buy)
    buy_btn.grid(column=5, row=3)

    #
    #Tracking
    # 
    track_label = Label(
        window, text="Search by Tracking Number: ")
    track_label. grid(column=0, row=5)
    track_entry = Entry(window, width=50)
    track_entry.grid(column=1, row=5)
    track_button = Button(window, text="Track",command=track)
    track_button.grid(column=2, row=5)



    trackstatus= Listbox(window, width= 70, height =50)
    trackstatus.grid(column=1, row=6, columnspan= 3) 


    """WINDOW INIT."""

    window.title("USER ACCOUNT PAGE")
    window.geometry(f"{WIDTH}x{HEIGHT}+10+10")
    window.mainloop()
