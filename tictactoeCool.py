#!/usr/bin/python

import os
import sys
import time
import numpy as np


def catch_names():

    name_1 = 0
    name_2 = 0

    while not isinstance(name_1, str) or not isinstance(name_2, str):
        print(f'\n\033[1;32m{"Tic Tac Toe":>24}\033[0m', end="\n")
        name_1 = input("\n\033[1m - > Name for the first player (q to quit): \033[0m")
        if not name_1.isalpha():
            print(f"\n\033[31m ERROR, you need to try again!!", end="\n")
            time.sleep(1)
            os.system('clear')
            continue
        elif name_1[0].lower() == "q":
            print(f"\n\033[31m Quitting.....\033[0m\n\n", end=" ")
            sys.exit(1)

        while True:
            name_2 = input("\033[1m - > Name of the second player (q to quit): \033[0m")
            if not name_2.isalpha():
                print(f"\n\033[31m ERROR, you need to try again!!\033[0m", end="\n\n")
                time.sleep(1)
            elif name_2[0].lower() == "q":
                print(f"\n\033[31m Quitting.....\033[0m\n\n", end=" ")
                sys.exit(1)
            else:
                break
    os.system('clear')
    return name_1, name_2


def draw_board(name_1, name_2, to_generate, *args):

    if to_generate == 1:
        tictactoe_board = np.array(np.full(9, "[   ]").reshape(3, 3))
    else:
        tictactoe_board = np.array(args[0])

    print(f'\n\033[1;32m{"Tic Tac Toe":>24}\n{name_1[0].capitalize():>16} vs {name_2[0].capitalize()}\033[0m', end="\n\n")

    for row in range(len(tictactoe_board)):
        for element in range(len(tictactoe_board[row])):
            if element == 0:
                print(f"\033[1m{tictactoe_board[row][element]:>15}\033[0m", end=" ")
            else:
                print(f"\033[1m{tictactoe_board[row][element]}\033[0m", end=" ")
        print()

    if to_generate == 1:
        return tictactoe_board


def who_goes(name_1, name_2):
    goes_first = 'X'
    goes_second = 'X'
    tictactoe_given_board = ''

    while goes_first.capitalize() not in [name_1.capitalize(), name_2.capitalize()]:
        tictactoe_given_board = draw_board(name_1, name_2, 1)
        print(f"\n\033[1m - > Who goes first, {name_1.capitalize()} or {name_2.capitalize()} "
              f"? (q to quit) - >", end=" ")
        goes_first = input()

        if goes_first.capitalize() not in [name_1.capitalize(), name_2.capitalize(), "Q"]:
            print(f"\n\033[31m ERROR, you need to try again!!", end="\n")
            time.sleep(1)
            os.system('clear')
        elif goes_first[0].capitalize() == 'Q':
            print(f"\n\033[31m Quitting.....\033[0m\n\n", end=" ")
            sys.exit(1)
        elif goes_first.capitalize() != name_1.capitalize():
            goes_second = name_1.capitalize()
        elif goes_first.capitalize() != name_2.capitalize():
            goes_second = name_2.capitalize()

    return goes_first, goes_second, tictactoe_given_board


def board_digits_populate(to_generate, *args):
    if to_generate == 1:
        digits_board = np.array(np.full(9, 100).reshape(3, 3), dtype=int)
        return digits_board
    else:
        board_start, row, column, player_1, player_2, choose_player = args
        digits_board = np.array(board_start.reshape(3, 3))

    if digits_board[row][column] == 100 and choose_player == 1:
        digits_board[row][column] = 1
    elif digits_board[row][column] == 100 and choose_player == 2:
        digits_board[row][column] = 2

    return digits_board


def board_populate_array_signs(board_with_all_digits, tic_board):
    for row in range(len(board_with_all_digits)):
        for column in range(len(board_with_all_digits[row])):
            if board_with_all_digits[row][column] == 1:
                tic_board[row][column] = '[ X ]'
            elif board_with_all_digits[row][column] == 2:
                tic_board[row][column] = '[ 0 ]'

    return tic_board


def select_row_column(what_to_select):
    if what_to_select == 1:
        print(f"\033[1m - > Row [1-3]: \033[0m", end="")
    else:
        print(f"\033[1m - > Column [1-3]: \033[0m", end="")

    element = input()

    if element in ['1', '2', '3']:
        element = (int(element) - 1)
    else:
        if element[0].capitalize() == "Q":
            print(f"\n\033[31m Quitting.....\033[0m\n\n", end=" ")
            sys.exit(1)

    return element


def ask_for_row_column(name_1, name_2, board_to_print, first_chooser):
    while True:
        draw_board(name_1, name_2, 0, board_to_print)

        if first_chooser == 1:
            print(f'\n\n\033[1m PLAYER: {name_1} will put an "X" (q to quit).\n{"-" * 60:>16}\033[0m')
        elif first_chooser == 2:
            print(f'\n\n\033[1m PLAYER: {name_2} will mark the spot with "0" (q to quit).\n{"-" * 60:>16}\033[0m')

        row = select_row_column(1)
        if row not in [0, 1, 2]:
            print(f"\n\033[31m ERROR please select again! \033[0m\n")
            time.sleep(0.5)
            os.system('clear')
            continue

        column = select_row_column(2)
        if column not in [0, 1, 2]:
            print(f"\n\033[31m ERROR please select again! \033[0m\n")
            time.sleep(0.5)
            os.system('clear')
        else:
            return row, column

def check_diags_winner(given_2d_array, diag_type):
    count_diag = []
    player = ''

    if diag_type == 2:
        given_2d_array = np.flip(given_2d_array, axis=1)

    for row in range(len(given_2d_array)):
        for column in range(len(given_2d_array[row])):
            if column == row:
                count_diag.append(given_2d_array[row][column])

    if count_diag.count(1) == 3:
        player = 'first'
    if count_diag.count(2) == 3:
        player = 'second'

    return player


def check_rows_columns_winner(given_array, for_row):
    winner_row = 100
    player = ''

    if for_row == 0:
        given_array = given_array.transpose()

    for row in range(len(given_array)):
        if sum(list(given_array[row])) == 3:
            winner_row = row
            player = 'first'
        elif sum(list(given_array[row])) == 6:
            winner_row = row
            player = 'second'

    return winner_row, player


def colorize_rows_column(given_array, element, to_choose):
    os.system('clear')
    print(f'\n\n\033[1m {"WINNER WINNER CHICKEN DINNER!!!":>37}\033[0m', end="\n\n")

    for row in range(len(given_array)):
        print(f'{" ":>13}', end="")
        for column in range(len(given_array[row])):
            if to_choose == 0 and element == column:
                print(f"\033[1;32m{given_array[row][column]}\033[0m", end=" ")
            elif to_choose == 1 and element == row:
                print(f"\033[1;33m{given_array[row][column]}\033[0m", end=" ")
            else:
                print(f"\033[1m{given_array[row][column]}\033[0m", end=" ")
        print()


def colorize_diags(given_array, diag_type):
    os.system('clear')
    print(f'\n\n\033[1m {"WINNER WINNER CHICKEN DINNER!!!":>37}\033[0m', end="\n\n")

    if diag_type == 1:

        for row in range(len(given_array)):
            print(f'{" ":>13}', end="")
            for column in range(len(given_array[row])):
                if row == column:
                    print(f"\033[1;31m{given_array[row][column]}\033[0m", end=" ")
                else:
                    print(f"\033[1m{given_array[row][column]}\033[0m", end=" ")
            print()

    elif diag_type == 2:

        for row in range(len(given_array)):
            print(f'{" ":>13}', end="")
            for column in range(len(given_array)):
                if row == (len(given_array) - column - 1):
                    print(f"\033[1;31m{given_array[row][column]}\033[0m", end=" ")
                else:
                    print(f"\033[1m{given_array[row][column]}\033[0m", end=" ")
            print()


def catch_winner_printing(goes_first, goes_second, digits_board_start, tictactoe_board):
    def printing_winner_rows_column(winner_type, player_type, if_type, if_diag=0):

        if winner_type in [0, 1, 2]:
            if if_type == 0:
                colorize_rows_column(tictactoe_board, winner_type, 0)
            elif if_type == 1:
                colorize_rows_column(tictactoe_board, winner_type, 1)
            else:
                if if_diag == 1:
                    colorize_diags(tictactoe_board, 1)
                elif if_diag == 2:
                    colorize_diags(tictactoe_board, 2)

            if player_type == 'first':
                print(f'\n\033[1m {"WINNER:":>20} {goes_first}\033[0m', end="\n\n")
                time.sleep(2)
                sys.exit(1)
            elif player_type == 'second':
                print(f'\n\033[1m {"WINNER:":>20} {goes_second}\033[0m', end="\n\n")
                time.sleep(2)
                sys.exit(1)

    winner_column, player_column = check_rows_columns_winner(digits_board_start, 0)
    printing_winner_rows_column(winner_column, player_column, 0)

    winner_row, player_row = check_rows_columns_winner(digits_board_start, 1)
    printing_winner_rows_column(winner_row, player_row, 1)

    player_first_diag = check_diags_winner(digits_board_start, 1)
    if player_first_diag == 'first' or player_first_diag == 'second':
        printing_winner_rows_column(1, player_first_diag, 3, 1)

    player_second_diag = check_diags_winner(digits_board_start, 2)
    if player_second_diag == 'first' or player_second_diag == 'second':
        printing_winner_rows_column(1, player_second_diag, 3, 2)



def put_X_and_O_first_player(goes_first, goes_second, tictactoe_board, first_player, digits_board_start):
    os.system('clear')
    row, column = ask_for_row_column(goes_first, goes_second, tictactoe_board, first_player)
    digits_board_start = board_digits_populate(0, digits_board_start, row, column, goes_first, goes_second,
                                               first_player)
    tictactoe_board = board_populate_array_signs(digits_board_start, tictactoe_board)
    catch_winner_printing(goes_first, goes_second, digits_board_start, tictactoe_board)

    return digits_board_start, tictactoe_board

def put_X_and_O_second_player(goes_first, goes_second, tictactoe_board, second_player, digits_board_start):
    os.system('clear')
    row, column = ask_for_row_column(goes_first, goes_second, tictactoe_board, second_player)
    digits_board_start = board_digits_populate(0, digits_board_start, row, column, goes_first, goes_second,
                                               second_player)
    tictactoe_board = board_populate_array_signs(digits_board_start, tictactoe_board)
    catch_winner_printing(goes_first, goes_second, digits_board_start, tictactoe_board)

    return digits_board_start, tictactoe_board


def main():
    first_player = 1
    os.system('clear')
    second_player = 2

    name_1, name_2 = catch_names()
    digits_board_start = board_digits_populate(1)
    goes_first, goes_second, tictactoe_board = who_goes(name_1, name_2)
    print(f'\n\033[1m - > {goes_first} will choose first and then {goes_second}. {goes_first} is using "X" and {goes_second} is with "0" \033[0m')
    time.sleep(3)

    while True:
        digits_board_start, tictactoe_board = put_X_and_O_first_player(goes_first, goes_second, tictactoe_board, first_player, digits_board_start)
        digits_board_start, tictactoe_board = put_X_and_O_second_player(goes_first, goes_second, tictactoe_board, second_player, digits_board_start)


main()
