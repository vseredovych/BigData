#!/usr/bin/env python3
import sys


def emit(pivots, values):
    n = len(pivots)

    pivots.sort()

    """ Dictionary of sets such that each subset contains values between pivot[i] and pivot[i+1] """
    subsets = {i: [] for i in range(n+1)}

    for v in values:
        if v <= pivots[0]:
            subsets[0].append(v)
            continue
        if pivots[n - 1] < v:
            subsets[n].append(v)
            continue

        for i in range(n - 1):
            if pivots[i] < v <= pivots[i + 1]:
                subsets[i + 1].append(v)
                break

    for key, L in subsets.items():
        for v in L:
            print(f"{key}: {v}")


def main():
    current_key = None

    """
    Processing lines in format:
    key: value (hash: object value)
    or
    key: value (hash: pivot value)

    key: int
        number of the baket (hash) 

    value: list(string, value)
        object/pivot: string which contain "object" or "pivot" flags 
        value: value of the element from the set
    """
    grouped_pivots = []
    grouped_values = []

    for line in sys.stdin:
        line = line.strip()

        key = line.split(':')[0].strip()
        value = line.split(':')[1].strip()

        origin = str(value.split()[0].strip())
        p_o_value = int(value.split()[1].strip())

        if current_key is None:
            current_key = key

        # If the value has current index add it to the sum
        if current_key == key:
            if origin == 'pivot':
                grouped_pivots.append(p_o_value)
            elif origin == 'object':
                grouped_values.append(p_o_value)
        else:
            emit(grouped_pivots, grouped_values)
            current_key = key

            if origin == 'pivot':
                grouped_pivots = [p_o_value]
                grouped_values = []
            elif origin == 'object':
                grouped_pivots = []
                grouped_values = [p_o_value]

    emit(grouped_pivots, grouped_values)


if __name__ == '__main__':
    main()
