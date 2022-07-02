#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

current_sum = 0
current_i = None

# Processing lines in format "i: int, value: float"
for line in sys.stdin:
    data = line.split()
 
    i = int(data[0])
    value = float(data[1])

    # If the value has current index add it to the sum
    if current_i == i:
        current_sum += value
    else:
        if current_sum:
            print("%d" % current_sum)
            current_sum = 0
    
        current_sum = value
        current_i = i

# Don't forget to return the last summed value at the end
if current_sum:
    print("%d" % current_sum)