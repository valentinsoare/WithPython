#!/usr/bin/python

import re
import pandas as pd
from time import sleep
from numpy import random
from yaml import safe_load
from os import path, system
from string import punctuation


def printing_header(given_message):
    message_to_print: str = '*#* '
    given_message = given_message.split()
    special_chars = list(punctuation)

    for word in range(len(given_message)):
        for letter in range(len(given_message[word])):
            random.shuffle(special_chars)
            value = random.randint(1, len(given_message[word]) - 1)
            if value == letter:
                message_to_print += f"{given_message[word][letter]}{special_chars[value]}"
            else:
                message_to_print += f"{given_message[word][letter]}"
        message_to_print += f" "

    message_to_print += '*#*'
    length_of_message: int = len(message_to_print)
    lines = f"{'-' * (2 * length_of_message - 20)}"

    print(f"\n{' ' * 15}{message_to_print:^{len(lines)}}", flush=True)
    print(f"{' ' * 15}{lines}", flush=True)


def load_configuration_with_pre_validation(given_config_file: str) -> tuple:
    cfg: dict = {}
    error: int = 0

    system('clear')
    printing_header('scrambling words')

    if not path.isfile(given_config_file):
        print(f"{' ' * 6}{'ERROR - given file'} \"{given_config_file}\" {'for configuration was not found.'}",
              flush=True)
        sleep(2)
        error = 1
    elif path.getsize(given_config_file) == 0:
        print(f"{' ' * 6}{'ERROR - given file'} \"{given_config_file}\" {'for configuration is empty'}",
              flush=True)
        sleep(2)
        error = 1
    else:
        with open(given_config_file, "r") as yml_config:
            cfg = safe_load(yml_config)

    return error, cfg


def checking_in_depth_file_content(given_dict: dict) -> int:
    value_of_error: int = 0

    for k, z in given_dict.items():
        if k == 'type' and (str(z).strip() == '' or z.lower() not in ['cli', 'file']):
            print(f'{" " * 6}{"ERROR - please use the right input value in configuration on"} "type" '
                  f'{"row:"} "cli" or "file".', flush=True)
            value_of_error = 1
            sleep(2)
        if k == 'if_file' and (str(z).strip() == '' or z not in [0, 1]):
            print(f'{" " * 6}{"ERROR - please put the proper argument in configuration on"} "if_file" '
                  f'{"line:"} "0" or "1".', flush=True)
            value_of_error = 1
            sleep(2)

        if value_of_error == 1:
            return 1

    if not (given_dict['type'] == 'cli' and given_dict['if_file'] == 0) and not (given_dict['type'] == 'file' and given_dict['if_file'] == 1):
        print(f'{" " * 6}{"ERROR - please put the proper argument in configuration on"} "if_file" and "type" to corespond one with the other.', flush=True)
        sleep(2)
        return 1

    return 0


def check_configuration_file_content(config_file_from_user: dict) -> int:
    configuration_for_input: dict
    configuration_for_output: dict

    def to_minimize(given_message_for_path: str, type_of_configuration: dict) -> int:
        for i, j in type_of_configuration.items():
            if checking_in_depth_file_content(type_of_configuration) == 1:
                return 1
            else:
                if i == 'file_entire_path' and type_of_configuration['if_file'] == 1 and (str(j).strip() == '' or
                                                                                          not path.isfile(j)):
                    print(f'{" " * 10}{given_message_for_path}', flush=True)
                    sleep(2)
                    return 1
        return 0

    configuration_for_input = config_file_from_user['input']
    message_to_use_for_path_input: str = f'{" " * 10}{"ERROR - please put the right argument in configuration on "} ' \
                                         f'"path"{"line where to load the file with words from."}'
    if to_minimize(message_to_use_for_path_input, configuration_for_input) == 1:
        return 1

    configuration_for_output = config_file_from_user['output']
    message_to_use_for_path_output: str = f'{"ERROR - please put the proper values in configuration on "}' \
                                          f'{"path line where to write the scrambled words."}'
    if to_minimize(message_to_use_for_path_output, configuration_for_output) == 1:
        return 1

    return 0


def validate_string_on_answering(answer_string: str) -> str:
    match answer_string:
        case 'q':
            print(f"\n{' ' * 6} Exiting...")
            sleep(2)
            exit(1)
        case 'b':
            print(f"\n{' ' * 6} Going back to loading configuration file...")
            sleep(2)
            return 'back_config'
        case 'c':
            print(f"\n{' ' * 6} Going forward to load text from the file...")
            sleep(2)
            return 'go_forward'

    if re.match(r'\s+', answer_string) or answer_string == '':
        print(f"\n{' ' * 6} ERROR - please do not use only whitespaces or enter.")
        sleep(2)
        return 'continue'


def ask_for_config_file() -> str:
    answer: str = ''
    error: int = 1

    while error == 1:
        system('clear')
        printing_header('scrambling words')

        print(f"{' ' * 2} * In order to start to use this script we need to load the configuration.\n{' ' * 1} "
              f"** Please enter the entire path of the config file (q to quit):", end=" ", flush=True)
        answer = input().strip()

        if validate_string_on_answering(answer) == 'continue':
            continue
        else:
            error = 0

    return answer


def load_text_from_cli() -> tuple:
    answer: str = ''
    to_break: int = 1
    processed_answer = ''

    while to_break == 1:
        system('clear')
        printing_header('scrambling words')
        print(f"{' ' * 3} * Please put the words that you want to be scrambled here\n{' ' * 2} ** Answer (q to quit b to back to cofig):", end=" ", flush=True)
        answer = input().strip()

        to_check = validate_string_on_answering(answer)
        if to_check == 'continue':
            continue
        elif to_check == 'back_config':
            return 1, answer

        try:
            processed_answer = int(answer)
        except ValueError:
            to_break = 0

        if len(answer.split()) <= 3 or isinstance(processed_answer, int):
            print(f"\n{' ' * 6} ERROR - please use only alphanumerical characters, "
                  f"but most preponderent alphabetic ones.",
                  flush=True)
            sleep(2)

    return 0, pd.Series(answer.split())


def parsing_config_file_and_decide(config_file_from_user: dict) -> tuple:

    def to_minimize(given_dict_with_config: dict) -> tuple:
        where_to: str = ''

        if given_dict_with_config['if_file'] == 1 and given_dict_with_config['type'] == 'file':
            where_to: str = given_dict_with_config['file_entire_path']
        elif given_dict_with_config['if_file'] == 0 and given_dict_with_config['type'] == 'cli':
            where_to: str = given_dict_with_config['type']

        type_of = given_dict_with_config['type']

        return where_to, type_of

    for_input = config_file_from_user['input']
    to_load_text_from, type_of_output_input = to_minimize(for_input)

    for_output = config_file_from_user['output']
    to_write_text_to, type_of_output_output = to_minimize(for_output)

    return to_load_text_from, type_of_output_input, to_write_text_to, type_of_output_output


def choose_text_from_file(given_path_of_file: str) -> tuple:

    while True:
        system('clear')
        printing_header('scrambling words')
        print(f"{' ' * 4}{'* We will loading text from'} \'{given_path_of_file.split('/')[-1]}\'"
              f"\n{' ' * 3}** (q to quit, b to put a new config file, f to go forward):"
              , end=" ", flush=True)
        answer = input().strip()

        to_check = validate_string_on_answering(answer)
        if to_check == 'continue':
            continue
        elif to_check == 'back_config':
            return 1, 'back_config'
        elif to_check == 'go_forward':
            with open(given_path_of_file, 'r') as file_with_text:
                loaded_text_in_string = file_with_text.read()
            return 0, pd.Series(loaded_text_in_string.split())

        print(f"\n{' ' * 6} ERROR - please use only one of those three options - q, f or b.", flush=True)
        sleep(2)


def main():
    loaded_cfg: dict = {}
    output_error: int = 0
    words_from_text: pd.Series() = []
    after_content_validation_error: int = 1

    while True:
        while after_content_validation_error == 1:
            config_file_from_user = ask_for_config_file()
            output_error, loaded_cfg = load_configuration_with_pre_validation(config_file_from_user)
            if output_error == 1:
                continue

            after_content_validation_error = check_configuration_file_content(loaded_cfg)

        load_text_from, type_of_input, write_text_to, type_of_output = parsing_config_file_and_decide(loaded_cfg)

        if type_of_input == 'cli':
            after_content_validation_error, words_from_text = load_text_from_cli()
        elif type_of_input == 'file':
            after_content_validation_error, words_from_text = choose_text_from_file(load_text_from)


if __name__ == '__main__':
    main()
