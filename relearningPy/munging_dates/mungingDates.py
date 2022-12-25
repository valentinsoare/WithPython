#!/usr/bin/python

##########################################################################
### - munging_dates with configparser vs scramblingWords with pyYAML - ###
##########################################################################
##### pyYAML is winning ######

import logging
import configparser
from time import sleep
from random import shuffle
from os import system, path
from pyparsing import Word, alphas
from string import ascii_lowercase
from typing import List, Dict, Tuple
from re import sub, match, findall, compile, search


def create_lines_header(multiply_by: int, size_of_string) -> str:
    i: int = 0
    line: str = ''
    lower_letters: List[str] = list(ascii_lowercase)

    while i < multiply_by:
        shuffle(lower_letters)
        line += ''.join(lower_letters[0:size_of_string])
        i += 1

    return line


def display_header(message_for_printing: str) -> None:
    message_to_print: str = ' '.join(message_for_printing)
    length_of_message: int = len(message_to_print)

    line_to_print = create_lines_header(2, -1)

    print(f"\n{' ' * 15}{line_to_print}", flush=True)
    message_to_print_without_extra_space: str = sub(r'\s{3}', '  ', message_to_print)
    print(f"{' ' * 15}{create_lines_header(2, -1)[0:(len(line_to_print) // 2 - length_of_message // 2) - 1]} "
          f"{message_to_print_without_extra_space} "
          f"{create_lines_header(2, -1)[0:(len(line_to_print) // 2 - length_of_message // 2) - 1]}", flush=True)
    print(f"{' ' * 15}{line_to_print}", flush=True)


def check_short_answers(given_answer: str) -> str:
    message_to_return: str = ''

    match given_answer:
        case 'q':
            print(f"\n{' ' * 10} Exiting....", flush=True)
            sleep(1)
            exit(1)
        case 'f':
            print(f"\n{' ' * 10} Going forward to load the text from source...", flush=True)
            message_to_return = 'go_forward'
            sleep(2)
        case 'r':
            print(f"\n{' ' * 10} Going back to load the configuration...", flush=True)
            message_to_return = 'reload'
            sleep(2)

    if match(r'\s+', given_answer) or given_answer == '':
        print(f"\n{' ' * 10} ERROR please specify a valid answer. Do not use only whitespaces!", flush=True)
        message_to_return: str = 'looping'
        sleep(2)

    return message_to_return


def to_summarize_checking_input_output(config, type_of_input) -> str:
    to_break: int = 0
    error_exists: str = 'looping'

    for option_select in config.options(type_of_input):
        if option_select == 'path_of_file' and config.get(type_of_input, 'type') == 'file' \
                and len(config.get(type_of_input, option_select)) == 0:
            print(f"\n{' ' * 10} ERROR please specify a file for {type_of_input}!", flush=True)
            to_break = 1

        if option_select == 'type':
            if config.get(type_of_input, option_select) not in ['cli', 'file']:
                print(f"\n{' ' * 10} ERROR on {type_of_input} option type, we need cli or file as an option!",
                      flush=True)
                to_break = 1
            elif config.get(type_of_input, option_select) == 'file' and not path.isfile(config.get(type_of_input, 'path_of_file')):
                print(f"\n{' ' * 10} ERROR {type_of_input} file doesn't exists!", flush=True)
                to_break = 1
            elif config.get(type_of_input, 'type') == 'file' \
                    and path.getsize(config.get(type_of_input, 'path_of_file')) == 0:
                print(f"\n{' ' * 10} ERROR {type_of_input} file is empty!", flush=True)
                to_break = 1
            else:
                error_exists = 'not_looping'

        if to_break == 1:
            sleep(2)
            break

    return error_exists


def to_summarize_checking_other(config, type_of_input) -> str:
    to_break: int = 0
    error_exists: str = 'looping'

    for option_select in config.options(type_of_input):
        if option_select == 'enable_logging' and config.getboolean(type_of_input, option_select) not in [True, False]:
            print(f"\n{' ' * 10} We do not have a boolean value for logging on {type_of_input}"
                  f" section. By default logging will be enable!", flush=True)
            to_break = 1
        elif option_select == 'logging_level' and config.get(type_of_input, option_select) not in ['debug', 'info',
                                                                                                   'warn', 'error',
                                                                                                   'critical']:
            print(f"\n{' ' * 10} ERROR please specify a valid logging level!", flush=True)
            to_break = 1

        if option_select == 'path_of_logging':
            if len(config.get(type_of_input, option_select)) == 0:
                print(f"\n{' ' * 10} ERROR please specify a valid path for logging file!", flush=True)
                to_break = 1
            elif not path.isfile(config.get(type_of_input, option_select)):
                print(f"\n{' ' * 10} ERROR logging file doesn't exists!", flush=True)
                to_break = 1
            else:
                error_exists = 'not_looping'

        if to_break == 1:
            sleep(2)
            break

    return error_exists


def validate_config_content(given_config) -> str:
    given_input, given_output, given_other = tuple(given_config.sections())

    if (to_summarize_checking_input_output(given_config, given_input)
            or to_summarize_checking_input_output(given_config, given_output)) == 'looping':
        return 'looping'
    elif to_summarize_checking_other(given_config, given_other) == 'looping':
        return 'looping'
    else:
        print(f"{' ' * 10} 2. Parameters key/value pair from config file are ok. All Good!", flush=True)
        sleep(1)
        return 'not_looping'


def validate_config_file_and_load(given_file_path: str) -> Tuple:
    to_return_value: str = 'looping'

    print(f"\n{' ' * 10} 1. Checking validity of configuration file path....", end="", flush=True)
    sleep(1)

    if not path.isfile(given_file_path):
        print(f"ERROR the path doesn't exists!", flush=True)
    elif path.getsize(given_file_path) == 0:
        print(f"ERROR file exists but it's empty!", flush=True)
    else:
        to_return_value = 'not_looping'

    if to_return_value == 'looping':
        sleep(3)
        return to_return_value, 0
    else:
        cfg = configparser.RawConfigParser(allow_no_value=True)
        with open(given_file_path, 'r') as config_open:
            cfg.read_file(config_open)
            if cfg:
                print(f"OK", flush=True)
                sleep(1)

    if validate_config_content(cfg) == 'not_looping':
        return 'all_good', cfg
    else:
        return 'looping', cfg


def parsing_config_file_and_extract_information(config: configparser.RawConfigParser()) -> Tuple:
    values_to_return_input_output: Dict[str, List[str]] = {}
    values_to_return_logging: Dict[str, List[str]] = {}

    for section in config.sections()[0:2]:
        for option in config.options(section):
            if config.get(section, option) == 'cli':
                values_to_return_input_output[section] = ['cli', None]
            elif config.get(section, option) == 'file':
                values_to_return_input_output[section] = [config.get(section, 'path_of_file'), 'file']

    logging_section = config.sections()[-1]

    if config.get(logging_section, 'enable_logging') == 'yes':
        values_to_return_logging[logging_section] = [config.get(logging_section, 'path_of_logging'), config.get(logging_section, 'logging_level')]
    else:
        values_to_return_logging[logging_section] = ['no_logging', None]

    return values_to_return_input_output, values_to_return_logging, 0


def load_settings_from_cfg() -> configparser.RawConfigParser():
    type_of_exit: str = 'looping'
    cfg = configparser.RawConfigParser()

    while type_of_exit == 'looping':
        system('clear')
        display_header('munging dates')

        print(f"\n{' ' * 7} * Please specify the path for the configuration file (q to quit):", end=" ", flush=True)
        answer: str = input().strip()

        execute_to_check: str = check_short_answers(answer)
        if execute_to_check == 'looping':
            continue
        else:
            type_of_exit, cfg = validate_config_file_and_load(answer)

    return cfg


def load_text_from_cli() -> Tuple:
    message_to_check: str = 'looping'

    while message_to_check == 'looping':
        system('clear')
        display_header('munging dates')

        print(f"\n{' ' * 7} * Please give us the text to extract the dates from: (q to quit, "
              f"r to reload the config):", end=" ", flush=True)
        answer: str = input().strip()

        answer_from_short_checking: str = check_short_answers(answer)
        if answer_from_short_checking == 'looping':
            continue
        elif answer_from_short_checking == 'reload':
            return 0, 1
        else:
            return answer, 0


def load_text_from_file(input_type) -> Tuple:

    while True:
        system('clear')
        display_header('munging dates')

        print(f"\n{' ' * 8} * We will be loading the text from '{input_type['input'][0].split('/')[-1]}'\n"
              f"{' ' * 7} ** (q to quit, r to reload config, f to go forward):", end=" ", flush=True)
        answer = input().strip()

        to_check = check_short_answers(answer)
        if to_check == 'looping':
            continue
        elif to_check == 'reload':
            return 1, 1
        elif to_check == 'go_forward':
            with open(input_type['input'][0], 'r') as open_file:
                file_to_load = open_file.read()
            return file_to_load, 0

        print(f"\n{' ' * 10} ERROR - please use only one of those three options - q, r or f.", flush=True)
        sleep(2)


def check_for_first_rule(given_text):
    first_type_date = compile(r'(0[1-9]|1[0-2])([0-3][0-9])([0-9][0-9])')
    checking_text = findall(first_type_date, given_text)

    if checking_text:
        return 1, checking_text
    else:
        return 0, None


def check_for_second_rule(given_text):
    second_type_date = compile(r'(0[1-9]|1[0-2])/([0-3][0-9])/([1|2][0-9]{3})')
    checking_given_string = findall(second_type_date, given_text)

    if checking_given_string:
        return 2, checking_given_string
    else:
        return 0, None


def check_for_third_rule(given_text):
    third_type_date = compile(r'([A-Za-z][a-z]{,8})\s(0[1-9]|[1-2][0-9]|3[0-2]),\s(1[0-9][0-9][0-9]|20[0-9][0-9])')
    checking_string = findall(third_type_date, given_text)

    if checking_string:
        return 3, checking_string
    else:
        return 0, None


def extracting_dates_from_text(given_text) -> Tuple:
    dict_with_dates_extracted: Dict = {}
    number_of_dates: int = 0
    given_functions = [check_for_first_rule(given_text), check_for_second_rule(given_text), check_for_third_rule(given_text)]

    for rule in given_functions:
        rule_number, text_extracted_from_rule = rule
        if text_extracted_from_rule is not None:
            if rule_number in dict_with_dates_extracted.keys():
                dict_with_dates_extracted[rule_number] += text_extracted_from_rule
            else:
                dict_with_dates_extracted[rule_number] = text_extracted_from_rule
            number_of_dates += 1

    return dict_with_dates_extracted, number_of_dates


def converting_from_one_to_rest(given_list: List, dict_with_months: Dict) -> Dict:
    type_two = '/' + given_list[2]
    intermediary = search(r'[0-9]{2}$', type_two)

    if int(intermediary.group()) > 23:
        type_two = sub(r'[0-9]{2}$', "19", type_two)
    else:
        type_two = sub(r'[0-9]{2}$', "20", type_two)

    final_two = given_list[0] + '/' + given_list[1] + type_two + intermediary.group()
    final_three = dict_with_months[given_list[0]] + " " + given_list[1] + ', ' + search(r'[0-9]{2}$',
                                                                             type_two).group() + intermediary.group()

    return {''.join(given_list): [final_two, final_three]}


def converting_from_two_to_rest(given_list, dict_with_months) -> Dict:
    type_together = ''.join(given_list)
    final_one = type_together[slice(4)] + type_together[len(type_together) - 2: len(type_together)]
    final_three = dict_with_months[given_list[0]] + " " + given_list[1] + ', ' + given_list[2]

    return {(given_list[0] + '/' + given_list[1] + '/' + given_list[2]): [final_one, final_three]}


def converting_from_three_to_rest(given_list, dict_with_months) -> Dict:
    month_in_digits = list(dict_with_months.keys())[list(dict_with_months.values()).index(given_list[0].title())]
    final_one = month_in_digits + given_list[1] + given_list[2][2:4]
    final_two = month_in_digits + "/" + given_list[1] + "/" + given_list[2]

    return {(given_list[0] + ' ' + given_list[1] + ', ' + given_list[2]): [final_one, final_two]}


def converting_dates(given_text: Dict) -> Dict:
    converted_dates: Dict = {}

    dict_with_months = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May',
                        '06': 'June', '07': 'July', '08': 'August', '09': 'September',
                        '10': 'October', '11': 'November', '12': 'December'}

    for i, list_with_dates in given_text.items():
        for element in list_with_dates:
            if i == 1:
                converted_dates.update(converting_from_one_to_rest(element, dict_with_months))
            elif i == 2:
                converted_dates.update(converting_from_two_to_rest(element, dict_with_months))
            else:
                converted_dates.update(converting_from_three_to_rest(element, dict_with_months))

    return converted_dates


def converting_all_dates(number_of_dates_matched_pattern: int, dates_from_text: Dict, for_logging: int, given_level: str) -> Dict:
    dates_after_conversion: Dict = {}

    if number_of_dates_matched_pattern != 0:
        dates_after_conversion = converting_dates(dates_from_text)
    else:
        message_to_print = f"{' ' * 10} No valid dates that matches the patterns in the given text!"
        print(f"\n{message_to_print}", flush=True)
        sleep(2)
        if for_logging == 1:
            action_to_use: str = given_level.lower() + f"(message_to_print)"
            eval(action_to_use)

    return dates_after_conversion


def creating_text_parser_for_level(given_level_of_log: str) -> str:
    log_pattern = Word(alphas) + '.' + Word(alphas)

    for log in ['logging.DEBUG', 'logging.INFO', 'logging.WARNING', 'logging.ERROR', 'logging.CRITICAL']:
        log_level = log_pattern.parseString(log)
        if log_level[2].lower() == given_level_of_log:
            return ''.join(log_level)


def define_logging(level_of_logging: str, log_file: str):
    given_level_of_logging: str = creating_text_parser_for_level(level_of_logging)

    logging.basicConfig(filename=log_file,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%d/%m/%Y %I:%M:%S %p',
                        level=eval(given_level_of_logging))

    return given_level_of_logging


def printing_output(dict_with_dates: Dict, type_of_output: List, for_logging: int, given_level) -> int:
    if for_logging == 1:
        action_to_use: str = given_level.lower() + f"(dict_with_dates)"
        eval(action_to_use)

    if type_of_output[0] == 'cli':
        while True:
            system('clear')
            display_header('munging dates')

            print(f"\n{' ' * 7} {'Initial Date':<18} {'->':<10} {'Converted Dates'}", flush=True)
            print(f"{' ' * 7}{'-' * 47}", flush=True)

            for initial_date, converted_dates in dict_with_dates.items():
                print(f"{' ' * 7} {initial_date:<29} {converted_dates}", flush=True)

            print(f"\n{' ' * 7} * q to quit, r to reload the configuration or f to enter a new next in cli:", end=" ", flush=True)
            given_answer = input().strip()

            to_check = check_short_answers(given_answer)
            if to_check == 'looping':
                continue
            elif to_check == 'reload':
                return 1
            elif to_check == 'go_forward':
                return 0


def main() -> None:
    if_logging: int = 0
    given_level: str = ''
    dict_with_input_output: Dict = {}
    load_configuration_for_looping_and_text: int = 1

    while True:
        while load_configuration_for_looping_and_text == 1:
            config_to_use = load_settings_from_cfg()
            dict_with_input_output, dict_with_logging, load_configuration_for_looping_and_text = parsing_config_file_and_extract_information(config_to_use)
            if dict_with_logging['other'][0] != 'no_logging':
                given_level = define_logging(level_of_logging=dict_with_logging['other'][1], log_file=dict_with_logging['other'][0])
                if_logging = 1

        if dict_with_input_output['input'][0] == 'cli':
            text_to_be_process, load_configuration_for_looping_and_text = load_text_from_cli()
        else:
            text_to_be_process, load_configuration_for_looping_and_text = load_text_from_file(dict_with_input_output)

        if load_configuration_for_looping_and_text == 1:
            continue
        else:
            dates_from_txt, number_of_dates_matched_pattern = extracting_dates_from_text(text_to_be_process)
            dates_after_conversion = converting_all_dates(number_of_dates_matched_pattern, dates_from_txt, if_logging, given_level)

        if number_of_dates_matched_pattern != 0:
            load_configuration_for_looping_and_text = printing_output(dates_after_conversion, dict_with_input_output['output'],
                                                                      if_logging, given_level)


if __name__ == '__main__':
    main()
