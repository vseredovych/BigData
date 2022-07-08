#!/usr/bin/python3
""" mapper1.py """

import sys
import random

def main():
    """
    Terasort algorithm.
    p - is the expected number of pivots.
        Real number will be determined by random.
        Each element may become a pivot if random value generated for it is lower then (p-1)/N
    N - is the number of values which will be passed to this mapper
    """

    random.seed(42)

    p = 5
    N = 1000

    """ Processing lines in format:
    "value"
    value(float): value of an element from the set 
    """
    for line in sys.stdin:
        s = int(line.strip())
        print(f"{s % p}:object {s}")

        if random.random() <= (p-1)/N:
            for w in range(p):
                print(f"{w}:pivot {s}")


if __name__ == "__main__":
    main()
