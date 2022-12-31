#!/usr/bin/python


from time import sleep
from typing import Dict, Tuple, List


def printing_messages(given_message: str, type_of_print: str, file_to_print: str = '', type_of_sleep=2, same_line_cursor: int = 0) -> None:
    if type_of_print == 'cli':
        if same_line_cursor == 1:
            print(given_message, end="", flush=True)
        else:
            print(given_message, flush=True)
        sleep(type_of_sleep)
