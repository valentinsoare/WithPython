#!/usr/bin/python

import os
from decimal import Decimal
import statistics


# Task 3.6

# def check_answers(given_answer, list_with_answers):
#    if not given_answer.isalpha():
#        print(f'\n\tERROR - only letters.\n')
#        return 1, "error"
#    elif given_answer.lower() != 'yes' and given_answer.lower() != 'no':
#        return 2, "error"
#    else:
#        if given_answer.lower() == 'yes':
#            return 0, list_with_answers[0]
#        elif given_answer.lower() == 'no':
#            return 0, list_with_answers[1]


# def ask_the_question():
#    initial_question = "What is your problem ?"
#    after_initial_question = "Have you had this problem before (yes or no) ?"
#    answer_yes = "Well, you have it again."
#    answer_no = "Well, you have it now."

#    list_with_questions = [initial_question, after_initial_question]
#    list_with_answers = [answer_yes, answer_no]
#    length_questions = len(list_with_questions)

#    i = 0
#    while i < length_questions:
#        print(f' - > {list_with_questions[i]}', end=" ")
#        given_answer = input()

#        type_of_return, returned_answer = check_answers(given_answer, list_with_answers)

#        if type_of_return == 1:
#            continue
#        elif type_of_return == 2:
#            pass
#        elif type_of_return == 0 and i == 1:
#            print(f'\n ** {returned_answer}')

#        i += 1

def execute_code():
    # grade = 93

    # if grade >= 90:
    #    result = f'\033[1;31m** Passed with A\033[0m'
    # elif grade >= 80:
    #    result = f'** Passed with B'
    # elif grade >= 70:
    #    result = f'** Passed with C'
    # else:
    #    result = f'** Failed, try again!'

    # print(result)

    # second_result = ('Passed' if grade >= 70 else 'Failed')
    # print(second_result)

    # ---------------------------------------------------------
    # steps = 0
    # product = 3

    # while product < 50:
    #    product *= 3
    #    steps += 1

    # print(f'Product: {product} in {steps} steps.')

    # --------------------------------------------------------

    # number = 7
    # power = 1

    # while number < 1000:
    #    number = 7 ** power
    #    power += 1

    # print(f'Power of seven greater than 1000: {number}, 7 at {power}')

    # ----------------------------------------------------------

    # dash = "-"
    # string_to_print = f"Dati GOOOOOOOL Romania!"
    # list_with_letters = []

    # print(f"{dash * 68}")

    # for chrt in string_to_print:
    #    print(f"{chrt}", end="  ")
    #    list_with_letters.append(chrt)

    # to_print = "".join(list_with_letters)

    # print(f"\n{dash * 68}")
    # print(f"{to_print}!!")

    # total = 0
    # for i in [4, 10, 23, 1101, 77, -1000]:
    #    total += i

    # print(f'\nTotal: {total}')

    # for j in range(0, 20, 3):
    #    print(f'{j}', end=" ")

    # print(f'\n')
    # for k in range(-20, 0, 2):
    #    print(k, end=" ")

    # print(f'\n')
    # for z in range(1000, 0, -100):
    #    print(f'{z}', end=" ")

    # ---------------------------------------------------------

    # total = 0
    # for i in range(0, 1_000_001):
    #    total += i

    # print(f'Total up to one million: {total}')

    # x = 12
    # print(x ** 2)
    # print(x**(1/2))

    # --------------------------------------------------------
    # sum_of_grades = 0
    # number_of_grades = 0
    # student = 'Laura X-ulescu'
    # list_of_grades = [10, 8, 6, 2, 7, 9, 4, 10, 7, 9, 8, 10, 9, 8, 6, 2, 10, 8]

    # for i in list_of_grades:
    #    sum_of_grades += i
    #    number_of_grades += 1

    # print(f' - > Student: {student} with an average of {sum_of_grades/number_of_grades:.2f}')

    # ---------------------------------------------------------

    # first_number = 2345
    # second_number = 235
    # print(f'{first_number / second_number:.2f}')

    # ---------------------------------------------------------=

    # counter_grades = 0
    # count = 1
    # sum_of_all_grades = 0
    # list_with_grades = []

    # print(f'\n\t===Math course===', end="\n\n")

    # while True:
    #    print(f'{count}. Enter grade (-1 to end):', end=" ")
    #    grade = input()

    #    if grade == "-1":
    #        print(f'\n - > Stop taking grades....')
    #        os.system('sleep 1')
    #        break

    #    try:
    #        grade = int(grade)
    #    except ValueError:
    #        try:
    #            grade = float(grade)
    #        except ValueError:
    #            print(f'\n - > ERROR you need to enter an integer or float!\n')
    #            os.system('sleep 1')
    #            continue

    #    counter_grades += 1
    #    count += 1
    #    list_with_grades.append(grade)
    #    sum_of_all_grades += grade

    # if sum_of_all_grades == 0:
    #    print(f'\n ** Error no grades were entered!')
    # else:
    #    print(f'\n ** Average for Math: {sum_of_all_grades/counter_grades:.2f}')

    # --------------------------------------------------------------
    # print(f'AIUREA')

    # for i in range(10, -2, -2):
    #    print(f'{i}', sep="/ ", end=" ")

    # -----------------------------------------------------------------

    # for i in range(99, -1, -11):
    #    print(f'{i}', end=" ")

    # suma = 0
    # for i in range(2, 101, 2):
    #    suma += i

    # print(f'\nSum of even integers: {suma}')

    # -----------------------------------------------------------------

    # given_number = 4.21
    # print(f'{given_number:.21f}')
    # print(f'{given_number:.2f}')

    # cool_number = Decimal('21.4231334')
    # print(f'{cool_number:.21f}')

    # rate = Decimal('0.05')
    # x = Decimal('12.5')
    # y = Decimal('4')

    # print(f'{(x + y) * rate:.4f}')

    # ------------------------------------------------------------------

    # tax_bill = Decimal('0.0625')
    # bill_amount = Decimal('37.45')

    # only_tax = tax_bill * bill_amount
    # calculate_final = only_tax + bill_amount

    # print(f'Final Bill: {calculate_final:.2f}$')

    # ------------------------------------------------------------------
    # age = 36
    # name = 'Valentin'

    # if isinstance(name, str) and age >= 30:
    #    print(f' - > WoW')

    # ------------------------------------------------------------------

    # given_grades = [85, 93, 45, 89, 85, 33, 89, 83, 67]

    # list_length = len(given_grades)
    # sum_of_grades = sum(given_grades)

    # print(f'\n - > Average of those grades: {sum_of_grades/list_length:.1f}')
    # print(f' - > Median: {statistics.median(given_grades)}')
    # print(f' - > Mode: {statistics.mode(given_grades)}')

    # ----------------------------------
    # ================Tasks for chapter 3===================

    # Task 3.7

    #print(f"number\tsquare\tcube")
    #for i in range(6):
    #    print(f'{i:>6}{i ** 2:>8}{i ** 3:>6}')

    #-------------------------------------------------------

    #Task 3.8
    #print(4 % 10)

    #-------------------------------------------------------

    

def main():
    # ask_the_question()
    execute_code()


if __name__ == "__main__":
    main()
