#!/usr/bin/python3

import re


def ask_for_input_string():
    given_string = input(f'\n\033[1m**Enter the desired text to analyze the dates and '
                         f'convert the format for these dates:\033[0m ')
    return given_string


def detect_first_type_of_date(giving_text, multi=False):
    pattern = re.compile(r"(0[1-9]|[1-2][0-9]|3[0-2])(0[1-9]|1[0-2])(1[0-9][0-9][0-9]|20[0-9][0-9])")
    checking_pattern = re.search(pattern, giving_text)

    if multi:
        return (1, checking_pattern.groups()) \
            if checking_pattern else (0, None)
    else:
        return 1 if checking_pattern else 0


def detect_second_type_of_date(giving_text, multi=False):
    pattern = re.compile(r"(0[1-9]|[1-2][0-9]|3[0-2])/(0[1-9]|1[0-2])/(1[0-9][0-9][0-9]|20[0-9][0-9])")
    checking_pattern = re.search(pattern, giving_text)
    if multi:
        return (2, checking_pattern.groups()) \
            if checking_pattern else (0, None)
    else:
        return 2 if checking_pattern else 0


def detect_third_type_if_date(giving_text, multi=False):
    pattern = re.compile(r'([A-Z][a-z]{,8})\s(0[1-9]|[1-2][0-9]|3[0-2]),\s(1[0-9][0-9][0-9]|20[0-9][0-9])')
    checking_pattern = re.search(pattern, giving_text)
    if multi:
        return (3, checking_pattern.groups()) \
            if checking_pattern else (0, None)
    else:
        return 3 if checking_pattern else 0


def convert_first_type(type_string, months):
    pattern, groups_output = detect_first_type_of_date(type_string, multi=True)
    result_to_second = f'{groups_output[0]}/{groups_output[1]}/{groups_output[2]}'
    result_to_third = f'{months.get(groups_output[1])} {groups_output[0]}, {groups_output[2]}'

    print(f"\n\033[1m *After conversion of {''.join(groups_output)}:\033[0m")
    print(f'   - {result_to_second}\n   - {result_to_third}')


def convert_second_type(type_string, months):
    pattern, groups_output = detect_second_type_of_date(type_string, multi=True)
    result_to_first = f'{groups_output[0]}{groups_output[1]}{groups_output[2]}'
    result_to_third = f'{months.get(groups_output[1])} {groups_output[0]}, {groups_output[2]}'

    print(f"\n\033[1m *After conversion of {groups_output[0]}/{groups_output[1]}/{groups_output[2]}:\033[0m")
    print(f'   - {result_to_first}\n   - {result_to_third}')


def convert_third_type(type_string, months):
    pattern, groups_output = detect_third_type_if_date(type_string, multi=True)
    month_extracted_and_converted = ''.join([i for i, j in months.items() if j == groups_output[0]])
    result_to_first = f'{groups_output[1]}{month_extracted_and_converted}{groups_output[2]}'
    result_to_second = f'{groups_output[1]}/{month_extracted_and_converted}/{groups_output[2]}'

    print(f"\n\033[1m *After conversion of {groups_output[0]} {groups_output[1]}, {groups_output[2]}:\033[0m")
    print(f'   - {result_to_first}\n   - {result_to_second}')


def printing_detected_format(our_string, functions_detect_dict):
    checking = 0
    date_format_dict = {
        'DDMMYY': 1,
        'DD/MM/YY': 2,
        'January DD, YY': 3
    }

    print(f'\n\033[1m**We have the following string to analyze:\033[0m\n \"{our_string}\"\n')
    for i, j in functions_detect_dict.items():
        if eval(i) != 0:
            checking += 1
            for k, l in date_format_dict.items():
                if eval(i) == l:
                    print(f'   - {k}')
    if checking == 0:
        print(f'\033[1;41m **No date patterns detected inside given text. \033[0m')


def converting_detected_formats(our_string, months, functions_detect_dict):
    for i, j in functions_detect_dict.items():
        if eval(i) == 1:
            convert_first_type(our_string, months)
        elif eval(i) == 2:
            convert_second_type(our_string, months)
        elif eval(i) == 3:
            convert_third_type(our_string, months)


def main():
    our_string = ask_for_input_string()

    months = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
              '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'
              }

    functions_detect_dict = {
        'detect_first_type_of_date(our_string)': 1,
        'detect_second_type_of_date(our_string)': 2,
        'detect_third_type_if_date(our_string)': 3
    }

    printing_detected_format(our_string, functions_detect_dict)
    converting_detected_formats(our_string, months, functions_detect_dict)


main()
