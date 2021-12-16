#!/usr/bin/python

import os
import sys
import random


def generate_numbers(difficulty_level=1):
    if difficulty_level == 1:
        number1 = random.randrange(1, 10)
        number2 = random.randrange(1, 10)
    else:
        number1 = random.randrange(10, 100)
        number2 = random.randrange(10, 100)

    return number1, number2


def printing_line(number_of_lines):
    x = 0
    while x <= number_of_lines:
        print(f"\033[1m=\033[0m", end="")
        x += 1
    print()

def generate_questions_and_answers(nr1, nr2, type_of_operation):
    return_value = 0
    answer_catch = ""
    type_of_operation = type_of_operation - 1
    given_operations = ["+", "-", "*", "/"]
    processed_operations = [(nr1 + nr2), (nr1 - nr2), (nr1 * nr2), float('%.1f' % (nr1 / nr2))]
    print(f"\n - > How much is {nr1} {given_operations[type_of_operation]} {nr2} ?")
    print(f" -- > Answer (chd, cho, q):", end=" ")
    answering = input()

    if answering.lower() in ("chd", "cho", "q"):
        answer_catch = answering
    elif answering.lstrip("-").isdigit():
        try:
            answering = int(answering)
        except ValueError:
            answering = float(answering)

        proper_answer = processed_operations[type_of_operation]

        if proper_answer == answering:
            answer_catch = answering
        else:
            return_value = 1
            answer_catch = answering
    else:
        return_value = 1

    return return_value, answer_catch


def printing_type_of_operations():
    given_operations = [(1, "Addition"), (2, "Subtraction"), (3, "Multiplication"), (4, "Division")]
    print(f"***Select one of this math operations: ", end="\n\n")
    given_error = 0
    for i in given_operations:
        print(f"{i[0]} - > {i[1]}")

    print(f"\n -- > Answer (chd, q):", end=" ")
    operation = input()

    if operation.isdigit() and (1 <= int(operation) <= 4):
        operation = int(operation)
    elif operation.lower() in ("chd", "q"):
        operation = operation.lower()
    else:
        given_error = 1

    return operation, given_error


def header_prt():
    name_of_script = "Math Questions"
    addition_information = "(multiplication, adding, subtract and divide)"
    explination = "chd (Difficulty level), cho (Type of operations), q (Quit)"
    os.system('clear')
    print(f"\n{name_of_script:>40}\n{addition_information:>56}")
    print(f"{explination:>63}")
    #printing_line(70)

    operating, erroring = printing_type_of_operations()

    if operating == "q" and erroring == 0:
        print(f"\n:( Quiting", end="\n\n")
    elif erroring == 1:
        print(f"\nWrong choice. Try one more time!", end="\n")
        os.system('sleep 0.5')
    elif operating == "chd":
        operating = operating.lower()

    return operating, erroring


def choose_difficulty_level():
    name_of_script = "Math Questions"
    addition_information = "(One digit numbers, Two digits numbers)"
    given_difficulty_levels = [(1, "One digit numbers"), (2, "Two digits numbers")]
    exit_success = 0
    os.system('clear')
    print(f"\n{name_of_script:>46}\n{addition_information:>54}")
    #printing_line(70)

    for i in given_difficulty_levels:
        print(f"{i[0]} - > {i[1]}")

    print(f"\n -- > Answer (cho, q):", end=" ")
    req_difficulty_level = input()

    if req_difficulty_level.isdigit():
        try:
            req_difficulty_level = int(req_difficulty_level)
        except ValueError:
            exit_success = 1
            print(f":( Wrong choice. Please try again.")
    elif req_difficulty_level.lower() in ("cho", "q"):
        req_difficulty_level = req_difficulty_level.lower()
    else:
        exit_success = 1

    return req_difficulty_level, exit_success


def printing_success_failure_messages(type_of_messages=0):
    given_success_messages = ['Very good!', 'Nice work!', ' Keep up the good work!']
    given_failure_messages = ['No. Please try again.', 'Wrong. Try once more.', 'No. Keep trying.']

    choose_message = random.randrange(3)

    if type_of_messages == 0:
        print(f" {given_success_messages[choose_message]}")
    elif type_of_messages == 1:
        print(f"{given_failure_messages[choose_message]}")


def main():
    erroring = 1

    while erroring == 1:
        operating, erroring = header_prt()

    if operating == "q":
        sys.exit(0)
    else:
        req_dif, exit_succ = choose_difficulty_level()
        if req_dif == "q" and exit_succ == 0:
            print(f"\n:( Quiting..", end="\n\n")
            sys.exit(0)

    answer_catching = operating
    if_correct_answer = 0
    numbering1 = numbering2 = ''
    print(f"\n\033[1;31m Wrong answer!! Try again!!\033[0m", end="\n\n")
    while answer_catching != "q" or req_dif != "q":

        if if_correct_answer == 0:
            numbering1, numbering2 = generate_numbers(req_dif)

        if isinstance(operating, int) or isinstance(answer_catching, str):
            if_correct_answer, answer_catching = generate_questions_and_answers(numbering1, numbering2, operating)
            if if_correct_answer == 0 and answer_catching == "cho":
                operating, erroring = header_prt()
            elif (if_correct_answer == 0 or if_correct_answer == 1) and (isinstance(answer_catching, int)
                                                                         or isinstance(answer_catching, float)):
                printing_success_failure_messages(if_correct_answer)
            elif answer_catching == "chd" and if_correct_answer == 0:
                req_dif, exit_succ = choose_difficulty_level()
            elif if_correct_answer == 0 and answer_catching == "q":
                print(f"\n:( Quiting", end="\n\n")
                sys.exit(0)

        if req_dif == "q" and exit_succ == 0:
            print(f"\n:( Quiting", end="\n\n")
            sys.exit(0)
        elif req_dif == "cho" and exit_succ == 0:
            operating, erroring = header_prt()


main()

