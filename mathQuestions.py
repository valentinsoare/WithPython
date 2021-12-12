#!/usr/bin/python3

import random


def to_exit(input_value):
    if input_value == 'q':
        print(f'\n:( Quiting...')
        exit()
    elif input_value.isdecimal():
        input_value = int(input_value)
        return input_value
    else:
        print(f'\n\033[1;31m ERROR -> Try again\033[0m')


def type_of_operation():
    operation_type = input(f'\n*Type of operation (from 1 to 5 (+, -, *, /, random operations) or q to quit) -> ')
    operation_type = to_exit(operation_type)
    return operation_type


def difficulty_level():
    difficulty = input(f'\n*Please enter difficulty level (1 for single digits or '
                       f'2 for double digits) or q to quit -> ')
    difficulty = to_exit(difficulty)
    return difficulty


def generate_digit_numbers(level_difficulty):
    first_generated_number = 0
    second_generated_number = 0
    if level_difficulty == 1:
        first_generated_number = (random.randrange(0, 9) + 1)
        second_generated_number = (random.randrange(0, 9) + 1)
    elif level_difficulty == 2:
        first_generated_number = (random.randrange(9, 100) + 1)
        second_generated_number = (random.randrange(9, 100) + 1)

    return first_generated_number, second_generated_number


def input_catching(operation_type, first_number, second_number):
    op_type = ['+', '-', '*', '/']
    answer = ''
    option = ''

    length_op_type = len(op_type)
    for i in range(length_op_type):
        if (i+1) == operation_type:
            answer = input(f"\n - How much is {first_number} {op_type[i]} "
                           f"{second_number} ? (q to quit, chd for difficulty level,"
                           f" cht for type of operation) -> ")

            if answer.isalpha():
                option = answer
            else:
                answer = int(answer)
                option = 'None'

    return answer, option


def executing(operation_t, first_number, second_number, operation_type):
    catch_input = 0
    correct_responses_messages = [' - Very good!', ' - Nice work!', ' - Keep up the good work']
    wrong_responses_messages = [' - No. Please try again.', ' - Wrong. Try once more.', ' - No. Keep trying.']

    while operation_t != catch_input:
        i = random.randrange(0, 3)

        catch_input, option = input_catching(operation_type, first_number, second_number)

        if option == 'chd':
            return -1
        elif option == 'cht':
            return -2
        elif option == 'q':
            print(f'\n :( Quiting...\n')
            exit()
        elif operation_t != catch_input:
            print(f'{wrong_responses_messages[i]}')
        else:
            print(f'{correct_responses_messages[i]}')


def operation(operation_type, first_number, second_number):
    value_after_exec = ''
    if operation_type == 5:
        given_option = random.randrange(1, 4)
    else:
        given_option = operation_type

    operations_to_execute = [(1, first_number + second_number), (2, first_number - second_number),
                             (3, first_number * second_number), (4, first_number / second_number)]

    length_operations_to_execute = len(operations_to_execute)
    for i in range(length_operations_to_execute):
        if given_option == operations_to_execute[i][0]:
            operation_t = operations_to_execute[i][1]
            value_after_exec = executing(operation_t, first_number, second_number, given_option)

    return value_after_exec


def main():

    difficulty_set = difficulty_level()
    type_of_o = type_of_operation()

    while difficulty_set != 0 and type_of_o != 0:
        first_number, second_number = generate_digit_numbers(difficulty_set)
        execute_operation = operation(type_of_o, first_number, second_number)

        if execute_operation == -1:
            difficulty_set = difficulty_level()
        elif execute_operation == -2:
            type_of_o = type_of_operation()


main()


