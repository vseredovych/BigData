#!/usr/bin/python3
""" mapper1.py """

import sys


def main():
    """ Processing lines in format:
    "row col value orid"

    row(int): row index
    col(int): column index
    value(float): value of a matrix element
    orid(bool): matrix number, true if it is the first matrix, false - otherwise
    """

    for line in sys.stdin:
        data = line.split()
        row, col = int(data[0]), int(data[1])
        value = float(data[2])
        orid = int(data[3])

        if orid == 0:
            print(f"{col}: {orid} {row} {value}")
        else:
            print(f"{row}: {orid} {col} {value}")


if __name__ == "__main__":
    main()
