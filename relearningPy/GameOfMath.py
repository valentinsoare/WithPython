#!/usr/bin/python

import os
import time
import random


def print_header(given_message):
    given_length_of_message = len(given_message)
    print(f"\n{' ' * 20}{' ' * (given_length_of_message // 2)}{given_message}")
    print(f"{' ' * 20}{'-' * given_length_of_message * 2}")


def generate_numbers_to_use(type_of_randoms):
    if type_of_randoms == 1:
        first_number = random.randrange(1, 10)
        second_number = random.randrange(1, 10)
    else:
        first_number = random.randrange(10, 100)
        second_number = random.randrange(10, 100)

    return first_number, second_number


def printing_messages(type_of_answer):
    randomizer_for_answer = random.randrange(0, 3)

    positive_answers = ['Very Good!', 'Nice Work!', 'Keep up the Good Work!']
    negative_answers = ['No. Please try again!', 'Wrong. Try once more!', 'No. Keep trying!']

    if type_of_answer == 1:
        return positive_answers[randomizer_for_answer]
    else:
        return negative_answers[randomizer_for_answer]


def check_validity_dif_type(given_answer, type_of_selection):
    for_checking = ''
    processed_answer = ''

    try:
        processed_answer = int(given_answer)
    except ValueError:
        for_checking = 'error'

    if (for_checking == 'error' or not 0 <= processed_answer - 1 <= 3) and type_of_selection == 0:
        print(f"\n{' ' * 9}\033[1;31m ERROR\033[0m Please use a value between 1 and 4 to the choose type of operation")
    elif (for_checking == 'error' or not 0 <= processed_answer - 1 <= 1) and type_of_selection == 1:
        print(f"\n{' ' * 9}\033[1;31m ERROR\033[0m Please use a value between 1 and 2 for choosing difficulty level")
    else:
        return processed_answer - 1

    os.system('sleep 1.5')

    return 'failed'


def choose_operation():
    type_of_problems = [('addition', '+'), ('subtraction', '-'), ('multiplication', "*"), ('division', '/')]
    number_of_operation = ''

    while isinstance(number_of_operation, str):
        os.system('clear')
        print_header('Ask a Math Question')
        print(f"{' ' * 6}* Please select the type of arithmetic operation to study.\n")

        for i in range(len(type_of_problems)):
            print(f"{' ' * 9}[{i + 1}] {type_of_problems[i][0]} (\"{type_of_problems[i][1]}\")")

        print(f"\n{' ' * 6}** Answer (q to quit):", end=" ")
        given_answer = input()

        if given_answer.lower()[0] == 'q':
            print(f"\n{' ' * 9}Exiting...\n")
            time.sleep(0.5)
            exit(0)

        number_of_operation = check_validity_dif_type(given_answer, 0)

    return type_of_problems[number_of_operation]


def choose_difficulty():
    list_with_difficulty = [('one digit', 1), ('two digits', 2)]
    type_of_operation = ''

    while isinstance(type_of_operation, str):
        os.system('clear')
        print_header('Ask a Math Question')
        print(f"{' ' * 6}* Please select the difficulty level of questions.\n")

        for i in range(len(list_with_difficulty)):
            print(f"{' ' * 9}[{i + 1}] {list_with_difficulty[i][0]}")

        print(f"\n{' ' * 6}** Answer (q to quit):", end=" ")
        given_answer = input()

        if given_answer.lower()[0] == 'q':
            print(f"\n{' ' * 9}Exiting..\n")
            time.sleep(0.5)
            exit(0)

        type_of_operation = check_validity_dif_type(given_answer, 1)

    return list_with_difficulty[type_of_operation]


def validate_math_answer(given_math_answer):
    error_msg = 0
    processed_answer = ''

    try:
        processed_answer = int(given_math_answer)
    except ValueError:
        try:
            processed_answer = float(given_math_answer)
        except ValueError:
            error_msg = 1

    if error_msg == 1:
        print(f"\n{' ' * 9}\033[1;31m ERROR \033[0m Please use only integers or float type for answering.")
        os.system('sleep 1')
        processed_answer = 'error'

    return processed_answer


def check_arithmetic_answers(nr_1, nr_2, operation_type, answer_to_question):
    results_after_math = [('+', (nr_1 + nr_2)), ('-', (nr_1 - nr_2)), ('/', (nr_1 / nr_2)), ('*', (nr_1 * nr_2))]

    if answer_to_question.lower()[0] == 's':
        print(f"\n{' ' * 9}\033[1;31m FAILED \033[0m Skip this question....")
        os.system('sleep 1')
        return 1

    answer_to_question = validate_math_answer(answer_to_question)

    if isinstance(answer_to_question, int) or isinstance(answer_to_question, float):
        for i in range(len(results_after_math)):
            if results_after_math[i][0] == operation_type and results_after_math[i][1] == answer_to_question:
                print(f"\n{' ' * 9}\033[1;32m SUCCESS \033[0m {printing_messages(1)}")
                os.system('sleep 1')
                return 1
            elif results_after_math[i][0] == operation_type and results_after_math[i][1] != answer_to_question:
                print(f"\n{' ' * 9}\033[1;31m FAILED \033[0m {printing_messages(-1)}")
                os.system('sleep 1')
                return 2


def ask_a_question(operation_type, difficulty_level):
    nr_1, nr_2 = generate_numbers_to_use(difficulty_level)
    answering_type = 2

    while answering_type == 2:
        os.system('clear')
        print_header('Ask a Math Question')
        print(f"{' ' * 6}* How much is {nr_1} {operation_type} {nr_2} (q to quit; s to skip):", end=" ")

        given_answer = input()

        if given_answer.lower()[0] == 'q':
            print(f"\n{' ' * 9}Exiting..\n")
            time.sleep(0.5)
            exit(0)

        answering_type = check_arithmetic_answers(nr_1, nr_2, operation_type, given_answer)


def main():

    while True:
        operation_in_words, operation_sign = choose_operation()
        difficulty_in_words, difficulty_digit = choose_difficulty()
        ask_a_question(operation_sign, difficulty_digit)


if __name__ == "__main__":
    main()
