#!/usr/bin/python3

def catch_dollar_amount_input():
    given_name = input('\n*Enter the name of the person the check is designated for: -> ')
    given_value = input('*Please enter a dollar amount: - > ')
    given_value_length = len(given_value)

    return int(given_value), given_value_length, given_name


def define_printing(input_value, person_name):
    value_to_print = f"{input_value:,}"
    final_length = len(value_to_print)
    final_name_length = len(person_name)

    def to_print():
        if final_length < 10:
            return f'\t\033[1m$ {value_to_print:*>10}\033[0m'
        else:
            return f'\t\033[1m$ {value_to_print}\033[0m'

    print(f'\n---PARTIAL CHECK---')
    print(f"\n\tPAY TO THE \033[1;31m\t{person_name}\033[0m{to_print()}\n\tORDER OF\t{'':-<{final_name_length}}")


value, value_length, name = catch_dollar_amount_input()
define_printing(value, name)
