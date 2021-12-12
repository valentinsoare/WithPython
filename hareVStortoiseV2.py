#!/usr/bin/python3

import random
import sys
import os


def moving_tortoise():
    rnd_number_tortoise = random.randrange(1, 11)

    if 1 <= rnd_number_tortoise <= 5:
        number_to_return = 3
    elif 6 <= rnd_number_tortoise <= 7:
        number_to_return = -6
    else:
        number_to_return = 1

    return number_to_return


def moving_hare():
    rnd_number_hare = random.randrange(1, 11)

    if 1 <= rnd_number_hare <= 2:
        return_for_hare = 0
    elif 3 <= rnd_number_hare <= 4:
        return_for_hare = 9
    elif rnd_number_hare == 5:
        return_for_hare = -12
    elif 6 <= rnd_number_hare <= 8:
        return_for_hare = 1
    else:
        return_for_hare = -2

    return return_for_hare


def print_initial_track():
    x = 1
    os.system('clear')
    os.system('tput civis')
    print(f"\n***The Tortoise and the Hare***", end="\n\n")
    print(f" - > The following track is given: ", end="\n\n")
    print(f"START: T H |", end="")

    while x <= 70:
        print(f"-", end="")
        x += 1

    print(f"| FINISH", end="\n")


def print_running(playerH, playerT, sleep_hare=0):
    os.system('clear')
    print(f"\n***The Tortoise and the Hare***", end="\n")
    print(f"\n\tBANG !!!\n\tAND THEY'RE OFF !!!!", end="\n")
    print(f"\nSTART: |", end="")

    for i in range(1, 71):
        if i == playerT == playerH:
            print(f"T OUCH!!", end="")
        elif i == playerT:
            print(f"T", end="")
        elif i == playerH:
            print(f"H", end="")
        elif i == playerH and sleep_hare == 1:
            print(f"HareSleep", end="")
        else:
            print(f"-", end="")

    print(f"| FINISH", end="\n")


def winner_determination(playerH, playerT):

    if playerT >= 70:
        print(f"\n\t TORTOISE WINS!!! YAY!!!**", end="\n\n")
    elif playerH >= 70:
        print(f"\n\t Hare wins!!", end="\n\n")
    elif playerT >= 70 and playerH >= 70:
        print(f"\n\t It's a tie!!", end="\n\n")

    os.system('tput cnorm')
    sys.exit(0)


def main():
    playerH = 1
    playerT = 1
    hare_sleep = 0

    print_initial_track()
    os.system('sleep 1.25')


    while playerH <= 70 and playerT <= 70:
        hare_var = moving_hare()
        if hare_var != 0:
            playerH += hare_var
        else:
            hare_sleep = 1

        if playerH < 1:
            playerH = 1

        playerT += moving_tortoise()
        if playerT < 1:
            playerT = 1

        os.system('sleep 1')

        if hare_sleep == 1:
            print_running(playerH, playerT, hare_sleep)
        else:
            print_running(playerH, playerT)

    winner_determination(playerH, playerT)


main()
