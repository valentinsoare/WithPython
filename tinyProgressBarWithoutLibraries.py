#!/usr/bin/python

def main():
    import os
    import time

    os.system('tput civis')

    for i in range(21):
        os.system('clear')
        print(f"\033[1m PROGRESS BAR:\033[0m", end=" ")
        print(f'\033[1m[{"#" * i:<20}] {i * 10/2}%\033[0m', end=" ")
        time.sleep(0.5)
        print(f"\033[1m COMPLETED!!!\033[0m")

    os.system('tput cnorm')


main()

