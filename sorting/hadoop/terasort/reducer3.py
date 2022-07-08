#!/usr/bin/env python3
import sys


def emit(key, cardinalities, values):
    cardinalities_parsed = []
    values_parsed = []

    """ Parse values """
    for c in cardinalities:
        split = c.split()
        cardinalities_parsed.append([int(split[1]), int(split[2])])

    for v in values:
        values_parsed.append(int(v.split()[1]))

    """ Sort values """
    cardinalities_parsed.sort(key=lambda x: x[0])
    values_parsed.sort()

    """ Numerate values """
    if key == 0:
        R = 0
    else:
        R = 1 + sum([cardinalities_parsed[i][1] for i in range(key)])

    for idx, s in enumerate(values_parsed):
        print(f"{R+idx}: {s}")


def main():
    current_key = None

    """
    Processing lines in format:
    key: value (bucket: object value)
    or
    key: value (bucket: card value)

    key (int):
        bucket(int): bucket number

    value: list(int, float)
        card:
            flag which means that this value represents cardinality of a set in this bucket
        object:
            flag which means that this value represents a value of an element from the set
        value (int):
            Either the cardinality of a set in this bucket OR the value of an element from the set
    """
    grouped_cardinalities = []
    grouped_values = []

    for line in sys.stdin:
        line = line.strip()
        key = int(line.split(':')[0].strip())
        value = line.split(':')[1].strip()

        origin = str(value.split()[0].strip())

        if current_key is None:
            current_key = key

        # If the value has current index add it to the sum
        if current_key == key:
            if origin == 'card':
                grouped_cardinalities.append(value)
            elif origin == 'object':
                grouped_values.append(value)
        else:
            emit(current_key, grouped_cardinalities, grouped_values)
            current_key = key

            if origin == 'card':
                grouped_cardinalities = [value]
                grouped_values = []
            elif origin == 'object':
                grouped_cardinalities = []
                grouped_values = [value]

    emit(current_key, grouped_cardinalities, grouped_values)


if __name__ == '__main__':
    main()
