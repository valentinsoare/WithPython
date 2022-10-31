#!/usr/bin/python

import os
type_of_math = [(0, 'addition'), (1, 'subtraction'), (2, 'multiplication'), (3, 'division')]


def printing_header(given_message):
    message_split = given_message.split()
    message_processed = ' * '.join(map(lambda i: i, message_split))
    length_of_message = len(message_processed)

    print(f"\n{' ' * 10}{' ' * ((length_of_message // 2) - 1)}{message_processed}")
    print(f"{' ' * 10}{'-' * (length_of_message * 2)}")


def ask_operation_type():
    error = 0
    processed_answer = ''

    while not isinstance(processed_answer, int):
        os.system('clear')
        printing_header("Game of Math")
        print(f"{' ' * 2} * Pleas select the type of operation you want:\n")

        for i in type_of_math:
            print(f"{' ' * 5} {(i[0] + 1)}. {i[1].capitalize()}")

        print(f"\n{' ' * 2} * Answer (q to quit):", end=" ")
        given_answer = input()

        if given_answer.lower()[0] == 'q':
            print(f"\n{' ' * 5} * Exiting...")
            os.system('sleep 2')
            exit(1)

        try:
            processed_answer = (int(given_answer) - 1)
        except ValueError:
            error = 1

        if error == 1 or processed_answer not in list(range(0, 4)):
            print(f"\n{' ' * 5} ERROR - please use an option between 1 and 5.")
            os.system('sleep 2')
            error = 0
        else:
            return processed_answer


def main():

    while True:
        chosen_operation = ask_operation_type()


if __name__ == '__main__':
    main()
