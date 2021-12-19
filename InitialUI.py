import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

WIDTH = 1200
HEIGHT = 700


def showUI(window, controller):
    """ User Sign-In lets the user sign in with ID and password"""
    display_message1 = Label(
        window, text="Are you a returning user? Please sign in here! ").place(x=40, y=40)

    user_ID = Label(window, text="User ID").place(x=40, y=60)
    user_ID_entry_area = Entry(window, width=30).place(x=110, y=60)

    user_password = Label(window, text="Password").place(x=40, y=100)
    user_password_entry_area = Entry(window, width=30).place(x=110, y=100)

    signin_button = Button(window, text="Sign In",
                           command=controller.show_User).place(x=40, y=130)

    """User Sign-Up lets the user sign up with their username, email, password, Billing Address and Shipping Address"""
    display_message2 = Label(
        window, text="Are you a new user? Please sign up here!"). place(x=40, y=200)

    new_user_name = Label(window, text="User Name").place(x=40, y=250)
    new_user_ID_entry_area = Entry(window, width=30).place(x=150, y=250)

    new_user_password = Label(window, text="Password").place(x=40, y=300)
    new_user_password_entry_area = Entry(window, width=30).place(x=150, y=300)

    new_user_email = Label(window, text="Email").place(x=40, y=350)
    new_user_email_entry = Entry(window, width=40). place(x=150, y=350)

    new_user_shipping = Label(
        window, text="Shipping Address").place(x=40, y=400)
    new_user_shipping_entry = Entry(window, width=40). place(x=150, y=400)

    new_user_billing = Label(window, text="Billing Address").place(x=40, y=450)
    new_user_billing_entry = Entry(window, width=40). place(x=150, y=450)

    signup_button = Button(window, text="Sign Up",
                           command=controller.show_User).place(x=40, y=520)

    """ Bookstore owner sign in section """

    display_message3 = Label(
        window, text="Are you a bookstore owner? Sign in here! ").place(x=700, y=40)

    owner_ID = Label(window, text="User ID").place(x=700, y=60)
    owner_ID_entry_area = Entry(window, width=30).place(x=810, y=60)

    owner_password = Label(window, text="Password").place(x=700, y=100)
    owner_password_entry_area = Entry(window, width=30).place(x=810, y=100)

    signin_button = Button(window, text="Sign In",
                           command=controller.show_Owner).place(x=700, y=130)

    window.title("LOGIN PAGE")
    window.geometry(f"{WIDTH}x{HEIGHT}+10+10")
    window.mainloop()


def print_text():
    print("JESLA")
