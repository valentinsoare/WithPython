#!/usr/bin/python


import re
from sys import exit
from os import system
from time import sleep
from statistics import mean
from collections import Counter
from operator import itemgetter

def catch_input_text():
    to_continue = 0
    input_file = ''

    while to_continue == 0:
        system('clear')
        print(f'\n\033[1m   Please enter desire text file, entire path of the file, '
              f'to check and displays statistics on the content (q to quit):', end=" ")
        input_text = input()

        if input_text.lower()[0] == 'q':
            print(f'\n\033[1;33m{"Quitting...":>17}\033[0m', end="\n\n")
            sleep(0.5)
            exit(0)

        try:
            input_file = open(f"{input_text}", "r")
        except FileNotFoundError:
            print(f'\n\033[1;31m\tGiven file {input_text} does not exists. '
                  f'Please give the correct name and path.\033[0m', end="\n\n")
            sleep(1.5)
            continue

        to_continue = 1

    text_for_processing = input_file.read()

    return text_for_processing


def printing_output(*arguments):
    count_word, count_characters, average_length_word, average_length_sentences, words_ten, words_distribution = arguments

    print(f'\n\033[1m{" - > Statistics from the given text:":>43}\033[0m', end="\n")
    print(f'{"*Word count":>25} {count_word:>22}')
    print(f'{"**Total character count":>37} {count_characters:>11}', end="\n")
    print(f'{"***Average word length":>36} {average_length_word:>10.1f}', end="\n")
    print(f'{"****Average sentence length":>41} {average_length_sentences:>7.1f}', end="\n")
    print(f'{"*****Top ten words by length":>42}:', end=" ")

    for i, j in words_ten.items():
        print(f"{i}: {j}", end=" ")

    print(f'\n{"******Words distribution:":>39}', end="\n")
    print(f'{words_distribution}')


def statistics_with_length(given_text):
    pattern_for_word_count = re.compile(r'\w{1,}')
    extracted_words = re.findall(pattern_for_word_count, given_text)
    word_count = len(extracted_words)

    # all characters but without spaces, tabs or newlines
    pattern_for_character_count = re.compile(r'\S')
    character_count = len(re.findall(pattern_for_character_count, given_text))

    length_of_words = list(map(lambda i: len(i), extracted_words))
    average_word_length = mean(length_of_words)

    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', given_text)
    sentences_length = list(map(lambda j: len(j), sentences))
    average_sentences_length = mean(sentences_length)

    words_distribution_sorted_order = sorted(dict(Counter(extracted_words)).items(), key=itemgetter(1), reverse=True)

    dict_with_length = {i: len(i) for i in extracted_words}
    sorted_by_length = dict(sorted(dict_with_length.items(), key=itemgetter(1), reverse=True))
    #top_ten = sorted(Counter(dict_with_length.values()), reverse=True)
    word_ten = {}
    counting = 0

    for i, j in sorted_by_length.items():
        word_ten[i] = j
        if counting == 9:
            break
        counting += 1

    #### to display top ten words by length but we have multiple words with the same length

    #word_ten = []
    #counting = 0

    #for k in top_ten:
    #    for i, j in sorted_by_length.items():
    #        if j == k:
    #            word_ten += [i]

    #    counting += 1

    #    if counting == 10:
    #        break

    return word_count, character_count, average_word_length,\
        average_sentences_length, words_distribution_sorted_order, word_ten


def main():
    text_to_check = catch_input_text()
    w_count, c_count, av_word_length, av_sent_length, words_distribution, words_ten_list = statistics_with_length(text_to_check)
    printing_output(w_count, c_count, av_word_length, av_sent_length, words_ten_list, words_distribution)


main()

