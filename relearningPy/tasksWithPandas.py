#!/usr/bin/python

import re
import copy
import numpy as np
import pandas as pd


def colorize_rows_column(given_board, type_of_print, number_of_slice):             # column
    for row in range(len(given_board)):
        for column in range(len(given_board[row])):
            if (type_of_print == 0 and row == number_of_slice) or (type_of_print == 1 and column == number_of_slice):
                print(f"\033[1;32m{given_board[row][column]}\033[0m", end=" ")
            else:
                print(f"{given_board[row][column]}", end=" ")
        print()


def colorize_1st_2nd_diag(given_board, number_diag):
    if number_diag == 1:
        for row in range(len(given_board)):
            for column in range(len(given_board[row])):
                if row == column:
                    print(f"\033[1;31m{given_board[row][column]}\033[0m", end=" ")
                else:
                    print(f"{given_board[row][column]}", end=" ")
            print()
    elif number_diag == 2:
        for row in range(len(given_board)):
            for column in range(len(given_board[row])):
                if ((len(given_board[row]) - 1) - row) == column:
                    print(f"\033[1;31m{given_board[row][column]}\033[0m", end=" ")
                else:
                    print(f"{given_board[row][column]}", end=" ")
            print()


def shallow_vs_deep_copy():
    dictionary = {'Sophia': [97, 88]}
    a_copy_of_dict_shallow = dictionary.copy()  # shallow copy
    a_deepcopy_of_dict = copy.deepcopy(dictionary)

    dictionary['Sophia'].extend([101, 42, 23])

    print(a_copy_of_dict_shallow)
    print(a_deepcopy_of_dict)


def simple_tasks_with_pandas_series():
    given_series = pd.Series([7, 11, 13, 17])
    print(given_series)

    five_elements = pd.Series(np.array(np.full(5, 100.0)), name="five_elements")
    print(five_elements)

    temperatures = pd.Series([98.6, 98.9, 100.2, 97.9], index=['Julie', 'Charlie', 'Sam', 'Andrea'], name="Temperatures")
    print(f"{temperatures}")

    given_dict_with_temperatures = {'Julie': 98.6, 'Charlie': 98.9, 'Sam': 100.2, 'Andrea': 97.9}
    temperatures = pd.Series(given_dict_with_temperatures.values(), index=given_dict_with_temperatures.keys(), name="Temperatures")
    print(temperatures)


def tasks_with_pandas_frame():
    given_dict_with_temps = {'Maxine': 97.9, 'James': 100.4, 'Amanda': 99.5}

    temperatures = pd.DataFrame(given_dict_with_temps.values(), index=list(given_dict_with_temps.keys()), columns=['temperatures'])
    print(temperatures)

    temperatures_period_of_day = pd.DataFrame(given_dict_with_temps.values(), index=['Morning', 'Afterrnoon', 'Evening'], columns=['temperatures'])
    print(temperatures_period_of_day)

    print(f"\nTemp for Maxine: {temperatures.loc['Maxine']}")
    print(f"{temperatures_period_of_day.loc['Morning']}")
    print(f"{temperatures_period_of_day.loc[['Morning', 'Evening'], :]}")
    print(temperatures.loc[['Amanda', 'Maxine'], :])
    print(f"{temperatures.describe()}")
    print(temperatures.transpose())
    print(f"{temperatures.sort_index()}")


def various_tasks_pandas():
    #zips = pd.Series({'Boston': '02215', 'Miami': '3310'})
    #values_matched = zips.str.match(r'\d{5}')
    #print(values_matched)

    #----------
    #cities = pd.Series(['Boston MA 02215', 'Miami, FL 33101'])
    #ay = cities.str.contains(r'\s[A-Z]{2}\s')
    #print(ay)

    #------------
    contacts = [['Mike Green', 'demo1@gmail.com', '0722776491'],
                ['Sue Brown', 'demo2@gmail.com', '0722853840']]

    make_df_contacts = pd.DataFrame(contacts, columns=['Name', 'Email', 'Phone'])

    def format_phone_number(given_value):
        our_result = re.fullmatch(r'(\d{4})(\d{3})(\d{3})', given_value)

        if our_result:
            value_to_return = '-'.join(our_result.groups())
        else:
            value_to_return = given_value

        return value_to_return

    #for i in make_df_contacts.values:
    #    i[2] = format_phone_number(i[2])
    #print(make_df_contacts)

    formatted_phone = make_df_contacts['Phone'].map(format_phone_number)
    make_df_contacts['Phone'] = formatted_phone

    print(make_df_contacts)


def main():
    #numpy_array = np.array(np.random.randint(1, 9, 9).reshape(3, 3))
    #print(f"{numpy_array}\n\n")
    #colorize_rows_column(numpy_array, 1, 1)
    #colorize_1st_2nd_diag(numpy_array, 2)
    #shallow_vs_deep_copy()
    #simple_tasks_with_pandas_series()
    #tasks_with_pandas_frame()
    #various_tasks_pandas()


if __name__ == '__main__':
    main()
