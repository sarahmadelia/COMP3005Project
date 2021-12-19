""" 
Acts as the controller 
main.py creates the connector and initializes a window for the user interfaces 
to appear on and sets the initial user interface 
"""
import data
import InitialUI
from tkinter import *
import UserUI
import OwnerUI


class Controller:
    def __init__(self) -> None:
        """Initializes a new window and sets it to the initial log-in screen 
        """
        self.connector = data.getConnector()
        self.window = Tk()
        InitialUI.showUI(self.window, self)

    def print_test(self):
        self.clear_frame()

    def show_login(self):
        """Initializes the Initial UI page (login)
        """
        self.clear_frame()
        InitialUI.showUI(self.window, self)

    def show_User(self):
        """Initializes the User UI page 
        """
        self.clear_frame()
        UserUI.showUI(self.window, self)

    def show_Owner(self):
        """Initializes the Owner UI page 
        """
        self.clear_frame()
        OwnerUI.showUI(self.window, self)

    def clear_frame(self):
        """Clears the window and sets a new one
        """
        new_window = Tk()
        self.window.destroy()
        self.window = new_window

    def get_bookstore_names(self):
        """Returns a list containing the names of all the bookstores

        Returns:
            list: list of bookstores
        """
        result = data.sql_execute_command(
            self.connector, "SELECT Store_Name FROM BookStore")
        return [res[0] for res in result]

    def get_bookstore_books(self):
        """Returns a list of ISBN containing the names of all the bookstores 

        Returns:
            list: list of ISBN
        """

        result = data.sql_execute_command(
            self.connector, "SELECT ISBN, Title FROM Book")
        return [res[0]+"    "+res[1] for res in result]

    def get_bank_transfers(self):
        """Returns a list of ID and amount of bank transfers

        Returns:
            list: list
        """

        result = data.sql_execute_command(
            self.connector, "SELECT ID, Publisher_ID, Amount FROM banktransfers")
        return [res[0]+"    "+res[1] + "  "+res[2] for res in result]


def main():
    Controller()


if __name__ == "__main__":
    main()
