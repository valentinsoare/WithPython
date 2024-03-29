#!/usr/bin/python

import os
import sys
import time
import string
import numpy as np
import pandas as pd

##This small project is only with integers from zero to nine. Also result of any operation is with integers.


def check_if_in_range(given_input_string):
    counting_alpha = 0
    counting_operations = 0
    operations = np.array(['plus', 'minus', 'times', 'divided by'], dtype=str)
    digits_alpha = np.array(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'], dtype=str)

    for j in given_input_string:
        if j in digits_alpha:
            counting_alpha += 1

        if j in operations:
            counting_operations += 1

    if counting_operations != 1 or counting_alpha != 2:
        print(f"\n\033[1;31m\tERROR we need to use only the following operations {operations} "
              f"and digits from zero to nine in alpha characters\033[0m", end="\n")
        time.sleep(1)
        return False, list(string.digits), digits_alpha, operations

    return True, list(string.digits), digits_alpha, operations


def catch_input():
    digits = ''
    operations = ''
    var_to_exit = 0
    alpha_digits = ''
    var_to_continue = 0
    splitting_input_series = ''

    while var_to_exit == 0:
        os.system('clear')
        print(f'\n\033[1;1;32m {"< WORD_PROBLEMS >":>42}\033[0m', end="\n")
        print(f"\n\033[1m - > Enter your math operation in words with digits from zero to nine (q to quit):\033[0m",
              end=" ")

        math_operation = input()

        if math_operation[0].lower() == 'q':
            print(f'\n\033[1;33m{"Quitting...":>20}\033[0m', end="\n\n")
            time.sleep(1)
            sys.exit(1)

        splitting_input_series = np.array(math_operation.split(), dtype=str)

        for i in splitting_input_series:
            if i.isnumeric():
                var_to_continue = 1
                print(f"\n\033[1;31m\tERROR - we should use only alpha characters.", end="\n")
                time.sleep(1)
                break

        if var_to_continue == 1:
            continue

        type_of_truth, digits, alpha_digits, operations = check_if_in_range(splitting_input_series)

        if type_of_truth:
            var_to_exit = 1

    return splitting_input_series, digits, alpha_digits, operations


def exec_calculations(*args):
    from_char_to_math = []
    split_series, digits_with_alpha, operations_with_signs = args

    digits_with_alpha_swapped = {j: i for i, j in digits_with_alpha.items()}
    operations_with_signs_swapped = {l: k for k, l in operations_with_signs.items()}

    combined_dicts = {**digits_with_alpha_swapped, **operations_with_signs_swapped}

    for i in split_series:
        for j in combined_dicts.keys():
            if i == j:
                from_char_to_math += [combined_dicts[j]]

    to_execute = ' '.join(from_char_to_math)

    print(f'\n\033[1m - > Converting given operation in words to integers: ', end="")

    for i in split_series:
        print(f"{i} ", end="")

    print(f'equal {digits_with_alpha[eval(to_execute)]}', end=" ")
    print(f'< > {to_execute} = {eval(to_execute)}\033[0m', end="\n\n")


def main():
    split_series, digits, alpha_digits, operations = catch_input()

    digits_with_alpha = pd.Series(alpha_digits, index=digits)
    operations_with_signs = pd.Series(operations, index=['+', '-', '*', '/'])

    exec_calculations(split_series, digits_with_alpha, operations_with_signs)


main()
