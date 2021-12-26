#!/usr/bin/python

string = '14541'


def is_palindrome(given_string):
    processed_list = list(given_string.lower())
    length_of_a_list = len(processed_list)
    ranges = len(processed_list) // 2
    count = 0
    i = 0

    while i < ranges:
        if processed_list.pop() == processed_list.pop(0):
            count += 1
        i += 1

    if count == length_of_a_list // 2:
        print(f"\n\033[1;32m - > String is a palindrome.\033[0m", end="\n\n")
    else:
        print(f"\n\033[1;31m - > String is not a palindrome.\033[0m", end="\n\n")


def main():
    is_palindrome(string)


main()

