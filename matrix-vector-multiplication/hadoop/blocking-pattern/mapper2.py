#!/usr/bin/env python
import sys
import math


def main():
    """
    This is an Identity Mapper.

    Processing lines in format:
    key: value

    key (int): index of the resulted vector of matrix-vector multiplication
    value (float): partial value of multiplication
    """

    for line in sys.stdin:
        line = line.strip()
        print(line)


if __name__ == '__main__':
    main()


