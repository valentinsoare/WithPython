#!/usr/bin/python3

import re


def catch_input():
    password = input(f'\n\033[1;31m *Enter Your Password for Validation:\033[0m ')
    return password


def password_validator_basic_rule(given_password):
    pattern = re.search(r'([A-Za-z0-9].*[\-\s.,_]){5,}', given_password)
    return True if pattern else False


def password_validator_eight_chars_rule(given_password):
    texting = re.search(r'(?=.{8,})([A-Z].*)([a-z].*)([0-9].*)([@#$%^&+=].*)', given_password)
    return True if texting else False


def main():
    password_to_check = catch_input()
    checking = False

    while not checking:
        if password_validator_basic_rule(password_to_check):
            print(f'\n\033[1;34m **Basic rule applies here, looks ok.\033[0m\n')
            checking = True
        elif password_validator_eight_chars_rule(password_to_check):
            print(f'\n\033[1;34m **Eight characters rule applies here, we good to go.\033[0m\n')
            checking = True
        else:
            print(f'\n\033[1;41m***ERROR, given password is not within desired guidelines. Please try again.\033[0m')
            password_to_check = catch_input()


main()
