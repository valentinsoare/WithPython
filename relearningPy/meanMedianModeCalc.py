#!/usr/bin/python

"""Calculating the mean median mode from a list"""

import os
import statistics


def how_many_numbers_we_want():
    value_error = ''
    message = "** How many numbers you want to add to use in mean, median, mode (q to quit):"
    length_of_message = len(message)

    while True:
        print(f"\n{' ' * 5} {'-' * (length_of_message + 4)}")
        print(f"{' ' * 5} {message}", end=" ")
        give_answer = input()

        if give_answer.lower()[0] == 'q':
            print(f"\n{' ' * 9} Exiting...")
            os.system('sleep 1')
            exit(0)

        try:
            give_answer = int(give_answer)
        except ValueError:
            value_error = 'error'

        if value_error == 'error' or give_answer < 0:
            print(f"\n{' ' * 7}\033[1;31m ERROR \033[0m Please use only integers greater than zero.")
            os.system('sleep 1; clear')
            value_error = ''
        else:
            os.system('clear')
            return give_answer


def populate_list_to_process(number_of_values_in_the_list):
    counter = 0
    to_check_error = ''
    message = "** Please provide the number (q to quit):"
    length_of_given_message = len(message)
    list_to_return = []

    while counter < number_of_values_in_the_list:
        os.system('clear')
        print(f"\n{' ' * 5} {'-' * (length_of_given_message + 6)}")
        print(f"{' ' * 5} {counter + 1}. {message}", end=" ")
        given_answer = input()

        if given_answer.lower()[0] == 'q':
            print(f"\n{' ' * 9} Exiting...")
            os.system('sleep 1')
            exit(0)

        try:
            given_answer = int(given_answer)
        except ValueError:
            try:
                given_answer = float(given_answer)
            except ValueError:
                to_check_error = 'error'

        if to_check_error == 'error' or given_answer < 0:
            print(f"\n{' ' * 5}\033[1;31m ERROR \033[0m Please use only positive numbers of type integer or float.")
            os.system('sleep 1')
            to_check_error = ''
        else:
            list_to_return.append(given_answer)
            counter += 1

    print(f"\n{' ' * 8}\033[1;32m SUCCESS \033[0m All numbers have been added. We will calculate:")
    return list_to_return


def calculate_mean_median_mode(list_with_numbers):
    calculate_mode = statistics.mode(list_with_numbers)
    calculate_mean = statistics.mean(list_with_numbers)
    calculate_median = statistics.median(sorted(list_with_numbers))

    os.system('sleep 1')
    print(f"\n{' ' * 8} - > Mean: {calculate_mean:.2f}")
    print(f"{' ' * 8} -- > Median: {calculate_median:.2f}")
    print(f"{' ' * 8} --- > Mode: {calculate_mode:.2f}\n")


def main():
    number_of_reps = how_many_numbers_we_want()
    list_with_numbers = populate_list_to_process(number_of_reps)
    calculate_mean_median_mode(list_with_numbers)


if __name__ == "__main__":
    main()
