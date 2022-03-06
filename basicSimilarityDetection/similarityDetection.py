#!/usr/bin/python

import re
from time import sleep
from os import system, path
from statistics import mean
from string import punctuation


def to_exit(var_to_process):
    if var_to_process.lower()[0] == 'q':
        print(f'\n\033[31m{"Exiting...":>17}\33[0m', end="\n\n")
        sleep(1)
        exit(0)


def catch_number_of_texts():
    system('clear')
    var_to_continue = 0
    print(f'\n{" - > How many texts you want to compare (q to quit):"}', end=" ")
    number_of_texts = input()

    to_exit(number_of_texts)

    try:
        number_of_texts = int(number_of_texts)
    except ValueError:
        print(f'\n\033[1;31m{"ERROR - you need to give an integer written in digits.":>63}\033[0m', end="\n\n")
        sleep(1.5)
    else:
        var_to_continue = 1

    return number_of_texts, var_to_continue


def catch_text_files(number_of_text):
    i = 0
    validity_of_files = 0
    dict_with_files_names = {}
    text_numbers_in_letters = {0: 'First', 1: 'Second', 2: 'Third', 3: 'Fourth', 4: 'Fifth', 5: 'Sixth', 6: 'Seventh',
                               9: 'Eighth', 8: 'Ninth'}

    while validity_of_files == 0:
        system('clear')
        print(f'\n{" - > Enter the entire path for text files as input:  (q to quit):":>43}')
        print(f'{"-":>7} {text_numbers_in_letters[i]} text file:', end=" ")
        text_as_input = input()

        to_exit(text_as_input)

        if not path.isfile(text_as_input):
            print(f'\n\033[1;31m{"ERROR - file does not exists.":>63}\033[0m', end="\n\n")
            sleep(1.5)
            continue

        dict_with_files_names[i] = text_as_input

        i += 1

        if len(dict_with_files_names) == number_of_text:
            validity_of_files = 1

    return dict_with_files_names


def opening_files_put_text_in_dict(dict_with_file_names):
    dict_of_open_files = {}

    for i in dict_with_file_names.values():
        opn = open(i, mode='r')
        dict_of_open_files[i] = opn

    return dict_of_open_files


def put_the_text_in_dict_sentences(files_open):
    dict_with_files_open_and_split = {}

    for key, file in files_open.items():
        with file:
            read_file = file.read()
            extracted_sentences = re.split(r' *[\.\?!][\'"\)\]]* *', read_file)

            dict_with_files_open_and_split[key] = extracted_sentences

    return dict_with_files_open_and_split


def put_the_text_in_words(files_open):
    dict_with_words = {}

    for key, file in files_open.items():
        with file:
            reading_file = file.read()
            extracted_words = re.findall(r'\w{1,}', reading_file)
            dict_with_words[key] = extracted_words

    return dict_with_words


def remove_punctuation_from_text(dict_with_texts):
    punctuations = punctuation + '”“’'
    dict_to_remove_without_punctuation = {}

    for key, file in dict_with_texts.items():
        dict_to_remove_without_punctuation[key] = []

        for i in file:
            dict_to_remove_without_punctuation[key].append(re.sub(' +', ' ', (i.translate(str.maketrans('\n', ' ', punctuations))).strip()))

    return dict_to_remove_without_punctuation


def calculate_lengths(dict_with_words, dict_with_sentences):
    length_of_words = {}
    length_of_sentences = {}

    for name_of_text_for_word, list_of_items_words in dict_with_words.items():
        length_of_words[name_of_text_for_word] = {word: len(word) for word in list_of_items_words}

    for name_of_text_for_sentence, list_of_items_sentences in dict_with_sentences.items():
        length_of_sentences[name_of_text_for_sentence] = {sentence: len(sentence) for sentence in list_of_items_sentences}

    return length_of_words, length_of_sentences


def generate_averages_for_lengths(sentences_length, words_length):
    words_averages = {}
    sentences_averages = {}

    for i, j in words_length.items():
        words_averages[i] = mean(j.values())

    for k, l in sentences_length.items():
        sentences_averages[k] = mean(l.values())

    return words_averages, sentences_averages


def printing_the_result(average_words, average_sentences):
    print(f'\n{"*Average word length per file:":>31}')

    for name, value in average_words.items():
        print(f'{"-":>5}{name} | {value:.2f}')

    print(f'\n{"*Average sentence length per file:":>35}')

    for name, value in average_sentences.items():
        print(f'{"-":>5}{name} | {value:.2f}')

    print()


def main():
    var_to_continue = 0
    number_of_text_to_check = ''

    while var_to_continue == 0:
        number_of_text_to_check, var_to_continue = catch_number_of_texts()

        if var_to_continue == 0:
            continue

    dict_with_file_names = catch_text_files(number_of_text_to_check)

    # generate dict with sentences
    open_files_in_dict_for_sentences = opening_files_put_text_in_dict(dict_with_file_names)
    dict_with_text_process_sentences = put_the_text_in_dict_sentences(open_files_in_dict_for_sentences)
    dict_with_sentences_without_punctuation = remove_punctuation_from_text(dict_with_text_process_sentences)

    # generate dict with words
    open_files_in_dict_for_words = opening_files_put_text_in_dict(dict_with_file_names)
    dict_with_text_process_words = put_the_text_in_words(open_files_in_dict_for_words)
    dict_with_words_without_punctuation = remove_punctuation_from_text(dict_with_text_process_words)

    # calculate lengths and average
    length_of_words, length_of_sentences = calculate_lengths(dict_with_words_without_punctuation, dict_with_sentences_without_punctuation)
    words_average, sentences_average = generate_averages_for_lengths(length_of_words, length_of_sentences)

    # printing the result
    printing_the_result(words_average, sentences_average)


main()
