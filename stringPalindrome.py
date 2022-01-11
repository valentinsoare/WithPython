#!/usr/bin/python

import string

our_string = '123454321'


def is_palindrome(given_string):
    punctuation_list = string.punctuation
    processed_list = list(filter(lambda k: k not in punctuation_list and k != ' ' and k != string.whitespace,
                                 list(given_string.lower())))
    length_of_a_list = len(processed_list)
    ranges = len(processed_list) // 2
    count = 0
    i = 0

    while i < ranges:
        if processed_list.pop() == processed_list.pop(0):
            count += 1
        i += 1

    print(f'\n\033[1m String to check: "{given_string}"\033[0m', end="\n")

    if count == length_of_a_list // 2:
        print(f"\n\033[1;32m - > Given string is a palindrome.\033[0m", end="\n\n")
    else:
        print(f"\n\033[1;31m - > Given string is not a palindrome.\033[0m", end="\n\n")


def main():
    is_palindrome(our_string)


main()

