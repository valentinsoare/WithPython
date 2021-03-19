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

    for i, j in dict_of_values_for_conversion.items():
        if i in type_of_value:
            metric_order = 0
            break
        elif type_of_value in j[1]:
            metric_order = 1
            dict_of_values_for_conversion = {l[1]: (l[0], k) for k, l in dict_of_values_for_conversion.items()}
            break
     
    return metric_order, dict_of_values_for_conversion


def main():
    dict_of_values_for_conversion = {'inch': (2.5, 'centimeters'), 'feet': (30, 'centimeters'),
                                     'yards': (0.9, 'meters'), 'miles': (1.6, 'kilometers')}

    from_measurements, to_measurements = catch_given_input()
    many_qty, type_of_value = delimiter_fields(from_measurements)
    dict_for_sys_to_sys, dict_of_values_sys = find_order_from_sys_to_sys(type_of_value, dict_of_values_for_conversion)

    print(f'{dict_of_values_sys} and type: {dict_for_sys_to_sys}')


main()
