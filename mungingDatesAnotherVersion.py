#!/usr/bin/python

import os
import re
from sys import exit
from time import sleep


def check_for_first_rule(given_text):
    first_type_date = re.compile(r'(0[1-9]|1[0-2])([0-3][0-9])([0-9][0-9])')
    checking_text = re.findall(first_type_date, given_text)

    if checking_text:
        return 1, checking_text
    else:
        return 0, None


def check_for_second_rule(given_text):
    second_type_date = re.compile(r'(0[1-9]|1[0-2])/([0-3][0-9])/([1|2][0-9]{3})')
    checking_given_string = re.findall(second_type_date, given_text)

    if checking_given_string:
        return 2, checking_given_string
    else:
        return 0, None


def check_for_third_rule(given_text):
    third_type_date = re.compile(r'([A-Za-z][a-z]{,8})\s(0[1-9]|[1-2][0-9]|3[0-2]),\s(1[0-9][0-9][0-9]|20[0-9][0-9])')
    checking_string = re.findall(third_type_date, given_text)

    if checking_string:
        return 3, checking_string
    else:
        return 0, None


def catch_user_input(dict_with_functions):
    given_text = ''
    var_to_exit = 1

    while var_to_exit != 0:
        count = 0
        os.system('clear')
        print(f' \n\033[1m - > Enter given text with dates (q to quit):\033[0m', end=" ")
        given_text = input()

        if given_text.lower()[0] == "q":
            print(f'\n\033[1;33m{"Quitting...":>17}\033[0m', end="\n\n")
            sleep(1)
            exit(1)

        for i, j in dict_with_functions.items():
            return_value, list_with_values = eval(i)

            if return_value == j:
                var_to_exit = 0
            else:
                count += 1

        if count == 3:
            print(f'\n\033[1;31m{"Given text does not contain dates with the searched patterns.":>68}\033[0m')
            sleep(1)

    return given_text


def extracted_dates_from_text(given_text, dict_with_functions):
    dict_with_items = {}

    for i, j in dict_with_functions.items():
        return_value, elements = eval(i)

        if return_value == j:
            dict_with_items[j] = elements

    return dict_with_items


def print_given_dates_category(*args):
    design_format, dates_given = args

    print(f'\n\033[1m{" Dates format extracted from the given text:":>35}\033[0m', end="")

    for i, j in dates_given.items():
        print(f"\n - {design_format[i]}:", end=" ")
        for k in j:
            if i == 1:
                k = ''.join(list(k))
                print(f'"{k}"', end="  ")
            if i == 2:
                k = '/'.join(list(k))
                print(f'"{k}"', end="  ")
            if i == 3:
                k = list(k)
                k = k[0] + " " + k[1] + ", " + k[2]
                print(f'"{k}"', end="  ")

    print(f"\n")


def converting_from_one_to_rest(given_dict, dict_with_months, formats_design):
    list_type_one = [list(i) for i in given_dict[1]]

    print(f'\033[1m *Converting from {formats_design[1]} to ({formats_design[2]} and '
          f'{formats_design[3]})\033[0m', end="\n")

    for i in list_type_one:
        type_two = '/'.join(i)
        intermediary = re.search(r'[0-9]{2}$', type_two)

        if int(intermediary.group()) > 22:
            type_two = re.sub(r'[0-9]{2}$', "19", type_two)
        else:
            type_two = re.sub(r'[0-9]{2}$', "20", type_two)

        final_two = type_two + intermediary.group()
        final_three = dict_with_months[i[0]] + " " + i[1] + ', ' + re.search(r'[0-9]{2}$',
                                                                             type_two).group() + intermediary.group()

        print(f' - "{final_two}", "{final_three}"')


def converting_from_two_to_rest(given_dict, dict_with_months, formats_design):
    list_type_two = [list(i) for i in given_dict[2]]

    print(f'\033[1m *Converting from {formats_design[2]} to ({formats_design[1]} and '
          f'{formats_design[3]})\033[0m', end="\n")

    for j in list_type_two:
        type_together = ''.join(j)
        final_one = type_together[slice(4)] + type_together[len(type_together) - 2: len(type_together)]
        final_three = dict_with_months[j[0]] + " " + j[1] + ', ' + j[2]

        print(f' - "{final_one}", "{final_three}"')


def converting_from_three_to_rest(given_dict, dict_with_months, formats_design):
    list_type_three = [list(i) for i in given_dict[3]]

    print(f'\033[1m *Converting from {formats_design[3]} to ({formats_design[1]} and '
          f'{formats_design[2]})\033[0m', end="\n")

    for k in list_type_three:
        month_in_digits = list(dict_with_months.keys())[list(dict_with_months.values()).index(k[0].title())]
        final_one = month_in_digits + k[1] + k[2][2:4]
        final_two = month_in_digits + "/" + k[1] + "/" + k[2]

        print(f' - "{final_one}", "{final_two}"')


def what_to_convert(*args):
    dates_from_given_text, dict_with_months, formats_design = args

    for i in dates_from_given_text.keys():
        if i == 1:
            converting_from_one_to_rest(dates_from_given_text, dict_with_months, formats_design)
        elif i == 2:
            converting_from_two_to_rest(dates_from_given_text, dict_with_months, formats_design)
        elif i == 3:
            converting_from_three_to_rest(dates_from_given_text, dict_with_months, formats_design)


def main():
    dict_with_months = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May',
                        '06': 'June', '07': 'July', '08': 'August', '09': 'September',
                        '10': 'October', '11': 'November', '12': 'December'}

    dict_with_functions = {'check_for_first_rule(given_text)': 1,
                           'check_for_second_rule(given_text)': 2,
                           'check_for_third_rule(given_text)': 3}

    formats_design = {1: 'MMDDYY',
                      2: 'MM/DD/YYYY',
                      3: 'Month DD, YYYY'}

    text_after_catching = catch_user_input(dict_with_functions)
    dates_from_given_text = extracted_dates_from_text(text_after_catching, dict_with_functions)

    print_given_dates_category(formats_design, dates_from_given_text)
    what_to_convert(dates_from_given_text, dict_with_months, formats_design)


main()
