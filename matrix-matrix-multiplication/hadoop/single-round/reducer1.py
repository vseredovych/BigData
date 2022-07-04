#!/usr/bin/env python3
import sys


def emit(key, matrix1_values, matrix2_values):
    matrix1_values.sort(key=lambda x: x[0])
    matrix2_values.sort(key=lambda x: x[0])

    current_sum = 0
    for i in range(len(matrix1_values)):
        current_sum += matrix1_values[i][1]*matrix2_values[i][1]

    print(f"{key}: {current_sum}")


def main():
    current_key = None
    matrix1_grouped_values = []
    matrix2_grouped_values = []

    """
    Processing lines in format:
    key: value (i k: orid j m_n_value)

    key: list(int, int)
        i (int): first index of the matrix multiplication result 
        j (int): second index of the matrix multiplication result 

    value: list(int, int, float)
        orid (int):
            The flag denoting the origin matrix:
                0 - matrix M
                1 - matrix N
        j (int):
            column index of matrix M or row index of matrix N 
        m_n_value (float): 
            the value of an element of matrix M or N 
    """
    for line in sys.stdin:
        line = line.strip()

        key = line.split(':')[0].strip()
        value = line.split(':')[1].strip()
        value_split = value.split()

        orid = int(value_split[0].strip())
        j = int(value_split[1].strip())
        m_n_value = float(value_split[2].strip())

        if current_key is None:
            current_key = key

        # If the value has current index add it to the sum
        if current_key == key:
            if orid == 0:
                matrix1_grouped_values.append((j, m_n_value))
            elif orid == 1:
                matrix2_grouped_values.append((j, m_n_value))
        else:
            emit(current_key, matrix1_grouped_values, matrix2_grouped_values)
            current_key = key

            if orid == 0:
                matrix1_grouped_values = [(j, m_n_value)]
                matrix2_grouped_values = []
            elif orid == 1:
                matrix1_grouped_values = []
                matrix2_grouped_values = [(j, m_n_value)]

    emit(current_key, matrix1_grouped_values, matrix2_grouped_values)


if __name__ == '__main__':
    main()
