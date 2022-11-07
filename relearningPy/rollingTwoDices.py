#!/usr/bin/python

import math
import statistics
import numpy as np


def header(given_message):
    prepare_the_message = '# '
    prepare_the_message += ' # '.join(given_message.split())
    prepare_the_message += ' #'

    length_of_message = len(prepare_the_message)
    lines = f"{'-' * (length_of_message * 2)}"

    print(f"\n{' ' * 10}{lines}")
    print(f"{' ' * 10}|{' ' * (length_of_message // 2 - 2)}{prepare_the_message}{' ' * (length_of_message // 2)}|")
    print(f"{' ' * 10}{lines}")


def roll_thee_dice_and_calc_sum(size_of_number_of_rolls):
    dice_1 = np.random.randint(1, 7, size_of_number_of_rolls)
    dice_2 = np.random.randint(1, 7, size_of_number_of_rolls)
    return list(sum(i) for i in zip(dice_1, dice_2))


def print_the_body(values, count, number_of_rolls):
    print(f"\n{'Die Value':>19}\n{'Sum of Two Dices':>22}{'Frequency':>15}{'Percent':>12}{'Barchart':>13}")

    for i in range(len(values)):
        print(
            f"{' ' * 10}{values[i]:>12}{count[i]:>15}{' ' * 5}{((count[i] / number_of_rolls) * 100):>6.2f}%{' ' * 5}{'#' * int((count[i] / number_of_rolls) * 100)}")


def calc_stats_on_dices(values, count):

    index_max, = np.where(count == max(count))
    index_min, = np.where(count == min(count))

    print(f"\n{' ' * 4}{' - > Stats on roll of two dices:'}")
    print(f"{' ' * 4}{'0.'} {'Minimum of the appearances, sum from two dices: '}{min(count)}, {values[index_min][0]}")
    print(f"{' ' * 4}{'1.'} {'Maximum of the appearances, sum from two dices: '}{max(count)}, {values[index_max][0]}")
    print(f"{' ' * 4}{'2. '}{'Mean of the appearances of sum: '}{statistics.mean(count)}")
    print(f"{' ' * 4}{'3. '}{'Variance of appearances of sum: '}{statistics.variance(count)}")
    print(f"{' ' * 4}{'4. '}{'Standard deviation of appearances of sum: '}{math.sqrt(statistics.variance(count)):.1f}")


def main():
    number_of_rolls = 3_600

    header('Rolling Two Dice')
    list_with_sum = roll_thee_dice_and_calc_sum(number_of_rolls)
    values, count = np.unique(list_with_sum, return_counts=True)

    print_the_body(values, count, number_of_rolls)
    calc_stats_on_dices(values, count)


if __name__ == '__main__':
    main()
