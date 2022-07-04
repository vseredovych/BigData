#!/usr/bin/env python
"""mapper.py"""
import sys
import math

"""
Blocking algorithm for multiplying [n, n] matrix with [n, 1] vector.
Block size and n values have to be hardcoded.
"""
n = 20
block_size = 5
block_number = math.floor(n/block_size)


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

        """
        Note:
        0 - flag of the matrix
        1 - flag of the vector
        """
        if len(data) == 3:
            """ This is a matrix value """
            i, j = int(data[0]), int(data[1])
            mij = float(data[2])

            """ Determining block-row of mij """
            s = math.floor(i/block_size)
            """ Determining block-column of mij"""
            t = math.floor(j/block_size)

            key = (s, t)
            value = (0, i, j, mij)
            emit(key, value)

        elif len(data) == 2:
            """ This is a vector data """
            j = int(data[0])
            vj = float(data[1])

            """ Determining segment-row of vj"""
            t = math.floor(j/block_size)

            for s in range(block_number):
                key = (s, t)
                value = (1, j, vj)
                emit(key, value)


if __name__ == '__main__':
    main()


