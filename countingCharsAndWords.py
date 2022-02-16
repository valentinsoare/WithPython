#!/usr/bin/python

import re


def catching_input():
    print(f"\n\033[1m - > Please provide a text to analyze:\033[0m", end=" ")
    given_text = input()

    return given_text


def processing_given_text(given_string):
    digits = re.findall(r'\d{1,}', given_string)
    words = re.findall(r'[a-zA-Z]{1,}', given_string)
    non_digits = re.findall(r'[^\w\s]', given_string)
    whitespaces = re.findall(r'[\s]{1,}', given_string)

    return words, digits, non_digits, whitespaces


def printing_output(*args):
    words, digits, non_digits, whitespaces = args

    print(f'\n\033[1m{"*Counting type of characters:":>32}\033[0m', end=" ")
    print(f"\n\t- Words: length {len(words)}, {words}")
    print(f"\t- Digits: {len(digits)}, {digits}")
    print(f"\t- Non digits: {len(non_digits)}, {non_digits}")
    print(f"\t- Whitespaces: {len(whitespaces)}, {whitespaces}")


def main():
    given_string = catching_input()
    words, digits, non_digits, whitespaces = processing_given_text(given_string)
    printing_output(words, digits, non_digits, whitespaces)



main()
