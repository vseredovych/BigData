import sys
import string


def main():
    """ Processing lines in format:
    "word1 word2 word3"

    Words could have arbitrary values.
    """

    for line in sys.stdin:
        # Lower string
        line = line.lower()

        # Remove all punctuation characters
        line = line.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))

        for word in line.split():
            word = word.strip()
            print(f"{word}: 1")


if __name__ == '__main__':
    main()
