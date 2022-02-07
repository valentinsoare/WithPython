#!/usr/bin/python

import re
import pandas as pd


def loading_text():
    print(f"\n\033[1m - > Enter the name of the file from current directory that you want to analyze: ", end="\033[0m")
    given_text = input()

    given_file = open(f"{given_text}", "r")
    return given_file.read()


def loading_file():
    words_values = pd.read_csv('scoring.csv', index_col=False, engine='c').to_records(index=False)
    dict_with_values_words = {i.lower(): j for i, j in words_values}

    return dict_with_values_words


def long_match(text_for_anal, text_values):

    for searched_word in text_values.keys():
        for matching_word  in re.finditer(r'\b%s\b' % searched_word, text_for_anal):
            print(matching_word)


def main():
    text_for_analysis = loading_text()
    file_with_values = loading_file()
    long_match(text_for_analysis, file_with_values)


main()
