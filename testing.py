import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

WIDTH = 1200
HEIGHT = 700


def showUI(window, controller):
    def user_login():
        controller.user_login(user_name_input_area.get(),
                              user_password_entry_area.get())

    # the label for user_name
    user_name = Label(window, text="Username").place(x=40, y=60)

    # the label for user_password
    user_password = Label(window, text="Password").place(x=40, y=100)

    submit_button = Button(window, text="Sign In",
                           command=user_login)
    submit_button.place(x=40, y=130)

    user_name_input_area = Entry(window, width=30)
    user_name_input_area.place(x=110, y=60)

    user_password_entry_area = Entry(window, width=30)
    user_password_entry_area.place(x=110, y=100)

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