#!/usr/bin/python

import re
from os import system
from time import sleep
from numpy import random


def header_printing(message_to_print: str = 'mathematical word problems'):
    final_message: str = '| ^^'
    length_of_given_message: int
    split_message: list
    line_above_and_bellow: str
    split_message = message_to_print.split()

    length_of_given_message = len(split_message)

    for word in range(length_of_given_message):
        for letter in range(len(split_message[word])):
            if letter == random.randint(0, (len(split_message[word]) - 1), 1):
                final_message += split_message[word][letter].upper()
            else:
                final_message += split_message[word][letter]
        if word == length_of_given_message - 1:
            final_message += '^^ |'
        else:
            final_message += ' '

    line_above_and_bellow = f"{'-' * len(final_message)}"

    print(f"\n{' ' * 15}{line_above_and_bellow}", flush=True)
    print(f"{' ' * 15}{final_message}", flush=True)
    print(f"{' ' * 15}{line_above_and_bellow}", flush=True)


def generate_numbers(qty_of_numbers: int = 2, number_of_decimal_places: int = 1) -> list:
    nr_low: int
    nr_high: int
    generated_numbers: list

    if number_of_decimal_places == 1:
        nr_low = 0
        nr_high = 9
    else:
        nr_low = 10**(number_of_decimal_places - 1)
        nr_high = 10**number_of_decimal_places - 1

    generated_numbers = list(random.randint(nr_low, nr_high, qty_of_numbers))
    return generated_numbers


def validate_answer_beginning(given_answer: str) -> str:
    error_message: str = f"\n{' ' * 6}{'ERROR - please avoid do use only empty spaces or newlines.'}"

    if re.match(r'\s+', given_answer) or given_answer == '':
        print(error_message, end=" ", flush=True)
        sleep(2)
        return 'continue'
    elif given_answer.lower()[0] == 'q':
        print(f"\n{' ' * 8}{'Exiting...'}", flush=True)
        sleep(2)
        exit(0)
    elif given_answer.lower() == 'b':
        return 'back'


def ask_for_type_of_operation() -> int:
    question_to_ask: str = f"{' ' * 6} * Please select the type of problem you want:"
    given_list_with_problems: list = ['words to digits', 'digits to words']
    answer_message: str = f"\n\n{' ' * 6} # Answer (q to quit):"
    error_message_1: str = f"\n{' ' * 4} ERROR - You need to use only 1 or 2 as an option."
    catching_error: int = 1
    processed_answer: int = 0

    while catching_error == 1:
        system('clear')
        header_printing('mathematical word problems')
        print(question_to_ask, end=" ", flush=True)

        print()
        for i in range(len(given_list_with_problems)):
            print(f"\n{' ' * 8} {i + 1}. {' '.join(i.capitalize() for i in given_list_with_problems[i].split())}",
                  end="", flush=True)

        print(answer_message, end=" ", flush=True)
        answer_from_user = input().strip()

        if validate_answer_beginning(answer_from_user) == 'continue':
            continue

        try:
            processed_answer = int(answer_from_user)
            catching_error = 0
        except ValueError:
            pass

        if catching_error == 1 or processed_answer not in [1, 2]:
            print(error_message_1, flush=True)
            catching_error = 1
            sleep(2)

    return processed_answer


def ask_how_many_numbers() -> int:
    error: int = 0
    processed_answer: int = 0

    while True:
        system('clear')
        header_printing('mathematical word problems')
        print(f"{' ' * 6} * How many numbers you want for the problems ?", flush=True)
        print(f"{' ' * 6} # Answer (q to quit, b to back):", end=" ", flush=True)
        answer = input().strip()

        to_check = validate_answer_beginning(answer)
        if to_check == 'continue':
            continue
        elif to_check == 'back':
            return -1

        try:
            processed_answer = int(answer)
        except ValueError:
            error = 1

        if error == 1 or processed_answer < 2:
            print(f"\n{' ' * 4} ERROR - Please only positive integers greater than 1.", flush=True)
            sleep(2)
            error = 0
        else:
            return processed_answer


def numbers_and_qty_from_given(count: int, qty_of_numbers: int = 2, type_of_problems: int = 2) -> int:
    answering: int = 0
    how_many_numbers: int = 0
    questions_type: list = ['words to digits', 'digits to words']

    while answering == 0:
        system('clear')
        header_printing('mathematical word problems')
        print(f"{' ' * 6} * We will using {qty_of_numbers} numbers for '{questions_type[type_of_problems -1]}' type math questions.", flush=True)
        print(f"\n{' ' * 6} {count}. {'How many numbers you want to use from those'} {qty_of_numbers} "
              f"{'that you mentioned,'} \n{' ' * 10}{'then you need to select the number of digits (q to quit, b for back):'}", end=" ", flush=True)
        answer = input().strip()

        to_check = validate_answer_beginning(answer)
        if to_check == 'continue':
            continue
        elif to_check == 'back':
            return -1

        try:
            how_many_numbers = int(answer)
        except ValueError:
            answering = 1

        if answering == 1 or how_many_numbers <= 0 or how_many_numbers > qty_of_numbers:
            print(f"\n{' ' * 6}{'ERROR - Please use only a value between 1 and '}{qty_of_numbers}.", flush=True)
            answering = 0
            sleep(2)
        else:
            return how_many_numbers


def type_of_numbers(all_qty_of_numbers: int, only_selected_qty: int, operation: str, count: int) -> tuple:
    checking: int = 0
    processed_answer: int = 0
    types: list = ['words to digits', 'digits to words']

    while checking == 0:
        system('clear')
        header_printing('mathematical word problems')
        print(f"{' ' * 6} * We will using {only_selected_qty} numbers for '{types[operation - 1]}' type math questions from those {all_qty_of_numbers}.\n"
              f"\n{' ' * 7}{count}. Please input how many digits to be in a number (q to quit):", end=" ", flush=True)
        answer = input().strip()

        check = validate_answer_beginning(answer)
        if check == 'continue':
            continue
        elif check == 'back':
            return -1, -1

        try:
            processed_answer = int(answer)
        except ValueError:
            checking = 1

        if checking == 1 or processed_answer < 1:
            print(f"\n{' ' * 6} ERROR - please use a number greater or equal to 1.", flush=True)
            checking = 0
            sleep(2)
        else:
            return only_selected_qty, processed_answer


def ask_for_input_from_user():
    list_for_looping: list = [0, 0, 0]
    list_with_numbers_and_type: list = []
    numbers_for_the_operation: int = 0
    counting: int = 1

    while True:
        if list_for_looping[0] == 0:
            operation_to_use = ask_for_type_of_operation()
            list_for_looping[0] = -1

        if list_for_looping[1] == 0:
            numbers_for_the_operation = ask_how_many_numbers()
            list_for_looping[1] = -1
            if numbers_for_the_operation == -1:
                list_for_looping[0] = 0
                list_for_looping[1] = 0
                continue

        while numbers_for_the_operation != 0:
            if list_for_looping[2] == 0:
                numbers_to_select_type = numbers_and_qty_from_given(counting, numbers_for_the_operation,
                                                                    operation_to_use)
                list_for_looping[2] = -1
                counting += 1
                if numbers_to_select_type == -1:
                    list_for_looping[1] = 0
                    list_for_looping[2] = 0
                    break

            numbers_selected, numbers_type = type_of_numbers(numbers_for_the_operation, numbers_to_select_type,
                                                             operation_to_use, counting)
            counting += 1
            list_for_looping[2] = 0
            numbers_for_the_operation -= numbers_selected
            list_with_numbers_and_type.append((numbers_selected, numbers_type))

        return list_with_numbers_and_type, operation_to_use


def populate_list_with_numbers_by_rules(list_with_nrs_digits: list) -> list:
    list_with_numbers_to_used_in_equation: list = []

    for nr_numbers, nr_digits in list_with_nrs_digits:
        list_with_numbers_generated_by_rules = generate_numbers(qty_of_numbers=nr_numbers, number_of_decimal_places=nr_digits)
        list_with_numbers_to_used_in_equation.append([*list_with_numbers_generated_by_rules])

    return list_with_numbers_to_used_in_equation


def printing_type_of_problems_qty_digits(list_with_numbers_digits: list, problem_type: int):
    list_with_prbs: list = ['words to digits', 'digits to words']
    system('clear')
    header_printing('mathematical word problems')
    print(f"{' ' * 7} * Type of problem: {list_with_prbs[problem_type]}")
    print(f"{' ' * 6} ** {'Qty of numbers'}{'Number of digits':>20}")

    for i, j in list_with_numbers_digits:
        print(f"{' ' * 9} {i:>14}{j:>20}")

    print(f"\n{' ' * 6} * Going to print the math problems with selected options using random numbers...")
    sleep(2)


def convert_from_numeric_to_literal(given_number):
    first_category: dict = {
        0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
        7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
        13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
    }

    second_category: dict = {
        2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
        7: 'seventy', 8: 'eighty', 9: 'ninety'
    }

    third_category: dict = {
        1: 'thousand', 2: 'million', 3: 'billion', 4: 'trillion', 5: 'quadrillion',
        6: 'quintillion', 7: 'sextillion', 8: 'septillion', 9: 'octillion',
        10: 'nonillion', 11: 'decillion'
    }

    def joining_elements(*args):
        return ' '.join(filter(bool, args))

    def divide(dividend, divisor, magnitude):
        return joining_elements(process_number(dividend // divisor), magnitude, process_number(dividend % divisor))

    def process_number(i):
        if i < 20:
            return first_category[i]
        if i < 100:
            return joining_elements(second_category[i // 10], first_category[i % 10])
        if i < 1000:
            return divide(i, 100, 'hundred')
        for k, z in third_category.items():
            if i < 1000 ** (k + 1):
                break
        return divide(i, 1000 ** k, z)

    def catch_number(i):
        if i < 0:
            return joining_elements('negative', process_number(-i))
        if i == 0:
            return 'zero'
        return process_number(i)

    return catch_number(given_number)


def main():
    list_with_nrs_digits, type_of_problem = ask_for_input_from_user()
    printing_type_of_problems_qty_digits(list_with_nrs_digits, type_of_problem)
    list_with_nrs_to_use_in_equation = populate_list_with_numbers_by_rules(list_with_nrs_digits)

    liter_number_from_numeric = convert_from_numeric_to_literal(22)


if __name__ == '__main__':
    main()
