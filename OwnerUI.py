import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import data
#from main import Controller

WIDTH = 1200
HEIGHT = 1000


def showUI(window, controller):
    def print_text():
        controller.print_test()
        # this prints the content of the search entry box
        print(search_entry.get())

    """Search Inventory"""

    search_lbl = Label(window, text='Search')
    search_lbl.grid(column=0, row=1)

    search_entry = Entry(window, width=50)
    search_entry.grid(column=1, row=1)

    search_button = Button(window, text="Search").grid(column=2, row=1)

    """Search Results"""

    lb1 = Listbox(window, height=25, width=60)

    # grabs the ISBN and name  of all the bookstores from the sql database
    books = controller.get_bookstore_books()
    # inputs all the names at the end of listbox
    lb1.insert(END, *books)

    lb1.grid(column=0, row=2, columnspan=3, rowspan=2)

    """Altering Inventory """

    """Adding a book"""

    addnewBook = Button(window, text="Add New book")
    addnewBook.grid(column=0, row=4)

    title_entry = Entry(window, width=20)
    title_entry.grid(column=0, row=5)
    title_entry.insert(0, "Title")

    author_entry = Entry(window, width=20)
    author_entry.grid(column=0, row=6)
    author_entry.insert(0, "Author")

    genre_entry = Entry(window, width=20)
    genre_entry.grid(column=0, row=7)
    genre_entry.insert(0, "Genre")

    amount_entry = Entry(window, width=20)
    amount_entry.grid(column=0, row=8)
    amount_entry.insert(0, "Amount")

    publisher_entry = Entry(window, width=20)
    publisher_entry.grid(column=0, row=9)
    publisher_entry.insert(0, "Publisher")

    percent_entry = Entry(window, width=20)
    percent_entry.grid(column=0, row=10)
    percent_entry.insert(0, "Publisher's Percent")

    code_entry = Entry(window, width=20)
    code_entry.grid(column=0, row=11)
    code_entry.insert(0, "Series Code")

    addBook = Button(window, text="Add book")
    addBook.grid(column=1, row=4)

    add_entry = Entry(window, width=20)
    add_entry.grid(column=1, row=5)
    add_entry.insert(0, "ISBN")

    add_entry2 = Entry(window, width=20)
    add_entry2.grid(column=1, row=6)
    add_entry2.insert(0, "Amount")

    removeBook = Button(window, text="Remove book")
    removeBook.grid(column=2, row=4)

    rem_entry = Entry(window, width=19)
    rem_entry.grid(column=2, row=5)
    rem_entry.insert(0, "Amount")

    increase = Button(window, text="Increase")
    increase.grid(column=3, row=4)

    inc_entry = Entry(window, width=20)
    inc_entry.grid(column=3, row=5)
    inc_entry.insert(0, "ISBN")

    inc_entry2 = Entry(window, width=20)
    inc_entry2.grid(column=3, row=6)
    inc_entry2.insert(0, "Amount")

    """ Generate Report"""
    report = Label(window, text="Request Report:")
    report.grid(column=3, row=0)

    from_lbl = Label(window, text="From: ")
    from_lbl.grid(column=3, row=1)

    month_fr = Label(window, text="Month: ")
    month_fr.grid(column=3, row=2)

    mo_fr_entry = Entry(window, width=20)
    mo_fr_entry.grid(column=4, row=2)

    year_fr = Label(window, text="Year: ")
    year_fr.grid(column=3, row=3)

    yr_fr_entry = Entry(window, width=20)
    yr_fr_entry.grid(column=4, row=3)

    month_to = Label(window, text="Month: ")
    month_to.grid(column=5, row=2)

    mo_to_entry = Entry(window, width=20)
    mo_to_entry.grid(column=6, row=2)

    year_to = Label(window, text="Year: ")
    year_to.grid(column=5, row=3)

    yr_to_entry = Entry(window, width=20)
    yr_to_entry.grid(column=6, row=3)
    #yr_to_entry.insert("End Year")

    rep_type = Label(window, text="Report type: ")
    rep_type.grid(column=4, row=0)
    reporttype_entry = ttk.Combobox(
        window, values=["Sales"])
    reporttype_entry.grid(column=5, row=0)

    report_btn = Button(window, text="Generate")
    report_btn.grid(column=7, row=3)

    """Log out """
    logout = Button(window, text="   Logout   ")
    logout.grid(column=6, row=0)

    """Order transfer history """

    transfer_lbl = Label(window, text="Bank Transfer History")
    transfer_lbl.grid(column=4, row=4)

    transfer = Listbox(window, height=10, width=60)
    banktransfers = controller.get_bank_transfers()
    transfer.insert(END, *banktransfers)
    transfer.grid(column=4, row=5, columnspan=3)

    """WINDOW INIT."""

    window.title("OWNER ACCOUNT PAGE")
    window.geometry(f"{WIDTH}x{HEIGHT}+10+10")
    window.mainloop()
