#!/usr/bin/python

import dataclasses


def printing(obj_name):
    print(f'Account number: {obj_name.account}\nAccount name: {obj_name.name}\nAccount balance: {obj_name.balance}\n')


def main():
    account = dataclasses.make_dataclass('Account', ['account', 'name', 'balance'])      #### datatype which is a dataclass of type Account
    valentin_account = account('7823423523', 'Valentin', '8923$')                        #### creating the object from data type account

    printing(valentin_account)


if __name__ == "__main__":
    main()