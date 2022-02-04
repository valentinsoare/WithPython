#!/usr/bin/python

import pandas as pd


def load_text_for_analysis():
    print(f"\n\033[1m - > Enter the name of the file from current directory that you want to analyze: ", end="\033[0m")
    given_text = input()

    given_file = open(f"{given_text}", "r")
    words_from_text = pd.Series(given_file.read().split())

    return words_from_text


def load_file_with_words_value():
    words_values = pd.read_csv('scoring.csv', index_col=False, engine='c').to_records(index=False)
    dict_with_values_words = {i: j for i, j in words_values}

    return dict_with_values_words

#def processing_words(given_series):


def main():
    text_to_check = load_text_for_analysis()
    words_with_values_to_use = load_file_with_words_value()

    
main()

