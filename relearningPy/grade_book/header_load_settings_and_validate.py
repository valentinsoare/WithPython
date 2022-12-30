#!/usr/bin/python


from time import sleep
from re import sub, match
from random import shuffle
from os import system, path
from string import punctuation
from yaml import load, SafeLoader
import printing_phase as printing_stage
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
            instances = 0

    return to_run, instances


def check_logic_config_file(given_cfg: Dict) -> Tuple:
    error_value: int = 0
    error_message: str = ''
    classes_list: list = list(given_cfg['input']['classes'].items())

    if classes_list[1][1] != len(classes_list[2][1]):
        error_message: str = f"\n{' ' * 12} ERROR please check the how manu classes you put in number of classes and in the list with type of classes!"
        error_value = 1

    return error_value, error_message


def check_content_config_file(cfg_file) -> Tuple:
    message_from_content_validation: str = ''

    config_model = Schema(
        {
            "input": {
                "type": Or("cli", "file"),
                "input_from_file": {
                                "take_from_file": Or(True, False),
                                "type_of_file": Or(None, "txt", "csv", 'json'),
                                "file": Or(None, Regex(r'(.*[\.json|\.txt|\.csv])$'))
                },
                "classes": {
                                "number_of_students": And(int, lambda n: 1 <= n <= 500),
                                Optional("number_of_classes"): And(int, lambda m: 1 <= m <= 8),
                                "type_of_classes": [Regex(r"^([A-Z][a-z]{1,}$)|^([A-Z][a-z]{1,}\s+[A-Z][a-z]{1,})$")]
                }
            },
            "output": {
                "type": Or('cli', 'file'),
                "output_to_file": {
                                "put_to_file": Or(True, False),
                                "type_of_file": Or(None, "txt", "csv", 'json'),
                                "file": Or(None, Regex(r'(.*[\.txt|\.csv])$'))
                }
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
        to_exit, message_from_content_validation = check_logic_config_file(given_cfg=cfg_file)
        if to_exit == 1:
            printing_stage.printing_messages(given_message=message_from_content_validation, type_of_print='cli', type_of_sleep=3)
            return to_exit, message_from_content_validation
        else:
            message_from_content_validation = f"\n{' ' * 12}All good, content checked and configuration is valid!"
    except SchemaError as validation_error:
        to_exit = 1
        message_from_content_validation = f"\n{' ' * 12} ERROR - there are some issues with config file!\n\n{validation_error}"

    printing_stage.printing_messages(given_message=message_from_content_validation, type_of_print='cli', type_of_sleep=3)
    return to_exit, message_from_content_validation


def validate_config_file(given_file: str) -> Tuple:
    config_content: Dict = {}
    exit_message: str = ''
    value_for_running: int = 0

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
    else:
        with open(given_file, 'r') as file_config_open:
            config_content = load(file_config_open, Loader=SafeLoader)

        exit_message = f"\n{' ' * 12}All OK with config file itself, but not content. Also this will be checked!"

    printing_stage.printing_messages(given_message=exit_message, type_of_print='cli', type_of_sleep=2)
    return config_content, value_for_running, exit_message
