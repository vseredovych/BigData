#!/usr/bin/python3
""" mapper2.py """

import sys


def main():
    """
    This is an Identity Mapper.
    Processing lines in the following format
    key: value (bucket: value)

    bucket (int): bucket number
    value (int): value of the element from the set
    """

    for line in sys.stdin:
        """ This is an identity function, so we just returning the stripped line
        """
        print(line.strip())


if __name__ == '__main__':
    main()
