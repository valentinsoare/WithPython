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
    third_type_date = re.compile(r'([A-Z][a-z]{,8})\s(0[1-9]|[1-2][0-9]|3[0-2]),\s(1[0-9][0-9][0-9]|20[0-9][0-9])')
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


def get_month_digit(month_name):
    dict_with_months = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
                        'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
                        }

    if_not_present = 'Error requested element not available.'
    month_digit = dict_with_months.get(month_name.title()[0:3], if_not_present)

    return month_digit


def print_given_dates_category(*args):
    design_format, dates_given = args

    print(f'\n\033[1m{" Dates format extracted from the given text:":>35}\033[0m', end="")

    for i, j in dates_given.items():
        print(f"\n - {design_format[i]}:", end=" ")
        for k in j:
            if i == 1:
                k = ''.join(list(k))
                print(f"{k}", end="  ")
            if i == 2:
                k = '/'.join(list(k))
                print(f"{k}", end="  ")
            if i == 3:
                k = ' '.join(list(k))
                print(f"{k}", end="  ")


def main():
    dict_with_functions = {'check_for_first_rule(given_text)': 1, 'check_for_second_rule(given_text)': 2,
                           'check_for_third_rule(given_text)': 3}

    formats_design = {1: 'MMDDYY',
                      2: 'MM/DD/YYYY',
                      3: 'Month DD, YYYY'}

    text_after_catching = catch_user_input(dict_with_functions)
    dates_from_given_text = extracted_dates_from_text(text_after_catching, dict_with_functions)

    print_given_dates_category(formats_design, dates_from_given_text)

    #numerical_month = get_month_digit("november")


main()
