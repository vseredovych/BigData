#!/usr/bin/python3
""" mapper1.py """

import sys


def main():
    """
    Single round algorithm for multiplying M matrix [n, p] matrix on N matrix [p, m].
    Matrices dimensions have to be known, in particular p.
    """
    p = 20

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
        
        For M: emit ((i, k): (orid, j, m_value)), for k = 0,...,p-1
        For N: emit ((i, k): (orid, j, n_value)), for i = 0,...,p-1
        """
        if orid == 0:
            for k in range(p):
                print(f"{row} {k}: {orid} {col} {value}")
        else:
            for i in range(p):
                print(f"{i} {col}: {orid} {row} {value}")


if __name__ == "__main__":
    main()
