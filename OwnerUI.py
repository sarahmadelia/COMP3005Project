import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

WIDTH = 1200
HEIGHT = 700


def showUI(window):

    T = Text(window, height=5, width=52)

    # Create label
    l = Label(window, text="Fact of the Day")
    l.config(font=("Courier", 14))
    l.pack(side=LEFT)
    T.pack(side=LEFT)
    B = tk.Button(window, text="Hello", command=print_text)
    B.pack()

    window.title("LOGIN")
    window.geometry(f"{WIDTH}x{HEIGHT}+10+10")
    window.mainloop()


def print_text():
    print("JESLA")

# showUI()
