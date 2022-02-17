#!/usr/bin/python

import os
import re
from time import sleep


def catching_input_passwords():
    os.system('clear')
    print(f"\n\033[1m - > Please provide desire passwords to validate (q to quit):\033[0m", end=" ")
    given_text = input()

    if given_text.lower()[0] == 'q':
        print(f'\n\033[1;33m{"Quiting...":>15}\033[0m', end="\n\n")
        sleep(1)
        exit(1)

    return given_text


def first_rule(given_input_text):
    variable_to_exit = 0

    fir_rule = re.compile(r'[a-zA-Z0-9]{5,}[-\s.,_]')

    if re.search(fir_rule, given_input_text):
        print(f"\n\033[32m Five words rule applied.\033[0m", end="\n")
    else:
        print(f"\n\033[31m Error! Five words rule not applied.\033[0m", end="\n")
        variable_to_exit = 1

    sleep(1)

    return variable_to_exit


def second_rule(input_text):
    variable_to_exit = 0

    sec_rule = re.compile(r'(?=.{8,})([A-Z].*)([a-z].*)([0-9].*)([@#$%^&+=].*)')
    if re.search(sec_rule, input_text):
        print(f"\n\033[32m Eight chars rule along with one char from each type set applied here.\033[0m", end="\n\n")
    else:
        print(f"\n\033[31m Error! We need at least one char from all types of characters, digits, uppercase, "
              f"lowercase and punctuations rule.\033[0m", end="\n\n")
        variable_to_exit = 2

    sleep(2)

    return variable_to_exit


def main():
    var_for_first = 1
    var_for_second = 1

    while var_for_first and var_for_second != 0:
        given_text = catching_input_passwords()
        var_for_first = first_rule(given_text)

        if var_for_first == 0:
            continue

        var_for_second = second_rule(given_text)


main()
