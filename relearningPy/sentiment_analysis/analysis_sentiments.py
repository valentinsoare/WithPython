#!/usr/bin/python

import os
import re
import time
import random
import logging
import pandas as pd
import pyparsing as pp


def header_printing(given_message):
    processed_words = []
    processed_message = "*|* "
    list_with_title_tokenized = given_message.split()

    for i in range(len(list_with_title_tokenized)):
        word = ''
        for j in range(len(list_with_title_tokenized[i])):
            location_to_use = random.randrange(0, (len(list_with_title_tokenized[i]) - 1))
            if j == location_to_use:
                word += list_with_title_tokenized[i][j].upper()
            else:
                word += list_with_title_tokenized[i][j]
        processed_words.append(word)
    processed_message += ' '.join(processed_words) + ' *|*'

    line_above = f"{'-' * (2 * len(processed_message))}"

    print(f"\n{' ' * 10}{processed_message:^{len(line_above)}}")
    print(f"{' ' * 10}{line_above}")


def import_document_with_sentiments():
    given_sentiments = pd.read_csv(r'scoring.csv', names=['word', 'score'])

    positive_sentiments = pd.Series({i[0]:  i[1] for i in given_sentiments.values if i[1] >= 0})
    negative_sentiments = pd.Series({i[0]:  i[1] for i in given_sentiments.values if i[1] < 0})

    return negative_sentiments, positive_sentiments


def to_quit(given_answer):
    variable_to_return = 'forward'
    message_to_give = f"\n{' ' * 4}{' ERROR please do not use only whitespaces.'}\n"

    if re.match(r'\s+', given_answer) or given_answer == "":
        print(f"{message_to_give}")
        time.sleep(2)
        variable_to_return = False
    elif given_answer.lower()[0] == 'q':
        print(f"\n{' ' * 5}{' Exiting...'}\n")
        time.sleep(1)
        exit(0)
    elif given_answer.lower()[0] == 'b':
        variable_to_return = 'backward'

    return variable_to_return


def applying_to_quit(given_answer):
    output_for_first_validation = to_quit(given_answer)
    if not output_for_first_validation:
        return 0
    elif output_for_first_validation == 'backward':
        return 1


def validate_answer_for_source(given_word):
    if not to_quit(given_word):
        return 0, given_word

    issue = 1
    processed_word = ''
    error_message = f"\n{' ' * 5} ERROR - please select one of those two options using only those indexes, 1 or 2.\n"

    try:
        processed_word = int(given_word)
        if processed_word not in [1, 2]:
            issue = 0
    except ValueError:
        issue = 0

    if issue == 0:
        print(error_message)
        time.sleep(1)

    return issue, processed_word


def validate_read_input_from_command_line(given_answer):
    message_to_give_1 = f"\n{' ' * 4}{' ERROR you can use only char b as a single character which means to return to sources'}"
    exit_value = applying_to_quit(given_answer)
    if exit_value in [0, 1]:
        return exit_value
    else:
        if len(given_answer) == 1:
            print(message_to_give_1)
            time.sleep(2)
            return 0

    exit_value = 0
    message_to_give = f"\n{' ' * 4} ERROR - please use also alpha characters not only numerical ones or whitespaces\n"

    try:
        processed_answer = int(given_answer)
    except ValueError:
        try:
            processed_answer = float(given_answer)
        except ValueError:
            exit_value = 1
            return exit_value

    if isinstance(processed_answer, int) or isinstance(processed_answer, float):
        print(f"{message_to_give}")
        time.sleep(2)

    return exit_value


def validate_load_txt_file(given_answer):
    message_to_give_1 = f"\n{' ' * 4}{' ERROR you can use only char b as a single character which means to return to sources'}"
    issue = applying_to_quit(given_answer)
    if issue in [0, 1]:
        return issue
    else:
        if len(given_answer) == 1:
            print(message_to_give_1)
            time.sleep(2)
            return 0

    issue = 0
    given_message_1 = f"{' ' * 4}{' ERROR the file does not exists.'}"
    given_message_2 = f"{' ' * 4}{' ERROR the file is empty.'}"

    if not os.path.isfile(given_answer):
        print(f"\n{given_message_1}\n")
        time.sleep(2)
    else:
        if os.path.getsize(given_answer) == 0:
            print(f"{' ' * 4}{given_message_2}\n")
            time.sleep(2)
        else:
            issue = 1

    return issue


def read_input_from_command_line():
    to_exit = 0
    answer = ''

    while to_exit == 0:
        os.system('clear')
        header_printing("sentiment analysis")

        print(f"{' ' * 2}{' * Please put here the sentence(s) you want to analyze (q to quit or b to return to sources):'}", end=" ")
        answer = input()

        to_exit = validate_read_input_from_command_line(answer)

    return answer


def load_input_from_text_file():
    error = 0
    answer = ''

    while error == 0:
        os.system('clear')
        header_printing("sentiment analysis")
        print(f"{' ' * 2}{' * Please enter the entire path of the file which is use to load the text from (q to quit or b to return to sources):'}", end=" ")
        answer = input()

        error = validate_load_txt_file(answer)

    if answer != 'b':
        with open(answer) as given_file:
            our_contents = given_file.read()
            return our_contents
    else:
        return 'b'


def ask_for_input_source():
    error = 0
    processed_answer = ''
    dict_with_options = {'1.': 'Command Line', '2.': 'Text File'}

    while error == 0:
        os.system('clear')
        header_printing("sentiment analysis")
        print(f"{' ' * 2}{' * From where you want to load the text to analyse, command line or file:'}\n")

        for i, j in dict_with_options.items():
            print(f"{' ' * 6}{i} {j}")

        print(f"\n{' ' * 3}{'** Answer (q to quit):'}", end=" ")
        answer = input()

        error, processed_answer = validate_answer_for_source(answer)

    return processed_answer


def prepare_text_for_analysis(given_text):
    punctuation = '!"#$%&\'()*+,./:;<=>?[\]`{|}~'
    split_text = given_text.split()

    split_without_punctuation_beginning_end = list(word.translate(str.maketrans('', '', punctuation)).lower()
                                                   for word in split_text)
    return split_without_punctuation_beginning_end


def creating_text_parser_for_level(given_level_of_log):
    log_pattern = pp.Word(pp.alphas) + '.' + pp.Word(pp.alphas)

    for log in ['logging.DEBUG', 'logging.INFO', 'logging.WARNING', 'logging.ERROR', 'logging.CRITICAL']:
        log_level = log_pattern.parseString(log)
        if log_level[2].lower() == given_level_of_log:
            return ''.join(log_level)

    raise ValueError('Please use one of the five classic log levels.')


def logging_the_output(logging_level_to_use, list_with_words):
    # tested for security gaps and all is ok with using eval in this instance.
    given_level = creating_text_parser_for_level(logging_level_to_use)

    logging.basicConfig(filename='sentiments_values_analysis.log',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%d/%m/%Y %I:%M:%S %p',
                        level=eval(given_level))

    action_to_use = given_level.lower() + f"(list_with_words)"
    eval(action_to_use)

#def find_sentiment_value(given_list_with_words, positive_words, negative_words):


def main():
    while True:
        what_type_of_input = ask_for_input_source()

        if what_type_of_input == 1:
            text_to_use = read_input_from_command_line()
        else:
            text_to_use = load_input_from_text_file()

        if len(text_to_use) > 1:
            words_in_list_for_analysis = prepare_text_for_analysis(text_to_use)
            negative_sentiments, positive_sentiments = import_document_with_sentiments()

            logging_the_output('info', words_in_list_for_analysis)

            #find_sentiment_value(words_in_list_for_analysis, positive_sentiments, negative_sentiments)


if __name__ == '__main__':
    main()
