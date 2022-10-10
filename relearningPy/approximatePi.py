#!/usr/bin/python

"""Approximating the math constant pi using the following series: pi = 4- 4/3 + 4/5 - 4/7 + 4/9 - 4/11......
calculate how many terms of this series we need to calculate to obtain the Pi value: 3.14, 3.141, 3.1415, 3.14159"""

import os


def header_printing(message):
    length_of_message = len(message) * 2
    space_to_use = length_of_message - len(message)

    print(f"\n{' ' * 20}{' ' * (space_to_use // 2)}{message}")
    print(f"{' ' * 20}{'-' * length_of_message}")


def calculate_pi(number_of_repetitions):
    pi = 0
    for i in range(1, number_of_repetitions, 4):
        pi += 4/i - 4/(i + 2)

    return pi


def validate_answer(given_number):
    try:
        given_number = int(given_number)
        if given_number < 0:
            given_number *= -1
    except ValueError:
        print(f"\n\033[1;31m{' ERROR ' }\033[0m You can use only integers and not 0. Thank you!")
        os.system('sleep 1')
        given_number = -1

    return given_number


def catch_input_from_user_as_number_repetitions():
    count = 0

    while True:
        print(f"\n {count}. How many terms of that series you want to parse to find the value of Pi ? |:", end=" ")
        input_number = input()

        processed_number = validate_answer(input_number)
        count += 1

        if processed_number > 0:
            return processed_number


def main():
    header_printing('Approximate value of Pi')
    number_of_repetitions = catch_input_from_user_as_number_repetitions()
    pi_after_reps = calculate_pi(number_of_repetitions)

    print(f'\n\033[1;32m SUCCESS \033[0m The value of Pi after {number_of_repetitions} terms is {pi_after_reps}.\n')


if __name__ == '__main__':
    main()
