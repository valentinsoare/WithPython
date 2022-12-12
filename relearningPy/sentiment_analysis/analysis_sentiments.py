#!/usr/bin/python


"""this is a cool way, but rough around the edges, to do sentiment analysis without any ddicated library. i used only a list with text which contains#
negative words and positive and each words has a numeric value, positive or negative associated with it.
made by Valentin S."""


import re
import logging
import pandas as pd
from time import sleep
from os import system, path
from random import randrange
from collections import Counter
from pyparsing import Word, alphas

header_name = 'sentiment analysis'
sleep_time = 2


def header_printing(given_message):
    processed_words = []
    processed_message = "*|* "
    list_with_title_tokenized = given_message.split()

    for i in range(len(list_with_title_tokenized)):
        word = ''
        for j in range(len(list_with_title_tokenized[i])):
            location_to_use = randrange(0, (len(list_with_title_tokenized[i]) - 1))
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
        sleep(sleep_time)
        variable_to_return = False
    elif given_answer.lower()[0] == 'q':
        print(f"\n{' ' * 5}{' Exiting...'}\n")
        sleep(sleep_time)
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
        sleep(sleep_time)

    return issue, processed_word


def validate_read_input_from_command_line(given_answer):
    message_to_give_1 = f"\n{' ' * 4} ERROR you can use only char b as a single " \
                        f"character which means to return to sources"
    exit_value = applying_to_quit(given_answer)
    if exit_value in [0, 1]:
        return exit_value
    else:
        if len(given_answer) == 1:
            print(message_to_give_1)
            sleep(sleep_time)
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
        sleep(sleep_time)

    return exit_value


def validate_load_txt_file(given_answer):
    message_to_give_1 = f"\n{' ' * 4} ERROR you can use only char b as a single " \
                        f"character which means to return to sources"
    issue = applying_to_quit(given_answer)
    if issue in [0, 1]:
        return issue
    else:
        if len(given_answer) == 1:
            print(message_to_give_1)
            sleep(sleep_time)
            return 0

    issue = 0
    given_message_1 = f"{' ' * 4}{' ERROR the file does not exists.'}"
    given_message_2 = f"{' ' * 4}{' ERROR the file is empty.'}"

    if not path.isfile(given_answer):
        print(f"\n{given_message_1}\n")
        sleep(sleep_time)
    else:
        if path.getsize(given_answer) == 0:
            print(f"{' ' * 4}{given_message_2}\n")
            sleep(sleep_time)
        else:
            issue = 1

    return issue


def read_input_from_command_line():
    to_exit = 0
    answer = ''

    while to_exit == 0:
        system('clear')
        header_printing(header_name)

        print(f"{' ' * 2} * Please put here the sentence(s) you want to analyze (q to quit or b to return to "
              f"sources:", end=" ")
        answer = input()

        to_exit = validate_read_input_from_command_line(answer)

    return answer


def load_input_from_text_file():
    error = 0
    answer = ''

    while error == 0:
        system('clear')
        header_printing(header_name)
        print(f"{' ' * 2} * Please enter the entire path of the file which is use "
              f"to load the text from (q to quit or b to return to sources):", end=" ")
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
        system('clear')
        header_printing(header_name)
        print(f"{' ' * 2}{' * From where you want to load the text to analyse, command line or file:'}\n")

        for i, j in dict_with_options.items():
            print(f"{' ' * 6}{i} {j}")

        print(f"\n{' ' * 3}{'** Answer (q to quit):'}", end=" ")
        answer = input()

        error, processed_answer = validate_answer_for_source(answer)

    return processed_answer


def prepare_text_for_analysis(given_text):
    punctuation = '!"#$%&\'()*+,./:;<=>?[\]`{|}~'
    split_without_punctuation_beginning_end = pd.Series(word.translate(str.maketrans('', '', punctuation)).lower()
                                                        for word in given_text.split())
    return split_without_punctuation_beginning_end


def creating_text_parser_for_level(given_level_of_log):
    log_pattern = Word(alphas) + '.' + Word(alphas)

    for log in ['logging.DEBUG', 'logging.INFO', 'logging.WARNING', 'logging.ERROR', 'logging.CRITICAL']:
        log_level = log_pattern.parseString(log)
        if log_level[2].lower() == given_level_of_log:
            return ''.join(log_level)

    raise ValueError('Please use one of the five classic log levels.')


def logging_the_output(logging_level_to_use, list_with_words):
    # tested for security gaps and all is ok with using eval in this case.
    path_of_the_log_file = 'sentiments_values_analysis.log'
    given_level = creating_text_parser_for_level(logging_level_to_use)

    logging.basicConfig(filename=path_of_the_log_file,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%d/%m/%Y %I:%M:%S %p',
                        level=eval(given_level))

    action_to_use = given_level.lower() + f"(list_with_words)"
    eval(action_to_use)


def populate_sentiment_value_dict(given_list_with_words, positive_words, negative_words):
    global positive_dict_with_words_from_text
    positive_dict_with_words_from_text = pd.Series(dtype=str)
    global negative_dict_with_words_from_text
    negative_dict_with_words_from_text = pd.Series(dtype=str)
    global positive_words_freq
    positive_words_freq = pd.Series(dtype=str)
    global negative_words_freq
    negative_words_freq = pd.Series(dtype=str)

    counting_words_freq = pd.Series(Counter(given_list_with_words))

    for word, freq in counting_words_freq.items():
        if word in positive_words.keys():
            positive_dict_with_words_from_text[word] = (freq * positive_words.loc[word])
            positive_words_freq[word] = freq
        elif word in negative_words.keys():
            negative_dict_with_words_from_text[word] = (freq * negative_words.loc[word])
            negative_words_freq[word] = freq

    return counting_words_freq, positive_dict_with_words_from_text, positive_words_freq, \
        negative_dict_with_words_from_text, negative_words_freq


def printing_statistics(total_count_freq, entire_text, positive_words, positive_freq, negative_words, negative_freq):
    number_of_positive_words = positive_freq.values.sum()
    five_most_used_positive_words = (positive_freq.sort_values(ascending=False)).iloc[0:6]
    percent_of_appearances_of_positive = number_of_positive_words * 100 / len(entire_text)

    number_of_negative_words = negative_freq.values.sum()
    percent_of_appearances_of_negative = number_of_negative_words * 100 / len(entire_text)
    five_most_used_negative_words = (negative_freq.sort_values(ascending=False)).iloc[0:6]

    final_score = positive_words.values.sum() + negative_words.values.sum()
    score_to_print_for_text = (final_score * 100) / len(entire_text)

    system('clear')
    header_printing(header_name)
    if final_score < 0:
        type_of_sentiments = f"negative"
        score_to_print_for_text *= -1
    elif final_score > 0:
        type_of_sentiments = f"positive"
    else:
        type_of_sentiments = f"undetermined"

    count = list(range(1, 5))
    header_1 = f"{' ' * 4} {count[0]}. given text has a {type_of_sentiments.upper()} connotation: words with {type_of_sentiments} meaning are stronger by {score_to_print_for_text:.2f}%"

    if type_of_sentiments == 'negative':
        number_of_words = number_of_negative_words
        percent_of_appearances = percent_of_appearances_of_negative
        five_most_used = five_most_used_negative_words
        header_1_continuation = f" compared to positive ones."
    elif type_of_sentiments == 'positive':
        number_of_words = number_of_positive_words
        percent_of_appearances = percent_of_appearances_of_positive
        five_most_used = five_most_used_positive_words
        header_1_continuation = f" compared to negative ones."
    else:
        header_1 = f"\n{' ' * 8} :( Cannot determine which way the text is going due to the fact that the power of negative words is equal to that of positive ones.\n"
        header_1_continuation = ""
        exit(0)

    content = f"\n{' ' * 4} {count[1]}. number of {type_of_sentiments} words: {number_of_words}"
    content += f"\n{' ' * 4} {count[2]}. five most used {type_of_sentiments} words from the text:"
    content += f"\n{' ' * 8}{'WORD':<15}{'FREQUENCY'}"

    for i, j in five_most_used.items():
        content += f"\n{' ' * 8}{i:<15}{j}"

    content += f"\n{' ' * 4} {count[3]}. the percent of {type_of_sentiments} words: {percent_of_appearances:.2f}%"
    final = header_1 + header_1_continuation + content

    return final


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

            total_count_freq, positive_words, positive_freq, negative_words, negative_freq = populate_sentiment_value_dict(words_in_list_for_analysis,
                                                                                                                        positive_sentiments,
                                                                                                                        negative_sentiments)
            text_to_output = printing_statistics(total_count_freq, words_in_list_for_analysis, positive_words, positive_freq, negative_words, negative_freq)

            print(text_to_output)
            logging_the_output('info', f"\n" + text_to_output)

            exit(0)


if __name__ == '__main__':
    main()
