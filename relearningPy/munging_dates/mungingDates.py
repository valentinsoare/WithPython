#!/usr/bin/python

import mypy
import pyparsing
import configparser
from time import sleep
from re import sub, match
from random import shuffle
from os import system, path
from string import ascii_lowercase
from typing import List, Dict, Tuple


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
        case 'c':
            print(f"\n{' ' * 10} Going forward to load the configuration....", flush=True)
            message_to_return = 'forward'
            sleep(2)
        case 'q':
            print(f"\n{' ' * 10} Exiting....", flush=True)
            sleep(1)
            exit(1)
        case 'r':
            print(f"\n{' ' * 10} Reloading the configuration...", flush=True)
            message_to_return = 'reload'
            sleep(2)

    if match(r'\s+', given_answer) or given_answer == '':
        print(f"\n{' ' * 10} ERROR please specify a valid file path or q in order to quit!", flush=True)
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
        print(f"{' ' * 10} 2. Parameters key/value pair from config file are ok. All Good!")
        sleep(1)
        return 'not_looping'


def validate_config_file_and_load(given_file_path: str) -> tuple:
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
                print(f"OK.", flush=True)
                sleep(1)

    if validate_config_content(cfg) == 'not_looping':
        return 'all_good', cfg
    else:
        return 'looping', cfg


#def parsing_config_file_and_extract_information(config):


def load_settings_from_cfg() -> configparser.RawConfigParser():
    cfg = configparser.RawConfigParser()
    type_of_exit: str = 'looping'

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


def main() -> None:
    config_to_use = load_settings_from_cfg()


if __name__ == '__main__':
    main()
