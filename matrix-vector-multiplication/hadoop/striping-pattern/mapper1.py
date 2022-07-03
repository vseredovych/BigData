#!/usr/bin/env python
"""mapper.py"""
import sys
import math

"""
Striping algorithm for multiplying [n, n] matrix with [n, 1] vector.
Block size and n values have to be hardcoded.
"""
n = 20
block_size = 2


def emit(key, value):
    print(*key, ":", *value)


def main():
    """
    Processing lines in format:
    key: value (i j mij)
    or
    key: value (i mj)
    (Depends on the data. Matrix values has 3 fields, vector - 2)

    key: list(int, int)
        i (int): index of a row of matrix
        j (int): index of a column of matrix

    value (float):
        mij: value of a matrix element
    """

    for line in sys.stdin:
        line = line.strip()
        data = line.split()

        if len(data) == 3:
            """ This is a matrix value """
            i, j = int(data[0]), int(data[1])
            mij = float(data[2])

            key = (i, math.floor(j / block_size))
            value = (j, mij)
            emit(key, value)

        elif len(data) == 2:
            """ This is a vector data """
            i = int(data[0])
            vi = float(data[1])

            for k in range(n):
                key = (k, math.floor(i / block_size))
                value = (i, vi)
                emit(key, value)


if __name__ == '__main__':
    main()


