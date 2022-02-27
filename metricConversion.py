#!/usr/bin/python3

from time import sleep
from os import system
from sys import exit


def execute_quit(input_variable):
    if input_variable.lower()[0] == 'q':
        print(f"\n\033[1;34m Quitting...\033[0m", end="\n\n")
        sleep(0.5)
        exit(1)


def catch_given_input():
    system('clear')
    print(f'\n\033[1m**Enter your desired conversion...\033[0m\n')

    print(f'\033[1;33m - From (q to quit):\033[0m ', end=" ")
    from_qty = input()
    execute_quit(from_qty)

    print(f'\033[1;32m - To (q to quit):\033[0m ', end=" ")
    to_qty = input()
    execute_quit(to_qty)

    return from_qty, to_qty


def delimiter_fields(from_value):
    how_many = 0
    what_value = ''
    value_to_continue = 0
    from_value = from_value.split()
    error_message = f'\n\033[1;31m ERROR - You need to have a digit' \
                    f' and then a measurement in order to know what to convert. Ex: 23 feet or 40 centimeters\033[0m'

    if len(from_value) != 2:
        print(error_message, end="\n\n")
        sleep(0.5)
    else:
        how_many, what_value = from_value
        if how_many.isalpha():
            print(error_message, end="\n\n")
            sleep(0.5)
        else:
            value_to_continue = 1
            try:
                how_many = int(how_many)
            except ValueError:
                how_many = float(how_many)

    return how_many, what_value, value_to_continue


def determine_from_what_to_what(from_type, *arguments):
    dict_of_values_english_system_length, dict_of_values_metric_system_length = arguments
    x = 0; y = 0

    if from_type.lower() in dict_of_values_english_system_length.keys():
        x = 1; y = 2
    elif from_type.lower() in dict_of_values_metric_system_length.keys():
        x = 2; y = 1

    return x, y


def from_system_to_meters(type_of_operation, *arguments):
    many_qty, type_of_value, dict_of_values = arguments
    var_to_return = 0

    dict_to_read = dict_of_values.items()
    for i, j in dict_to_read:
        if i == type_of_value.lower():
            if type_of_operation == 1:
                var_to_return = many_qty * j
            else:
                var_to_return = many_qty / j

    return var_to_return


def from_meters_to_system(value_in_meters, to_type, input_dict, type_of_operation):
    value_after_conv = 0

    dict_to_read = input_dict.items()
    for i, j in dict_to_read:
        if i == to_type.lower():
            if type_of_operation == 1:
                value_after_conv = value_in_meters * j
            else:
                value_after_conv = value_in_meters / j

    return value_after_conv


def main():
    global many_qty, type_of_value, to_measurements
    dict_of_values_english_system_length = {'inches': 0.0254, 'feet': 0.3048, 'yards': 0.9144, 'miles': 1609.344}

    dict_of_values_metric_system_length = {'millimeters': 1000, 'centimeters': 100, 'decimeters': 10, 'meters': 1,
                                           'decameters': 0.1, 'hectometers': 0.01, 'kilometers': 0.001}
    to_continue = 0
    while to_continue == 0:
        from_measurements, to_measurements = catch_given_input()
        many_qty, type_of_value, to_continue = delimiter_fields(from_measurements)

    from_value, to_value = determine_from_what_to_what(type_of_value, dict_of_values_english_system_length,
                                                       dict_of_values_metric_system_length)
    print(f'\n{"-"*45}')
    print(f'\033[1m**Conversion: {many_qty} {type_of_value} =', end=" ")

    if from_value == 1:
        from_english_to_meters = from_system_to_meters(1, many_qty, type_of_value, dict_of_values_english_system_length)
        metric_after_conv = from_meters_to_system(from_english_to_meters, to_measurements, dict_of_values_metric_system_length, 1)
        print(f'{metric_after_conv:.2f} {to_measurements}\033[0m', end="\n")
    elif from_value == 2:
        metric_to_meters = from_system_to_meters(0, many_qty, type_of_value, dict_of_values_metric_system_length)
        meters_to_english = from_meters_to_system(metric_to_meters, to_measurements, dict_of_values_english_system_length, 0)
        print(f'{meters_to_english:.2f} {to_measurements}\033[0m', end="\n")
    print(f'{"-" * 45}', end="\n\n")


main()
