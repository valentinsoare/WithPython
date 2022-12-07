#!/usr/bin/python

import os
import re
import time


def header(given_message):
    given_message = given_message.split()
    processed_message = '** '

    for i in given_message:
        processed_message += '_'.join(list(i)) + ' '

    processed_message += '**'

    length_of_processed_message = len(processed_message)
    line_to_use = f"{'#' * (2 * length_of_processed_message)}"

    print(f"\n{' ' * 10}{processed_message:^{len(line_to_use)}}")
    print(f"{' ' * 10}{line_to_use}")


def catch_given_phrase():
    error = 1

    while error == 1:
        os.system('clear')
        header('Comparing Strings')
        print(f"{' * Strings, but with alnum chars, to compare:'}", end=" ")

        answer = input()

        if len(answer) == 0 or re.match(r'\s+', answer):
            print(f"\n{' ' * 3}{'ERROR - we need an input as strings with alnum chars to compare.'}")
            time.sleep(2)
        else:
            return answer


def tokenize_the_input_and_extract_only_selected(given_input, selection_var):
    tokenized_input = given_input.split()
    list_with_selected = []

    for i in tokenized_input:
        if i[0] == selection_var:
            list_with_selected.append(i)

    return set(list_with_selected)


def printing_selected_words(given_set, filter_to_select):
    var_to_print = ', '.join(given_set)
    print(f"\n{' ** Words selected with letter '}\"{filter_to_select}\" at the beginning:", end=" ")
    print(f"{var_to_print}")


def main():
    select_category = 'b'

    input_from_user = catch_given_phrase()
    selected_elements = tokenize_the_input_and_extract_only_selected(input_from_user, select_category)

    printing_selected_words(selected_elements, select_category)


if __name__ == '__main__':
    main()
