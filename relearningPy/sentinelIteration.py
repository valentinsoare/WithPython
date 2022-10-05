#!/usr/bin/python

""" Script where we calculate average for a student. Also here we have a sentinel in
iterations when we take input from the user. Also several functions and one of them is returning two values"""

import os


def take_input_and_calculate(counter_grades, count, sum_of_all_grades, list_with_grades):
    print(f'\n\t===Math course===', end="\n\n")

    while True:
        print(f'{count}. Enter grade (-1 to end):', end=" ")
        grade = input()

        if grade == "-1":
            print(f'\n - > Stop taking grades....')
            os.system('sleep 1')
            break

        try:
            grade = int(grade)
        except ValueError:
            try:
                grade = float(grade)
            except ValueError:
                print(f'\n - > ERROR you need to enter an integer or float!\n')
                os.system('sleep 1')
                continue

        counter_grades += 1
        count += 1
        list_with_grades.append(grade)
        sum_of_all_grades += grade

    return counter_grades, sum_of_all_grades, list_with_grades


def decide_what_to_do(sum_of_all_grades, counter_grades, grades_list):
    if sum_of_all_grades == 0:
        print(f'\n ** Error no grades were entered!')
    else:
        print(f'\n * We have the following grades: {grades_list}')
        print(f' ** Average for Math: {sum_of_all_grades/counter_grades:.2f}\n')


def main():
    counter_grades, sum_of_all_grades, list_grades = take_input_and_calculate(0, 1, 0, [])
    decide_what_to_do(sum_of_all_grades, counter_grades, list_grades)


if __name__ == "__main__":
    main()
