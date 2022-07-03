#!/usr/bin/env python3
import sys


def emit(key, value):
    print(f"{key}: {value}")


def main():
    """
    Processing lines in format:
    key: value

    key (int): index of the resulted vector of matrix-vector multiplication
    value (float): partial value of multiplication
    """

    current_key = None
    current_sum = 0

    for line in sys.stdin:
        line = line.strip()

        key = int(line.split(':')[0].strip())
        value = float(line.split(':')[1].strip())

        if current_key is None:
            current_key = key

        # If the value has current index add it to the sum
        if current_key == key:
            current_sum += value
        else:
            emit(current_key, current_sum)
            current_key = key
            current_sum = value

    emit(key, current_sum)


if __name__ == '__main__':
    main()
