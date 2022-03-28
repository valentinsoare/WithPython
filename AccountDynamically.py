#!/usr/bin/python

import dataclasses


def printing(obj_name):
    print(f'Account number: {obj_name.account}\nAccount name: {obj_name.name}\nAccount balance: {obj_name.balance}\n')


def main():
    account = dataclasses.make_dataclass('Account', ['account', 'name', 'balance'])      #### datatype which is a dataclass of type Account
    valentin_account = account('RO30 BCR 7823941234', 'Valentin', '8923$')                        #### creating the object from data type account

    count = 1
    print(f'\n{"-" * 32}')

    for i, j in dataclasses.asdict(valentin_account).items():
        print(f'{count}. {i.title()}: {j}')
        print(f'{"-" * 32}')
        count += 1


if __name__ == "__main__":
    main()
