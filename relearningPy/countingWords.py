#!/usr/bin/python

import string
import numpy as np
from collections import Counter


def header(message):
    chars_to_replace = {'u': '|_|', 's': '5', 'a': '@', 'o': '0', 'e': '3'}
    processed_message = ' *** '
    list_with_keys_for_message = chars_to_replace.keys()

    for i in message:
        if i in list_with_keys_for_message:
            processed_message += ' ' + chars_to_replace[i]
        else:
            processed_message += ' ' + i

    processed_message += ' *** '
    length_of_message = len(processed_message)

    print(f"\n{' ' * int(length_of_message * 0.5)}{processed_message}")
    print(f"{' ' * int(length_of_message * 0.25)}{'-' * int(length_of_message * 1.5)}")


def load_text():
    given_text = """Established in 1973, the WRC is an epic battle against the elements and the clock. It is spread across 12 rallies, covering four continents and 13 countries. Man and machine must master everything from snow-packed forest tracks in intense cold, to rock-strewn mountain passes in blistering heat.
                    Each rally features a number (typically between 15 and 25) of timed sections - known as special stages - on closed roads.
                    Drivers battle one at a time to complete these stages as quickly as possible, with timing taken to 1/10th second. A co-driver reads detailed pace notes that explain the hazards ahead.
                    Competitors drive to and from each stage on public roads, observing normal traffic regulations.
                    The crew which completes all the stages in the shortest cumulative time is the rally winner. WRC points are allocated to the top 10 finishers on a 25-18-15-12-10-8-6-4-2-1 basis in both the drivers’ and manufacturers’ championships."""
    splitting_text = list(map(lambda j: j.lower(), given_text.split()))
    return splitting_text


def prepare_words_for_analysis(given_words):
    punctuation_to_be_remove = list(string.punctuation + '’')
    length_of_words = len(given_words)

    for i in range(length_of_words):
        for j in punctuation_to_be_remove:
            if j in list(given_words[i]):
                given_words[i] = given_words[i].replace(j, '')

    return given_words


def print_in_alphabetical_order(words, count):
    counter = 0
    print(f"\n{' ' * 9} - > In alphabetical sorted order by count:")

    for i in range(len(words)):
        if words[i] != '':
            print(f"{' ' * 9}{counter + 1:>3}.{' ' * 3}{words[i]:<20}{count[i]} ")
            counter += 1


def print_sorted_count(words, count):
    dict_with_values_for_sorting_by_count = dict(sorted(zip(words, count), key=lambda j: j[1], reverse=True))
    print(f"\n{' ' * 9} - > In sorted order by count:")

    counter = 0
    for i, j in dict_with_values_for_sorting_by_count.items():
        if i != '':
            print(f"{' ' * 9}{counter + 1:>3}.{' ' * 3}{i:<20}{j} ")
            counter += 1


def main():
    header('Counting Words')

    text_to_be_process = load_text()
    list_with_words_prepared_to_be_process = prepare_words_for_analysis(text_to_be_process)

    #to_count = Counter(list_with_words_prepared_to_be_process)
    words, count = np.unique(list_with_words_prepared_to_be_process, return_counts=True)

    print(f"\n{' ' * 16}{'Words':<20}{'Count':<12}")
    print_in_alphabetical_order(words, count)
    print_sorted_count(words, count)

    print(f"\n{' ' * 9} - > Number of uniq words: {len(count) - 1}")


if __name__ == '__main__':
    main()
