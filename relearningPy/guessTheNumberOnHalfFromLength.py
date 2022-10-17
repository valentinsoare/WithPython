#!/usr/bin/python

import os
import random


def header_printing_with_style(message_to_print_as_header):
    length_of_header = len(message_to_print_as_header)
    print(f"\n{' ' * 15}{'-' * length_of_header * 2}")
    print(f"{' ' * (15 + (length_of_header // 2))}{message_to_print_as_header}")
    print(f"{' ' * 15}{'-' * length_of_header * 2}")


def for_exit(given_answer):
    if given_answer.lower()[0] == 'q':
        print(f"\n{' ' * 10} Exiting...\n")
        os.system('sleep 1')
        exit(0)


def ask_questions(value_for_exit=0):
    if value_for_exit == 0:
        print(f"\n{' ' * 4} [1] Please give the min of the range, only integers, for generating the number to guess (q to quit):",
              end=" ")
        given_range = input()
    elif value_for_exit == 1:
        print(f"\n{' ' * 4} [2] Please give the max of the range, only integers, for generating the number to guess (q to quit):",
              end=" ")
        given_range = input()
    elif value_for_exit == 2:
        print(f"\n{' ' * 4} [3] Please give the number of tries we have to guess the number (q to quit):", end=" ")
        given_range = input()

    for_exit(given_range)

    return given_range


def ask_for_limits_of_range_numbers():
    value_for_exit = 0
    list_with_values = []

    while len(list_with_values) != 3:
        header_printing_with_style('**Number To Guess**')

        given_range = ask_questions(value_for_exit)

        try:
            after_processed = int(given_range)
        except ValueError:
            after_processed = 'error'

        if (str(after_processed) == 'error' or after_processed < 0) or (len(list_with_values) == 1 and after_processed < list_with_values[0]):
            print(f"\n{' ' * 10}\033[1;31mERROR\033[0m - Please use only integers greater than or equal to 0. Second number should be greater than first number.")
            os.system('sleep 2; clear')
        else:
            list_with_values.append(after_processed)
            os.system('clear')
            value_for_exit += 1

    return tuple(list_with_values)


def set_number_to_guess(range_min=1, range_max=100):
    number_to_guess = random.randrange(range_min, range_max, 1)
    return number_to_guess


def ask_for_question(value_min, value_max, nr_of_tries):
    print(f"\n {' ' * 4}[{nr_of_tries + 1} attempt] ** Guess the number between {value_min} and {value_max} (q to quit):", end=" ")
    given_answer = input()

    for_exit(given_answer)

    to_check = 0

    try:
        processed_answer = int(given_answer)
    except ValueError:
        to_check = 'error'

    if to_check == 'error' or not (value_min <= processed_answer <= value_max):
        print(f"\n{' ' * 10}\033[1;31m ERROR \033[0m - Only integers between {value_min} and {value_max}! ")
        os.system('sleep 1')
        processed_answer = -1

    return processed_answer


def main():
    number_of_guesses = 0
    guessed_number = -1

    min_value, max_value, limit_of_guesses = ask_for_limits_of_range_numbers()
    number_for_guessing = set_number_to_guess(min_value, max_value)

    while guessed_number != number_for_guessing:
        os.system('clear')
        header_printing_with_style('**Number To Guess**')

        guessed_number = ask_for_question(min_value, max_value, number_of_guesses)

        if guessed_number == -1:
            continue
        elif guessed_number < number_for_guessing:
            print(f"\n{' ' * 10} Too low. Try again!")
            os.system('sleep 1')
        elif guessed_number > number_for_guessing:
            print(f"\n{' ' * 10} Too high. Try again!")
            os.system('sleep 1')

        number_of_guesses += 1

    print(f"\n{' ' * 10} \033[1;32m SUCCESS\033[0m You guessed the number {guessed_number} in {number_of_guesses + 1} attempts.")

    if number_of_guesses <= limit_of_guesses:
        print(f"{' ' * 19} Either you know the secret or you got lucky punk!\n")
    elif number_of_guesses > limit_of_guesses:
        print(f"{' ' * 19} Should be able to do better!\n")


if __name__ == '__main__':
    main()
