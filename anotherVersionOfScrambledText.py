#!/usr/bin/python

import numpy as np
from sys import exit
from os import system


def catch_input():
    alpha_type = 0
    exiting_var = 0
    splitting_input = ''

    while exiting_var == 0:
        system('clear')
        print(f'\n\033[1;32m{"< SCRAMBLING_TEXT >":>40}\033[0m', end="\n")

        print(f"\n\033[1m - > Enter a phrase in order to scramble the containing words (q to quit): ", end="\033[0m")
        input_text = input()

        if input_text[0].lower() == 'q':
            print(f'\n\033[1;33m{"Quitting...":>20}\033[0m', end="\n\n")
            system('sleep 1')
            exit(1)

        splitting_input = np.array(input_text.split())

        for i in splitting_input:
            if i.isalpha():
                alpha_type += 1
                break

        if alpha_type == 0:
            print(f'\n\033[1;31m{"ERROR - we need at least one word in the given text.":>60}', end="\n")
            system('sleep 1')
        else:
            exiting_var = 1

    return splitting_input


def processing_entire_array(given_array):
    array_after_processing = np.array([], dtype=str)

    for i in range(len(given_array)):
        if len(given_array[i]) > 3:
            first = given_array[i][0]
            last = given_array[i][len(given_array[i]) - 1]
            extracted_array_to_shuffle = np.array(list(given_array[i][1:len(given_array[i]) - 1]))

            np.random.shuffle(extracted_array_to_shuffle)
            extracted_array_to_shuffle = ''.join(extracted_array_to_shuffle)

            word = first + extracted_array_to_shuffle + last
            array_after_processing = np.append(array_after_processing, word)
        else:
            array_after_processing = np.append(array_after_processing, given_array[i])

    return array_after_processing


def printing_output(given_array):
    print(f'\n\033[1m{"*Scrambled text:":>20}\033[0m', end=" ")

    for i in given_array:
        print(f"{i}", end=" ")

    print("\n")


def main():
    after_splitting_and_checking = catch_input()
    array_after_processing = processing_entire_array(after_splitting_and_checking)
    printing_output(array_after_processing)


main()
