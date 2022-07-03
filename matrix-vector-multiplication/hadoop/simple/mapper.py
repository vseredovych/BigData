#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""mapper.py"""
import sys

"""
Example of matrix-vector multiplication:

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

v.T = [[1],
       [1], 
       [1]]

M * v = [6, 15, 24]

M[i][j] * v[j]

Example data for Map Reduce:
1 0 4
0 0 1
1 1 2
2 2 1
0 2 10
1 2 6
0 1 2
2 1 8
2 0 5
*
1 2 3
=
35 26 24
"""


def main():
    """
    Processing lines in format:
    key: value (i j mij)

    key: list(int, int)
        i (int): index of a row of matrix
        j (int): index of a column of matrix

    value: int
        mij: value of a matrix element
    """

    """
    In this basic algorithm the vector is supposed to be 
    loaded into the memory. For simplicity we hardcode it here.
    """
    v = [3, 5, 5, 0, 9, 0, 8, 2, 8, 4, 1, 6, 9, 1, 7, 5, 8, 4, 4, 6]

    for line in sys.stdin:
        line = line.strip()
        data = line.split()

        i, j = int(data[0]), int(data[1])
        mij = float(data[2])

        key = i
        value = mij * v[j]

        print(f'{key}: {value}')


if __name__ == '__main__':
    main()


