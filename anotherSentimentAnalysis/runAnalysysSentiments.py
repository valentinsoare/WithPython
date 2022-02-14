#!/usr/bin/python

import re
import sys
import string
import operator
import numpy as np
import pandas as pd


def load_text_for_analysis():
    print(f'\n\033[1;32m{"< SENTIMENT_ANALYSIS >":>84}\033[0m')
    print(f"\n\033[1m - > Enter the name of the file from current directory that you want to "
          f"analyze or entire path if the file is in another location (q to quit): ", end="\033[0m")
    given_text = input()

    if given_text.lower()[0] == "q":
        print(f'\n\033[1m{"Quitting...":>17}\033[0m\n')
        sys.exit(1)

    try:
        given_file = open(f"{given_text}", "r")
    except FileNotFoundError:
        print(f'\n\033[1;1;31m {"ERROR - file not found!!":>30}\033[0m', end="\n\n")
        sys.exit(0)

    words_from_text = np.array(given_file.read().split())

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
    dict_words = {}
    given_text = ' '.join(given_text)

    for searched_word in given_values_with_text.keys():
        for matching_word in re.finditer(r'(\b%s\b)' % searched_word, given_text):
            if matching_word.group() not in dict_words:
                dict_words[matching_word.group()] = 1
            else:
                dict_words[matching_word.group()] += 1

    return dict_words


def divide_word_positive_negative(given_list_of_matched_words, given_values_text):
    positive_words_values = {}
    negative_words_values = {}
    positive_freq = {}
    negative_freq = {}

    for word, freq in given_list_of_matched_words.items():
        if given_values_text[word] > 0:
            positive_words_values[word] = freq * given_values_text[word]
            positive_freq[word] = freq
        else:
            negative_words_values[word] = freq * given_values_text[word]
            negative_freq[word] = freq

    positive_freq = dict(sorted(positive_freq.items(), key=operator.itemgetter(1), reverse=True))
    negative_freq = dict(sorted(negative_freq.items(), key=operator.itemgetter(1), reverse=True))

    return positive_words_values, negative_words_values, positive_freq, negative_freq


def sort_words_and_calculate_per_type(words_positive, words_negative, positive_freq, negative_freq):
    number_of_positive_words = sum(filter(lambda l: l, positive_freq.values()))
    number_of_negative_words = sum(filter(lambda m: m, negative_freq.values()))

    positive_scoring = sum(filter(lambda i: i, words_positive.values()))
    negative_scoring = sum(filter(lambda j: j, words_negative.values()))

    return number_of_positive_words, number_of_negative_words, positive_scoring, negative_scoring


def print_dict_freq_output(input_dict, limit):
    count = 0

    for word, freq in input_dict.items():
        print(f'{"|":>7} {word:<15} |  {freq}  |')
        count += 1
        if count == limit:
            break


def printing_statistics_and_output(*args):
    p_frequency, n_frequency, l_positive, l_negative, p_scoring, n_scoring, text_to_process = args

    print(f"\n\033[1m Number of words in the processed text after removing punctuation: {len(text_to_process)}\033[0m",
          end="\n")

    if l_negative != 0:
        print(f"\n\033[1m *Negative words: {l_negative}\033[0m")
        print(f"\033[1m **Percentage of negative words: {(l_negative * 100)/len(text_to_process):.2f}\033[0m")
        print(f"\033[1m ***Top five negative words sorted by frequency:\033[0m")
        print(f'{"-" * 25:>31}')
        print_dict_freq_output(n_frequency, 5)
        print(f'{"-" * 25:>31}', end="\n")
    else:
        print(f"\n\033[1m *No negative words in the given text\033[0m", end="\n")

    if l_positive != 0:
        print(f"\n\033[1m *Positive words: {l_positive}\033[0m")
        print(f"\033[1m **Percentage of positive words: {(l_positive * 100) / len(text_to_process):.2f}\033[0m")
        print(f"\033[1m **Top five positive words sorted by frequency:\033[0m")
        print(f'{"-" * 25:>31}')
        print_dict_freq_output(p_frequency, 5)
        print(f'{"-"* 25:>31}', end="\n\n")
    else:
        print(f"\n\033[1m *No positive words in the given text.\033[0m", end="\n")


def main():
    text_to_check = load_text_for_analysis()
    words_with_values_to_use = load_file_with_words_value()

    text_to_process_after_removing_punctuation = remove_punctuation_text(text_to_check)

    matching_text_words_appearances = extracting_matched_words(text_to_process_after_removing_punctuation, words_with_values_to_use)

    positive_words_with_scoring, negative_words_with_scoring, positive_freq, negative_freq = divide_word_positive_negative(matching_text_words_appearances, words_with_values_to_use)
    number_positive, number_negative, pos_scoring, neg_scoring = sort_words_and_calculate_per_type(positive_words_with_scoring, negative_words_with_scoring, positive_freq, negative_freq)

    printing_statistics_and_output(positive_freq, negative_freq, number_positive, number_negative, pos_scoring, neg_scoring, text_to_process_after_removing_punctuation)


main()
