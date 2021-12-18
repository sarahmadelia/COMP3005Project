import data
import InitialUI
from tkinter import *
import UserUI
import OwnerUI


class Controller:
    def __init__(self) -> None:
        self.connector = data.getConnector()
        self.window = Tk()
        InitialUI.showUI(self.window, self)

    def print_test(self):
        self.clear_frame()

    def show_login(self):
        self.clear_frame()
        InitialUI.showUI(self.window, self)

    def show_User(self):
        self.clear_frame()
        UserUI.showUI(self.window, self)

    def show_Owner(self):
        self.clear_frame()
        OwnerUI.showUI(self.window, self)

    def clear_frame(self):
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


def main():
    Controller()


if __name__ == "__main__":
    main()
