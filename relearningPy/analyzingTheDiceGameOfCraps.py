#!/usr/bin/python

import os
import statistics
import numpy as np

list_with_wins = []
list_with_losses = []


def create_header(given_message):
    message_processed = ' ### '
    message_processed += ' '.join(given_message)
    message_processed += ' ### '
    length_of_message = len(message_processed)

    print(f"\n{' ' * int(length_of_message * 0.5)}{message_processed}")
    print(f"{' ' * int(length_of_message * 0.25)}{'-' * int(length_of_message * 1.5)}")


def generate_two_dice_values():
    dice_1 = np.random.randint(1, 7)
    dice_2 = np.random.randint(1, 7)
    return dice_1, dice_2


def check_the_dice(dice1, dice2, number_of_roll, point):
    value_to_return = ''
    sum_of_dices = sum((dice1, dice2))

    if number_of_roll != 0:
        if sum_of_dices == point:
            list_with_wins.append(number_of_roll)
            value_to_return = 'w'
        elif sum_of_dices == 7:
            list_with_losses.append(number_of_roll)
            value_to_return = 'l'
        else:
            value_to_return = -3
    else:
        if sum_of_dices in [7, 11]:
            list_with_wins.append(1)
            value_to_return = 'w'
        elif sum_of_dices in [2, 3, 12]:
            list_with_losses.append(1)
            value_to_return = 'l'
        elif 8 <= sum_of_dices <= 10 or 4 <= sum_of_dices <= 6:
            value_to_return = sum_of_dices

    return value_to_return


def printing_stats_table(*args):
    on_number_of_rolls_win, number_of_games_won, on_number_of_rolls_lost, number_of_games_lost, number_of_games, wins, losses = args
    print(f"\n{' ' * 16}{'Rolls':<10}{'Games Won':<15}{'Percent From Games Won'}{'BarChart':>13}")

    for i in range(len(on_number_of_rolls_win)):
        values_to_use_for_percent = percent = (number_of_games_won[i]/sum(number_of_games_won)) * 100
        if percent < 1:
            percent = 1
        print(f"{' ' * 16}{on_number_of_rolls_win[i]:>5}{number_of_games_won[i]:>14}{values_to_use_for_percent:>27.2f}%{' ' * 5}{'#' * int(percent)}")

    print(f"\n{' ' * 16}{'Rolls':<10}{'Games Lost':<15}{'Percent From Games Lost'}{'BarChart':>13}")

    for i in range(len(on_number_of_rolls_lost)):
        values_to_use_for_percent = percent = (number_of_games_lost[i]/sum(number_of_games_lost)) * 100
        if percent < 1:
            percent = 1
        print(f"{' ' * 16}{on_number_of_rolls_lost[i]:>5}{number_of_games_lost[i]:>14}{values_to_use_for_percent:>28.2f}%{' ' * 5}{'#' * int(percent)}")


def printing_stats_wins_and_losses(*args):
    on_number_of_rolls_win, number_of_games_won, on_number_of_rolls_lost, number_of_games_lost, number_of_games, wins, losses = args

    percent_won = ((wins/number_of_games) * 100)
    percent_lost = ((losses/number_of_games) * 100)

    print(f"\n{' ' * 16}{'Count':<10}{'Percent':<12}{'Barchart'}")
    print(f"{' ' * 8}{'Wins':<9}{wins}{percent_won:>11.2f}%{' ' * 5}{'#' * int(percent_won)}")
    print(f"{' ' * 8}{'Losses':<9}{losses}{percent_lost:>11.2f}%{' ' * 5}{'#' * int(percent_lost)}")

    print(f"\n{' ' * 7} * Mean for the length of a game of craps with win rolls: {statistics.mean(on_number_of_rolls_win)}")
    print(f"{' ' * 7} * Mean for the length of a game of craps with lost rolls: {statistics.mean(on_number_of_rolls_lost)}")
    print(f"{' ' * 7} * The Mode for Win Rolls: {statistics.mode(on_number_of_rolls_win)}")
    print(f"{' ' * 7} * The Mode for Lost Rolls: {statistics.mode(on_number_of_rolls_lost)}")
    print(f"{' ' * 7} * The Median for Win Rolls: {statistics.median(on_number_of_rolls_win)}")
    print(f"{' ' * 7} * The Median for Lost Rolls: {statistics.median(on_number_of_rolls_lost)}")


def main():
    wins = 0
    losses = 0
    counting = 0
    my_point = ''
    number_games = 36

    os.system('clear')
    create_header('Analysing The Game of Craps')

    while counting < number_games:
        counter_rolls = 0
        while True:
            d_1, d_2 = generate_two_dice_values()
            output_after_checking = check_the_dice(d_1, d_2, counter_rolls, my_point)

            if output_after_checking == 'w':
                wins += 1
                break
            elif output_after_checking == 'l':
                losses += 1
                break
            if isinstance(output_after_checking, int) and output_after_checking > 0:
                my_point = output_after_checking

            counter_rolls += 1

        counting += 1

    on_number_of_rolls_win, number_of_games_won = np.unique(list_with_wins, return_counts=True)
    on_number_of_rolls_lost, number_of_games_lost = np.unique(list_with_losses, return_counts=True)

    printing_stats_table(on_number_of_rolls_win, number_of_games_won, on_number_of_rolls_lost, number_of_games_lost, number_games, wins, losses)
    printing_stats_wins_and_losses(on_number_of_rolls_win, number_of_games_won, on_number_of_rolls_lost, number_of_games_lost, number_games, wins, losses)


if __name__ == '__main__':
    main()
