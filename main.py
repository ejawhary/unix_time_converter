import math
from time import time

import StampToDate


def welcome():
    print(
        """***  Unix Time Converter  ***"""
    )


if __name__ == '__main__':
    print("")
    welcome()
    print("")
    date = StampToDate.StampToDate(math.floor(time()))
    date.calculateDate()
