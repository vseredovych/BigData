#!/usr/bin/python3
""" mapper2.py """

import sys


def main():
    """ Identity function, which accepts lines in the following format
    "key: value"
    or
    "row col: value"

    row(int): row index
    col(int): column index
    value(float): value of two multiplied matrices' elements
    """

    for line in sys.stdin:
        """ This is an identity function, so we just returning the stripped line
        """
        print(line.strip())


if __name__ == '__main__':
    main()
