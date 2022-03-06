#!/usr/bin/python

import csv
from time import sleep
from os import system, path
from statistics import mean


def catch_text():
    parsable_text = ''
    var_continue = 0

    while var_continue == 0:
        system('clear')
        print(f'\n{" - > Enter the csv to parse (q to quit):"}\033[0m', end=" ")
        parsable_text = input()

        if parsable_text.lower()[0] == 'q':
            print(f'\n\033[31m{"Exiting...":>17}\33[0m', end="\n\n")
            sleep(1)
            exit(0)
        elif not path.exists(parsable_text):
            print(f'\n\033[31m{"ERROR - file does not exists.":>35}\033[0m', end="\n\n")
            sleep(1.5)
            continue

        var_continue = 1

    return parsable_text


def open_files_as_csv_and_parse_it(given_file):
    file_csv_open = open(given_file, mode='r', newline='')
    students_age = {}

    with file_csv_open:
        dict_from_csv = csv.DictReader(file_csv_open)
        for student_line in dict_from_csv:
            line, name, pc_class, age, sex, survived, sexcode = student_line.items()
            if age[1].isnumeric():
                students_age[name[1]] = age[1]

    return students_age


def calculate_average_age(dict_with_names_age):
    values_age = dict_with_names_age.values()

    average_age = mean(map(lambda i: int(i), values_age))
    counting_individuals = len(values_age)

    return average_age, counting_individuals


def printing_output(average_age, counting_individuals):
    print(f'\n *We have {counting_individuals} names in the dataset that have a valid age input value.')
    print(f' **Average age on all individuals from the dataset with mention valid age: {average_age:.2f}\n')


def main():
    csv_to_check = catch_text()
    dict_with_numeric_age = open_files_as_csv_and_parse_it(csv_to_check)
    average_age, counting_persons = calculate_average_age(dict_with_numeric_age)

    printing_output(average_age, counting_persons)


main()
