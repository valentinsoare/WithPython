#!/usr/bin/python

import os
import re
from sys import exit
from time import sleep


def check_for_first_rule(given_text):
    first_type_date = re.compile(r'(0[1-9]|1[0-2])([0-3][0-9])([0-9][0-9])')
    checking_text = re.findall(first_type_date, given_text)

    if len(checking_text) != 0:
        return 1, checking_text
    else:
        return 0, None


def check_for_second_rule(given_text):
    second_type_date = re.compile(r'(0[1-9]|1[0-2])/([0-3][0-9])/([1|2][0-9]{3})')
    checking_given_string = re.findall(second_type_date, given_text)

    if len(checking_given_string) != 0:
        return 2, checking_given_string
    else:
        return 0, None


def check_for_third_rule(given_text):
    third_type_date = re.compile(r'[A-Z][a-z]{,8}\s([0-3][0-9]),\s([1|2][0-9]{3})')
    checking_string = re.findall(third_type_date, given_text)

    if len(checking_string) != 0:
        return 3, checking_string
    else:
        return 0, None


def catch_user_input():
    catch_text = ''
    var_to_exit = 1
    list_with_funct_values = ["check_for_first_rule(catch_text)",
                              "check_for_second_rule(catch_text)",
                              "check_for_third_rule(catch_text)"]

    while var_to_exit != 0:
        count = 0
        os.system('clear')
        print(f' \n\033[1m - > Enter given text with dates (q to quit):\033[0m', end=" ")
        catch_text = input()

        if catch_text.lower()[0] == "q":
            print(f'\n\033[1;33m{"Quitting...":>17}\033[0m', end="\n\n")
            sleep(1)
            exit(1)

        for i in list_with_funct_values:
            return_value, list_with_values = eval(i)

            if return_value in [1, 2, 3]:
                var_to_exit = 0
            else:
                count += 1

        if count == 3:
            print(f'\n\033[1;31m{"Given text does not contain dates with the searched patterns.":>68}\033[0m')
            sleep(1)

    return catch_text


def get_month_digit(month_name):
    dict_with_months = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
                        'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
                        }

    if_not_present = 'Error requested element not available.'
    month_digit = dict_with_months.get(month_name.title()[0:3], if_not_present)

    return month_digit


def main():
    text_after_catching = catch_user_input()
    #numerical_month = get_month_digit("november")


main()
