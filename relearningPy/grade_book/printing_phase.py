#!/usr/bin/python

from time import sleep


def printing_messages(given_message, type_of_print, file_to_print='', type_of_sleep=2):
    if type_of_print == 'cli':
        print(given_message, flush=True)

        sleep(type_of_sleep)
