#!/usr/bin/python

import re
import string
import numpy as np
import pandas as pd
from decimal import Decimal


def strings_exercises():
    given_string = f"{'nebunie':>15}"
    char = f'{670:c}'

    print(char)

    print(f"{'hello world bo$$!!':40}")

    number_to_print = f"{Decimal(4.19871119520010):.3f}"
    print(number_to_print)

    smile_emoji = f"{58:c}{45:c}{41:c}"
    print(smile_emoji)


def formatting_strings():
    given_number = f"[{27:>15d}]"
    given_number_floating = f"[{27:>15f}]"

    given_text = f"[{'hello':15s}]"
    given_text_right = f"[{'hello':>15s}]"
    given_text_center = f"[{'#' * 13}{'waat':^11s}{'#' * 13}]"

    print(given_number_floating)
    print(given_number)
    print(given_text)
    print(given_text_center)

    print(f"[{'Amanda':>10s}]\n[{'Amanda':^10s}]\n[{'Amanda':<10s}]")


def concatenate_and_repeat_strings():
    positive_type_number = f"{101:+15d}"
    positive_type_number_padded = f"{101:+015d}"

    #print(positive_type_number_padded)
    #print(f"{27:d}\n{30:+d}\n{10: d}")

    number_with_comas = f"{1423523534:,d}"
    #print(f"{number_with_comas}")

    #print(f"{10240.473:+10,.2f}\n{-3210.9521:10,.2f}")


def stripping_whitespaces():
    given_string = f"\n\t\t\t\t \n What are we doing here man ? \t \n"
    print(given_string.strip())
    print(given_string.lstrip())
    print(given_string.rstrip())

    input_string = '    hello    '
    print(input_string.lstrip())
    print(input_string.rstrip())


def chancing_char_case():
    given_string = 'hello world'

    print(given_string.capitalize())
    print(given_string.title())

    print(given_string.upper())


def operators_for_strings():
    if 'Orange' == 'orange':
        print(f"GOOD!")
    elif 'Orange'.lower() == 'orange':
        print(f"GG")


def searching_the_string():
    sentence = 'to be or not to be that is the question'

    #print(sentence.count('to'))
    #print(sentence.count('to', 12))
    #print(sentence.count('to', 0, 10))

    location = sentence.index('be')
    print(location)

    location_2 = sentence.rindex('be')
    print(location_2)

    location_3 = sentence.find('be')
    print(location_3)

    location_4 = sentence.rfind('be')
    print(location_4)

    if 'be' in sentence:
        print(f"{sentence.index('be')}")

    if sentence.startswith('to'):
        print("True")

    if sentence.endswith('question'):
        print(f"True again!")

    print(f" * Words from sentence that starts with 't':", end=" ")
    for i in sentence.split():
        if i.lower().startswith('t'):
            print(f"{i}", end=" ")


def replacing_substrings():
    values = '1\t2\t3\t4\t5\t6'

    after_replacement = values.replace('\t', ', ')
    print(after_replacement)

    given_values = '1 2 3 4 5'

    rplc = given_values.replace(' ', ' --> ')
    print(rplc)


def splitting_joining_strings():
    letters = 'A, B, C, D'
    after_split = letters.split(', ')

    after_split_2 = letters.split(', ', 2)

    print(after_split)
    print(after_split_2)

    letters_list = ['A', 'B', 'C', 'D']

    combined = ', '.join(letters_list)
    print(combined)

    print(f"{', '.join([str(i) for i in range(11)])}")

    return_value = list('Valentin: 89, 90, 67'.partition(': '))
    print(return_value)

    url_given = 'https://learning.oreilly.com/videos/python-fundamentals/9780135917411/9780135917411-PFLL_Lesson08_11'
    address_extracted = url_given.rpartition('/')

    splitted_by_sep = url_given.split('/')
    print(splitted_by_sep)

    print(address_extracted)

    given_text = """nebunieee mare
sa fie bine sa nuj fie rau boss
lux si opulenta nebunue"""

    extracted = given_text.splitlines()
    extracted_2 = given_text.splitlines(True)
    print(extracted)
    print(extracted_2)

    #----
    given_line = 'Pamela White'

    extracted_words = given_line.split()
    final_word_to_print = ', '.join(reversed(extracted_words))

    print(final_word_to_print)
    #-----

    our_text = 'https://www.digionline.ro/general/tvr1'
    protocol, separator, entire_link = our_text.rpartition('//')

    extracted_link, separator, channel = entire_link.partition('/')
    channel = channel.rpartition('/')[2]

    print(f"\n{' * Website to access: '}{extracted_link}\n{' * Channel: '}{channel:>14}")


def char_testing_methods():
    var = '-23'
    var = '23'
    print(f"{var.isdigit()}")

    var_1 = 'A78235'
    print(var_1.isalnum())

    sentence = 'hello world'
    print(sentence.isalnum())
    print(sentence.isascii())

    ax = sentence.center(18, '#')
    print(ax)


def raw_string():
    given_raw_string = r'https://vpnoverview.com/unblocking/sports/watch-nfl-online/'
    print(given_raw_string)


def regex_with_python():
    given_pattern = '03045'

    if re.fullmatch(given_pattern, '03045'):
        print(f"Matched")

    given_pattern_to_search_for = r"(\d.*\.\d.*)\s(\d+\.\d+)"

    if re.fullmatch(given_pattern_to_search_for, '42.3 101.2 44.2'):
        print(f"{'All Good!!'}")

    my_filelist_id_pattern = r'[A-Za-z]\d+[a-z]+\d+'

    if re.fullmatch(my_filelist_id_pattern, 's0ar3'):
        print(f"we have a match!")

    my_id = r'^[^A-Za-z].*'
    if re.fullmatch(my_id, '5oarevalentinn'):
        print(f'Good!')

    given_text_to_match = 'Str. Inginer Lucretiu Patrascanu, Nr. 9, Bl. Y2, Ap. 21'
    pattern_to_use = r'str\. \w.*, nr\. \d.*, bl\. [A-Za-z0-9].*, ap\. [A-Za-z0-9].*'

    if re.fullmatch(pattern_to_use, given_text_to_match.lower()):
        print(f"All OK!")


def replacing_and_splitting_substrings():
    to_work_on = '1\t2\t3\t4\t5'

    output_result = re.sub(r'\t', ', ', to_work_on, count=2)
    print(output_result)

    text_to_work = '1, 2, 3,4,       5,6,7,8'

    out_result = re.split(r',\s*', text_to_work)
    print(out_result)

    #-----
    txt_to_work_with = 'A\tB\t\tC\t\t\tD'
    text_after_processing = re.sub(r'\t+', ', ', txt_to_work_with)

    print(text_after_processing)

    #------

    address = '123$Main$$Street'
    after_processing = re.split(r'\$+', address)
    print(after_processing)


def other_tasks_with_re():
    result = re.search(r'[Pp]ython', 'We learn some cool things in python3.11.')
    print(result.group())

    result_2 = re.search(r'python', 'We just love PyThOn', flags=re.IGNORECASE)
    print(result_2.group())


    #-----
    contact = 'Valentin Soare, Home: 0246-218035, Mobile: 0723-138-260'
    name_from_contact = r'([A-Za-z]+)\s([A-Za-z]+)'
    phone_numbers = r'\d{4}-\d{6}|\d{4}-\d{3}-\d{3}'

    result_name = re.findall(name_from_contact, contact)
    result_phone_numbers = re.findall(phone_numbers, contact)

    print(f"\nName extracted: {result_name}")
    print(f"Phone numbers extracted: {result_phone_numbers}")

    for phone in re.finditer(phone_numbers, contact):
        print(phone.group())


    #-----------

    text = 'Valentin Soare, email: soarevalentinn@gmail.com'
    pattern = r'([A-Z][a-z]+ [A-Z][a-z]+)|([a-z]+@[a-z]+\.com)'

    list_with_output = []
    for result in re.findall(pattern, text):
        for element in result:
            if element:
                list_with_output.append(element)

    print(list_with_output)

    #-----------

    given_text = '10 + 5'
    pattern_to_use = r'(\d+)\s([+\-*/])\s(\d+)'

    result_after_executed = re.search(pattern_to_use, given_text)
    print(result_after_executed.groups())


    ax = 'Nebunie'

    print(ax.capitalize())

def main():
    #strings_exercises()
    #formatting_strings()
    #concatenate_and_repeat_strings()
    #stripping_whitespaces()
    #chancing_char_case()
    #operators_for_strings()
    #searching_the_string()
    #replacing_substrings()
    #splitting_joining_strings()
    #char_testing_methods()
    #raw_string()
    #regex_with_python()
    #replacing_and_splitting_substrings()
    other_tasks_with_re()

if __name__ == '__main__':
    main()
