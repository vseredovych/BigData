import sys
import string


def main():
    """ Processing lines in format:
    "word: count"

    word(str): arbitrary string
    count(int): arbitrary integer
    """
    for line in sys.stdin:
        line = line.strip()
        key = line.split(':')[0].strip()
        value = int(line.split(':')[1].strip())

        print(f'{key}: {value} {1}')


if __name__ == '__main__':
    main()
