import math
from time import time

import StampToDate


def welcome():
    print(
        """***  Unix Time Converter  ***"""
    )

def menu():
    print("""
        Options:
        1. Enter a timestamp
        2. Current timestamp
        0. Quit""")


if __name__ == '__main__':
    print("")
    welcome()

    while True:
        print("")
        menu()
        selection = input("        Selection: ")

        if selection == "1":
            timestamp = int(input("TimeStamp: "))
            print("")
            print("Custom Timestamp:")
            date = StampToDate.StampToDate(math.floor(timestamp))
            date.calculateDate()
        elif selection == "2":
            print("")
            print("Current Timestamp:")
            date = StampToDate.StampToDate(math.floor(time()))
            date.calculateDate()
        elif selection == "0":
            print("Exiting... Goodbye...")
            break
        else:
            print("Invalid selection... Please try again.")

