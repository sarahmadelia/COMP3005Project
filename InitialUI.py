import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

WIDTH = 1200
HEIGHT = 700


def showUI(window, cont):

    # # Create label
    # l = Label(root, text="Bookstore User")
    # l.config(font=("Courier", 14))

    # ll = tk.Label(window, text='lower left')

    # lr = tk.Label(window, text='lower right')
    # ##ll.place(x=0, y=250, anchor='sw')
    # ##lr.place(x=1000, y=250, anchor='se')
    # ll.place(relx=0.0, rely=1.0, anchor='sw')
    # lr.place(relx=1.0, rely=1.0, anchor='se')

    # buttonSI = tk.Button(window, text="Sign In")
    # buttonSI.pack(side='left', ipadx=50, padx=50)

    # userID_lbl = Label(window, text='userID')
    # userID_lbl.grid(column=0, row=0)

    # passwd_lbl = Label(window, text='password')
    # passwd_lbl.grid(column=0, row=1)

    # userID_entry = Entry(window, width=50)
    # userID_entry.grid(column=1, row=0)

    # passwd_entry = Entry(window, width=50)
    # passwd_entry.grid(column=1, row=1)

    # the label for user_name
    user_name = Label(window, text="Username").place(x=40, y=60)

    # the label for user_password
    user_password = Label(window, text="Password").place(x=40, y=100)

    submit_button = Button(window, text="Sign In",
                           command=cont.show_User).place(x=40, y=130)

    user_name_input_area = Entry(window, width=30).place(x=110, y=60)

    user_password_entry_area = Entry(window, width=30).place(x=110, y=100)

    # buttonE = tk.Button(window, text="East")
    # buttonE.pack(side='right', ipadx=20, padx=30)

    # buttonS = tk.Button(window, text="   ")
    # buttonS.pack(side='bottom', ipadx=20, padx=30)

    # T = Text(window, height=5, width=52)

    # # Create label
    # l = Label(window, text="Fact of the Day")
    # l.config(font=("Courier", 14))
    # l.pack(side=LEFT)
    # T.pack(side=LEFT)
    # B = tk.Button(window, text="Hello", command=print_text)
    # B.pack()

    window.title("LOGIN")
    window.geometry(f"{WIDTH}x{HEIGHT}+10+10")
    window.mainloop()
#


def print_text():
    print("JESLA")


# showUI(Tk())
