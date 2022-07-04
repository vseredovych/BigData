#!/usr/bin/python3
""" reducer2.py """

import sys


def main():
    current_sum = 0
    current_key = None

    """
     Processing lines in the following format:

     key: value (row, col: value)

     key: list(int, int)
         Key for a reducer

     value: float
         Value of two multiplied matrices' elements
     """
    for line in sys.stdin:
        line = line.strip()
        key = line.split(':')[0].strip()
        value = line.split(':')[1].strip()

        x = float(value)

        """
        Setting the current_key. This should only happen for the first iteration.
        """
        if current_key is None:
            current_key = key

        if key == current_key:
            current_sum += x
        else:
            print(f"{current_key}: {current_sum}")
            current_sum = x
            current_key = key

    print(f"{current_key}: {current_sum}")


if __name__ == '__main__':
    main()
