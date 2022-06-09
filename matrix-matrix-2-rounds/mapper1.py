#!/usr/bin/python3
""" mapper1.py """

import sys

""" Processing lines in format:
"orid row col value"

orgid(bool): matrix number, true if it is the first matrix, false - otherwise
row(int): row index
col(int): column index
value(float): value of a matrix element
"""

for line in sys.stdin:
    try:
        data = line.split()
        orid = int(data[0])
        row, col = int(data[1]), int(data[2])
        value = float(data[3])
    except Exception as err:
        continue

    if orid == 0:
        print(f"{col}: {int(orid)} {row} {value}")
    else:
        print(f"{row}: {int(orid)} {col} {value}")
