import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import data

WIDTH = 2000
HEIGHT = 1500


def showUI(window, controller):
    def user_search():
        result = controller.user_Search(search_entry.get())
        #clear box
        lb1.delete(0,END)
        lb1.insert(END,*result)
    def resetInfo():
        lb1.delete(0,END)
        books = controller.showInventory()
        lb1.insert(END, *books)
        
        transfer.delete(0,END)
        banktransfers = controller.getBankHistory()
        transfer.insert(END, *banktransfers)

    def logout():
            controller.logout()
    def addBook():
        controller.addBook(add_entry.get(),
                            int(add_entry2.get()))
        resetInfo()
    def removeBook():
        controller.removeBook(rem_entry.get())
        resetInfo()
    def addNewBook():
        controller.addNewBook(title_entry.get(),
                                publisher_entry.get(),
                                genre_entry.get(),
                                author_entry.get(),
                                int(price_entry.get()),
                                int(percent_entry.get()),
                                code_entry.get(),
                                int(amount_entry.get()))
        resetInfo()
    def increaseBook():
        controller.increaseBook(inc_entry.get(),
                                int(inc_entry2.get()))
        resetInfo()
    def report():
        print("..............................................")
        result = controller.getReport(int(mo_fr_entry.get()),
                                    int(mo_to_entry.get()),
                                    int(yr_fr_entry.get()),
                                    int(yr_to_entry.get()))
        gen_report.delete(0,END)
        gen_report.insert(END,*result)
    
    """Search Inventory"""

    search_lbl = Label(window, text='WELCOME TO ADMIN PAGE')
    search_lbl.grid(column=0, row=1)

    search_entry = Entry(window, width=50)
    search_entry.grid(column=1, row=1)

    search_button = Button(window, text="Search", command=user_search)
    search_button.grid(column=2, row=1)

    """Search Results"""

    lb1 = Listbox(window, height=25, width=110)

    # grabs the ISBN and name  of all the bookstores from the sql database
    books = controller.showInventory()
    # inputs all the names at the end of listbox
    lb1.insert(END, *books)

    lb1.grid(column=0, row=2, columnspan=3, rowspan=2)

    """Altering Inventory """

    """Adding a book"""

    addnewBook = Button(window, text="Add New book",command=addNewBook)
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

    price_entry = Entry(window, width=20)
    price_entry.grid(column=0, row=8)
    price_entry.insert(0, "Price")

    publisher_entry = Entry(window, width=20)
    publisher_entry.grid(column=0, row=9)
    publisher_entry.insert(0, "Publisher")

    percent_entry = Entry(window, width=20)
    percent_entry.grid(column=0, row=10)
    percent_entry.insert(0, "Publisher's Percent")

    code_entry = Entry(window, width=20)
    code_entry.grid(column=0, row=11)
    code_entry.insert(0, "Series Code")

    amount_entry = Entry(window, width=20)
    amount_entry.grid(column=0, row=12)
    amount_entry.insert(0, "Amount")

    addBook_lbl = Button(window, text="Add book",command=addBook)
    addBook_lbl.grid(column=1, row=4)

    add_entry = Entry(window, width=20)
    add_entry.grid(column=1, row=5)
    add_entry.insert(0, "ISBN")

    add_entry2 = Entry(window, width=20)
    add_entry2.grid(column=1, row=6)
    add_entry2.insert(0, "Amount")

    removeBook_lbl = Button(window, text="Remove book",command=removeBook)
    removeBook_lbl.grid(column=2, row=4)

    rem_entry = Entry(window, width=19)
    rem_entry.grid(column=2, row=5)
    rem_entry.insert(0, "Amount")

    increase = Button(window, text="Increase",command=increaseBook)
    increase.grid(column=3, row=4)

    inc_entry = Entry(window, width=20)
    inc_entry.grid(column=3, row=5)
    inc_entry.insert(0, "ISBN")

    inc_entry2 = Entry(window, width=20)
    inc_entry2.grid(column=3, row=6)
    inc_entry2.insert(0, "Amount")

    """ Generate Report"""
    report_lbl = Label(window, text="Request Report:")
    report_lbl.grid(column=3, row=0)

    from_lbl = Label(window, text="From: ")
    from_lbl.grid(column=3, row=1)

    month_fr = Label(window, text="Month: ")
    month_fr.grid(column=3, row=2)

    mo_fr_entry = Entry(window, width=20)
    mo_fr_entry.grid(column=4, row=2)
    mo_fr_entry.insert(0,"start month")

    year_fr = Label(window, text="Year: ")
    year_fr.grid(column=3, row=3)

    yr_fr_entry = Entry(window, width=20)
    yr_fr_entry.grid(column=4, row=3)
    yr_fr_entry.insert(0,"start year")

    to_lbl = Label(window, text="To: ")
    to_lbl.grid(column=5, row=1)

    month_to = Label(window, text="Month: ")
    month_to.grid(column=5, row=2)

    mo_to_entry = Entry(window, width=20)
    mo_to_entry.grid(column=6, row=2)
    mo_to_entry.insert(0,"end month")

    year_to = Label(window, text="Year: ")
    year_to.grid(column=5, row=3)

    yr_to_entry = Entry(window, width=20)
    yr_to_entry.grid(column=6, row=3)
    yr_to_entry.insert(0,"end year")

    rep_type = Label(window, text="Report type: ")
    rep_type.grid(column=4, row=0)
    reporttype_entry = ttk.Combobox(
        window, values=["Sales"])
    reporttype_entry.grid(column=5, row=0)

    report_btn = Button(window, text="Generate", command=report)
    report_btn.grid(column=7, row=3)

    report_label= Label(window, text="Generated report")
    report_label.grid(column=7, row=4) 

    gen_report= Listbox(window, height =10, width = 60)
    gen_report.grid(column=7, row=5, columnspan= 3) 


    """Log out """
    logout = Button(window, text="   Logout   ",command=logout)
    logout.grid(column=6, row=0)

    """Order transfer history """

    transfer_lbl = Label(window, text="Bank Transfer History")
    transfer_lbl.grid(column=4, row=4)

    transfer = Listbox(window, height=10, width=60)
    banktransfers = controller.getBankHistory()
    transfer.insert(END, *banktransfers)
    transfer.grid(column=4, row=5, columnspan=3)

    """WINDOW INIT."""

    window.title("OWNER ACCOUNT PAGE")
    window.geometry(f"{WIDTH}x{HEIGHT}+10+10")
    window.mainloop()
