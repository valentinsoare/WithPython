#!/usr/bin/python

import re
from sys import exit
from os import system
from time import sleep
import pandas as pd


def to_quit(input_var):
    if input_var.lower()[0] == 'q':
        print(f'\n\033[1;33m{"Quitting...":>18}\033[0m', end="\n\n")
        sleep(1)
        exit(0)


def how_many_students(header):
    how_many = ''

    while isinstance(how_many, str):
        system('clear')
        print(header)
        print(f"\n - > Tell us how may students you have (q to quit):", end=" ")
        how_many = input()

        to_quit(how_many)

        try:
            how_many = int(how_many)
        except ValueError:
            print(f'\n\033[1;31m {"ERROR - you need to tell us how many students you have.":>64}\033[0m')
            sleep(1)

    return how_many


def name_of_the_students(number_of_students, header):
    students_name = ''

    while len(students_name) < number_of_students:
        system('clear')
        print(header)
        print(f'\n{"*We need the name of":>21} {number_of_students} {"students."}', end="\n\n")
        print(f' - > Enter the name of the students separated by a comma (q to quit):', end=" ")
        students_name = input()

        to_quit(students_name)

        if isinstance(students_name, int):
            print(f'\n\033[1;31m {"ERROR - you need to enter the name of the students in alnum characters.":>64}\033[0m', end="\n\n")
            sleep(1)

        students_name = [i.strip(' ') for i in students_name.split(sep=',')]

        if len(students_name) != number_of_students:
            print(f'\n\033[1;31m {"ERROR - We need the names of ":>35}{number_of_students} students.\033[0m', end="\n\n")
            sleep(1)

    return students_name


def catch_number_of_courses(header, students_name):
    j = 0
    dict_with_number_of_courses = {}

    system('clear')
    print(header)
    print(f' \n **We have the following students:', end=" ")

    for i in students_name:
        print(f'{i}', end=" ")

    print("\n")

    print(f' - > How many courses you want to add for (q to quit):', end="\n")
    while len(dict_with_number_of_courses.keys()) < len(students_name):
        print(f' {j + 1:>10} - {students_name[j]}:', end=" ")
        number_of_courses = input()
        to_quit(number_of_courses)

        try:
            number_of_courses = int(number_of_courses)
        except ValueError:
            print(f'\n\033[1;31m {"ERROR you need to enter an integer that represents how many courses we have for ":>83}{students_name[j]}.\033[0m', end="\n\n")
            sleep(1)
        else:
            dict_with_number_of_courses[students_name[j]] = number_of_courses
            j += 1

    return dict_with_number_of_courses


def populate_with_courses_and_grades(name_of_students, number_of_courses):
    nums = {1: "First", 2: "Second", 3: "Third", 4: "Fourth", 5: "Fifth", 6: "Sixth", 7: "Seventh", 8: "Eighth", 9: "Nineth"}
    dict_with_courses_grades = {}
    nr_courses = 0

    for i in range(len(name_of_students)):

        print(f'\n **Courses and grades for {name_of_students[i]} (ex: Math 8, 0, 10, 6) (q to quit):\n', end=" ")
        list_to_add_to_dict = []

        while nr_courses < number_of_courses[name_of_students[i]]:
            print(f'\t{nr_courses + 1}) {nums[nr_courses+1]} course:', end=" ")

            grades_courses_for_student = input()
            to_quit(grades_courses_for_student)

            grades_course_for_student = [i.removesuffix(",") for i in grades_courses_for_student.split(sep=' ')]

            if len(grades_course_for_student) > 1 and re.search(r'[A-Za-z][a-z]{1,}', grades_course_for_student[0])\
                    and grades_course_for_student[1].isnumeric():
                list_to_add_to_dict += [grades_course_for_student]
            else:
                print(f'\n\033[1;31m{"ERROR - we need at least an integer or float on mentioned course after the course name.":>90}\033[0m\n')
                continue

            if nr_courses == number_of_courses[name_of_students[i]] - 1:
                dict_with_courses_grades[name_of_students[i]] = list_to_add_to_dict

            nr_courses += 1

        nr_courses = 0

    print(dict_with_courses_grades)
    return dict_with_courses_grades


def populate_the_file_with_grades():
    file_with_grades = open('grades_file.txt', mode='w')

    list_with_students = ['Jones', 'Andreea', 'Valentin', 'Dimitri']
    dict_grades = {'Math': [['7', '8', '10', '8'], ['10', '4', '7', '9'], ['9', '10', '8', '1', '4'], ['9', '10', '7', '9']],
                   'English': [['7', '2', '9', '4'], ['10', '4', '5', '9'], ['3', '2', '10', '5', '4'], ['8', '10', '4', '9']]}

    with file_with_grades:
        for i in range(len(list_with_students)):
            file_with_grades.write(f'\n')
            file_with_grades.write(list_with_students[i])
            file_with_grades.write(f'\n')

            for j, k in dict_grades.items():
                file_with_grades.writelines([j, "  ", ' '.join(k[i]), "\n"])

            file_with_grades.write(f'\n')


def main():
    header = f'\n\033[1m{"-" * 35:>65}\n{"**GRADE BOOK**":>54}\n{"-" * 35:>65}\033[0m'

    number_of_students = how_many_students(header)
    students_list = name_of_the_students(number_of_students, header)
    number_of_courses_per_student = catch_number_of_courses(header, students_list)
    courses_and_grades = populate_with_courses_and_grades(students_list, number_of_courses_per_student)



main()

