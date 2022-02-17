#!/usr/bin/python

import re
from time import sleep


def catch_input_from_user():
    print(f'\n\033[1m - > Please enter the desire text containing numbers: (q to quit):\033[0m', end=" ")
    user_input = input()

    if user_input.lower()[0] == 'q':
        print(f'\n\033[1;33m{"Quiting...":>15}\033[0m', end="\n")
        sleep(1)
        exit(1)

    return user_input


def processing_input(given_text):
    valid_numbers_pattern = re.compile(r'[+-]*[0-9]{1,}[\.]*[0-9]{1,}')
    valid_numbers = re.findall(valid_numbers_pattern, given_text)
    sleep(0.5)
    print(f'\n\033[1m{"*Extracted numbers from the given text: ":>45}\033[0m{valid_numbers}', end="\n")


def main():
    given_input = catch_input_from_user()
    processing_input(given_input)


main()