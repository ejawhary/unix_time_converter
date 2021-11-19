import math
from time import time

import StampToDate


def welcome():
    print(
        """***  Unix Time Converter  ***"""
    )

def menu():
    print("""Options
        1. Enter a timestamp
        2. Current timestamp""")


if __name__ == '__main__':
    print("")
    welcome()
    print("")
    menu()
    selection = input("Selection: ")

    match selection:
        case "1":
            timestamp = math.floor(input("TimeStamp: "))
            date = StampToDate.StampToDate(timestamp)
            date.calculateDate()
        case "2":
            timestamp = input("TimeStamp: ")
            date = StampToDate.StampToDate(math.floor(time()))
            date.calculateDate()

