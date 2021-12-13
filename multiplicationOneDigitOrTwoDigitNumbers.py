#!/usr/bin/python

import random


def printing_header(number_of_lines):
    print(f"\033[1m", end="")

    for i in range(number_of_lines):
        print(f"-", end="")

    print(f"\033[0m", end="\n")


def generate_numbers(numbers_type=1):
    number_1 = 1
    number_2 = 1

    if numbers_type == 1:
        number_1 = random.randrange(1, 10)
        number_2 = random.randrange(1, 10)
    elif numbers_type == 2:
        number_1 = random.randrange(10, 100)
        number_2 = random.randrange(10, 100)

    return number_1, number_2


def printing_question_and_catch_answer(nr1, nr2):
    print(f" \033[1m- > How much is {nr1} * {nr2} ?\033[0m", end="\n")
    answer = int(input(" \033[1m-- > Answer: \033[0m"))

    return answer


def validate_answer(answr, n1, n2):
    output_var = 0
    to_g = 0

    if answr == n1 * n2:
        output_var = 1
        to_g = 1
        print(f"\n\t\033[1;32mVery good!!\033[0m", end="\n")
    else:
        print(f"\n\t\033[1;31mNo. Please try again!!\033[0m", end="\n")
        printing_header(60)

    return output_var, to_g


def main():
    if_right = 0
    to_gen = 1
    print(f"\n\t\t\033[1;34m*** Math Questions V2 ***\033[0m")
    printing_header(60)

    while if_right == 0:
        if to_gen == 1:
            num1, num2 = generate_numbers(1)

        answr = printing_question_and_catch_answer(num1, num2)
        if_right, to_gen = validate_answer(answr, num1, num2)

    printing_header(60)
    print()

main()

