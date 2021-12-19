import data
import ui


def main():
    connector = data.getConnector()

    data.print_all_data(connector)
