#!/usr/bin/python3

"""We have system to system conversion (metric <-> U.S. System)"""


def catch_given_input():
    print(f'\n\033[1m**Enter your desired conversion...\033[0m\n')

    from_qty = input(f'\033[1;33m - From:\033[0m ')
    to_qty = input(f'\033[1;32m - To:\033[0m ')

    return from_qty, to_qty


def delimiter_fields(from_value):
    from_value = from_value.split()
    how_many, what_value = from_value

    return how_many, what_value


def main():

    dict_of_values_english_system_length = {'inches': [0.0833, 'feet'], 'feet': [1, 'feet'], 'yards': [3, 'feet'],
                                            'miles': [5280, 'feet']}

    dict_of_values_for_conversion_length = {'inches': [0.0254, 'meters'], 'feet': [0.3048, 'meters'],
                                            'yards': [0.9144, 'meters'], 'miles': [1609.344, 'meters']}

    list_of_values_metric_system_length = [[1000, 'millimeters'], [100, 'centimeters'],
                                           [1, 'meters'],[10, 'decimeters'], [0.1, 'dekameters'],
                                           [0.01, 'hectometers'], [0.001, 'kilometers']]

    from_measurements, to_measurements = catch_given_input()
    many_qty, type_of_value = delimiter_fields(from_measurements)


main()
