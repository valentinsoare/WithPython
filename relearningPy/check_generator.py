#!/usr/bin/python

import re
import os
import numpy as np


def printing_header_cashier_check(id_of_the_check):
    header_message_border = f'this document has a void background * microprint borders and signature line ' \
                            f'* watermark present, holdp to light to view'
    message_cashier = "Cashier's Check".center(len(header_message_border), '-')
    name_of_bank = f"ING ROMANIA"
    bank_address_first_part = f"Bucuresti, 14"
    bank_address_second_part = f"{' ' * 2}Lucretiu Patrascanu"

    print(f"\n\033[1;5;47m {header_message_border.upper()} \033[0m")
    print(f" {message_cashier}")

    print(f"\n{' ' * 2}{name_of_bank}", end="")
    print(f"{' ' * 89}{'Branch No: '}\033[4;4m{' ' * 1}{'467':<7}\033[0m")

    print(f"{' ' * 2}{bank_address_first_part}", end="")
    print(f"{' ' * 87}{'Branch: '}\033[4;4m{' ' * 1}{'Morarilor':<10}\033[0m")
    print(f"{bank_address_second_part}", end="")

    print(f"\n{' ' * 98}{id_of_the_check}")


def validate_date(given_date):
    error_message = f"{' ' * 4}ERROR - please use a valid date format (you can use ., - or / between day, month and year. " \
                    f"Also year can be written 2022 or 22)"

    patterns_for_validation_date = r'([0-2]\d|30|31)[-\./]([0-1][0-2])[-\./](\d{4}|\d{2})'
    after_validation = re.fullmatch(patterns_for_validation_date, given_date)

    if after_validation:
        return after_validation.groups()
    else:
        os.system('clear')
        print(f"\n * Printing cashier's check....\n")
        print(f"{error_message}")
        os.system('sleep 1')
        exit(0)


def generate_check_id_from_date(given_date_as_tuple, numbers_of_check_generated_until_now):
    id_to_return = ''

    if numbers_of_check_generated_until_now % 10000 != 0:
        id_to_return += str(numbers_of_check_generated_until_now)[0]
    else:
        id_to_return = str(int(str(numbers_of_check_generated_until_now)[0]) + 1)

    day, month, year = given_date_as_tuple
    id_to_return += year[0:] + month + day

    while True:
        given_digits = np.random.randint(0, 9, 8)
        to_use = int(''.join(str(i) for i in given_digits))

        if to_use % 7 == 0:
            id_to_return += ''.join(i for i in str(to_use))
            return id_to_return


def printing_date_name_sum_in_digits(date_to_use, money_to_pay, name_of_receiver):
    print(f"\n{' ' * 75}{'Date '}\033[4;4m{' ' * 3}{date_to_use:<30}\033[0m")
    print(f"\n{' ' * 2}{'Pay to the'}\n{' ' * 2}{'order of'}", end=" ")
    print(f"\033[4;4m{' ' * 6}{name_of_receiver.title():<60}\033[0m", end="")
    print(f"{' ' * 10}\033[4;4m${' ' * 21} {money_to_pay:*>10} \033[0m")


def from_digits_to_letters(input_amount, after_dot):

    numbers_dict = {
        1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: "Five", 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
        11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen',
        18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty',
        70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 100: 'Hundred', 1000: 'Thousand'
    }

    numbers_after_processed = []

    def for_two_digits(input_value):
        after_mod = input_value % 10
        input_value = input_value - after_mod
        numbers_after_processed.extend([input_value, after_mod])
        input_value = 0

        return input_value

    def for_three_digits(input_value):
        after_mod = input_value % 100
        input_value = input_value - after_mod
        input_value = list(str(input_value))
        numbers_after_processed.extend([int(input_value[0]), 100])

        return after_mod

    def for_four_digits(input_value):
        after_mod = input_value % 1000
        input_value = input_value - after_mod
        input_value = list(str(input_value))
        numbers_after_processed.extend([int(input_value[0]), 1000])

        return after_mod

    while input_amount != 0:
        if input_amount in numbers_dict.keys():
            numbers_after_processed.append(input_amount)
            input_amount = 0
        elif len(str(input_amount)) == 2:
            input_amount = for_two_digits(input_amount)
        elif len(str(input_amount)) == 3:
            input_amount = for_three_digits(input_amount)
        else:
            input_amount = for_four_digits(input_amount)

    value_to_returned = '**'

    for i in numbers_after_processed:
        value_to_returned += f" {numbers_dict.get(i)}"

    if after_dot:
        value_to_returned += f" and {after_dot}/100 **"
    else:
        value_to_returned += f" **"

    return value_to_returned


def processed_input_digit_value(given_input_value):
    after_dot_amount = 0

    try:
        amount = int(given_input_value)
    except ValueError:
        given_input_value = list(given_input_value)
        index_dot = given_input_value.index('.')
        amount = int(''.join(given_input_value[0:index_dot]))
        after_dot_amount = int(''.join(given_input_value[(index_dot+1):]))

    return amount, after_dot_amount


def print_money_in_letters_on_check_and_footer(money_in_letters, remitter_id, signature):
    print(f"\n{' ' * 2}\033[4;4m{' ' * 35}{money_in_letters}\033[0m\033[4;4m{' ' * 23}\033[0m dollars")

    print(f"\n{'Notice To Customers':>50}")
    print(f"{' ' * 8}{'The purchase of an Indemnity Bond may be required before an official check of this bank'}")
    print(f"{' ' * 8}{'will be replaced or refunded in the event it is lost, misplaced or stolen.'}")

    print(f"\n{' ' * 2}{'Remitter'} \033[4;4m{' ' * 3}{remitter_id}{' ' * 40}\033[0m", end="")
    print(f"{' ' * 16}{'Signature'}\033[4;4m{' ' * 2}{signature}{' ' * 25}\033[0m\033[0m\n\n")


def main():
    # limit of th cashier's check is 9999$, no more than that.
    current_date = '12-11-21'
    money_to_cash = '8762'
    name_receiver = 'Andrei Caramitru'
    #-------

    issuing_date = validate_date(current_date)

    id_to_use_on_check = generate_check_id_from_date(issuing_date, 10245)
    printing_header_cashier_check(id_to_use_on_check)

    printing_date_name_sum_in_digits(current_date, money_to_cash, name_receiver)
    before_dot_amount, after_dot_amount = processed_input_digit_value(money_to_cash)
    money_in_letters = from_digits_to_letters(before_dot_amount, after_dot_amount)

    print_money_in_letters_on_check_and_footer(money_in_letters, 'ASUS LTD.', 'VSoare')


if __name__ == '__main__':
    main()

