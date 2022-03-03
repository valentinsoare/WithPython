#!/usr/bin/python

import re
import csv
import json
from sys import exit
from os import system
from time import sleep
from statistics import mean


def to_quit(input_var):
    if input_var.lower()[0] == 'q':
        print(f'\n\033[1;33m{"Quitting...":>18}\033[0m', end="\n\n")
        sleep(1)
        exit(0)


def catch_input_text(header):
    system('clear')
    print(header)

    print(f' \n{"- > Enter the name of the text file(.txt)/csv file (.csv) with grades that we need to read (q to quit):"}', end=" ")
    name_of_file = input()

    if not name_of_file:
        return name_of_file

    to_quit(name_of_file)

    return name_of_file


def reading_the_file_txt(given_file):
    student_name = ''
    var_to_continue = 0
    dict_with_names_grades = {}

    try:
        opening_file = open(given_file, mode='r')
    except FileNotFoundError:
        print(f'\n\033[1;31m{"ERROR - file not found":>30}\033[0m\n')
        sleep(1)

        return dict_with_names_grades, var_to_continue

    with opening_file:
        entire_text = opening_file.readlines()

        for line in entire_text:
            list_with_lines = line.split()

            if len(list_with_lines) == 1 and re.search(r'[A-Za-z][a-z]{1,}', list_with_lines[0]) and list_with_lines[0].isalpha():
                student_name = list_with_lines[0]
                dict_with_names_grades[student_name] = {}
            elif len(list_with_lines) == 2 and re.search(r'[A-Za-z][a-z]{1,}', list_with_lines[0]) and re.search(r'[A-Za-z][a-z]{1,}', list_with_lines[1])\
                    and list_with_lines[0].isalpha() and list_with_lines[1].isalpha():
                student_name = ' '.join([list_with_lines[0], list_with_lines[1]])
                dict_with_names_grades[student_name] = {}

            if len(list_with_lines) >= 2 and re.search(r'[A-Za-z][a-z]{1,}', list_with_lines[0]) and list_with_lines[1].isnumeric():
                dict_with_names_grades[student_name].update({list_with_lines[0]: [list_with_lines[i] for i in range(1, len(list_with_lines))]})

    var_to_continue = 1

    return dict_with_names_grades, var_to_continue


def reading_the_file_csv(given_file):
    var_to_continue = 0
    dict_with_grades = {}

    try:
        open_file = open(given_file, mode='r', newline='')
    except FileNotFoundError:
        print(f'\n\033[1;31m{"ERROR - file not found":>30}\033[0m\n')
        sleep(1)

        return dict_with_grades, var_to_continue

    with open_file:
        reading = csv.reader(open_file)

        for line in reading:
            if line[0] not in dict_with_grades:
                dict_with_grades[line[0]] = {}

            if line[0] in dict_with_grades:
                dict_with_grades[line[0]].update({line[1]: [line[item] for item in range(2, len(line))]})

    var_to_continue = 1

    return dict_with_grades, var_to_continue


def reading_the_file_json(given_file):
    var_to_continue = 0
    dict_with_grades = {}

    try:
        open_file = open(given_file, mode='r', newline='')
    except FileNotFoundError:
        print(f'\n\033[1;31m{"ERROR - file not found":>30}\033[0m\n')
        sleep(1)

        return dict_with_grades, var_to_continue

    with open_file:
        reading_file = json.load(open_file)
        print(reading_file)
        for i in reading_file.values():
            for k in i:
                dict_with_grades[''.join(k.keys())] = {x: y for i in k.values() for x, y in i.items()}

    var_to_continue = 1

    return dict_with_grades, var_to_continue


def statistics_on_grades(header, dict_with_courses_grades):
    average_per_class = {}
    system('clear')
    print(header)

    print(f'\n - > Statistics for students on the given courses:')
    for student, courses_grades in dict_with_courses_grades.items():
        print(f'{"*":>7}{student}:')
        for course, grades in courses_grades.items():
            print(f'{"Course:":>18} {course}', end="\n")
            grades_string = ' '.join(grades)
            grades = [float(i) for i in grades]
            print(f'{"Grades: ":>19}{grades_string}\n{"Count:":>17} {len(grades)}, Average: {mean(grades):.2f}\n')

            if course not in average_per_class:
                average_per_class[course] = []

            if course in average_per_class:
                average_per_class[course] += grades

    for courses, all_grades in average_per_class.items():
        print(f'{"*Class:":>12} {courses}, Average: {mean(all_grades):.2f}')

    print()


def main():
    to_continue = 0
    dict_students_grades = {}
    header = f'\n\033[1m{"-" * 35:>58}\n{"**GRADES BOOK**":>48}\n{"-" * 35:>58}\033[0m'

    while to_continue == 0:
        name_of_given_file = catch_input_text(header)

        if re.search(r'\.txt$', name_of_given_file):
            dict_students_grades, to_continue = reading_the_file_txt(name_of_given_file)
        elif re.search(r'\.csv$', name_of_given_file):
            dict_students_grades, to_continue = reading_the_file_csv(name_of_given_file)
        elif re.search(r'\.json$', name_of_given_file):
            dict_students_grades, to_continue = reading_the_file_json(name_of_given_file)

    statistics_on_grades(header, dict_students_grades)


main()
