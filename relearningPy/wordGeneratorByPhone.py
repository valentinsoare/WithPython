#!/usr/bin/python

import string


def map_digits_letters():
    left = 0
    right = 3
    count = 2
    list_with_mapping = []
    given_letters_list = list(letter for letter in string.ascii_lowercase if letter not in ['q', 'z'])

    while count != 10:
        list_with_mapping.append([count, tuple(given_letters_list[left:right])])
        left += 3
        right += 3
        count += 1

    return list_with_mapping


def main():
    mapping_digits_letters = map_digits_letters()


if __name__ == '__main__':
    main()
