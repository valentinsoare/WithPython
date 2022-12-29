#!/usr/bin/python


import json
import logging
import pandas as pd
from time import sleep
from re import sub, match
from random import shuffle
from os import system, path
from string import punctuation
from yaml import load, SafeLoader
from typing import List, Union, Dict, Tuple
from schema import Or, Schema, SchemaError, Regex, And, Optional


def create_line(size_of_multiply: Union[int | float], size_of_string: int) -> str:
    final_string_as_line: str = ''
    initial_list_as_punctuation: List[str] = (list(punctuation))[0:size_of_string]
    limit_of_string = round(len(initial_list_as_punctuation) * size_of_multiply)
    size_to_reach: int = limit_of_string

    to_run: bool = True
    shuffle(initial_list_as_punctuation)

    while to_run:
        for i in range(limit_of_string):
            if i == (len(initial_list_as_punctuation) - 1):
                shuffle(initial_list_as_punctuation)
                limit_of_string -= len(initial_list_as_punctuation)
                final_string_as_line += initial_list_as_punctuation[i]
                break
            final_string_as_line += initial_list_as_punctuation[i]
        if len(final_string_as_line) == size_to_reach:
            to_run = False

    return final_string_as_line


def printing_header_notebook(given_message: str, if_upper: int = 0, width: int = 0, nr_of_newlines: int = 0) -> None:
    given_message = ' '.join(given_message)
    multiply_value: float = 1.5
    length_of_line = len(create_line(multiply_value, len(punctuation)))
    value_of_space: int = 0

    if if_upper == 1:
        value_of_space = width // 2 - (len(given_message) + 12) // 2

    for i in range(nr_of_newlines): print()

    print(f"{' ' * value_of_space}{create_line(size_of_multiply=1.5, size_of_string=len(punctuation))}")
    without_spaces: str = sub(r'\s{3}', '  ',given_message)
    print(f"{' ' * value_of_space}{(create_line(size_of_multiply=1.5, size_of_string=len(punctuation)))[0: (length_of_line // 2 - len(given_message) // 2) - 1]}"
          f" {without_spaces} {(create_line(size_of_multiply=1.5, size_of_string=len(punctuation)))[0: (length_of_line // 2 - len(given_message) // 2)]}")
    print(f"{' ' * value_of_space}{create_line(size_of_multiply=1.5, size_of_string=len(punctuation))}")


def printing_what_we_have() -> None:
    printing_header_notebook(given_message='students grade book', if_upper=1, width=120, nr_of_newlines=1)
    print(f"\n{' ' * 7} * We gonna have grades for five classes and each student will have at least three grades per class.\n"
          f"{' ' * 10}Average per exam, per class and then per all classes will be calculated. After teacher will input all\n"
          f"{' ' * 10}these grades along with the names of the students in the gradebook and then we will calculate descriptive statistics.......")
    sleep(2)


def to_check_keys(answer_to_check, react_on_reconfig) -> str:
    value_to_return: str = ''

    if match(r'\s+', answer_to_check) or answer_to_check == '':
        print(f"\n{' ' * 12} ERROR - please do not use only whitespaces or newline.", flush=True)
        value_to_return = 'looping'
        sleep(1)
    elif answer_to_check == 'q':
        print(f"\n{' ' * 12} * Quiting...\n", flush=True)
        sleep(2)
        exit(1)
    elif answer_to_check == 'r' and react_on_reconfig == 1:
        print(f"\n{' ' * 12} * Reloading the configuration.....", flush=True)
        value_to_return = 'reload'
        sleep(2)
    else:
        value_to_return = answer_to_check

    return value_to_return


def ask_for_config(instances: int) -> Tuple:
    to_run: str = 'looping'

    while to_run == 'looping':
        system('clear')
        printing_header_notebook(given_message='students grade book', if_upper=1, width=120, nr_of_newlines=1)

        if instances == 0:
            print(f"\n{' ' * 25} * Please provide entire path of configuration file (q to quit):", end=" ", flush=True)
            instances += 1
        else:
            print(f"\n{' ' * 9} * Please provide the absolute path of configuration file (q to quit, r to reload the previous configuration):", end=" ", flush=True)

        given_answer: str = input().strip()

        to_run = to_check_keys(answer_to_check=given_answer, react_on_reconfig=0)
        if to_run == 'looping':
            continue

    return to_run, instances


def check_logic_config_file(given_cfg: Dict) -> int:
    print(given_cfg['input'])



def check_content_config_file(cfg_file) -> Tuple:
    message_from_content_validation: str = ''

    config_model = Schema(
        {
            "input": {
                "type": Or("cli", "file"),
                "input_from_file": {
                                "type_of_file": Or(None, "txt", "csv", 'json'),
                                "file": Or(None, Regex(r'(.*[\.json|\.txt|\.csv])$'))},
                "classes": {
                                "number_of_students": And(int, lambda n: 1 <= n <= 500),
                                Optional("number_of_classes"): And(int, lambda m: 1 <= m <= 8),
                                "type_of_classes": [Regex(r"^([A-Z][a-z]{1,}$)|^([A-Z][a-z]{1,}\s+[A-Z][a-z]{1,})$")]}
            },
            "output": {
                "type": Or('cli', 'file'),
                "output_to_file": {
                                "type_of_file": Or(None, "txt", "csv", 'json'),
                                "file": Or(None, Regex(r'(.*[\.txt|\.csv])$'))}
            },
            "logging": {
                "input_logging": {
                    "if_logging_input": Or(True, False),
                    "file_logging_input": Or(None, Regex(r'(.*[\.txt|\.log])$'))
                },
                "output_logging": {
                    "if_logging_output": Or(True, False),
                    "file_logging_output": Or(None, Regex(r'(.*[\.txt|\.log])$'))
                }
            }
        }
    )

    to_exit: int = 0
    try:
        config_model.validate(cfg_file)
        check_logic_config_file(cfg_file)
        message_from_content_validation = f"\n{' ' * 12} All good configuration is valid!"
    except SchemaError as pretty_error:
        message_from_content_validation = f"\n{' ' * 12} ERROR - there are some issues with config file!\n\n{pretty_error}"
        to_exit = 1

    return to_exit, message_from_content_validation


def validate_config_file(given_file: str) -> Tuple:
    config_content: Dict = {}
    exit_message: str = ''
    value_to_running: int = 0

    if '/' in given_file:
        processed_file_as_list: List[str] = list(i for i in given_file.split('/'))
        processed_dir: str = '/'.join(given_file[0:(len(processed_file_as_list)-1)])
        if not path.isdir(processed_dir):
            exit_message = f"\n{' ' * 12} ERROR - directory tree is not valid!"
    else:
        if not path.isfile(given_file):
            exit_message = f"\n{' ' * 12} ERROR - the file doesn't exists!"
        else:
            if path.getsize(given_file) == 0:
                exit_message = f"\n{' ' * 12} ERROR - config file exists but it is empty!"
            elif not match(r'(.*\.yml)|(.*\.yaml)$', given_file):
                exit_message = f"\n{' ' * 12} ERROR - .yml or .yaml is required!"

    if len(exit_message) != 0:
        value_for_running = 1
        return config_content, value_for_running, exit_message
    else:
        with open(given_file, 'r') as file_config_open:
            open_file: Dict = load(file_config_open, Loader=SafeLoader)

        return open_file, value_to_running


def main() -> None:
    instances: int = 0
    value_to_run: int = 0
    config_content: Dict = {}
    message_from_validation: str = ''

    printing_what_we_have()
    path_of_config_file, instances = ask_for_config(instances=0)
    config_content, value_to_run, message_from_validation = validate_config_file(given_file=path_of_config_file)
    value_to_run, message_from_validation = check_content_config_file(config_content)


if __name__ == '__main__':
    main()
