#!/usr/bin/python

import re
import string
import numpy as np
import pandas as pd


def load_text_for_analysis():
    print(f"\n\033[1m - > Enter the name of the file from current directory that you want to analyze: ", end="\033[0m")
    given_text = input()

    given_file = open(f"{given_text}", "r")
    words_from_text = given_file.read().split()

    return words_from_text


def load_file_with_words_value():
    words_values = pd.read_csv('scoring.csv', index_col=False, engine='c').to_records(index=False)
    dict_with_values_words = {i.lower(): j for i, j in words_values}

    return dict_with_values_words


def remove_punctuation_text(given_text):
    array_after_removing = np.array([], dtype=str)
    punctuations = string.punctuation + ''.join(['”', '“', '’', '’'])

    for word in given_text:
        final_word = word.lower().translate(str.maketrans("", "", punctuations))
        array_after_removing = np.append(array_after_removing, final_word)

    return array_after_removing


def extracting_matched_words(given_text, given_values_with_text):
    matching_words = np.array([], dtype=str)

    given_text = ' '.join(given_text)

    for searched_word in given_values_with_text.keys():
        for matching_word in re.finditer(r'\b%s\b' % searched_word, given_text):
            matching_words = np.append(matching_words, matching_word.group())

    return matching_words


def divide_word_positive_negative(given_list_of_matched_words, given_values_text):
    positive_words_values = {}
    negative_words_values = {}

    for word in given_list_of_matched_words:
        if given_values_text[word] > 0:
            positive_words_values[word] = given_values_text[word]
        else:
            negative_words_values[word] = given_values_text[word]

    return positive_words_values, negative_words_values


def calculate_percentages(words_positive, words_negative, text_to_check):
    length_of_positive = len(words_positive)
    length_of_negative = len(words_negative)
    length_of_text_to_check = len(text_to_check)

    positive_scoring = sum(filter(lambda i: i, words_positive.values()))
    negative_scoring = sum(filter(lambda j: j, words_negative.values()))


def main():
    text_to_check = load_text_for_analysis()
    words_with_values_to_use = load_file_with_words_value()

    text_to_process_after_removing_punctuation = remove_punctuation_text(text_to_check)

    matching_text_words = extracting_matched_words(text_to_process_after_removing_punctuation, words_with_values_to_use)
    positive_words, negative_words = divide_word_positive_negative(matching_text_words, words_with_values_to_use)

    calculate_percentages(positive_words, negative_words, text_to_check)


main()
