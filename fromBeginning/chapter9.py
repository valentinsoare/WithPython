#!/usr/bin/python

import os
import csv
import json
import typing
import pandas as pd
from pprint import pprint
from bs4 import BeautifulSoup
from timeit import timeit



def to_write_to_file():
    with open('accounts.txt', mode='w') as accounts:
        accounts.write('200 Doe 245.67\n')
        accounts.write('100 Jones 24.98\n')
        accounts.write('300 White 0.00\n')
        accounts.write('400 Stone -42.14')


def to_read_from_file():
    with open('accounts.txt', mode='r') as accounts:
        open_file = accounts.read().splitlines()

    print(open_file)


def writing_grades_and_read():
    with open('grades.txt', mode='w') as grades:
        for i in ['1 Red A', '2 Green B', '3 White A']:
            grades.write(f"{i}\n")

    with open('grades.txt', mode='r', encoding='utf-8') as reading_grades:
        given_grades = reading_grades.read().splitlines()

    print(given_grades)


def updating_file():
    accounts = open('accounts.txt', mode='r')
    temp_file = open('temp_file.txt', mode='w')

    with accounts, temp_file:
        for i in accounts:
            account, name, balance = i.split()
            if account != '300':
                temp_file.write(i)
            else:
                temp_file.write(f"{account} {'Williams'} {balance}\n")

    os.remove('accounts.txt')
    os.rename('temp_file.txt', 'accounts.txt')


def serialization_object_to_json():
    accounts_dict = {'accounts': [{'account': 1728476, 'name': 'Valentin', 'balance': 24.98},
                                  {'account': 187111952, 'name': 'Aurelia', 'balance': 199.82},
                                  {'account': 283749274, 'name': 'Andrei', 'balance': 1000}]}
    #------writing
    with open('accounts.json', mode='w') as accounts:
        json.dump(accounts_dict, accounts, indent=4)

    #read_file_as_dict: dict = {}
    read_file_as_string: str = ''

    #-----reading
    with open('accounts.json', mode='r') as accounts:
        read_file_as_string = json.dumps(json.load(accounts), indent=4)
    print(read_file_as_string)
    accounts.close()


def optimized_json_reader():
    with open('accounts.json', mode='r', encoding='utf-8') as accounts:
        loaded_dict = json.load(accounts)
    accounts.close()

    loaded_dict['accounts'].append({'account': 9090, 'name': 'Andreea', 'balance': 100000})

    with open('accounts.json', mode='w', encoding='utf-8') as accounts:
        json.dump(loaded_dict, accounts, indent=4)
    accounts.close()


def ask_for_number() -> None:
    result: typing.Union[int | float | str] = -1

    while result == -1:
        try:
            print(f"{'Please enter nominator:'}", end=" ", flush=True)
            first_number = float(input())

            print(f"{'Please enter denominator:'}", end=" ", flush=True)
            second_number = float(input())

            result = first_number / second_number
        except ValueError:
            print(f"\n{'ERROR - please use only integers or floats.'}")
        except ZeroDivisionError:
            print(f"\n{'ERROR - attempted to divide by zero.'}")
        else:
            first_number = f"{first_number:.1f}".rstrip('.0')
            second_number = f"{second_number:.1f}".rstrip('.0')
            result = f"{result:.1f}".rstrip('.0')
            print(f"\n{first_number} / {second_number} = {result}")
        finally:
            print(f"If there is no error and we have valid nominator and denominator,"
                  f" script will end, if not, the loop will continue...\n")


def open_a_file_using_with_and_try():
    loaded_dict_from_json: dict = {}
    try:
        with open(file='accounts.json', mode='r', encoding='utf-8') as accounts:
            loaded_dict_from_json = json.load(accounts)
    except FileNotFoundError:
        print(f"{'File does not exists!'}", flush=True)
    else:
        print(f"{'JSON loaded:'}\n", flush=True)
        print(f"{json.dumps(loaded_dict_from_json, indent=4)}", flush=True)


def writing_to_a_csv():
    with open(file='bank_accounts.csv', mode='w', newline='') as bank_accounts:
        to_write = csv.writer(bank_accounts)
        #to_write.writerow([100, 'Jones', 24.98])
        #to_write.writerow([200, 'Doe', 345.67])
        #to_write.writerow([300, 'White', 0.00])
        #to_write.writerow([400, 'Stone', -42.16])
        to_write.writerows([[100, 'Jones', 24.98], [200, 'Doe', 345.67],
                            [300, 'White', 0.00], [400, 'Stone', -42.16]])


def reading_from_a_csv():
    with open('bank_accounts.csv', mode='r', newline='') as bank_accounts:
        csv_reader = csv.reader(bank_accounts)
        content_from_csv = list(i for i in csv_reader)

    print(content_from_csv)

    #----alternate method to read from a csv with pandas
    reading_csv_file = pd.read_csv('bank_accounts.csv', encoding='utf-8', names=['Account', 'Name', 'Balance'])
    print(reading_csv_file)


def cool_way_reading_from_csv():
    reading_csv: pd.DataFrame = pd.read_csv('bank_accounts.csv', encoding='utf-8', names=['Account', 'Name', 'Balance'])
    reading_csv.to_csv('accounts_from_dataframe.csv', index=False)


def load_from_url_titanic_survival():
    titanic = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv')
    pd.set_option('display.precision', 2)
    titanic.columns = ['Name', 'Survived', 'Sex', 'Age', 'Class']

    #print(titanic)

    print((titanic.loc[:, 'Survived'] == 'yes').describe())
    



def main() -> None:
    #to_write_to_file()
    #to_read_from_file()
    #writing_grades_and_read()
    #updating_file()

    #serialization_object_to_json()

    #optimized_json_reader()
    #ask_for_number()

    #open_a_file_using_with_and_try()

    #writing_to_a_csv()

    #setup_code = '''from chapter9 import writing_to_a_csv'''
    #test_code = '''csv_content = writing_to_a_csv()'''
    #timing = timeit(setup=setup_code, stmt=test_code, number=2)
    #print(timing)

    #reading_from_a_csv()

    #cool_way_reading_from_csv()
    load_from_url_titanic_survival()

if __name__ == '__main__':
    main()
