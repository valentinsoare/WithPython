#!/usr/bin/python

import os
import random

list_with_values = [-1, -1, -1]
value_to_sleep_one = 'sleep 1'
name_of_the_game = 'Game of Math'


def printing_header(given_message):
    message_split = given_message.split()
    message_processed = ' * '.join(map(lambda i: i, message_split))
    length_of_message = len(message_processed)

    print(f"\n{' ' * 10}{' ' * (length_of_message // 2)}{message_processed}")
    print(f"{' ' * 12}{'cd (chng diff)'}, {'co (chng op)'}")
    print(f"{' ' * 10}{'-' * (length_of_message * 2)}")


def ask_operation_type():
    error = 0
    processed_answer = ''
    type_of_math = [(0, 'addition'), (1, 'subtraction'), (2, 'multiplication'), (3, 'division')]

    while not isinstance(processed_answer, int):
        os.system('clear')
        printing_header(name_of_the_game)
        print(f"{' ' * 2} * Please select the type of operation you want:\n")

        for i in type_of_math:
            print(f"{' ' * 5} {(i[0] + 1)}. {i[1].capitalize()}")

        print(f"\n{' ' * 2} * Answer (q to quit):", end=" ")

        given_answer = input()

        try:
            if given_answer.lower()[0] == 'q':
                print(f"\n{' ' * 5} * Exiting...")
                os.system('sleep 2')
                exit(1)
            elif given_answer.lower() == 'cd':
                return given_answer
        except IndexError:
            print(f"\n{' ' * 5} ERROR - please use an option between 1 and 4.")
            os.system(value_to_sleep_one)
            continue

        try:
            processed_answer = (int(given_answer) - 1)
        except ValueError:
            error = 1

        if error == 1 or processed_answer not in list(range(0, 4)):
            print(f"\n{' ' * 5} ERROR - please use an option between 1 and 4.")
            os.system(value_to_sleep_one)
            error = 0
        elif processed_answer == 'cd':
            return processed_answer
        else:
            return type_of_math[processed_answer][0]


def ask_difficulty_level():
    error_value = 0
    processing_answer = ''
    difficulty_level = [(0, 'one digit'), (1, 'two digits')]

    while True:
        os.system('clear')
        printing_header(name_of_the_game)
        print(f"{' ' * 2} * Please select the difficulty level you want:\n")

        for j in difficulty_level:
            print(f"{' ' * 5} {(j[0] + 1)}. {j[1].capitalize()}")

        print(f"\n{' ' * 2} * Answer (q to quit):", end=" ")
        given_answer = input()

        try:
            if given_answer.lower()[0] == 'q':
                print(f"\n{' ' * 5}   Exiting...\n")
                os.system(value_to_sleep_one)
                exit(1)
            elif given_answer.lower() == 'co':
                return given_answer
        except IndexError:
            print(f"\n{' ' * 5} ERROR - please use an option between 1 and 2.")
            os.system(value_to_sleep_one)
            continue

        try:
            processing_answer = int(given_answer) - 1
        except ValueError:

            error_value = 1

        if error_value == 1 or processing_answer not in [0, 1]:
            print(f"\n{' ' * 5} ERROR - please use an option between 1 and 2.")
            os.system(value_to_sleep_one)
            error_value = 0
        else:
            return difficulty_level[processing_answer][0]


def generate_the_digits(diff_level):
    if diff_level == 0:
        digit_1 = random.randrange(1, 9)
        digit_2 = random.randrange(1, 9)
    else:
        digit_1 = random.randrange(10, 99)
        digit_2 = random.randrange(10, 99)
    return digit_1, digit_2


def ask_the_question(type_of_operation, d_1, d_2):
    processed_answer = ''
    list_with_math = [(0, '+'), (1, '-'), (2, '*'), (3, '/')]

    while not isinstance(processed_answer, int) and not isinstance(processed_answer, float):
        os.system('clear')
        printing_header(name_of_the_game)
        print(f"{' ' * 4} * How much is {d_1} {list_with_math[type_of_operation][1]} {d_2} (q to quit):", end=" ")

        given_answer = input()

        try:
            if given_answer.lower()[0] == 'q':
                print(f"\n{' ' * 5}   Exiting...\n")
                os.system(value_to_sleep_one)
                exit(1)
            elif given_answer.lower() == 'co':
                list_with_values[0] = -1
                return given_answer, '1'
            elif given_answer.lower() == 'cd':
                list_with_values[1] = -1
                return given_answer, '1'
        except IndexError:
            print(f"\n{' ' * 5} ERROR you need to use integers/floats when you answer to math questions or "
                  f"'cd' or 'cd' to change operation or difficulty.")
            os.system(value_to_sleep_one)
            continue

        try:
            processed_answer = int(given_answer)
        except ValueError:
            try:
                processed_answer = float(given_answer)
            except ValueError:
                print(f"\n{' ' * 5} ERROR you need to use integers/floats when you answer to math questions or 'cd' "
                      f"or 'cd' to change operation or difficulty.")
                os.system(value_to_sleep_one)
                continue

    return processed_answer, None


def validate_answer(type_of_operation, digit1, digit2, value_from_answer):
    list_with_operations = [(digit1 + digit2), (digit1 - digit2), (digit1 * digit2), float('%.1f' % (digit1 / digit2))]
    positive_messages = ['Very good!', 'Nice work!', 'Keep up the good work!']
    negative_messages = ['No. Please try again!', 'Wrong, Try once more!', 'No. Keep trying!']

    if value_from_answer == list_with_operations[type_of_operation]:
        print(f"\n{' ' * 8}{positive_messages[random.randrange(3)]}")
        os.system(value_to_sleep_one)
        value_to_return = '1'
    else:
        print(f"\n{' ' * 8}{negative_messages[random.randrange(3)]}")
        os.system(value_to_sleep_one)
        value_to_return = '0'

    return value_to_return


def main():
    d_1 = d_2 = ''
    chosen_operation = ''
    choose_difficulty_level = ''
    answer_after_math_checking = '1'

    while True:
        if list_with_values[0] != -2:

            chosen_operation = ask_operation_type()

            if chosen_operation == 'cd':
                print(f"\n{' ' * 5} ERROR please choose an operation first and then you can choose a difficulty "
                      f"level when you start the script.")
                os.system('sleep 1')
                list_with_values[1] = -1
                continue

            list_with_values[0] = -2

        if list_with_values[1] != -2:
            choose_difficulty_level = ask_difficulty_level()
            list_with_values[1] = -2

            if choose_difficulty_level == 'co':
                print(f"\n{' ' * 5} ERROR please choose a difficulty level first and then you can change the operation.")
                os.system('sleep 1')
                list_with_values[1] = -1
                list_with_values[0] = -2
                continue

        if answer_after_math_checking == '1':
            d_1, d_2 = generate_the_digits(choose_difficulty_level)

        answer_from_question, answer_after_math_checking = ask_the_question(chosen_operation, d_1, d_2)

        if isinstance(answer_from_question, int) or isinstance(answer_from_question, float):
            answer_after_math_checking = validate_answer(chosen_operation, d_1, d_2, answer_from_question)


if __name__ == '__main__':
    main()
