#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


def emit(i, current_sum):
    print(f"{i}: {current_sum}")


def main():
    pass

    current_sum = 0
    current_i = None

    """
    Processing lines in format:
    key: value (i mij)

    key: list(int, int)
        i (int): index of a row of matrix

    value: int
        mij: value of a matrix element
    """
    for line in sys.stdin:
        line = line.strip()
        i = int(line.split(':')[0].strip())
        value = float(line.split(':')[1].strip())

        if current_i is None:
            current_i = i

        # If the value has current index add it to the sum
        if current_i == i:
            current_sum += value
        else:
            emit(current_i, current_sum)
            current_sum = value
            current_i = i

    emit(i, current_sum)


if __name__ == '__main__':
    main()
