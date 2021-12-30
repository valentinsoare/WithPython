#!/usr/bin/python

import os
import sys
import random
import time

correct_answers = ["Very good!", "Nice work!", "Keep up the good work!"]
wrong_answers = ["No. Please try again!", "Wrong. Try once more!", "No. Keep Trying!"]


def lines(number_of_lines):
    x = 0
    while x <= number_of_lines:
        print(f"-", end="")
        x += 1
    print()


def print_header():
    lines(70)
    print(f"\033[1m {'MATH EXERCISES':>40}\n {'*add, subtract, multiplication and divide*':>55}\n "
          f"{'[cht] (change equations), [chd] (change difficulty), [q] (quit)':>66}  \033[0m", end="\n")
    lines(70)


def print_difficulty_levels():
    print(f"\n - > Difficulty Levels: ")
    given_list = [(1, 'One digit'), (2, 'Two digits')]
    to_choose = random.randrange(3)

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
            print(f"\n \033{wrong_answers[to_choose]}\033[0m", end="\n\n")
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
            print(f"\n \033[1;31m {wrong_answers[to_choose]}\033[0m", end="\n\n")
            time.sleep(0.5)
            value_if_right = 99

    return req_answer, value_if_right


def generate_numbers(difficulty_levels):
    number1 = number2 = 0

    if difficulty_levels == 1:
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

    return answer_from_difficulty, value_to_check


def execute_operations_and_validate(numbering1, numbering2, answer, operation_given):
    operations = [(numbering1 + numbering2), (numbering1 - numbering2), (numbering1 * numbering2), ('%.1f' % (numbering1 / numbering2))]
    to_choose = random.randrange(3)
    var_to_exit = 1
    operation_given = operation_given - 1

    if (operation_given == 3 and str(operations[operation_given]).rstrip('.0') == answer) \
            or (str(operations[operation_given]) == answer):
        print(f"\n\033[1;32m {correct_answers[to_choose]}\033[0m", end="\n")
        var_to_exit = 0
        time.sleep(0.5)
        return var_to_exit

    print(f"\n\033[1;31m {wrong_answers[to_choose]}\033[0m", end="\n\n")
    time.sleep(0.5)

    return var_to_exit


def ask_questions(nrm1, nrm2, oper_type):
    oper_type = oper_type - 1
    operations = ["+", "-", "*", "/"]
    print(f"\n - > How much is {nrm1} {operations[oper_type]} {nrm2} ?", end="\n\n")
    answer = input(" -- > Answer (q, chd, cht): ")
    swap_answer = answer
    to_choose = random.randrange(3)

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
                print(f"\n\033[1;31m {wrong_answers[to_choose]}\033[0m", end="\n\n")
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
    to_choose = random.randrange(3)

    print(f"\n - > Select Equation: ", end="\n\n")

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
            print(f"\n \033[1;31m {wrong_answers[to_choose]}\033[0m", end="\n\n")
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
            print(f"\n \033[1;31m {wrong_answers[to_choose]}\033[0m", end="\n\n")
            time.sleep(0.5)

    return answer, value_if_ok


def execute_print_operations():
    value = 0
    answering = 0

    while value != 1 and value != 3:
        os.system('clear')
        print_header()
        answering, value = print_operations()

    return answering, value


def exec_oper_diff(select_o, select_d, var_to_select=0):
    value_operations = value_difficulty = 100
    type_of_operation = return_difficulty = ''

    while value_operations + value_difficulty != 2:
        if select_o == 1:
            type_of_operation, value_operations = execute_print_operations()
            if var_to_select == 1:
                return type_of_operation, value_operations

        if value_operations + value_difficulty == 2:
            break

        if select_d == 1:
            return_difficulty, value_difficulty = execute_difficulty()
            if var_to_select == 1:
                return return_difficulty, value_difficulty

    return type_of_operation, value_operations, return_difficulty, value_difficulty


def generate_answering(answering):
    operation = difficulty = operations_value = difficulty_value = 'default'

    while isinstance(operation, str) and isinstance(difficulty, str):
        if answering == 'chd':
            difficulty, difficulty_value = exec_oper_diff(0, 1, 1)
            if difficulty == 'cht':
                answering = 'cht'
            else:
                operation, operations_value = exec_oper_diff(1, 0, 1)
        elif answering == 'cht':
            operation, operations_value = exec_oper_diff(1, 0, 1)
            if operation == 'chd':
                answering = 'chd'
            else:
                difficulty, difficulty_value = exec_oper_diff(0, 1, 1)
        else:
            operation, operations_value, difficulty, difficulty_value = exec_oper_diff(1, 1)

    return operation, operations_value, difficulty, difficulty_value


def main():
    nr1 = nr2 = val_to_exit = answering = 0

    while True:
        operation, operations_value, difficulty, difficulty_value = generate_answering(answering)
        while operations_value + difficulty_value == 2:

            if val_to_exit == 0:
                nr1, nr2 = generate_numbers(difficulty)

            answering = execute_questions(nr1, nr2, operation)

            if answering == 'chd' or answering == 'cht':
                break
            else:
                val_to_exit = execute_operations_and_validate(nr1, nr2, answering, operation)


main()
