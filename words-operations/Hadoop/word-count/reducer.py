import sys


def emit(key, count):
    print(f"{key}: {count}")


def main():
    """ Processing lines in format:
    key: value

    key: (str):
        Key (word) for a reducer

    value: (int)
        The number of occurrences of such key (word)
    """
    current_key = None
    count = 0

    for line in sys.stdin:
        line = line.strip()
        key = line.split(':')[0].strip()
        value = int(line.split(':')[1].strip())

        if current_key is None:
            current_key = key

        if key == current_key:
            count += value
        else:
            emit(current_key, count)
            count = value
            current_key = key

    emit(key, count)


if __name__ == '__main__':
    main()
