#!/usr/bin/python

import random
import os


def printing_header(number_of_lines):
    print(f"\033[1m", end="")
    x = 0

    while x <= number_of_lines:
        print(f"-", end="")
        x += 1

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


#def printing_operations():
#    print(f"\n Select one of this operations [1-4]: ", end="\n")
#    operations = [(1, "Adding"), (2, "Subtract"), (3, "Multiplication"), (4, "Divide")]
#    var_to_return = 1

#    for i in operations:
#        print(f"{i[0]} - > {i[1]}")

#    answer = input("\n \033[1m - > Answer: [1-4] \033[0m")

#    try:
#        if answer.lstrip().isdigit():
#            var_to_return = 0
#            return int(answer), var_to_return
#    except ValueError:
#        if answer == "q":
#            print(f"\n\033[1m:( Quitting...\033[0m", end="\n\n")
#        elif answer == "c":
#            print(f"\n\033[1m Continue...\033[0m", end="\n\n")
#            var_to_return = 1
#        else:
#            print(f" \033[1;31m Wrong choice !!", end="\n\n")

#   return answer, var_to_return


def printing_question_and_catch_answer(nr1, nr2):
    opers = ["+", "-", "*", "/"]
    print(f" \033[1m- > How much is {nr1} {opers[1]} {nr2} ?\033[0m", end="\n")
    answer = input(" \033[1m-- > Answer: \033[0m")

    to_good = answer
    answer = answer.lstrip("-")

    if answer.isdigit():
        return to_good
    elif answer == 'q':
        print(f"\n\033[1m:( Quitting...\033[0m", end="\n\n")
    elif answer == 'c':
        print(f"\n\033[1m Continue...\033[0m", end="\n\n")
    else:
        try:
            answer = float(answer)
            answer = str(answer)
        except ValueError:
            answer = answer.lower()

    return answer


def validate_answer(answr, n1, n2):
    output_var = 0
    given_operations = [(n1 + n2), (n1 - n2), (n1 * n2), float('%.1f' % (n1 / n2))]

    for i in given_operations:
        if str(i) == answr:
            output_var = 'c'
            to_g = 1
            print(f"\n\t\033[1;32mVery good!!\033[0m", end="\n\n")
            return output_var, to_g

    if answr == "c":
        to_g = 1
        output_var = "c"
    elif answr == "q":
        output_var = "q"
        to_g = 0
    else:
        print(f"\n\033[1;31m Wrong answer!! Try again!!\033[0m", end="\n\n")
        to_g = 0

    return output_var, to_g


def main():
    if_right = ''
    to_gen = 1
    num1 = 0
    num2 = 0

    while if_right != "q":
        os.system('clear')
        print(f"\n\t\t\033[1;34m*** Math Questions V2 ***\033[0m")
        printing_header(60)

        if to_gen == 1:
            num1, num2 = generate_numbers(1)

        answr = printing_question_and_catch_answer(num1, num2)
        if_right, to_gen = validate_answer(answr, num1, num2)
        os.system('sleep 0.5')

    printing_header(60)
    print()


main()
