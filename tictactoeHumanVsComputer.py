#!/usr/bin/python3

import os
import time
import random
import numpy as np

table_for_display = np.array(np.full(9, '[   ]').reshape((3, 3)))
signs = ['X', 'O']
numeric = np.array(np.full(9, 0).reshape((3, 3)))

print(f'\n\tCurrent game: Human VS Computer.\n')


def lines(number_of_lines):
    i = 0
    while i < number_of_lines:
        print(f'-', end='')
        i += 1
    print()


def display_board(giving_board):
    for i in giving_board:
        for j in i:
            print(f'{j}', end=' ')
        print()


def printing_board():
    print(f'Playing board:')
    lines(18)
    display_board(table_for_display)
    lines(18)


def register_player():
    print(f'\n*We need the name of only one player. The game is human vs computer.')
    return input('\t*Please enter your name in order to be registered: ').capitalize()


def choose_rounds(name):
    return int(input(f'\n*{name} who goes first, you or the computer ?\n\t-Human: 0\n\t-Computer: 1\n\t-Answer: '))


def print_present_order(players_order, player_name):
    print(f'\n*Present order:')

    if players_order == 0:
        print(f'\t-{player_name} will choose first and then the computer.')
    elif players_order == 1:
        print(f'\t-Computer is moving first.')

    time.sleep(1.5)
    os.system('clear')


def collect_possible_moves(table):
    available_options = []
    options_to_print = []

    length_table = len(table)
    for row in range(length_table):
        for column in range(len(table[row])):
            if np.any(table[row][column] != '[ X ]' and table[row][column] != '[ O ]'):
                options_to_print.append((row, column))
                available_options.append((row, column))

    return options_to_print, available_options


def print_possible_moves(options_to_print):
    print(f'\n*Computer is choosing now the row and column to put an {signs[1]}.', end=' ')
    print(f'{len(options_to_print)} options available: ', end='\n  ')

    for row, column in options_to_print:
        print(f'({row}, {column})', end=' ')
    print()

    time.sleep(1)


def print_first_diag(table):
    length_table = len(table)
    for i in range(length_table):
        for j in range(len(table[i])):
            if j == i:
                print(f'\033[31m{table[i][j]}\033[0m', end=' ')
            else:
                print(f'{table[i][j]}', end=' ')
        print()


def print_second_diag(table):
    length_table = len(table)
    for i in range(length_table):
        for j in range(len(table[i])):
            if i == length_table - 1 - j:
                print(f'\033[31m{table[i][j]}\033[0m', end=' ')
            else:
                print(f'{table[i][j]}', end=' ')
        print()


def pretty_print_rows_col(table, given_opt, location):
    length_table = len(table)
    for i in range(length_table):
        for j in range(len(table[i])):
            if location == 0 and i == given_opt:
                print(f'\033[31m{table[i][j]}\033[0m', end=' ')
            elif location == 1 and j == given_opt:
                print(f'\033[32m{table[i][j]}\033[0m', end=' ')
            else:
                print(f'{table[i][j]}', end=' ')
        print()


def colorized_winner_rows_col(table, given_opt, is_row):

    if is_row == 0:
        print(f'\nEnding...')
        lines(18)
        pretty_print_rows_col(table, given_opt, 0)
    elif is_row == 1:
        print(f'\nEnding...')
        lines(18)
        pretty_print_rows_col(table, given_opt, 1)

    lines(18)
    exit()


def colorized_winner_diags(diag, table, given_name):

    if diag == 1:
        print(f'\nWINNER WINNER CHICKEN DINNER !!\nDiag with same values, {given_name} is the winner.')
        print(f'\nEnding...')
        lines(18)
        print_first_diag(table)
    elif diag == 2:
        print(f'\nWINNER WINNER CHICKEN DINNER !!\nDiag with same values, {given_name} is the winner.')
        print(f'\nEnding...')
        lines(18)
        print_second_diag(table)

    lines(18)
    exit()


def checking_list(list_check, given_name, diag, table):
    if list_check.count(1) == 3:
        colorized_winner_diags(diag, table, given_name)
    elif list_check.count(2) == 3:
        colorized_winner_diags(diag, table, 'Computer')


def check_diagonals(numeric, given_name, table):
    list_check = []
    first_diag = 0
    second_diag = 0

    length_numeric = len(numeric)
    for i in range(length_numeric):
        for j in range(len(numeric[i])):
            if j == i:
                list_check.append(numeric[i][j])
                first_diag = 1

    checking_list(list_check, given_name, first_diag, table)

    list_check.clear()

    for i in range(length_numeric - 1, -1, -1):
        for j in range(len(numeric[i])):
            if j == (length_numeric - 1 - i):
                list_check.append(numeric[i][j])
                second_diag = 2

    checking_list(list_check, given_name, second_diag, table)


def check_winner(*args):
    table, given_name, numeric = args

    def select_winner(i, given_name, table, numeric):
        given_dict = {
            'list(numeric[i, :].flatten()).count(1)': ['colorized_winner_rows_col(table, i, 0)',
                                                       f"\nWINNER WINNER CHICKEN DINNER !!\n Row number {i}, "
                                                       f"{given_name} is the winner."],
            'list(numeric[i, :].flatten()).count(2)': ['colorized_winner_rows_col(table, i, 0)',
                                                       f"\nWINNER WINNER CHICKEN DINNER !!\n Row number {i},"
                                                       f" Computer is the winner."],
            'list(numeric[:, i].flatten()).count(1)': ['colorized_winner_rows_col(table, i, 1)', f"\nWINNER WINNER CHICKEN DINNER !!\n "
                                                       f"Column number {i}, {given_name} is the winner."],
            'list(numeric[:, i].flatten()).count(2)': ['colorized_winner_rows_col(table, i, 1)', f"\nWINNER WINNER CHICKEN DINNER !!\n "
                                                       f"Column number {i}, Computer is the winner."]
        }

        given_dict_items = given_dict.items()
        for j, k in given_dict_items:
            if eval(j) == 3:
                print(k[1])
                return eval(k[0])
            else:
                check_diagonals(numeric, given_name, table)

    table_length = len(table)
    for i in range(table_length):
        select_winner(i, given_name, table, numeric)


def human_player_check(*args):
    p1, reps, given_name, table, numeric = args

    printing_board()
    print(f'*{given_name} -> please specify row and column to put an {signs[0]} - >')
    player_row = int(input(f'\t-Row: '))
    player_column = int(input(f'\t-Column: '))

    if np.any(table[player_row, player_column] == '[ X ]' or table[player_row, player_column] == '[ O ]'):
        print(f'\nERROR - location already contains a given sign, please try again\n')
    else:
        table[player_row, player_column] = '[ X ]'
        numeric[player_row, player_column] = 1
        check_winner(table, given_name, numeric)
        reps += 1
        p1 += 1

    return p1, reps, table, numeric


def pc_player_check(*args):
    pc, reps, table, available_moves, moves_to_print, given_name, numeric = args
    print()
    printing_board()
    print_possible_moves(moves_to_print)

    random.shuffle(available_moves)
    choosen_row, choosen_column = available_moves[0]

    table[choosen_row, choosen_column] = '[ O ]'
    numeric[choosen_row, choosen_column] = 2
    print(f'\n*Computer has chosen {available_moves[0]}\n')
    check_winner(table, given_name, numeric)
    time.sleep(1)
    pc += 1
    reps += 1

    return pc, reps, table, numeric


def human_first(*args):
    p1, pc, reps, given_name, table, numeric = args

    while True:
        if p1 == 0:
            p1, reps, table, numeric = human_player_check(p1, reps, given_name, table, numeric)
        elif pc == 0:
            moves_to_print, available_moves = collect_possible_moves(table)
            pc, reps, table, numeric = pc_player_check(pc, reps, table, available_moves, moves_to_print, given_name, numeric)
        else:
            break

    return reps, given_name, table, numeric


def pc_first(*args):
    p1, pc, reps, given_name, table, numeric = args

    while True:
        if pc == 0 and reps <= 8:
            moves_to_print, available_moves = collect_possible_moves(table)
            pc, reps, table, numeric = pc_player_check(pc, reps, table, available_moves, moves_to_print, given_name, numeric)
        elif p1 == 0 and reps <= 8:
            p1, reps, table, numeric = human_player_check(p1, reps, given_name, table, numeric)
        else:
            break

    return reps, given_name, table, numeric


def fill_columns_rows(*args):
    p1 = 0
    pc = 0
    given_name, given_order, reps, table, numeric = args

    if given_order == 0:
        os.system('clear')
        reps, given_name, table, numeric = human_first(p1, pc, reps, given_name, table, numeric)
    elif given_order == 1:
        os.system('clear')
        reps, given_name, table, numeric = pc_first(p1, pc, reps, given_name, table, numeric)

    return reps


def main():
    i = 0
    repetitions = 0
    printing_board()
    player_name = register_player()
    players_order = choose_rounds(player_name)
    print_present_order(players_order, player_name)

    while i < 9:
        repetitions = fill_columns_rows(player_name, players_order, repetitions, table_for_display, numeric)
        i += 1

    print()
    printing_board()
    print('\n*We have a draw, nobody win.')


main()
