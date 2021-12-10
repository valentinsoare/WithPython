#!/usr/bin/python

import sys


def number_processing(processed_number):
    final = 0

    while processed_number // 10 != 0:
        number_after_modulo = processed_number % 10
        number_after_divide = processed_number // 10
        final = (number_after_modulo + final) * 10

        processed_number = number_after_divide

    return final, processed_number


def conclusion_if_palindrom(final, given_number):
    if final - given_number == 0:
        print(f"{given_number} is a palindrome")
    else:
        print(f"{given_number} is not a palindrome")


def main():
    given_number = 67876
    processed_number = given_number

    final, processed_number = number_processing(processed_number)
    final = final + processed_number

    conclusion_if_palindrom(final, given_number)


main()
sys.exit(0)
