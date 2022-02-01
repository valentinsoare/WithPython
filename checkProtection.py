#!/usr/bin/python

def catch_input():
    print(f"\n\033[1m - > Please enter the name of the person the check is designated for: ", end="\033[0m")
    name_of_the_person = input()

    print(f"\033[1m - > Enter the check amount in dollars: ", end="\033[0m")
    check_amount = input()

    try:
        check_amount = int(check_amount)
    except ValueError:
        check_amount = float(check_amount)

    return name_of_the_person, check_amount


def printing_header(given_name, given_amount):
    print(f'\n\t\t\033[1mPAY TO\t\033[0m\033[1;33m{given_name.capitalize():>10}\033[0m\033[1m{"$ ":>15}'
          f'{given_amount:*>10}\n', end=" ")


def main():
    name, amount = catch_input()
    printing_header(name, amount)


main()

