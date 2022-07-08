#!/usr/bin/python3
""" mapper1.py """
import math
import sys


def main():
    """
    Banding algorithm for multiplying M matrix [n, n] matrix on N matrix [p, n].
    Matrices dimensions have to be known.
    """
    n = 20
    band_size = 2
    band_number = math.floor(n/band_size)

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
            """ This is a matrix M """
            g_i = math.floor(row/band_number)
            for b in range(band_number):
                print(f"{g_i} {b}: {orid} {row} {col} {value}")
        else:
            g_i = math.floor(col/band_number)
            for b in range(band_number):
                print(f"{b} {g_i}: {orid} {row} {col} {value}")


if __name__ == "__main__":
    main()
