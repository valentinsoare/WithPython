#!/usr/bin/python

import os


def print_message(given_message):
    print(f"\n{'':>19}{'-' * (len(given_message) * 2 + 1)}")
    print(f"{'|':>20}{' ' * (len(given_message) // 2)}{given_message}{' ' * (len(given_message) // 2)}|")
    print(f"{'':>19}{'-' * (len(given_message) * 2 + 1)}")


def ask_for_how_many_numbers_we_want():
    while True:
        print_message('Two Largest Numbers')

        print(f"\n{' ' * 2}+ How many numbers you want to compare (q to quit):", end=" ")
        answer_from_user = input()

        try:
            answer_after_processing = int(answer_from_user)
            if answer_after_processing < 0:
                answer_after_processing *= -1
        except ValueError:
            if answer_from_user.lower()[0] == 'q':
                print(f"\n{' ' * 4} Exiting...")
                exit(0)

            answer_after_processing = 'error'

        if answer_after_processing == 'error' or answer_after_processing < 2:
            print(f"\n\033[1;31m ERROR\033[0m You need to use only integers greater or equal to 2.")
            os.system('sleep 1')
            os.system('clear')
        else:
            return answer_after_processing


def ask_for_numbers_to_compare(how_many):
    count = 0
    given_list_with_numbers = []

    os.system('clear')

    while count < how_many:
        print_message('Two Largest Numbers')

        print(f"\n\n {count}. Please enter a number:", end=" ")
        answer_number = input()

        try:
            answer_number = int(answer_number)
        except ValueError:
            try:
                answer_number = float(answer_number)
            except ValueError:
                print(f"\n{' ':>3}\033[1;31m ERROR \033[0m Wrong type of input. You can use only integers or float type.")
                os.system('sleep 1; clear')

        if isinstance(answer_number, int) or isinstance(answer_number, float):
            given_list_with_numbers.append(answer_number)
            count += 1
            os.system('clear')

    return given_list_with_numbers


def determine_largest_two_numbers(numbers_given):
    second_to_largest = 0
    largest_number = 0
    length_of_list = len(numbers_given)

    for i in range(length_of_list):
        if numbers_given[i] > largest_number:
            second_to_largest = largest_number
            largest_number = numbers_given[i]
        elif numbers_given[i] > second_to_largest:
            second_to_largest = numbers_given[i]

    return largest_number, second_to_largest


def print_result(first, second):
    print_message('Two Largest Numbers')

    print(f"\n{' ':>2} \033[1;32mRESULT - > \033[0m Largest: {first}, Second to largest: {second}")


def main():
    number_after_processed = ask_for_how_many_numbers_we_want()
    list_with_numbers_given = ask_for_numbers_to_compare(number_after_processed)

    largest, second = determine_largest_two_numbers(list_with_numbers_given)
    print_result(largest, second)


if __name__ == "__main__":
    main()
