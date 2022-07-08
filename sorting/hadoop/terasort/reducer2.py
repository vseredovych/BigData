#!/usr/bin/env python3
import sys


def emit(key, grouped_values):
    print(f"{key}: card {key} {len(grouped_values)}")

    for s in grouped_values:
        print(f"{key}: {s} ")


def main():
    current_key = None
    """
    Processing lines in the following format
    key: value (bucket: value)

    key (int):
        bucket (int): bucket number

    value (int):
        value (int): value of the element from the set
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
            emit(current_key, grouped_values)
            current_key = key
            grouped_values = [value]

    emit(current_key, grouped_values)


if __name__ == '__main__':
    main()
