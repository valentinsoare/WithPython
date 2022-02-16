#!/usr/bin/python

import re
from sys import exit
from time import sleep


def catch_input_as_urls():
    print(f'\n\033[1m\t - > Please enter the urls to be parsed (q to quit):\033[0m', end=" ")
    given_urls = input()

    if given_urls.lower()[0] == "q":
        print(f'\n\033[1;33m{"Quitting...":>25}', end="\n\n")
        sleep(1)
        exit(1)

    return given_urls


def processing_string(input_text):
    valid_url_pattern = re.compile(r"[https|http]+://[a-z0-9]*\.[a-z0-9]{2,}\.[a-z]{2,}|[https|http]+://[a-z0-9]{2,}\.[a-z]{2,}")
    urls_extracted = re.findall(valid_url_pattern, input_text)

    return urls_extracted


def printing_output(given_list_with_urls):
    print(f'\n\033[1m{"*Valid urls extracted from the given text:":>52}\033[0m', end=" ")
    print(f'{given_list_with_urls}')


def main():
    given_string = catch_input_as_urls()
    valid_urls = processing_string(given_string)

    printing_output(valid_urls)


main()
