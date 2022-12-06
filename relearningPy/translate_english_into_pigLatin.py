#!/usr/bin/python

import os
import re
import time


def show_title(message_to_use):
    message = message_to_use.split()
    message_to_use = ' '.join([i.capitalize() for i in message])
    length_of_message = len(message_to_use)

    line_to_use = f"{' ' * 15}{'-' * (length_of_message * 2)}"
    message_to_print = f"{' ' * 15}{message_to_use}"

    print(f"\n{message_to_print:^{len(line_to_use)}}")
    print(f"{line_to_use}")


def to_quit(input_value_from_user):
    if re.match(r"\s+", input_value_from_user) or input_value_from_user == "":
        print(f"\n{' ' * 9}{'ERROR - You should know that in order to translate we need alpha characters/words in english language in the sentence.'}")
        time.sleep(2)
        os.system('clear')
        return True
    elif input_value_from_user.lower()[0] == 'q':
        print(f"\n{' ' * 8} Exiting....")
        time.sleep(1)
        exit(0)


def ask_for_what_to_translate():
    processed_answer = 0

    while isinstance(processed_answer, int) or isinstance(processed_answer, float):
        show_title('english to pig latin translator')
        print(f"{' * Please give me what to translate (q to quit):'}", end=" ")
        answer = input()

        if to_quit(answer):
            continue

        try:
            processed_answer = int(answer)
        except ValueError:
            try:
                processed_answer = float(answer)
            except ValueError:
                processed_answer = answer

        if isinstance(processed_answer, int) or isinstance(processed_answer, float):
            print(f"\n{' ' * 9}{'ERROR - You should know that in order to translate we need alpha characters/words in english language in the sentence.'}")
            time.sleep(2)
            os.system('clear')

    return processed_answer


def processing_word(given_word):
    list_with_punctuation_location = []
    punctuation_chars = '!"#$%&\'()*+,./:;<=>?[\]`{|}~'
    word_after_punctuation = given_word.translate(str.maketrans('', '', punctuation_chars))

    for i in range(len(given_word)):
        if given_word[i] in punctuation_chars and (0 <= i <= 2 or (len(given_word) - 3) <= i <= (len(given_word) - 1)):
            list_with_punctuation_location.append((given_word[i], i))

    return list(word_after_punctuation), list_with_punctuation_location


def insert_punctuation(word, punctuation):
    for sign, location in punctuation:
        if 0 <= location <= 2:
            word.insert(location, sign)
        elif location <= len(word) - 1:
            word.insert(len(word),  sign)

    return word


def to_add_if_numeric_and_noun(word_without_punctuation):
    to_add = list('ay')
    list_with_nouns = ['a', 'e', 'i', 'o', 'u']

    if word_without_punctuation[0].lower() in list_with_nouns:
        final_word = word_without_punctuation[1:] + to_add
    else:
        word_without_punctuation = ''.join(word_without_punctuation)
        try:
            final_word = int(word_without_punctuation)
        except ValueError:
            try:
                final_word = float(word_without_punctuation)
            except ValueError:
                final_word = list(word_without_punctuation[1:]) + list(word_without_punctuation[0]) + to_add

    return final_word


def check_if_upper(given_word):
    check_capitalized = 0
    given_word = ''.join(given_word)

    try:
        if given_word.isupper():
            check_capitalized = 1
        elif given_word[0].isupper():
            check_capitalized = 2
    except ValueError:
        pass

    return check_capitalized


def word_to_add(word_without_punctuation, signs_location, if_capitalized):

    final_word = to_add_if_numeric_and_noun(word_without_punctuation)

    if isinstance(final_word, int) or isinstance(final_word, float):
        final_word = list(str(final_word))

    if len(signs_location) != 0:
        word_to_insert = ''.join(insert_punctuation(final_word, signs_location))
    else:
        word_to_insert = ''.join(final_word)

    if if_capitalized == 1:
        word_to_insert = word_to_insert.upper()
    elif if_capitalized == 2:
        word_to_insert = word_to_insert.capitalize()

    return word_to_insert


def start_translating(given_text):
    words_after_processing = []

    splitting_text = given_text.split()
    length_split_text = len(splitting_text)

    for i in range(length_split_text):
        word_without_punctuation, signs_location = processing_word(splitting_text[i])

        if_up = check_if_upper(word_without_punctuation)

        word_to_insert = word_to_add(word_without_punctuation, signs_location, if_up)
        words_after_processing.append(word_to_insert)

    return words_after_processing


def print_translated_sentence(given_list_with_words):
    sentence_to_print = ' '.join(given_list_with_words)

    print(f"\n{' ** Translation: '}{sentence_to_print}\n\n")


def main():
    what_to_translate = ask_for_what_to_translate()
    translated_sentence = start_translating(what_to_translate)
    print_translated_sentence(translated_sentence)


if __name__ == '__main__':
    main()
