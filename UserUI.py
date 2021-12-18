import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import data
from main import Controller

WIDTH = 1200
HEIGHT = 700


def showUI(window, controller: Controller):
    def print_text():
        controller.print_test()
        # this prints the content of the search entry box
        print(search_entry.get())

    search_lbl = Label(window, text='Search')
    search_lbl.grid(column=0, row=1)

    search_entry = Entry(window, width=50)
    search_entry.grid(column=1, row=1)

    # names = ["alex", "bob", "carl", "dave", "ed", "frank", "george", "harry", "ian", "james", "kate", "lisa",
    #          "mike", "nancy", "oliver", "paul", "quinn", "richard", "sarah", "tim", "will", "xavier", "yvonne", "zach"]

    lb1 = Listbox(window, height=25, width=60)
    names = controller.get_book_names()
    lb1.insert(END, *names)
    lb1.grid(column=0, row=2, columnspan=2)

    order_lbl = Label(window, text='Order history')
    order_lbl.grid(column=0, row=3)

    order_lbx = Listbox(window, width=60, height=10)
    order_lbx.grid(column=1, row=4, columnspan=2)

    basket_lbl = Label(window, text='Basket')
    basket_lbl.grid(column=3, row=1)

    basket_lbx = Listbox(window, width=60, height=20)
    basket_lbx.grid(column=3, row=2, columnspan=2)

    add_btn = Button(window, text='Add to basket')
    add_btn.grid(column=3, row=3)

    remove_btn = Button(window, text='Remove', command=print_text)
    remove_btn.grid(column=4, row=3)

    buy_btn = Button(window, text='Buy')
    buy_btn.grid(column=5, row=3)

    window.title("LOGIN")
    window.geometry(f"{WIDTH}x{HEIGHT}+10+10")
    window.mainloop()


# showUI(Tk())
