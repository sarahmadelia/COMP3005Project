import data
# import practiceUI
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
        # print(data.sql_execute_command(self.connector, "SELECT * FROM BookStore"))
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
        # frame = Frame(self.window)
        # for widget in frame.winfo_children():
        #     widget.destroy()
        new_window = Tk()
        self.window.destroy()
        self.window = new_window


def main():
    Controller()
    # connector = data.getConnector()
    # results = data.sql_execute_command(connector, "SELECT * FROM BookStore")
    # print(results)
    # window = Tk()
    # InitialUI.showUI(window)


if __name__ == "__main__":
    main()
