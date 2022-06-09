#!/usr/bin/python3
""" reducer1.py """

import sys
from typing import List

def reduce_per_current_key(matrix1_values: List[int], matrix2_values: List[int]):
    """
    Reduce function.
    """
    for m1_val in matrix1_values:
        for m2_val in matrix2_values:
            i, m1_ij = int(m1_val[1]), float(m1_val[2])
            k, m2_jk = int(m2_val[1]), float(m2_val[2])

            print(f"{i} {k}: {m1_ij * m2_jk}")


matrix1_current_key_values = []
matrix2_current_key_values = []
current_key = None


if __name__ == '__main__':
    """
    Processing lines in the following format: 
    key: value (key: index1 index2 element)
    
    key: (int):
        Key for a reducer 

    value: list(int, int, int)
        index1: int
            The first matrix index (col or row)
        index2: int
            The second matrix index (col or row) 
        element: float
            The value a matrix element
    """
    for line in sys.stdin:
        try:
            line = line.strip()
            key = int(line.split(':')[0].strip())
            value = line.split(':')[1].strip()
            
            value_split = value.split()
            orid = int(value_split[0])
        except Exception as err:
            continue
        
        """
        Setting the current_key. This should only happen for the first iteration.
        """
        if current_key is None:
            current_key = key

        if key == current_key:
            """ Adding element to the current key group """
            if orid == 0:
                matrix1_current_key_values.append(value_split)
            else:
                matrix2_current_key_values.append(value_split)
        else:
            """ Executing reduce operation """
            reduce_per_current_key(matrix1_current_key_values, matrix2_current_key_values)
    
            """ Clearing the current key groups """
            matrix1_current_key_values = []
            matrix2_current_key_values = []
            current_key = key
            
            """ Adding element to the current key group """
            if orid == 0:
                matrix1_current_key_values.append(value_split)
            else:
                matrix2_current_key_values.append(value_split)

    """ Executing reduce operation """
    reduce_per_current_key(matrix1_current_key_values, matrix2_current_key_values)
