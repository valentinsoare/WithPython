#!/usr/bin/python

import os
import sys
import random
import time


def lines(number_of_lines):
    x = 0
    while x <= number_of_lines:
        print(f"-", end="")
        x += 1
    print()


def print_header():
    lines(60)
    print(f"\033[1m {'MATH EXERCISES':>35} \033[0m", end="\n")
    lines(60)


def print_difficulty_levels():
    print(f"\n - > Difficulty Levels: ")
    given_list = [(1, 'One digit'), (2, 'Two digits')]

    print()
    for i in given_list:
        print(f"{i[0]:>3} - {i[1]}")

    print("\n\n - > Answer (q, cht):", end=" ")
    req_answer = input()

    try:
        req_answer = int(req_answer)
        if req_answer in (1, 2):
            value_if_right = 1
        else:
            print(f"\n \033[1;31m Wrong answer !!!\033[0m", end="\n\n")
            time.sleep(0.5)
            value_if_right = 99
    except ValueError:
        req_answer = req_answer.lower()
        if req_answer == "q":
            print(f"\n\033[1;36m :( Quitting...\033[0m", end="\n\n")
            time.sleep(0.5)
            sys.exit(0)
        elif req_answer == 'cht':
            value_if_right = 1
        else:
            print(f"\n\033[1;31m Wrong answer !!!\033[0m", end="\n\n")
            time.sleep(0.5)
            value_if_right = 99

    return req_answer, value_if_right


def generate_numbers(difficulty_levels):
    number1 = number2 = 0

    if 1 == difficulty_levels:
        number1 = random.randrange(1, 10)
        number2 = random.randrange(1, 10)
    elif difficulty_levels == 2:
        number1 = random.randrange(10, 100)
        number2 = random.randrange(10, 100)

    return number1, number2


def execute_difficulty():
    print_header()
    answer_from_difficulty = 0
    value_to_check = 0

    while value_to_check != 1:
        os.system('clear')
        print_header()
        answer_from_difficulty, value_to_check = print_difficulty_levels()

    return answer_from_difficulty


#def execute_operations_and_validate(numbering1, numbering2, type):
#    operations = [(numbering1 + numbering2), (numbering1 - numbering2), (numbering1 * numbering2), (numbering1 / numbering2)]


def ask_questions(nrm1, nrm2, oper_type):
    oper_type = oper_type - 1
    operations = ["+", "-", "*", "/"]
    print(f"\n - > How much is {nrm1} {operations[oper_type]} {nrm2} ?", end="\n\n")
    answer = input(" -- > Answer (q, chd, cht): ")
    swap_answer = answer

    try:
        swap_answer = int(swap_answer.lstrip('-'))
        operation_to_exit = 1
    except ValueError:
        try:
            swap_answer = float(swap_answer.lstrip('-'))
            operation_to_exit = 1
        except ValueError:
            swap_answer = swap_answer.lower()
            if swap_answer == 'q':
                print(f"\n\033[1;36m :( Quitting...\033[0m", end="\n\n")
                time.sleep(0.5)
                sys.exit(0)
            elif swap_answer == 'chd':
                operation_to_exit = 1
            else:
                print(f"\n\033[1;31m Wrong answer !!!\033[0m", end="\n\n")
                time.sleep(0.5)
                operation_to_exit = 99

    return answer, operation_to_exit


def execute_questions(numbering1, numbering2, type_of_o):
    value = 0
    answr = 0

    while value != 1:
        os.system('clear')
        print_header()
        answr, value = ask_questions(numbering1, numbering2, type_of_o)

    return answr


def main():
    count_answers = 0
    return_difficulty = execute_difficulty()

    while count_answers <= 20:
        nr1, nr2 = generate_numbers(return_difficulty)
        answering = execute_questions(nr1, nr2, 2)
        equation = nr1 - nr2

        if str(equation) == answering:
            print("\n Right answer !!", end="\n")
            time.sleep(0.5)
            count_answers += 1
        else:
            print(f"\n Wrong answer!!", end="\n")
            time.sleep(0.5)


main()

