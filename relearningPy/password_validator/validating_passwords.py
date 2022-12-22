#!/usr/bin/python


import re
import base64
import random
import pwinput
from os import system
from time import sleep
from string import punctuation
from typing import List, Dict, Tuple, AnyStr


def printing_header(message_to_print: AnyStr) -> None:
    while_processing: int = 0
    splitting_msg: List[str] = message_to_print.split()
    processed_message: AnyStr = '######### '

    while while_processing < len(message_to_print):
        if while_processing in [len(splitting_msg[0]), (len(splitting_msg[0]) - 1),
                                                         len(splitting_msg[0]) + len(splitting_msg[1])]:
            processed_message += message_to_print[while_processing]
        else:
            processed_message += message_to_print[while_processing] + \
                                 punctuation[random.randrange(0, (len(punctuation) - 1))]
        while_processing += 1

    processed_message += ' #########'
    length_of_message: int = len(processed_message)
    lines: AnyStr = f"{'-' * length_of_message}"

    print(f"\n{' ' * 15}{lines}", flush=True)
    print(f"{' ' * 15}{processed_message:^{len(lines)}}", flush=True)
    print(f"{' ' * 15}{lines}", flush=True)


def validate_for_complexity(given_string: AnyStr, type_of_input: AnyStr) -> int:
    checks_to_apply: Dict = {'lower letters': '[a-z]', 'upper letters': '[A-Z]',
                             'digit': '[0-9]', 'special char': '[@$!%*_#?&]'}

    for type_of_chars, chars in checks_to_apply.items():
        if not re.search(chars, given_string):
            if type_of_input == 'user':
                print(f"\n{' ' * 12} ERROR - please use at last one {type_of_chars} characters.", flush=True)
                sleep(2)
            return 1
    return 0


def validate_password(given_password: AnyStr) -> int:
    first_rule = r'([A-Za-z0-9].*[\-\s.,_]){4,}[A-Za-z0-9].*'

    if validate_for_complexity(given_password, 'password') == 1 and not re.search(first_rule, given_password):
        print(f"\n{' ' * 12} ERROR - password must contain at least five words, each separatd by a hyphen, a space, a period,\n"
              f"{' ' * 20} a comma or an underscore or password must have a minimum of 5 characters and contain at least one each\n"
              f"{' ' * 21}from uppercase, lowercase, digits and punctuation chars.", flush=True)
        sleep(2)
        return 0
    else:
        return 1


def ask_for_user_password() -> Tuple:
    count: int = 0
    given_user = ''
    to_loop: int = 1
    given_password = ''

    while True:
        system('clear')
        printing_header('password validator')

        our_prompt = f" "
        print(f"{' ' * 7} * Please provide the credentials to validate (q to quit):", flush=True)
        if to_loop == 1:
            print(f"{' ' * 9} - username:", end=" ", flush=True)
            given_user = input()

            to_loop = validate_for_complexity(given_user, 'user')
            if to_loop == 1:
                continue
        else:
            if len(given_user) != 0 and count >= 1:
                print(f"{' ' * 9} - username: {given_user}", flush=True)

            print(f"{' ' * 9} - password:", end="", flush=True)
            given_password = pwinput.pwinput(our_prompt, "*")

            to_loop = validate_password(given_password)
            if to_loop == 1:
                break

        count += 1

    return given_user, given_password


def printing_results(user: AnyStr, password: AnyStr) -> None:
    print(f"\n{' ' * 7} ** Username and password are within complexity requirements.", flush=True)
    print(f"{' ' * 9} - username: {user}", flush=True)

    to_process_print = re.sub(r'["\']', '', str(base64.b64encode(bytes(password, 'utf-8'))))
    print(f"{' ' * 9} - ciphered 64 bits password: {to_process_print}", flush=True)


def main():
    user_from_keyboard, password_from_keyboard = ask_for_user_password()
    printing_results(user_from_keyboard, password_from_keyboard)


if __name__ == '__main__':
    main()
