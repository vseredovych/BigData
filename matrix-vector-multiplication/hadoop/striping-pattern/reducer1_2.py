#!/usr/bin/env python3
import sys

""" Second implementation of reducer for striping pattern problem """


def emit(grouped_values):
    for idx, value in grouped_values.items():
        """ We know that each dict value will consist only of two values """
        _, index1, value1 = value[0]
        row, index2, value2 = value[1]
        print(f"{row}: {value1 * value2}")


def main():
    current_key = None

    """
    Processing lines in format:
    key: value (index1 stripe: index2: m_v_value)

    key: list(int, int)
        index1 (int):
            index of a row of the result of matrix-vector multiplication
        stripe (int):
            index of a stripe

    value: list(int, float)
        index2 (int): 
            index of a column of a matrix or column of a vector
        m_v_value (float): 
            the value of a matrix or a vector to be multiplied.
    """

    grouped_values = {}

    for line in sys.stdin:
        line = line.strip()
        key = line.split(':')[0].strip()
        value = line.split(':')[1].strip()

        i = int(key.split()[0].strip())
        j = int(value.split()[0].strip())
        m_v_value = float(value.split()[1].strip())

        if current_key is None:
            current_key = key

        # If the value has current index add it to the sum
        if current_key == key:
            if (key, i, j) not in grouped_values.keys():
                grouped_values[(key, i, j)] = [(i, j, m_v_value)]
            else:
                grouped_values[(key, i, j)].append((i, j, m_v_value))
        else:
            emit(grouped_values)
            current_key = key
            grouped_values.clear()
            grouped_values[(key, i, j)] = [(i, j, m_v_value)]

    emit(grouped_values)


if __name__ == '__main__':
    main()
