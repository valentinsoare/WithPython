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
    #lines(60)
    print(f"\033[1m {'MATH EXERCISES':>35} \033[0m", end="\n")
    print(f"\033[1m {'*add, subtract, multiplication and divide*':>49} \033[0m", end="\n")
    print(f"\033[1m {'[cht] (change operations), [chd] (change difficulty)':>54} \033[0m", end="\n")
    #lines(60)


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
            value_if_right = 2
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

    while value_to_check != 1 and value_to_check != 2:
        os.system('clear')
        print_header()
        answer_from_difficulty, value_to_check = print_difficulty_levels()

    return answer_from_difficulty


def execute_operations_and_validate(numbering1, numbering2, answer):
    operations = [(numbering1 + numbering2), (numbering1 - numbering2), (numbering1 * numbering2), ('%.1f' % (numbering1 / numbering2))]
    var_to_exit = 1

    for i in range(len(operations)):
        if (i == 3 and str(operations[i]).rstrip('.0') == answer) or (str(operations[i]) == answer):
            print(f"\033\n[1;32m Right answer, keep it going !!\033[0m", end="\n")
            var_to_exit = 0
            time.sleep(0.5)
            return var_to_exit

    print(f"\n\033[1;31m Wrong answer !!!\033[0m", end="\n\n")
    time.sleep(0.5)

    return var_to_exit


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
                operation_to_exit = 3
            elif swap_answer == 'cht':
                operation_to_exit = 2
            else:
                print(f"\n\033[1;31m Wrong answer !!!\033[0m", end="\n\n")
                time.sleep(0.5)
                operation_to_exit = 99

    return answer, operation_to_exit


def execute_questions(numbering1, numbering2, type_of_o):
    value = 0
    answr = 0

    while value != 1 and value != 3 and value != 2:
        os.system('clear')
        print_header()
        answr, value = ask_questions(numbering1, numbering2, type_of_o)

    return answr


def print_operations():
    given_operations = [(1, "Add"), (2, "Subtract"), (3, "Multiply"), (4, "Divide")]
    value_if_ok = 0

    print(f"\n - > Select Operations: ", end="\n\n")

    for i in given_operations:
        print(f"  {i[0]} - {i[1]}")

    print(f"\n\n - > Answer (q, chd): ", end="")
    answer = input()

    try:
        answer = int(answer)

        if 1 <= answer <= 4:
            value_if_ok = 1
            return answer, value_if_ok
        else:
            print(f"\n \033[1;31m Wrong answer !!!\033[0m", end="\n\n")
            time.sleep(0.5)
    except ValueError:
        answer = answer.lower()

        if answer == "q":
            print(f"\n\033[1;36m :( Quitting...\033[0m", end="\n\n")
            time.sleep(0.5)
            sys.exit(0)
        elif answer == "chd":
            value_if_ok = 3
        else:
            print(f"\n \033[1;31m Wrong answer !!!\033[0m", end="\n\n")
            time.sleep(0.5)

    return answer, value_if_ok


def execute_print_operations():
    value = 0
    answering = 0

    while value != 1 and value != 3:
        os.system('clear')
        print_header()
        answering, value = print_operations()

    return answering


def main():
    val_to_exit = 0
    return_difficulty = ''
    type_of_o = ''
    nr1 = 0
    nr2 = 0

    while True:
        if not isinstance(type_of_o, int):
            type_of_o = execute_print_operations()
            swap_type_o = type_of_o

        if not isinstance(return_difficulty, int):
            return_difficulty = execute_difficulty()
            if return_difficulty == 'cht':
                type_of_o = ''
                continue

        if val_to_exit == 0:
            nr1, nr2 = generate_numbers(return_difficulty)

        answering = execute_questions(nr1, nr2, swap_type_o)

        if answering == 'chd':
            return_difficulty = ''
        elif answering == 'cht':
            type_of_o = ''
        else:
            val_to_exit = execute_operations_and_validate(nr1, nr2, answering)


main()

