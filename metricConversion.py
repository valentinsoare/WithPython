#!/usr/bin/python3


def catch_given_input():
    print(f'\n\033[1m**Enter your desired conversion...\033[0m\n')

    from_qty = input(f'\033[1;33m - From:\033[0m ')
    to_qty = input(f'\033[1;32m - To:\033[0m ')

    return from_qty, to_qty


def delimiter_fields(from_value):
    from_value = from_value.split()
    how_many, what_value = from_value

    try:
        how_many = int(how_many)
    except ValueError:
        how_many = float(how_many)

    return how_many, what_value


def determine_from_what_to_what(from_type, *arguments):
    dict_of_values_english_system_length, dict_of_values_metric_system_length = arguments
    x = 0; y = 0

    if from_type.lower() in dict_of_values_english_system_length.keys():
        x = 1; y = 2
    elif from_type.lower() in dict_of_values_metric_system_length.keys():
        x = 2; y = 1

    return x, y


def from_system_to_meters(*arguments):
    many_qty, type_of_value, dict_of_values = arguments
    var_to_return = 0

    dict_to_read = dict_of_values.items()
    for i, j in dict_to_read:
        if i == type_of_value.lower():
            var_to_return = many_qty * j

    return var_to_return


def from_meters_to_system(value_in_meters, to_type, dict_of_values_metric_system_length, type_of_oper = 0):
    value_after_conv = 0

    dict_to_read = dict_of_values_metric_system_length.items()
    for i, j in dict_to_read:
        if i == to_type.lower():
            if type_of_oper == 1:
                value_after_conv = value_in_meters * j
            else:
                value_after_conv= value_in_meters / j

    return value_after_conv


def main():
    dict_of_values_english_system_length = {'inches': 0.0254, 'feet': 0.3048, 'yards': 0.9144, 'miles': 1609.344}

    dict_of_values_metric_system_length = {'millimeters': 1000, 'centimeters': 100, 'decimeters': 10, 'meters': 1,
                                           'decameters': 0.1, 'hectometers': 0.01, 'kilometers': 0.001}

    from_measurements, to_measurements = catch_given_input()
    many_qty, type_of_value = delimiter_fields(from_measurements)

    from_value, to_value = determine_from_what_to_what(type_of_value, dict_of_values_english_system_length,
                                                       dict_of_values_metric_system_length)
    print(f'\n{"-"*45}')
    print(f'\033[1m**Conversion: {many_qty} {type_of_value} =', end=" ")

    if from_value == 1:
        from_english_to_meters = from_system_to_meters(many_qty, type_of_value, dict_of_values_english_system_length)
        metric_after_conv = from_meters_to_system(from_english_to_meters, to_measurements, dict_of_values_metric_system_length, 1)
        print(f'{metric_after_conv:.2f} {to_measurements}\033[0m', end="\n")
    elif from_value == 2:
        metric_to_meters = from_system_to_meters(many_qty, type_of_value, dict_of_values_metric_system_length)
        meters_to_english = from_meters_to_system(metric_to_meters, to_measurements, dict_of_values_english_system_length, 0)
        print(f'{meters_to_english:.2f} {to_measurements}\033[0m', end="\n")
    print(f'{"-" * 45}', end="\n\n")


main()
