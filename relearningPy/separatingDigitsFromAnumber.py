#!/usr/bin/python3

"""Separating digits in a number but with math, // and %."""

import os


def header():
    print(f"\n{'|':>17}{'':#>32}|")
    print(f"{'|':>17} Separating Digits from Numbers |")
    print(f"{'|':>17}{'':#>32}|\n")


def number_validation(number_from_keyboard):
    try:
        number_given = int(number_from_keyboard)
        return number_given
    except ValueError:

        if number_from_keyboard.lower()[0] == 'q':
            print(f"\n{ 'Exiting...':>20}")
            os.system('sleep 1')
            exit(0)

        print(f"\n{'ERROR - please provide an integer!':>37}\n")
        os.system('sleep 1')
        os.system('clear')

        return '-1'


def catch_number():
    processed_number = ''

    while not isinstance(processed_number, int):
        header()
        print(f" - > Please enter your integer with how many digits you want (q to quit):", end=" ")
        given_number = input()

        processed_number = number_validation(given_number)

    return processed_number


def process_number(given_number_by_user):
    list_after_process = []

    while given_number_by_user != 0:
        number_after_modulo = given_number_by_user % 10
        given_number_by_user = given_number_by_user // 10
        list_after_process.append(str(number_after_modulo))

    return list_after_process


def printing_result(separated_number):
    dash = "-"
    print(f"{dash * 67}")
    print(f" <*> Separated digits by space: {separated_number}")


def main():
    given_number = catch_number()
    separated_digits = ' '.join(reversed(process_number(given_number)))
    printing_result(separated_digits)


if __name__ == "__main__":
    main()
