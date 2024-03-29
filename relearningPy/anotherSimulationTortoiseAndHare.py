#!/usr/bin/python

import os
import random


def header(message_for_print):
    processed_message = ''
    for i in message_for_print:
        processed_message += '-' + i

    processed_message += '-'
    length_of_processed_message = len(processed_message)

    print(f"\n{' ' * 16}{processed_message}")
    print(f"{' ' * 16}{'=' * length_of_processed_message}")


def print_message_before_the_race():
    os.system('tput civis')
    os.system('clear')
    header('TORTOISE vs HARE')

    print(f"\n{' ' * 9} The Race will begin in a few moments...")
    print(f"\n{' ' * 6} START |", end="")
    print(f"{'-' * 70}", end="")
    print(f"| FINISH\n")
    os.system('sleep 2')
    print(f"{' ' * 9}BANG!!!!\n{' ' * 9}AND THEY ARE OFF!!!")
    os.system('sleep 1')


def generate_random_number_for_moving(start, finish):
    generated_number = random.randrange(start, finish, 1)
    return generated_number


def determine_how_to_move_tortoise(value_from_randomizer):
    value_for_tortoise_to_move = 0

    if 1 <= value_from_randomizer <= 5:
        value_for_tortoise_to_move += 3
    elif 6 <= value_from_randomizer <= 7:
        value_for_tortoise_to_move -= 6
    else:
        value_for_tortoise_to_move += 1

    return value_for_tortoise_to_move


def determine_how_to_move_hare(randomizer_value):
    value_for_hare_to_move = 0
    hare_sleeps = 0

    if 1 <= randomizer_value <= 2:
        value_for_hare_to_move += 0
        hare_sleeps = 1
    elif 3 <= randomizer_value <= 4:
        value_for_hare_to_move += 9
    elif randomizer_value == 5:
        value_for_hare_to_move -= 12
    elif 6 <= randomizer_value <= 8:
        value_for_hare_to_move += 1
    else:
        value_for_hare_to_move -= 2

    return value_for_hare_to_move, hare_sleeps


def determine_winner(position_hare, position_tortoise, length_line):
    message = 1

    if position_hare >= length_line:
        message = f"Hare Wins!!"
    elif position_tortoise >= length_line:
        message = f"Tortoise Wins!!"
    elif position_hare <= length_line <= position_tortoise:
        message = f"We have a tie!!"

    if isinstance(message, str):
        print(f"\n{' ' * 9}{message}\n")
        os.system('tput cnorm')
        exit(0)


def print_line(hare_position, tortoise_position, length_line, if_hare_sleeps):
    print(f"\n{' ' * 6}START |", end="")

    for i in range(length_line):
        if i == hare_position and if_hare_sleeps == 1:
            print(f"HS", end="")
        elif hare_position == tortoise_position == i:
            print(f"OUCH!!", end="")
        elif hare_position == i:
            print(f"H", end="")
        elif tortoise_position == i:
            print(f"T", end="")
        else:
            print(f"-", end="")

    print(f"| FINISH")


def main():
    length_of_race = 70
    h_position = 0
    t_position = 0

    print_message_before_the_race()

    while True:
        os.system('clear')
        header('TORTOISE vs HARE')
        random_position = generate_random_number_for_moving(1, 11)

        value_to_move_h, if_hare_sleeps = determine_how_to_move_hare(random_position)
        h_position += value_to_move_h

        if h_position < 1:
            h_position = 1

        value_to_move_t = determine_how_to_move_tortoise(random_position)
        t_position += value_to_move_t

        if t_position < 1:
            t_position = 1

        print_line(h_position, t_position, length_of_race, if_hare_sleeps)
        determine_winner(h_position, t_position, length_of_race)

        os.system('sleep 1')


if __name__ == '__main__':
    main()
