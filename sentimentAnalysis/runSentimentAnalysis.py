#!/usr/bin/python3

"""Best way to do this is using NLTK library but here we are using scoring to implement this analysis."""

import pandas as pd
import re


def printing_lines(number):
    i = 0
    while i < number:
        print(f'\033[1m-\033[0m', end='')
        i += 1
    print()


def phrase_processing_remove_punctuation_and_splitting(given_phrase):
    processed = re.sub(r'\W', ' ', given_phrase)
    phrase_after_processing = processed.split()

    return phrase_after_processing


def calculating_scoring(phrase_to_use, sentiment_words_to_use):
    scoring = 0
    sentiment_words = sentiment_words_to_use.items()
    for i in phrase_to_use:
        i = i.lower()
        for j, k in sentiment_words:
            if i == j:
                scoring += k

    return scoring


def add_items_pos(word, dict_of_pos):

    if word in dict_of_pos:
        dict_of_pos[word] += 1
    else:
        dict_of_pos[word] = 1

    return dict_of_pos


def add_items_negs(word, dict_of_negs):

    if word in dict_of_negs:
        dict_of_negs[word] += 1
    else:
        dict_of_negs[word] = 1

    return dict_of_negs


def text_analysis(phrase_for_using, list_of_sentiments):
    number_of_positives = 0
    number_of_negatives = 0
    dict_of_pos = {}
    dict_of_negs = {}

    items_sentiments = list_of_sentiments.items()
    for k in phrase_for_using:
        k = k.lower()
        for i, j in items_sentiments:
            if k == i:
                if j > 0:
                    number_of_positives += 1
                    dict_of_pos.update(add_items_pos(i, dict_of_pos))
                else:
                    number_of_negatives += 1
                    dict_of_negs.update(add_items_negs(i, dict_of_negs))

    return number_of_positives, dict_of_pos, number_of_negatives, dict_of_negs


def statistics_printing(words_given_counter, processed_phrase, type_of_words):

    words_appearances_within_entire_phrase = words_given_counter.values.sum() * 100 / len(processed_phrase)

    if len(words_given_counter) >= 5:
        print(f'\033[1;34m*Number of {type_of_words.lower()} words: {len(words_given_counter)}\033[0m')
        print(f'\033[1;34m**Five most used {type_of_words.lower()} words:\033[0m')
        k = 0

        dict_items = words_given_counter.items()
        for i, j in dict_items:
            if k == 5:
                break
            print(f'\033[1m{i:<20}{j}\033[0m')
            k += 1

        print(f'\n\033[1;35m*Number of appearances of {type_of_words.lower()}\033[0m \n'
              f'\033[1;35mwords compare to entire text length: \033[0m'
              f'\033[1m{words_appearances_within_entire_phrase:.1f}%\033[0m')
    else:
        print(f'\033[1;34m*Most used {type_of_words.lower()} words:\033[0m')

        words_given_counter_items = words_given_counter.items()

        for i, j in words_given_counter_items:
            print(f'\033[1m{i:<20}{j}\033[0m')

        print(f'\n\033[1;35m*Number of appearances of {type_of_words.lower()}\033[0m \n'
              f'\033[1;35mwords compare to entire text length:\033[0m '
              f'\033[1m{words_appearances_within_entire_phrase:.1f}%\033[0m')


def printing_words(type_words, message, type_of_color, processed_phrase):
    sorted_series_by_values = pd.Series(type_words).sort_values(ascending=False)

    if type_of_color == 1:
        print(f'\n\033[1;42m {message} words stats from the given \033[0m\n'
              f'\033[1;42m text(words/number of appearances): \033[0m')
    elif type_of_color == 0:
        print(f'\n\033[1;41m {message} words stats from the given \033[0m\n'
              f'\033[1;41m text(words/number of appearances): \033[0m')

    printing_lines(45)
    statistics_printing(sorted_series_by_values, processed_phrase, message)
    printing_lines(45)


def existing_positives(list_of_positives_and_counter, processed_phrase):
    if len(list_of_positives_and_counter) > 0:
        printing_words(list_of_positives_and_counter, 'POSITIVE', 1, processed_phrase)
    else:
        print(f'\n\033[1;42m No positive words in the given text. \033[0m\n')


def existing_negatives(list_of_negatives_and_counter, processed_phrase):
    if len(list_of_negatives_and_counter) > 0:
        printing_words(list_of_negatives_and_counter, 'NEGATIVE', 0, processed_phrase)
    else:
        print(f'\n\033[1;41m No negative words in the given text. \033[0m\n')


def main():

    file = open(input(f'\n*\033[1mEnter your desired file (entire path is needed):\033[0m '), "r")
    phrase = file.read()

    sentiment_words = {i: j for i, j in pd.read_csv('wordsWithScoring.csv', index_col=False,
                       engine='c', sep=r',').to_records(index=False)}
    processed_phrase = phrase_processing_remove_punctuation_and_splitting(phrase)
    number_of_positives, list_of_positives_and_counter, number_of_negatives, list_of_negatives_and_counter \
        = text_analysis(processed_phrase, sentiment_words)

    output = calculating_scoring(processed_phrase, sentiment_words)

    if output < 0:
        output_to_print = (output * 100) / (-3 * len(processed_phrase))
        print(f'\n\033[1m*Given text:\033[0m\n\033[1;32m[ \033[0m{file}\033[1;32m ]\033[0m')
        print(f'\n\033[1m*Possibility expressed in percentages that the sentiment deduced from the text\n'
              f' is a negative one calculating from the score on each word:\033[0m '
              f'\033[1;31m{output_to_print:.1f}%\033[0m')
    elif output > 0:
        output_to_print = (output * 100) / (3 * len(processed_phrase))
        print(f'\n\033[1m*Given file:\033[0m\n\033[1;32m[ \033[0m{phrase}\033[1;32m ]\033[0m')
        print(f'\n\033[1m*Possibility expressed in percentages that the sentiment deduced from the text is\n'
              f' a positive one calculating from the score on each word:\033[0m '
              f'\033[1;34m{output_to_print:.1f}%\033[0m')
    else:
        print(f'\n\033[1m*There is an equality of chances between positive and negative'
              f'sentiment for the given text, taking into consideration the score on each word.\033[0m ')

    existing_positives(list_of_positives_and_counter, processed_phrase)
    existing_negatives(list_of_negatives_and_counter, processed_phrase)


main()
