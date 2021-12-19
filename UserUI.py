import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import data
from main import Controller

WIDTH = 2000
HEIGHT = 700


def showUI(window, controller: Controller):
    def print_text():
        controller.print_test()
        # this prints the content of the search entry box
        print(search_entry.get())

    """Search Books"""

    search_lbl = Label(window, text='Search')
    search_lbl.grid(column=0, row=0)

    search_entry = Entry(window, width=50)
    search_entry.grid(column=1, row=0)

    search_button = Button(window, text="Search").grid(column=2, row=0)

    """Search Results"""

    lb1 = Listbox(window, height=25, width=60)

    # grabs the names of all the bookstores from the sql database
    names = controller.get_bookstore_names()
    # inputs all the names at the end of listbox
    lb1.insert(END, *names)

    lb1.grid(column=0, row=2, columnspan=2)

    """Order History Display"""

    #order_lbl = Label(window, text='Order history')
    #order_lbl.grid(column=0, row=4)

    order_lbl = Label(window, text='Order history').grid(column=0, row=3)

    order_lbx = Listbox(window, width=80, height=5)
    order_lbx.grid(column=0, row=4, columnspan=4)

    """Display Basket= Add items, remove items, buy items"""

    basket_lbl = Label(window, text='Basket').grid(column=3, row=2)

    basket_lbx = Listbox(window, width=80, height=20)
    basket_lbx.grid(column=4, row=2, columnspan=2)

    # amountadd_label = Label(window, text="Amount".grid(column=4, row=0))
    # amountadd_entry = Entry(window, width=10).grid(column=5, row=0)

    # amountrm_label = Label(window, text="Amount").grid(column=4, row=1)
    # amountrm_entry = Entry(window, width=10).grid(column=5, row=1)

    add_btn = Button(window, text='Add to basket')
    add_btn.grid(column=5, row=0)
    add_entry = Entry(window, width=50).grid(column=4, row=0)

    remove_btn = Button(window, text='Remove from basket', command=print_text)
    remove_btn.grid(column=5, row=1)

    amount_entry = ttk.Combobox(
        window, values=[str(i) for i in range(1, 10)]).grid(column=4, row=1)

    add_label = Label(window, text="ISBN :").grid(column=3, row=0)
    amount_label = Label(window, text="Amount :").grid(column=3, row=1)

    filler1 = Label(window, text="         "). grid(column=3, row=4)

    buy_btn = Button(window, text='    Buy   ')
    buy_btn.grid(column=5, row=4)

    search_label = Label(
        window, text="Search by Tracking Number: "). grid(column=0, row=5)
    search_entry = Entry(window, width=50).grid(column=1, row=5)
    search_button = Button(window, text="Track").grid(column=2, row=5)

    """WINDOW INIT."""

    window.title("USER ACCOUNT PAGE")
    window.geometry(f"{WIDTH}x{HEIGHT}+10+10")
    window.mainloop()
