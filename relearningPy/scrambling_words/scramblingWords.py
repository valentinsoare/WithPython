#!/usr/bin/python


import logging
from re import match
from time import sleep
from numpy import random
from pandas import Series
from yaml import safe_load
from os import path, system
from string import punctuation
from pyparsing import Word, alphas
from typing import List, AnyStr, Dict, Tuple


def printing_header(given_message: AnyStr) -> None:
    message_to_print: AnyStr = '*#* '
    given_message: List[str] = given_message.split()
    special_chars: List[str] = list(punctuation)

    for word in range(len(given_message)):
        for letter in range(len(given_message[word])):
            random.shuffle(special_chars)
            value: int = random.randint(1, len(given_message[word]) - 1)
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


def load_configuration_with_pre_validation(given_config_file: AnyStr) -> Tuple:
    cfg: Dict = {}
    error: int = 0

    system('clear')
    printing_header('scrambling words')

    if not path.isfile(given_config_file):
        print(f"{' ' * 6}{'ERROR - given file'} \"{given_config_file}\" {'for configuration was not found.'}",
              flush=True)
        sleep(2)
        error: int = 1
    elif path.getsize(given_config_file) == 0:
        print(f"{' ' * 6}{'ERROR - given file'} \"{given_config_file}\" {'for configuration is empty'}",
              flush=True)
        sleep(2)
        error: int = 1
    else:
        with open(given_config_file, "r") as yml_config:
            cfg: AnyStr = safe_load(yml_config)

    return error, cfg


def checking_in_depth_file_content(given_dict: Dict) -> int:
    value_of_error: int = 0

    for k, z in given_dict.items():
        if k == 'type' and (str(z).strip() == '' or z.lower() not in ['cli', 'file']):
            print(f'{" " * 6}{"ERROR - please use the right input value in configuration on"} "type" '
                  f'{"row:"} "cli" or "file".', flush=True)
            value_of_error: int = 1
            sleep(2)
        if k == 'if_file' and (str(z).strip() == '' or z not in [0, 1]):
            print(f'{" " * 6}{"ERROR - please put the proper argument in configuration on"} "if_file" '
                  f'{"line:"} "0" or "1".', flush=True)
            value_of_error: int = 1
            sleep(2)

        if value_of_error == 1:
            return 1

    if not (given_dict['type'] == 'cli' and given_dict['if_file'] == 0) and not (given_dict['type'] == 'file' and given_dict['if_file'] == 1):
        print(f'{" " * 6}{"ERROR - please put the proper argument in configuration on"} "if_file" and "type" to corespond one with the other.', flush=True)
        sleep(2)
        return 1

    return 0


def check_configuration_file_content(config_file_from_user: Dict) -> int:
    configuration_for_input: Dict
    configuration_for_output: Dict

    def to_minimize(given_message_for_path: AnyStr, type_of_configuration: Dict) -> int:
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

    configuration_for_input: Dict = config_file_from_user['input']
    message_to_use_for_path_input: AnyStr = f'{" " * 10}{"ERROR - please put the right argument in configuration on "} ' \
                                         f'"path"{"line where to load the file with words from."}'
    if to_minimize(message_to_use_for_path_input, configuration_for_input) == 1:
        return 1

    configuration_for_output: Dict = config_file_from_user['output']
    message_to_use_for_path_output: AnyStr = f'{"ERROR - please put the proper values in configuration on "}' \
                                          f'{"path line where to write the scrambled words."}'
    if to_minimize(message_to_use_for_path_output, configuration_for_output) == 1:
        return 1

    return 0


def validate_string_on_answering(answer_string: AnyStr) -> AnyStr:
    match answer_string:
        case 'q':
            print(f"\n{' ' * 6} Exiting...\n", flush=True)
            sleep(1)
            exit(1)
        case 'b':
            print(f"\n{' ' * 6} Going back to loading configuration file...", flush=True)
            sleep(2)
            return 'back_config'
        case 'f':
            print(f"\n{' ' * 6} Going forward to load text from the file...", flush=True)
            sleep(2)
            return 'go_forward'
        case 'p':
            print(f"\n{' ' * 6} Write new text in the cli...", flush=True)
            sleep(2)
            return 'new_text_cli'

    if match(r'\s+', answer_string) or answer_string == '':
        print(f"\n{' ' * 6} ERROR - please do not use only whitespaces or enter.")
        sleep(2)
        return 'continue'


def ask_for_config_file() -> AnyStr:
    answer: AnyStr = ''
    error: int = 1

    while error == 1:
        system('clear')
        printing_header('scrambling words')

        print(f"{' ' * 2} * In order to start to use this script we need to load the configuration.\n{' ' * 1} "
              f"** Please enter the entire path of the config file (q to quit):", end=" ", flush=True)
        answer: AnyStr = input().strip()

        if validate_string_on_answering(answer) == 'continue':
            continue
        else:
            error = 0

    return answer


def load_text_from_cli() -> Tuple:
    answer: AnyStr = ''
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
            processed_answer: int = int(answer)
        except ValueError:
            to_break = 0

        if len(answer.split()) < 1 or isinstance(processed_answer, int):
            print(f"\n{' ' * 6} ERROR - please use only alphanumerical characters, "
                  f"but most preponderent alphabetic ones.",
                  flush=True)
            sleep(2)

    return 0, Series(answer.split())


def parsing_config_file_and_decide(config_file_from_user: Dict) -> Tuple:

    def to_minimize(given_dict_with_config: Dict) -> Tuple:
        where_to: AnyStr = ''

        if given_dict_with_config['if_file'] == 1 and given_dict_with_config['type'] == 'file':
            where_to = given_dict_with_config['file_entire_path']
        elif given_dict_with_config['if_file'] == 0 and given_dict_with_config['type'] == 'cli':
            where_to = given_dict_with_config['type']

        type_of: Dict = given_dict_with_config['type']

        return where_to, type_of

    for_input = config_file_from_user['input']
    to_load_text_from, type_of_output_input = to_minimize(for_input)

    for_output = config_file_from_user['output']
    to_write_text_to, type_of_output_output = to_minimize(for_output)

    return to_load_text_from, type_of_output_input, to_write_text_to, type_of_output_output


def choose_text_from_file(given_path_of_file: AnyStr) -> Tuple:

    while True:
        system('clear')
        printing_header('scrambling words')
        print(f"{' ' * 4}{'* We will loading text from'} \'{given_path_of_file.split('/')[-1]}\'"
              f"\n{' ' * 3}** (q to quit, b to put a new config file, f to go forward):"
              , end=" ", flush=True)
        answer: AnyStr = input().strip()

        to_check: AnyStr = validate_string_on_answering(answer)
        if to_check == 'continue':
            continue
        elif to_check == 'back_config':
            return 1, 'back_config'
        elif to_check == 'go_forward':
            with open(given_path_of_file, 'r') as file_with_text:
                loaded_text_in_string = file_with_text.read()
            return 0, Series(loaded_text_in_string.split())

        print(f"\n{' ' * 6} ERROR - please use only one of those three options - q, f or b.", flush=True)
        sleep(2)


def creating_text_parser_for_level(given_level_of_log) -> AnyStr:
    log_pattern = Word(alphas) + '.' + Word(alphas)

    for log in ['logging.DEBUG', 'logging.INFO', 'logging.WARNING', 'logging.ERROR', 'logging.CRITICAL']:
        log_level = log_pattern.parseString(log)
        if log_level[2].lower() == given_level_of_log:
            return ''.join(log_level)

    raise ValueError('Please use one of the five classic log levels.')


def locate_punctuation_and_save_and_remove_punctuation_from_word(given_word_from_input: str) -> Tuple:
    punctuation_to_locate: AnyStr = '!"#$%&\'()*+,./:;<=>?[\]`{|}~'
    word_after_punctuation: AnyStr = given_word_from_input.translate(str.maketrans('', '', punctuation_to_locate))
    list_with_punctuation_location: List[Tuple[str, int]] = []

    for i in range(len(given_word_from_input)):
        if given_word_from_input[i] in punctuation_to_locate and (0 <= i <= 2 or (len(given_word_from_input) - 3) <= i <= (len(given_word_from_input) - 1)):
            list_with_punctuation_location.append((given_word_from_input[i], i))

    return list(word_after_punctuation), list_with_punctuation_location


def insert_punctuation(word_without_punctuation: AnyStr, our_punctuation: List) -> AnyStr:
    word_without_punctuation = list(word_without_punctuation)

    for sign, location in our_punctuation:
        word_without_punctuation.insert(location, sign)

    return ''.join(word_without_punctuation)


def start_scrambling_words(given_words_with_punctuation: Series(dtype=object)) -> Series:
    words_after_scrambling: List = []

    for i, j in given_words_with_punctuation.items():
        word_after_punctuation, signs_location = locate_punctuation_and_save_and_remove_punctuation_from_word(j)
        if len(word_after_punctuation) > 3:
            word_to_shuffle: List = list(word_after_punctuation[1:(len(word_after_punctuation) - 1)])
            random.shuffle(word_to_shuffle)
            final_word: AnyStr = word_after_punctuation[0] + ''.join(word_to_shuffle) + word_after_punctuation[len(word_after_punctuation) - 1]

            final_word: AnyStr = insert_punctuation(final_word, signs_location)
            words_after_scrambling.append(final_word)
        else:
            words_after_scrambling.append(j)

    return Series(words_after_scrambling)


def printing_text_to_cli(given_words_scrambled: Series) -> Tuple:
    processed_answer: AnyStr = ''

    while processed_answer not in ['q', 'b', 'p']:
        system('clear')
        printing_header('scrambling words')
        text_as_string: AnyStr = ''

        text_as_string += ' '.join(i for i in given_words_scrambled.values)

        print(f"{' ' * 4} * Text after scrambling......", flush=True)
        print(f"\n{' ' * 3}\"{text_as_string}\"\n", flush=True)
        sleep(1)

        print(f"{' ' * 3} ** q to quit, b to load a new config file, p to put new text in cli:", end=" ", flush=True)
        given_answer = input().strip()

        to_check = validate_string_on_answering(given_answer)
        if to_check == 'continue':
            continue
        elif to_check == 'back_config':
            return 1, given_answer
        elif to_check == 'new_text_cli':
            return 0, given_answer
        else:
            print(f"{' ' * 6} ERROR - please choose one eof those options, q, b or p.\n", flush=True)
            sleep(2)


def printing_the_text_to_file(logging_level_to_use: AnyStr, file_to_write_to: AnyStr, words_to_write: Series()) -> Tuple:
    given_level: AnyStr = creating_text_parser_for_level(logging_level_to_use)

    while True:
        system('clear')
        printing_header('scrambling words')

        txt_to_print_in_log: AnyStr = ' '.join(words_to_write.values)

        logging.basicConfig(filename=file_to_write_to,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            datefmt='%d/%m/%Y %I:%M:%S %p',
                            level=eval(given_level))

        action_to_use: AnyStr = given_level.lower() + f"(txt_to_print_in_log)"
        eval(action_to_use)

        print(f"{' ' * 4} * Scrambled words were printed in the file...", flush=True)
        print(f"{' ' * 3} ** q to quit, b to load again the config file:", end=" ", flush=True)
        given_answer = input().strip()

        to_check = validate_string_on_answering(given_answer)
        if to_check == 'continue':
            continue
        elif to_check == 'back_config':
            return 1, given_answer
        else:
            print(f"\n{' ' * 6} ERROR - please choose one of those options, q or b.\n", flush=True)
            sleep(2)


def main():
    loaded_cfg: Dict = {}
    output_error: int = 0
    words_from_text = Series(dtype=object)
    after_content_validation_error: int = 1

    while True:
        while after_content_validation_error == 1:
            config_file_from_user = ask_for_config_file()
            output_error, loaded_cfg = load_configuration_with_pre_validation(config_file_from_user)
            if output_error == 1:
                continue

            after_content_validation_error = check_configuration_file_content(loaded_cfg)

        load_text_from, type_of_input, write_text_to, type_of_output = parsing_config_file_and_decide(loaded_cfg)

        while after_content_validation_error == 0:
            if type_of_input == 'cli':
                after_content_validation_error, words_from_text = load_text_from_cli()
            elif type_of_input == 'file':
                after_content_validation_error, words_from_text = choose_text_from_file(load_text_from)

            words_after_scrambling_with_punctuation = start_scrambling_words(words_from_text)

            if type_of_output == 'cli':
                after_content_validation_error, text = printing_text_to_cli(words_after_scrambling_with_punctuation)
            elif type_of_output == 'file':
                logging_level = loaded_cfg['output']['logging_level']
                after_content_validation_error, text = printing_the_text_to_file(logging_level, write_text_to,
                                                                                 words_after_scrambling_with_punctuation)


if __name__ == '__main__':
    main()
