#!/usr/bin/python3
""" mapper1.py """

import sys
import math


def main():
    """
    Blocking pattern algorithm for multiplying M matrix [n, n] matrix on N matrix [n, n].
    Matrices dimensions have to be known.
    """
    n = 20
    block_size = 2
    block_number = math.floor(n/block_size)

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

        """
        Having:
        m_i_j - matrix M
        n_j_k - matrix N
        B - number of blocks (block_number)
        
        For M: emit ((s, t, k): (orid, i, j, n_i_j)), for k = 0,...,B, s = floor(i/B), k = floor(j/B)
        For N: emit ((s, t, k): (orid, j, k, m_j_k)), for s = 0,...,B, t = floor(j/B), k = floor(k/B)
        """
        if orid == 0:
            s = math.floor(row/block_size)
            t = math.floor(col/block_size)
            """ This is a matrix M """
            for k in range(block_number):
                print(f"{s} {t} {k}: {orid} {row} {col} {value}")
        else:
            t = math.floor(row/block_size)
            k = math.floor(col/block_size)
            """ This is a matrix N """
            for s in range(block_number):
                print(f"{s} {t} {k}: {orid} {row} {col} {value}")


if __name__ == "__main__":
    main()
