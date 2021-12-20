import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

WIDTH = 1200
HEIGHT = 700


def showUI(window, controller):
    def user_login():
        controller.user_login(user_email_input_area.get(),
                                user_password_entry_area.get())

    def user_signUp():
        controller.user_signUp(new_user_ID_entry_area.get(),
                                new_user_password_entry_area.get(),
                                new_user_email_entry.get(),
                                new_user_shipping_entry.get(),
                                new_user_billing_entry.get())
    def owner_login():
        controller.ownerSignIn()

    """ User Sign-In lets the user sign in with ID and password"""
    display_message1 = Label(
        window, text="Are you a returning user? Please sign in here! ")
    display_message1.place(x=40, y=40)

    user_email = Label(window, text="User Email")
    user_email.place(x=40, y=60)
    user_email_input_area = Entry(window, width=30)
    user_email_input_area.place(x=110, y=60)

    user_password = Label(window, text="Password")
    user_password.place(x=40, y=100)
    user_password_entry_area = Entry(window, width=30)
    user_password_entry_area.place(x=110, y=100)

    signin_button = Button(window, text="Sign In",
                           command=user_login)
    signin_button.place(x=40, y=130)

    """User Sign-Up lets the user sign up with their username, email, password, Billing Address and Shipping Address"""
    display_message2 = Label(
        window, text="Are you a new user? Please sign up here!")
    display_message2. place(x=40, y=200)

    new_user_name = Label(window, text="User Name")
    new_user_name.place(x=40, y=250)
    new_user_ID_entry_area = Entry(window, width=30)
    new_user_ID_entry_area.place(x=150, y=250)

    new_user_password = Label(window, text="Password")
    new_user_password.place(x=40, y=300)
    new_user_password_entry_area = Entry(window, width=30)
    new_user_password_entry_area.place(x=150, y=300)

    new_user_email = Label(window, text="Email")
    new_user_email.place(x=40, y=350)
    new_user_email_entry = Entry(window, width=40)
    new_user_email_entry.place(x=150, y=350)

    new_user_shipping = Label(
        window, text="Shipping Address")
    new_user_shipping.place(x=40, y=400)
    new_user_shipping_entry = Entry(window, width=40)
    new_user_shipping_entry. place(x=150, y=400)

    new_user_billing = Label(window, text="Billing Address")
    new_user_billing.place(x=40, y=450)
    new_user_billing_entry = Entry(window, width=40)
    new_user_billing_entry. place(x=150, y=450)

    signup_button = Button(window, text="Sign Up",
                           command=user_signUp)
    signup_button.place(x=40, y=520)

    """ Bookstore owner sign in section """

    display_message3 = Label(
        window, text="Are you a bookstore owner? Sign in here! ")
    display_message3.place(x=700, y=40)

    # owner_ID = Label(window, text="User ID")
    # owner_ID.place(x=700, y=60)
    # owner_ID_entry_area = Entry(window, width=30)
    # owner_ID_entry_area.place(x=810, y=60)

    # owner_password = Label(window, text="Password")
    # owner_password.place(x=700, y=100)
    # owner_password_entry_area = Entry(window, width=30)
    # owner_password_entry_area.place(x=810, y=100)

    signin_button = Button(window, text="   Sign In   ",
                           command=owner_login)
    signin_button.place(x=700, y=60)

    window.title("LOGIN PAGE")
    window.geometry(f"{WIDTH}x{HEIGHT}+10+10")
    window.mainloop()


def print_text():
    print("JESLA")
