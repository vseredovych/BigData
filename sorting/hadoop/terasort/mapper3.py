#!/usr/bin/python3
""" mapper3.py """

import sys


def main():
    """ We receive the eta (e.g. number of reducers in the previous run as argument)"""
    eta = int(sys.argv[1])

    """
    Processing lines in the following format
    key: value (bucket: card cardinality)
    or
    key: value (bucket: value)

    key (imt):
        bucket (int): bucket number 

    value:
        card (string):
            flag means that this value represents cardinality of a set in this bucket
        cardinality (int):
            the cardinality of a set in this bucket
        value(float):
            value of an element from the set
    """
    for line in sys.stdin:
        line = line.strip()
        key = int(line.split(':')[0].strip())
        value = line.split(':')[1].strip()

        value_split = value.split()

        if len(value_split) == 1:
            """ This is a value """
            obj_value = int(value.strip())
            print(f"{key}: object {obj_value}")

        elif len(value_split) == 3:
            cardinality = int(value_split[2].strip())

            """ This is a cardinality value """
            for w in range(eta + 1):
                print(f"{w}: card {key} {cardinality}")


if __name__ == '__main__':
    main()
