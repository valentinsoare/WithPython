#!/usr/bin/python

# book analysis without NLP

import re
import pandas as pd
from sys import exit
from os import system
from time import sleep
from statistics import mean
from string import punctuation
from operator import itemgetter


def for_quit(input_var):
    if input_var.lower()[0] == 'q':
        print(f'\n\033[1;33m{"Quitting...":>18}\033[0m', end="\n\n")
        sleep(1)
        exit(0)


def catch_input_text():
    opening_file = ''
    to_continue = 0

    system('clear')
    print(f'\n {"- > Enter the book in txt file in order to analyse (q to quit):":>40}', end=" ")
    txt_file = input()

    for_quit(txt_file)

    try:
        opening_file = open(txt_file, mode='r')
    except FileNotFoundError:
        print(f'\n\033[1;31m{"ERROR - file not found":>30}\033[0m\n')
        sleep(1)
    else:
        to_continue = 1

    return opening_file, to_continue


def reading_the_file(file_open):
    with file_open:
        intermediary = file_open.read()
        file_open_read = pd.Series(intermediary.split(), dtype=str)

    return intermediary, file_open_read


def work_on_text_remove_punctuation(given_series):
    punctuations = punctuation + '”“’'
    length_of_series = len(given_series)

    for i in range(length_of_series):
        given_series[i] = given_series[i].translate(str.maketrans('', '', punctuations))

    return given_series


def generate_statistics_count(given_series_book):
    number_of_chars = 0
    word_count = given_series_book.count()

    for i in given_series_book:
        chars_number = len(list(i))
        number_of_chars += chars_number

    print(f'\n{"*Number of words in the book: "}{word_count}')
    print(f'{"*Chars count: "}{number_of_chars}', end="\n")


def stats_average_length(given_input, input_with_punct):
    dict_for_average = {i: len(i) for i in given_input}
    average_word_length = mean(dict_for_average.values())

    print(f'{"*Average word length: "}{average_word_length:.2f}', end="\n")

    dict_with_length_sentences = {}
    extracting_words_pattern = re.compile(r'\w{1,}')
    sentences_prepared = re.split(r' *[\.\?!][\'"\)\]]* *', input_with_punct)

    for i in sentences_prepared:
        words_from_sentences = re.findall(extracting_words_pattern, i)
        dict_with_length_sentences[i] = len(words_from_sentences)

    average_sentence_length = mean(dict_with_length_sentences.values())

    print(f'{"*Average sentence length: "}{average_sentence_length:.2f}', end="\n")

    longest_words = sorted(list(map(lambda i: i, dict_for_average.items())), key=itemgetter(1), reverse=True)

    print(f'{"*Top 10 longest words: "}', end="\n")

    for match in range(0, 15):
        word, counter = longest_words[match]
        print(f'{"- ":>5}{word} {counter}')

    print()


def main():
    file_open_read = ''
    intermediary = ''
    var_to_continue = 0

    while var_to_continue == 0:
        file_open, var_to_continue = catch_input_text()
        if var_to_continue == 1:
            intermediary, file_open_read = reading_the_file(file_open)

    after_remove_punctuation = work_on_text_remove_punctuation(file_open_read)

    generate_statistics_count(after_remove_punctuation)
    stats_average_length(after_remove_punctuation, intermediary)


main()
