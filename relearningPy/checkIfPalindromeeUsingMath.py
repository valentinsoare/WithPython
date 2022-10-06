#!/usr/bin/python

"""Checking if it is a palindrome but analysis is based on Math with // and %"""

import os


def header_print(message, right, left):
    length_of_a_string = len(message)
    print(f"\n\n{' ':>20}{'#' * (length_of_a_string + right + left)}")
    print(f"{'#':>20}{message:>{length_of_a_string + left}}{'#':>{right + 1}}")
    print(f"{' ':>20}{'#' * (length_of_a_string + right + left)}")


def sanity_check_number(given_value):
    try:
        given_value = int(given_value)
    except ValueError:
        print(f"\n{' ** ERROR - we need an integer in order to check if it is a palindrome.':>70}")
        os.system('sleep 1')
        given_value = 'error'

    return given_value


def ask_for_number():
    number_after_analysis = ''

    while isinstance(number_after_analysis, str):
        print(f'\n - > Give an integer in order to analyse:', end=" ")
        given_number = input()
        number_after_analysis = sanity_check_number(given_number)

    return number_after_analysis


def analysing_number(number_given):
    i = 0
    list_with_digits_reverse = []
    length_of_number = len(str(number_given))
    initial_number = number_given

    while i < length_of_number:
        after_modulo = number_given % 10
        number_given = number_given // 10
        list_with_digits_reverse.append(str(after_modulo))
        i += 1

    number_in_reverse = int(''.join(list_with_digits_reverse))

    if initial_number == number_in_reverse:
        print(f'\n - Given number "{initial_number}" is a palindrome.\n')
    else:
        print(f'\n - Number "{initial_number}" is not a palindrome.\n')


def main():
    header_print("Palindrome Analyzer", 8, 8)

    number_to_check = ask_for_number()
    analysing_number(number_to_check)


if __name__ == '__main__':
    main()
