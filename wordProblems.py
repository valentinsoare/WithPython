#!/usr/bin/python3

import re

dict_of_digits = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
                  'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
                  'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20,
                  'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90,
                  'hundred': 100, 'thousand': 1000}


def printing_lines(number):
    i = 0
    while i < number:
        print(f'-', end='')
        i += 1
    print()


def catch_input():
    print(f'\n\033[1;34m*Script was made for numbers under 99999.\033[0m \n\033[1;33m**If you want a broader range, '
          f'you need to edit for_returning function and add a new formula.\033[0m')
    print(f'\033[1;32m***Enter your equation only with letters like (two minus one). We can use only the following operations: plus, minus, times, '
          f'divided by\033[0m')
    printing_lines(94)
    given_number = input(f'\033[1m - > Enter your desired equation: \033[0m')

    return given_number


def define_fields(given_string):
    type_of_operations = ['plus', 'minus', 'times', 'divided by']

    for i in type_of_operations:
        if i in given_string:
            return given_string.partition(i)


def determine_integer_from_string(given_number, output_integers):

    def for_returning(length_of_return_list, output_integers):
        return_dict = {
            12: 'sum(output_integers)',
            3: 'output_integers[0] * output_integers[1] + output_integers[2]',
            4: 'output_integers[0] * output_integers[1] + sum(output_integers[2:])',
            6: 'output_integers[0] * output_integers[1] + output_integers[2] * output_integers[3] + sum(output_integers[4:])',
            7: '(sum(output_integers[0:2]) * output_integers[2]) + (output_integers[3] * output_integers[4]) + sum(output_integers[5:])'
        }
        return eval(return_dict.get(length_of_return_list))

    if re.search(r'\w-\w', given_number):
        given_number = re.sub(r'-', ' ', given_number)

    list_to_processed = list(map(lambda g: g.lower(), given_number.split()))
    length_integers = len(list_to_processed)

    for i in range(length_integers):
        for j, k in dict_of_digits.items():
            if list_to_processed[i] == j:
                output_integers.append(k)
                break

    if length_integers <= 2:
        return for_returning(12, output_integers)
    else:
        return for_returning(length_integers, output_integers)


def main():
    output_integers = []
    given_equation = catch_input()
    first, operator, second = define_fields(given_equation)

    first_number = determine_integer_from_string(first, output_integers)
    output_integers.clear()
    second_number = determine_integer_from_string(second, output_integers)

    processed_results_operations = {'plus': first_number + second_number, 'minus': first_number - second_number,
                                    'times': first_number * second_number, 'divided by': first_number / second_number}

    if operator in processed_results_operations:
        print(f'\n\033[1m RESULT FROM THE EQUATION: {processed_results_operations.get(operator)}')


main()