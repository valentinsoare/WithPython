# variousChecking.py

from os import system
from time import sleep
from typing import Union
from re import split, match
from collections import namedtuple


def _check_if_str(given_value) -> str:
    flag_to_use: bool = False
    to_return: Union[str, float] = ''

    if given_value == '' or match(r'\s+', given_value):
        flag_to_use = True
    else:
        try:
            to_return = float(given_value)
        except ValueError:
            to_return = given_value

    if isinstance(to_return, float) or flag_to_use:
        to_return = 'POL1005'
        print(f"\n{' ' * 3} \033[31mPOL1005 - Given value value should be a string!\033[0m\n", flush=True)
        sleep(2)

    return to_return


def _check_if_numeric(given_value: Union[float, str, int]) -> Union[str, float]:
    try:
        to_return: Union[str, float] = float(given_value)
    except ValueError:
        to_return = 'POL1006'
        print(f"\n{' ' * 3} \033[31mPOL1006 - Given value {given_value} should be a string - but numeric value, "
              f"float or integer!\033[0m\n", flush=True)
        sleep(2)

    return to_return


def _for_name_checking(given_name) -> str:
    first_last: list = list(map(lambda i: i.capitalize(), split(r',\s*|\s+', given_name)))

    if given_name == '' or match(r'\s+', given_name) or len(first_last) != 2:
        print(f"\n{' ' * 3} \033[31mPOL1007 - Name should be a string with first name and last name "
              f"separated by a comma and a space, or just a comma!\033[0m\n")
        sleep(2)
        return 'POL1007'

    else:
        return ', '.join(first_last)


def _working_on_grades_from_add(*args) -> tuple:
    grade_with_exceptions_type: Union[list, None] = []
    course, *grades_to_add = args

    course = _check_if_str(course)

    for i, j in enumerate(grades_to_add):
        action: Union[str, float] = _check_if_numeric(j)
        if action == '-1':
            grade_with_exceptions_type.append(i)
        else:
            grades_to_add[i] = action

    if len(grade_with_exceptions_type) != 0:
        grades_to_add = list(float(j) for j in grades_to_add if j not in grade_with_exceptions_type)
    else:
        grade_with_exceptions_type = None

    return course, grades_to_add, grade_with_exceptions_type


def _check_address(address: str) -> namedtuple:
    print_message = """POL1008 - Address should be a string containing at least the name of the street and number \
separated by a comma and space or just a comma!"""
    split_address: list = []

    for i in split(r',\s*', address):
        if len(split(r'\s+', i)) > 1:
            split_address.append(' '.join(j.capitalize() for j in split(r'\s+', i)))
        else:
            split_address.append(i.capitalize())

    if not isinstance(address, str) or len(split_address) < 2:
        print(f"\n{' ' * 3} \033[31m{print_message}\033[0m\n")
        sleep(2)
        return 'POL1008'

    given_address = namedtuple(typename='given_address',
                               field_names=['street', 'house_number', 'building',
                                            'apartment', 'district', 'city', 'zipcode'])
    given_address.__new__.__defaults__ = (None,) * len(given_address._fields)
    current_address = given_address(*split_address)

    return current_address


def _print_banner(grade_book_class: str, short_print: bool = False) -> int:
    system('clear')

    if short_print:
        name_of_book: str = f"{grade_book_class}"
    else:
        name_of_book: str = f"{grade_book_class} {'Grade book'}"

    length_of_name: int = len(name_of_book)
    white_space: int = ((6 * length_of_name) // 2 - (length_of_name // 2))

    print(f"\n{' ' * 8}\033[1;32m{'-' * (6 * length_of_name)}\033[0m", flush=True)
    print(f"{' ' * 8}\033[1;32m|\033[0m\033[1;1;42m{' ' * white_space}{name_of_book}"
          f"{' ' * (white_space - 3)}\033[0m\033[1;32m|\033[0m", flush=True)
    print(f"{' ' * 8}\033[1;32m{'-' * (6 * length_of_name)}\033[0m", flush=True)

    return 6 * length_of_name


def _check_if_integer(given_value: str, return_tuple: bool = True) -> Union[tuple, str, int]:
    try:
        to_return: Union[int, str] = int(given_value)
        to_exit = True
    except ValueError:
        if given_value == 'b':
            to_return = -1
            to_exit = True
        else:
            to_return = 'POL1010'
            print(f"\n{' ' * 3} \033[31mPOL1010 - Given value should be a string - "
                  f"but numeric value, only an integer!\033[0m\n", flush=True)
            sleep(2)
            to_exit = False

    if return_tuple:
        return to_return, to_exit
    else:
        return to_return


def _ask_how_many_students(name_of_class: str) -> Union[int, str]:
    to_exit: bool = False
    number_of_students_to_add: Union[str, int, float] = ''

    while not to_exit:
        _print_banner(grade_book_class=_check_if_str(name_of_class))
        print(f"{' ' * 8}{'[Option 1 Selected] Register student...'}")

        print(f"\n{' ' * 8} * Number of students (q to quit/b for back):", end=" ", flush=True)
        how_many_students: str = input()

        number_of_students_to_add, to_exit = _check_if_integer(_check_input_quit_or_back(how_many_students))

    return number_of_students_to_add


def _check_if_bool(given_value: str) -> str:
    if given_value not in ['True', 'False']:
        print(f"\n{' ' * 3} \033[31mPOL1011 - {given_value} should be a boolean!\033[0m\n", flush=True)
        sleep(2)
        to_return = 'POL1011'
    else:
        to_return = given_value

    return to_return


def _check_strings_instances_to_list_for_teacher_names(given_value: str) -> list:
    return [', '.join((j.capitalize() for j in split(r',\s*|\s+', i))) for i in split(r';\s*', _check_if_str(given_value))]


def _check_strings_instances_to_list_for_classes(given_value: str) -> list:
    return list(map(lambda i: i.capitalize(), split(r';\s*|\s+', _check_if_str(given_value))))


def _ask_for_students_details(number_of_students_to_add: int, name_of_class: str) -> Union[dict, int]:
    list_of_parameters: list = [('name', _for_name_checking), ('age', _check_if_numeric),
                                ('address', _check_address), ('employed', _check_if_bool),
                                ('classes', _check_strings_instances_to_list_for_classes),
                                ('teacher_name', _check_strings_instances_to_list_for_teacher_names)]
    i: int = 0
    count_student: int = 0
    students_added: dict = {i: {} for i in range(number_of_students_to_add)}

    while i < len(list_of_parameters) and count_student < number_of_students_to_add:
        system('clear')
        _print_banner(grade_book_class=name_of_class)

        print(f"""{' ' * 8} [Option 1 Selected] Registering {number_of_students_to_add - count_student} students left...
         (q to quit/b to main menu/u for one step back)\n""", flush=True)

        print(f"{' ' * 10}{i}. {list_of_parameters[i][0].capitalize()}:", end=" ", flush=True)
        value_from_user: str = _back_to_previous_entry(_check_input_quit_or_back((input())))

        if value_from_user == 'b':
            return -1
        elif value_from_user == 'u':
            if len(students_added[count_student]) != 0:
                students_added[count_student].popitem()

                if i == 0 and not students_added[0].values():
                    return -1
                i -= 1
            else:
                if count_student == 0:
                    return -1
                count_student -= 1
                i = len(students_added[count_student]) - 1
        else:
            after_checking = list_of_parameters[i][1](value_from_user)

            if ('POL' or 'ERR') in str(after_checking):
                continue

            students_added[count_student].update({list_of_parameters[i][0]: after_checking})

            if i == 5:
                i = 0
                count_student += 1
            else:
                i += 1

    return students_added


def _check_input_quit_or_back(given_value: str) -> Union[str, int]:
    if given_value.lower() == 'q':
        print(f"\n{' ' * 8} \033[1;32m Exiting...\033[0m\n", flush=True)
        sleep(2)
        exit(1)
    elif given_value.lower() == 'b':
        print(f"\n{' ' * 8} \033[1;32m Going back to previous menu...\033[0m", flush=True)
        sleep(2)

    return given_value


def _back_to_previous_entry(given_input: str) -> str:
    if given_input.lower() == 'q':
        print(f"\n{' ' * 8} \033[1;32m Exiting...\033[0m\n", flush=True)
        sleep(2)
        exit(1)
    elif given_input.lower() == 'u':
        print(f"\n{' ' * 8} \033[1;32m Going one step back...\033[0m", flush=True)
        sleep(2)

    return given_input


def _load_grade_book_prerequisites() -> dict:
    questions_for_intro: list = [('The name of the class', _check_if_str),
                                 ('How many students', _check_if_integer),
                                 ('Class headmaster', _for_name_checking)]

    i: int = 0
    answers_prerequisites: dict = {}
    length_of_list_questions: int = len(questions_for_intro)

    while i < length_of_list_questions:
        system('clear')
        _print_banner(grade_book_class='Loading....', short_print=True)
        print(f"{' ' * 12}[ Loading prerequisites (q to quit/u for one step back) ]")
        print(f"\n{' ' * 10}{i + 1}. {questions_for_intro[i][0]}:", end=" ", flush=True)
        answer: str = _back_to_previous_entry(input())

        if i == 1:
            after_checking: int = questions_for_intro[i][1](answer, return_tuple=False)
        else:
            after_checking: str = questions_for_intro[i][1](answer)

        if after_checking == 'u':
            if len(answers_prerequisites.values()) == 0:
                print(f"\n{' ' * 8} \033[1;32m There are no more answers available - exiting...\033[0m\n", flush=True)
                sleep(2)
                exit(1)
            answers_prerequisites.popitem()
            i -= 1
        else:
            if 'POL' in str(after_checking):
                continue
            answers_prerequisites.update({questions_for_intro[i][0]: after_checking})

            i += 1

    return answers_prerequisites


def _printing_content(line_separator_length: int):
    message_to_print = """In order to start the application and create the 
            initial grade book we will need the following:
        class name, number of students and class headmaster!"""
    print(f"{' ' * 10}{message_to_print}", flush=True)
    print(f"{' ' * 8}\033[1;32m{'-' * line_separator_length}\033[0m", flush=True)
    sleep(3)


def _intro_to_app() -> dict:
    length_of_line_sep = _print_banner(grade_book_class='Loading..', short_print=True)
    _printing_content(length_of_line_sep)
    values_to_start_grade_book: dict = _load_grade_book_prerequisites()

    return values_to_start_grade_book
