#!/usr/bin/python3

import random
import time
import os


def tortoise():
    given_rnd_number = random.randrange(1, 10)
    if 1 <= given_rnd_number <= 5:
        return 3
    elif 6 <= given_rnd_number <= 7:
        return -6
    elif 8 <= given_rnd_number <= 10:
        return 1


def hare():
    rnd_number = random.randrange(1, 10)
    if 1 <= rnd_number <= 2:
        return 0  # hare sleeps
    elif 3 <= rnd_number <= 4:
        return 9
    elif rnd_number == 5:
        return -12
    elif 6 <= rnd_number <= 8:
        return 1
    elif 9 <= rnd_number <= 10:
        return -2


def print_run(playerH, playerT, return_value_H):
    print(f'START', end='')

    for i in range(0, 70):
        if i == playerH == playerT:
            print(f'OUCH!!', end='')
        elif i == playerH and return_value_H == 0:
            print(f'HS', end='')  # hare sleeps
        elif i == playerT:
            print('T', end='')
        elif i == playerH:
            print('H', end='')
        print(f'-', end='')

    print(f'FINISH', end='')


def main():
    playerH = 1
    playerT = 1

    while playerH < 70 and playerT < 70:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

        print(f'**Tortoise and The Hare Racing to Victory', end='\n\n')
        print(f'\tBANG !!! AND THEY`RE OFF !!!! ', end='\n\n')

        playerT = tortoise() + playerT
        if playerT < 1:
            playerT = 1

        return_value_H = hare()
        playerH = return_value_H + playerH
        if playerH < 1:
            playerH = 1

        print_run(playerH, playerT, return_value_H)

        if playerT >= 70:
            print(f'  TORTOISE WINS!!!')
        elif playerH >= 70:
            print(f'  Hare wins. Yuck!!!')
        elif playerT >= 70 and playerH >= 70:
            print(f"  It's a tie")

        print()
        time.sleep(1)


main()

