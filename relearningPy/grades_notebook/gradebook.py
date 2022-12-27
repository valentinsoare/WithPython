#!/usr/bin/python


import csv
import json
import random

import math
from os import system
from time import sleep
from typing import List, Union
from string import punctuation
from random import randrange, shuffle


def create_line(size_of_multiply: Union[int | float], size_of_string: int) -> str:
    final_string_as_line: str = ''
    initial_list_as_punctuation: list = (list(punctuation))[0:size_of_string]
    limit_of_string = round(len(initial_list_as_punctuation) * size_of_multiply)
    size_to_reach: int = limit_of_string

    to_run: bool = True
    random.shuffle(initial_list_as_punctuation)

    while to_run:
        for i in range(limit_of_string):

            if i == (len(initial_list_as_punctuation) - 1):
                random.shuffle(initial_list_as_punctuation)
                limit_of_string -= len(initial_list_as_punctuation)
                final_string_as_line += initial_list_as_punctuation[i]
                break

            final_string_as_line += initial_list_as_punctuation[i]

        if len(final_string_as_line) == size_to_reach:
            to_run = False

    return final_string_as_line


def printing_header_notebook(given_message: str) -> None:
    line_to_print = create_line(1.5, len(punctuation))




def main() -> None:
    printing_header_notebook('students grade book')


if __name__ == '__main__':
    main()
