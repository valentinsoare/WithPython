#!/usr/bin/python

import os
import numpy as np

one_second = 'sleep 1'


def printing_header(message_for_header, type_of_game):
    processed_message = ' * '
    what_type = ' ** '
    processed_message += ' '.join(i for i in message_for_header)
    what_type += ' '.join(j for j in type_of_game)
    processed_message += ' * '
    what_type += ' ** '

    length_first_message = len(processed_message)
    length_second_message = len(what_type)

    print(f"\n{' ' * length_second_message}{'-' * length_second_message}")
    print(f"{' ' * (length_second_message + (length_second_message - length_first_message) // 2)}{processed_message}")
    print(f"{' ' * length_second_message}{what_type}")
    print(f"{' ' * length_second_message}{'-' * length_second_message}")

    return length_first_message, length_second_message


def initialize_empty_board(rows=3, columns=3):
    empty_board = np.full((rows, columns), ' [   ] ')
    board_to_use_for_analyse = np.full((rows, columns), 100)
    return empty_board, board_to_use_for_analyse


def printing_tictactoe_board(game_board, length_second_message):

    print(f"\n{' ' * (length_second_message + (length_second_message // 4) - 2)}", end="")

    for row in range(len(game_board)):
        for column in range(len(game_board[row])):
            print(f"{game_board[row, column]}", end=" ")
        print(f"\n{' ' * (length_second_message + (length_second_message // 4) - 2)}", end="")


def writing_to_boards(row, column, sign, board_game, board_to_determine):
    if sign == 1:
        board_game[row, column] = ' [ X ] '
        board_to_determine[row, column] = 1
    else:
        board_game[row, column] = ' [ 0 ] '
        board_to_determine[row, column] = 0

    return board_game, board_to_determine


def check_if_quit(answer, second_message_length, message_to_use):
    if answer.isspace() or answer == '':
        print(f"\n{' ' * second_message_length} {message_to_use}")
        os.system(one_second)
        return True
    elif answer.lower()[0] == 'q':
        print(f"\n{' ' * second_message_length} Exiting....")
        os.system(one_second)
        exit(1)


def check_if_int_or_float(processed_answer, second_message_length, message_to_use):
    if isinstance(processed_answer, int) or isinstance(processed_answer, float):
        print(f"\n{' ' * second_message_length} {message_to_use}")
        os.system(one_second)


def names(game_board):
    count = 0
    name_of_players = []
    order = {'1': 'first', '2': 'second'}

    while count < 2:
        processed_answer = 'default'
        os.system('clear')
        first_message_length, second_message_length = printing_header('2D Tic-Tac-Toe', 'human vs human')
        printing_tictactoe_board(game_board, second_message_length)

        print(f"\n{' ' * (second_message_length // 2 + 8)} {list(order.keys())[count]}. Tell me the name of the {list(order.values())[count]} player (q to quit):", end=" ")
        answer = input().upper()

        if check_if_quit(answer, second_message_length, "ERROR - please use only strings or strings combined with integers/floats."):
            continue

        try:
            processed_answer = int(answer)
        except ValueError:
            try:
                processed_answer = float(answer)
            except ValueError:
                name_of_players.append(answer.capitalize().strip())
                count += 1

        check_if_int_or_float(processed_answer, second_message_length, "ERROR - please use only strings or strings combined with integers/floats.")

    return name_of_players


def who_will_start_first(list_of_players, game_board):
    count = 0
    order_of_start = []
    processed_answer = 'default'
    list_ways = ['first', 'second']

    while count < 2:
        processed_answer = 'default'
        os.system('clear')
        first_message_length, second_message_length = printing_header('2D Tic-Tac-Toe', 'human vs human')
        printing_tictactoe_board(game_board, second_message_length)

        print(f"\n{' ' * (second_message_length // 2 + 8)} * Please tell me who will start {list_ways[count]}", end=" ")
        print(f"{list_of_players} (q to quit)", end=": ")
        answer = input().upper()

        if check_if_quit(answer, second_message_length, "ERROR - please use only one of those two names."):
            continue

        try:
            processed_answer = int(answer)
        except ValueError:
            try:
                processed_answer = float(answer)
            except ValueError:
                answer = answer.capitalize().strip()
                if answer not in list_of_players:
                    print(f"\n{' ' * second_message_length} ERROR - please use only those names from the list.")
                    os.system(one_second)
                else:
                    order_of_start.append(answer)
                    list_of_players.remove(answer)
                    count += 1

        check_if_int_or_float(processed_answer, second_message_length, "ERROR - please use only those names from the list.")

    return order_of_start


def choose_sign(list_with_players_in_order, game_board):
    list_with_sign = ['X', '0']
    players_signs = {}
    count = 0

    while len(players_signs) < 2:
        os.system('clear')
        first_message_length, second_message_length = printing_header('2D Tic-Tac-Toe', 'human vs human')
        printing_tictactoe_board(game_board, second_message_length)
        name_of_player = list_with_players_in_order[0]

        print(f"\n{' ' * (second_message_length // 2 + 8)} * {count + 1}. {name_of_player}, what do you want to play with, {list_with_sign} (q to quit):", end=" ")

        answer = input().upper()

        if check_if_quit(answer, second_message_length, "ERROR - please use only X or 0."):
            continue
        elif answer not in list_with_sign:
            print(f"\n{' ' * second_message_length} ERROR - please use only X or 0.")
            os.system(one_second)
        else:
            count += 1
            list_with_players_in_order.remove(name_of_player)
            players_signs[name_of_player] = answer
            list_with_sign.remove(answer)

    players_values_for_board = {}

    for name, value in players_signs.items():
        if value == 'X':
            players_values_for_board[name] = 1
        else:
            players_values_for_board[name] = 0

    return players_signs, players_values_for_board


def print_board(players_order_signs, game_board, if_starting=0):
    os.system('clear')
    first_message_length, second_message_length = printing_header('2D Tic-Tac-Toe', 'human vs human')
    printing_tictactoe_board(game_board, second_message_length)

    if if_starting == 1:
        print(f"\n{' ' * second_message_length} {'[ 1. ]':>7} {list(players_order_signs.keys())[0]} will move first with {list(players_order_signs.values())[0]}")
        print(f"{' ' * second_message_length} {'[ 2. ]':>7} Then {list(players_order_signs.keys())[1]} with {list(players_order_signs.values())[1]}")

        os.system(one_second)
        print(f"\n{' ' * second_message_length}  < Let's START the game.... >")
        os.system(one_second)


def row_and_column(type_of_select, message_length):
    error = 0
    processed_answer = ''

    if type_of_select == 1:
        print(f"{' ' * message_length} - > Row [1-3]: \033[0m", end="")
    else:
        print(f"{' ' * message_length} - > Column [1-3]: \033[0m", end="")

    answer = input()

    if answer[0] == "q":
        print(f"\n{' ' * message_length} * Exiting.....\n\n", end=" ")
        os.system(one_second)
        exit(1)

    try:
        processed_answer = int(answer)
    except ValueError:
        error = 1

    if error == 1 or processed_answer not in [1, 2, 3]:
        print(f"\n{' ' * message_length} ERROR - please use only integers in the range 1 - 3 for rows and columns.")
        os.system(one_second)
    elif processed_answer in [1, 2, 3]:
        processed_answer = (int(processed_answer) - 1)

    return processed_answer


def start_moving(players_with_values, players_with_signs, game_board, board_for_check, too_choose_from):
    row = column = -1
    error = 1
    player_1, player_2 = tuple(players_with_values.keys())

    if too_choose_from == 0:
        player_to_move = player_1
    else:
        player_to_move = player_2

    while error == 1 or not 0 <= (row and column) <= 2:
        os.system('clear')
        first_message_length, second_message_length = printing_header('2D Tic-Tac-Toe', 'human vs human')
        printing_tictactoe_board(game_board, second_message_length)

        message_to_give = f'[ * {player_to_move} will put an "{players_with_signs[player_to_move]}" (q to quit) ]'

        print(f'\n{" " * second_message_length}{message_to_give}')
        print(f'{" " * second_message_length}{"-" * len(message_to_give)}')

        row = row_and_column(1, second_message_length)
        if isinstance(row, str) or isinstance(row, float) or row not in range(0, 3):
            continue

        column = row_and_column(2, second_message_length)
        if isinstance(column, str) or isinstance(column, float) or column not in range(0, 3):
            continue

        if board_for_check[row][column] != 100:
            print(f"\n{' ' * second_message_length} * ERROR - this move was made already. Please choose another rown and column")
            os.system('sleep 2')
        else:
            error = 0

    return player_to_move, row, column


def check_row_column_winner(players_with_values, board_to_check_winner, to_transpose=1):
    name_of_winner = ''
    winner_element = ''
    players_with_values = {j: i for i, j in players_with_values.items()}

    if to_transpose == 2:
        board_to_check_winner = np.transpose(board_to_check_winner)

    for i in range(len(board_to_check_winner)):
        sum_of_elements = sum(board_to_check_winner[i])

        if sum_of_elements in [0, 3]:
            winner_element = i
            name_of_winner = players_with_values[board_to_check_winner[i][0]]
            break

    return name_of_winner, winner_element


def check_1st_2nd_diag_winner(players_with_values, board_to_check_winner, diag_type):
    name_of_winner = ''
    winner_element = ''
    summing_elements = 0
    players_with_values = {j: i for i, j in players_with_values.items()}

    if diag_type == 1:
        for i in range(len(board_to_check_winner)):
            summing_elements += board_to_check_winner[i][i]
    elif diag_type == 2:
        for j in range((len(board_to_check_winner) - 1), -1, -1):
            summing_elements += board_to_check_winner[((len(board_to_check_winner) - 1) - j)][j]

    if summing_elements in [0, 3]:
        winner_element = diag_type
        name_of_winner = players_with_values[board_to_check_winner[1][1]]

    return name_of_winner, winner_element


def colorize_rows_column(given_board, winner_name, type_of_print, number_of_slice):
    os.system('clear')
    first_message_length, second_message_length = printing_header('2D Tic-Tac-Toe', 'human vs human')

    print()
    for row in range(len(given_board)):
        print(f"{' ' * (second_message_length + (second_message_length // 4) - 2)}", end="")
        for column in range(len(given_board[row])):
            if (type_of_print == 1 and row == number_of_slice) or (type_of_print == 2 and column == number_of_slice):
                print(f"\033[1;32m{given_board[row][column]}\033[0m", end=" ")
            else:
                print(f"{given_board[row][column]}", end=" ")
        print()

    print(f"\n{' ' * second_message_length}\033[1m * {winner_name} you are the winner. Congrats!!\033[0m\n")


def colorize_1st_2nd_diag(given_board, winner_name, number_diag):
    os.system('clear')
    first_message_length, second_message_length = printing_header('2D Tic-Tac-Toe', 'human vs human')

    print()
    if number_diag == 1:
        for row in range(len(given_board)):
            print(f"{' ' * (second_message_length + (second_message_length // 4) - 2)}", end="")
            for column in range(len(given_board[row])):
                if row == column:
                    print(f"\033[1;31m{given_board[row][column]}\033[0m", end=" ")
                else:
                    print(f"{given_board[row][column]}", end=" ")
            print()
    elif number_diag == 2:
        for row in range(len(given_board)):
            print(f"{' ' * (second_message_length + (second_message_length // 4) - 2)}", end="")
            for column in range(len(given_board[row])):
                if ((len(given_board[row]) - 1) - row) == column:
                    print(f"\033[1;31m{given_board[row][column]}\033[0m", end=" ")
                else:
                    print(f"{given_board[row][column]}", end=" ")
            print()

    print(f"\n{' ' * second_message_length}\033[1m * {winner_name} you are the winner. Congrats!!\033[0m\n")


def print_winner(given_board, winner_name, what_to_print, diag, row_column):
    if what_to_print in [0, 1, 2]:
        if row_column == 1:
            colorize_rows_column(given_board, winner_name, 1, what_to_print)
        elif row_column == 2:
            colorize_rows_column(given_board, winner_name, 2, what_to_print)
        elif diag == 1:
            colorize_1st_2nd_diag(given_board, winner_name, what_to_print)

        exit(1)


def check_winner(players_with_values, board_to_use_to_check_winner, game_board):
    winner_name, number_of_row = check_row_column_winner(players_with_values, board_to_use_to_check_winner, to_transpose=1)
    print_winner(game_board, winner_name, number_of_row, 0, 1)

    winner_name, number_of_column = check_row_column_winner(players_with_values, board_to_use_to_check_winner, to_transpose=2)
    print_winner(game_board, winner_name, number_of_column, 0, 2)

    winner_name, first_diag = check_1st_2nd_diag_winner(players_with_values, board_to_use_to_check_winner, diag_type=1)
    print_winner(game_board, winner_name, first_diag, 1, 0)

    winner_name, second_diag = check_1st_2nd_diag_winner(players_with_values, board_to_use_to_check_winner, diag_type=2)
    print_winner(game_board, winner_name, second_diag, 1, 0)


def moving_player(players_with_values, players_with_signs, game_board, board_to_use_to_check_winner, which_player):
    player_to_move, row, column = start_moving(players_with_values, players_with_signs, game_board,
                                               board_to_use_to_check_winner, which_player)
    board_to_print, board_with_values = writing_to_boards(row, column, players_with_values[player_to_move], game_board,
                                                          board_to_use_to_check_winner)

    check_winner(players_with_values, board_to_use_to_check_winner, game_board)

    return board_to_print, board_with_values


def main():
    game_board, board_to_use_to_check_winner = initialize_empty_board(3, 3)
    player_names = names(game_board)
    starting_order = who_will_start_first(player_names, game_board)
    players_with_signs, players_with_values = choose_sign(starting_order, game_board)

    print_board(players_with_signs, game_board, 1)

    while True:
        game_board, board_to_use_to_check_winner = moving_player(players_with_values, players_with_signs,
                                                                 game_board, board_to_use_to_check_winner, 0)
        game_board, board_to_use_to_check_winner = moving_player(players_with_values, players_with_signs,
                                                                 game_board, board_to_use_to_check_winner, 1)


if __name__ == '__main__':
    main()
