import sys


def emit(key, current_sum, current_count):
    print(f"{key}: {current_sum/current_count}")


def main():
    """ Processing lines in format:
    key: value (key: sum count))

    key: (str):
        Key (word) for a reducer

    value: list(int, int)
        sum (int): partial set sum from mapper or combiner
        count (int): partial count of set values from mapper or combiner
    """
    current_key = None
    current_sum = 0
    current_count = 0

    for line in sys.stdin:
        line = line.strip()
        key = line.split(':')[0].strip()
        value = line.split(':')[1].strip()

        partial_sum = int(value.split()[0])
        partial_count = int(value.split()[1])

        if current_key is None:
            current_key = key

        if key == current_key:
            current_sum += partial_sum
            current_count += partial_count
        else:
            emit(current_key, current_sum, current_count)
            current_count = partial_count
            current_sum = partial_sum
            current_key = key

    emit(key, current_sum, current_count)


if __name__ == '__main__':
    main()
