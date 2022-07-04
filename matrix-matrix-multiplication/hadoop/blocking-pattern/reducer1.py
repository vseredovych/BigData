#!/usr/bin/env python3
import sys


def emit(matrix1_values, matrix2_values):
    """ Initializing partial block matrix result """
    partial_block_result = {}

    """ Combining and multiplying values from both matrices """
    for i, j1, v1 in matrix1_values:
        for j2, k, v2 in matrix2_values:
            if j1 == j2:
                if (i, k) in partial_block_result.keys():
                    partial_block_result[(i, k)] += v1 * v2
                else:
                    partial_block_result[(i, k)] = v1 * v2

    """ Emitting partial results """
    for key, value in partial_block_result.items():
        i, k = key
        print(f"{i} {k}: {value}")


def main():
    current_key = None
    matrix1_grouped_values = []
    matrix2_grouped_values = []

    """
    Processing lines in format:
    key: value (s t k: orid i j m_n_value)

    key: list(int, int)
        s (int): block-row    index of M or replication  value of N
        t (int): block-column index of M or block-row    index of N 
        k (int): replication  value of M or block-column index of N 

    value: list(int, int, int, float)
        orid (int):
            The flag denoting the origin matrix:
                0 - matrix M
                1 - matrix N
        i (int): row index of M or N
        j (int): column index of M or N 
        m_n_value (float): 
            the value of an element of matrix M or N 
    """
    for line in sys.stdin:
        line = line.strip()

        key = line.split(':')[0].strip()
        value = line.split(':')[1].strip()
        value_split = value.split()

        orid = int(value_split[0].strip())
        i = int(value_split[1].strip())
        j = int(value_split[2].strip())
        m_n_value = float(value_split[3].strip())

        if current_key is None:
            current_key = key

        # If the value has current index add it to the sum
        if current_key == key:
            if orid == 0:
                matrix1_grouped_values.append((i, j, m_n_value))
            elif orid == 1:
                matrix2_grouped_values.append((i, j, m_n_value))
        else:
            emit(matrix1_grouped_values, matrix2_grouped_values)
            current_key = key

            if orid == 0:
                matrix1_grouped_values = [(i, j, m_n_value)]
                matrix2_grouped_values = []
            elif orid == 1:
                matrix1_grouped_values = []
                matrix2_grouped_values = [(i, j, m_n_value)]

    emit(matrix1_grouped_values, matrix2_grouped_values)


if __name__ == '__main__':
    main()
