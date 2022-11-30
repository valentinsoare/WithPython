#!/usr/bin/python

import numpy as np


def printing_header_board(message_to_use):
    message_to_print = ' ## '
    message_to_print += ' '.join(i for i in message_to_use)
    message_to_print += ' ## '

    length_message = len(message_to_print)

    print(f"\n{' ' * (length_message // 2)}{message_to_print}")
    print(f"{' ' * (length_message // 4)}{'-' * int(length_message * 1.6)}")

    return length_message


def create_checkerboard(row, column):
    dash = '-'
    asterisk = '*'

    checker_board = np.full((row, column), " ")

    for i in range(len(checker_board)):
        for j in range(len(checker_board[i])):
            if (i + j) % 2 == 0:
                checker_board[i][j] = dash
            else:
                checker_board[i][j] = asterisk

    return checker_board


def printing_checkerboard(checker_board, length_of_message):
    for row in range(len(checker_board)):
        print(f"{' ' * int(length_of_message // 1.5)}", end="")
        for column in range(len(checker_board[row])):
            print(f"{checker_board[row][column]}", end=" ")
        print()

    print(f"{' ' * int(length_of_message // 4)}{'-' * int(length_of_message * 1.6)}")


def main():
    length_of_message_header = printing_header_board('Checkerboard')
    checker_board_to_print = create_checkerboard(10, 10)
    printing_checkerboard(checker_board_to_print, length_of_message_header)


if __name__ == '__main__':
    main()
