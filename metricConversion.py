#!/usr/bin/python3

"""We have system to system conversion (metric <-> U.S. System)"""

import re


def catch_given_input():
    print(f'\n\033[1m**Enter your desired conversion...\033[0m\n')

    from_qty = input(f'\033[1;33m - From:\033[0m ')
    to_qty = input(f'\033[1;32m - To:\033[0m ')

    return from_qty, to_qty


def delimiter_fields(from_value):
    from_value = from_value.split()
    how_many, what_value = from_value

    return how_many, what_value


def find_order_from_sys_to_sys(type_of_value, dict_of_values_for_conversion):
    metric_order = -1
    dict_after_conv = {}

    for i, j in dict_of_values_for_conversion.items():
        if i in type_of_value:
            metric_order = 0
            for k, j in dict_of_values_for_conversion.items():
                dict_after_conv.update({(j[0], j[1]): k})
            break
        elif type_of_value in j[1]:
            metric_order = 1
            for k, j in dict_of_values_for_conversion.items():
                dict_after_conv.update({(j[0], k): j[1]})
            break

    return metric_order, dict_after_conv


def converting_all_metric_in_metric(value_to_convert):
    given_value, given_type_of_value = value_to_convert.split()


def converting(*args):
    type_of_value, type_of_operation, dict_of_values, given_value_to_convert, \
        to_measurements_to_convert = args

    def operation(type_operation):
        our_list = []

        for i, j in dict_of_values.items():
            if j in type_of_value:
                if type_operation == 1:
                    value_after_conversion = float(given_value_to_convert) * i[0]
                    our_list = [str(value_after_conversion), i[1]]
                elif type_operation == 0:
                    value_after_conversion = float(given_value_to_convert) / i[0]
                    our_list = [str(value_after_conversion), i[1]]

        return ' '.join(our_list)

    if type_of_operation == 0:
        return operation(1)
    elif type_of_operation == 1:
        return operation(0)


def main():

    dict_of_values_english_system_length = {'feet': [12, 'inches'], 'yards': ['3', 'feet'], 'miles': [1760, 'yards']}

    dict_of_values_for_conversion_length = {'inches': [2.54, 'centimeters'], 'feet': [0.30, 'meters'],
                                            'yards': [0.91, 'meters'], 'miles': [1.60, 'kilometers']}

    dict_of_values_metric_system_length = {'meters': [1000, 'millimeters'], 'meters': [100, 'centimeters'],
                                           'meters': [10, 'decimeters'], 'dekameters': [10, 'decimeters'],
                                           'hectometers': [100, 'meters'], 'kilometers': [1000, 'meters']}


    from_measurements, to_measurements = catch_given_input()
    many_qty, type_of_value = delimiter_fields(from_measurements)
    dict_for_sys_to_sys, dict_of_values_sys = find_order_from_sys_to_sys(type_of_value, dict_of_values_for_conversion_length)
    #print(f'{from_measurements} and {to_measurements} and {many_qty} and {type_of_value} and {dict_for_sys_to_sys}')
    #print(f'{dict_of_values_sys}')

    value_after_initial_converting = converting(type_of_value, dict_for_sys_to_sys, dict_of_values_sys, many_qty, to_measurements)
    number_value, value_type = value_after_initial_converting.split()

    if value_type == to_measurements:
        print(f'{number_value} {value_type}')
    else:
        print(f'Not yet finished.')


main()
