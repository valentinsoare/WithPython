#!/usr/bin/python

"""Estimates the value of e constant after how many terms from the series we want to add.
The number of terms is asked from the user."""

import os


def header_define(given_message):
    print(f"\n{' ' * 25}{' ' * (len(given_message) // 2)}{given_message}")
    print(f"{' ' * 25}{'-' * (len(given_message) * 2)}")


def calc_factorial(number_given):
    result = 1
    for i in range(number_given, 1, -1):
        result *= i

    return result


def calculate_e(number_of_terms):
    e = 1
    for i in range(1, number_of_terms + 1):
        e += 1/calc_factorial(i)

    return e


def ask_for_input():
    number_extracted = ''

    while not isinstance(number_extracted, int):
        header_define('Value Of e Constant')

        print(f"{' ' * 18} (*)(*) How many terms from series you want ot use:", end=" ")
        answer = input()

        try:
            number_extracted = int(answer)
            if number_extracted < 0:
                return number_extracted * -1
        except ValueError:
            print(f"\n{' ' * 20}\033[1;31m error \033[0m only integers are allowed greater than 0.")
            os.system('sleep 1')
            number_extracted = 'error'
            os.system('clear')

    return number_extracted


def main():
    number_of_terms = ask_for_input()
    calculated_e = calculate_e(number_of_terms)

    print(f"\n{' ' * 17}\033[1;32m success\033[0m value of e after {number_of_terms} terms is {calculated_e}.")


if __name__ == "__main__":
    main()
