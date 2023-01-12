#!/usr/bin/python

from os import system
from typing import Dict, List, Tuple
from . import printing_phase as printing_stage
from . import header_load_settings_and_validate as loading_stage


def extract_from_config_file(given_cfg: Dict) -> Tuple:
    put_output_to_settings: Dict = {}
    take_input_from_settings: Dict = {}

    input_settings = given_cfg['input']
    if input_settings['type'] == 'cli':
        take_input_from = 'cli'
    else:
        take_input_from = 'file'
        take_input_from_settings = input_settings['input_from_file']

    classes_input_settings = input_settings['classes']

    output_settings = given_cfg['output']
    if output_settings['type'] == 'cli':
        put_output_to = 'cli'
    else:
        put_output_to = 'fli'
        put_output_to_settings = output_settings['output_to_file']

    logging_settings: Dict = given_cfg['logging']
    input_logging: Dict = logging_settings['input_logging']
    output_logging: Dict = logging_settings['output_logging']

    return take_input_from, take_input_from_settings, classes_input_settings, put_output_to, put_output_to_settings, \
        input_logging, output_logging


def validate_students(given_input: list, cfg_classes: Dict) -> Tuple:
    number_of_students_required = cfg_classes['number_of_students']
    error_message: str = f"\n{' ' * 12} ERROR - please enter {number_of_students_required} students and then we can proceed further."
    ok_message: str = f"\n{' ' * 12} All OK - {number_of_students_required} students were given."
    value_to_return: int = 0

    if len(given_input) != number_of_students_required:
        printing_stage.printing_messages(given_message=error_message, type_of_print='cli', type_of_sleep=2, same_line_cursor=0)
        value_to_return = 1
    else:
        printing_stage.printing_messages(given_message=ok_message, type_of_print='cli', type_of_sleep=2,
                                         same_line_cursor=0)

    return given_input, value_to_return


def load_students_grades_from_cli(classes_cfg: Dict) -> Tuple:
    running: int = 1
    validated_answer: List = []
    desired_number_of_students = classes_cfg['number_of_students']

    system('clear')
    loading_stage.printing_header_notebook(given_message='students grade book', if_upper=1, width=120, nr_of_newlines=1)

    message_to_use_for_intro: str = f"\n{' ' * 17} * We need at least three grades per student ({desired_number_of_students} students) for each class in this" \
                          f" list:\n{' ' * 17} [ {', '.join(classes_cfg['type_of_classes'])} ]......."
    printing_stage.printing_messages(message_to_use_for_intro, 'cli', type_of_sleep=3, same_line_cursor=1)

    message_for_asking_nr_students = f"\n{' ' * 20} * Please enter the name of {desired_number_of_students} students separated by a comma plus space after it\n" \
                                     f"{' ' * 23}(q to quit, or b to go back to reload config): "

    while running == 1:
        system('clear')
        loading_stage.printing_header_notebook(given_message='students grade book', if_upper=1, width=120,
                                               nr_of_newlines=1)

        printing_stage.printing_messages(message_for_asking_nr_students, 'cli', type_of_sleep=0.1, same_line_cursor=1)
        given_answer: str = input().strip()

        to_check: str = loading_stage.to_check_keys(given_answer, react_on_reconfig=0, react_on_back=1)
        if to_check == 'looping':
            continue
        elif to_check == 'back_to_config':
            return 'back_to_config', 1

        answer = given_answer.split(', ')

        validated_answer, running = validate_students(answer, classes_cfg)

    return validated_answer, 0


def load_content(where_to_load_content: str, input_config: Dict, output_config: Dict, classes_config: Dict) -> Tuple:
    what_to_do: int = 0
    value_loaded: List = []

    if where_to_load_content == 'cli':
        value_loaded, what_to_do = load_students_grades_from_cli(classes_cfg=classes_config)
        if value_loaded == 'back_to_config':
            return value_loaded, what_to_do



