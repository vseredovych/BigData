#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""mapper.py"""
import sys

"""
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

v = [1, 1, 1]
v.T = [[1],
       [1], 
       [1]]

M * v = [6, 15, 24]

M[i][j] * v[j]
"""

"""
1 0 4
0 0 1
1 1 2
2 2 1
0 2 10
1 2 6
0 1 2
2 1 8
2 0 5

1 2 3
=
35 26 24
"""

# TODO: consider loading vector from the file in dfs
v = [1, 2, 3]

# Processing lines in format "i: int, j: int, float: mij"
for line in sys.stdin:
    try:
        data = line.split()
        i, j = int(data[0]), int(data[1])
        mij = float(data[2])
    except Exception as err:
        continue

    # Debug
    # print(f"i: {i}, j: {j}, mij: {mij}\n")
    value = mij * v[j]
    key = i
    print("%d\t%d" % (key, value))