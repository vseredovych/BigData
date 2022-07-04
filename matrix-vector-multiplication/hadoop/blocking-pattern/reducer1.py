#!/usr/bin/env python3
import sys

""" First implementation of reducer1 for striping pattern problem """


def emit(grouped_values):
    for l in grouped_values:
        l_split = l.split()
        l_flag = int(l_split[0].strip())

        """ if flag is 0, then the element belongs to matrix """
        if l_flag == 0:
            w_i = 0
            l_i = int(l_split[1].strip())
            l_j = int(l_split[2].strip())
            l_value = float(l_split[3].strip())

            for m in grouped_values:
                m_split = m.split()
                m_flag = int(m_split[0].strip())

                """ if flag is 1, then the element belongs to vector """
                if m_flag == 1:
                    m_j = int(m_split[1].strip())
                    m_value = float(m_split[2])

                    if l_j == m_j:
                        w_i += m_value * l_value
            print(f'{l_i}: {w_i}')


def main():
    current_key = None

    """
    Processing lines in format:
    key: value (block-row-index block-col-index: matrix-vector-flag i j m_v_value)
    or
    key: value (segment-row-index: matrix-vector-flag j vj)

    key: list(int, int)
        block-row-index (int)
        block-col-index (int)

    value: list(int, float)
        matrix-vector-flag (int):
            If the entry belongs to matrix, matrix-vector-flag=0
            If the entry belongs to matrix, matrix-vector-flag=1
        i (int):
            index of a row of matrix
        j (int):
            index of a row of matrix or vector
        m_v_value (float): 
            the value of a matrix or a vector
    """
    grouped_values = []

    for line in sys.stdin:
        line = line.strip()

        key = line.split(':')[0].strip()
        value = line.split(':')[1].strip()

        if current_key is None:
            current_key = key

        # If the value has current index add it to the sum
        if current_key == key:
            if not grouped_values:
                grouped_values = [value]
            else:
                grouped_values.append(value)
        else:
            emit(grouped_values)
            current_key = key
            grouped_values = [value]

    emit(grouped_values)


if __name__ == '__main__':
    main()
