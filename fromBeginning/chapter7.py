#!/usr/bin/python
import copy

import numpy as np
import pandas as pd


def exercises_1():
    numbers = np.array([4, 10, 2, 12, 200])
    print(numbers)

    print(type(numbers))

    numbers_2 = np.array([[2, 4, 10], [4, 200, 1]])
    print(numbers_2)

    one_d_array = np.array(range(2, 21, 2))
    print(one_d_array)

    two_d_array = np.array([range(2, 11, 2), [i for i in range(1, 10) if i % 2 != 0]])
    print(two_d_array)
    print(two_d_array.dtype)
    print(numbers.ndim)
    print(two_d_array.shape)
    print(one_d_array.shape)

    print(numbers.size)
    print(numbers.itemsize)

    print(two_d_array.size)
    print(two_d_array.shape)

    print()
    for row in two_d_array:
        for column in row:
            print(f"{column:>3}", end=" ")
        print()

    print(two_d_array)

    for i in sorted(two_d_array.flat):
        print(f"{i}", end=" ")


def exercises_2():
    one_d_array = np.array(range(2, 21, 2))
    two_d_array = np.array([range(2, 11, 2), [i for i in range(1, 10) if i % 2 != 0]])

    print(f"{one_d_array.ndim}")
    print(f"{one_d_array.shape}")
    print(f"{one_d_array.size}")
    print()
    print(f"{two_d_array.ndim}")
    print(f"{two_d_array.shape}")
    print(f"{two_d_array.size}")

    #---------------------

    ax = np.zeros(5, dtype=str)
    ay = np.zeros(5, dtype=int)
    print(ay)

    az = np.ones((2, 4), dtype=int)
    print(az)

    at = np.full((3, 4), 'X')
    print(at)

    #------------------------------

    random_2d_array = np.random.randint(1, 21, 10).reshape((2, 5))
    print(random_2d_array)

    print(f"\n{np.arange(5)}\n")

    az = np.linspace(0, 1, num=5)
    print(az)

    #-----------------------------

    array_to_print = np.arange(2, 41, 2).reshape((4, 5))
    print(array_to_print)

    #-----------------------------
    new = np.empty((2, 3), dtype=int)
    new[0][0] = 124
    new[0][1] = 125
    new[1][2] = 44

    print(new)

    #-------------------------------

    numbers_1 = np.random.randint(1, 6, 5)
    numbers_2 = np.random.randint(1, 6, 5)
    print((numbers_1 + 100))
    print()
    print(numbers_1)
    print(numbers_2)
    print()
    print((numbers_1 + numbers_2))

    print(numbers_1[ax])

    az = numbers_1 < numbers_2
    print(numbers_1[az])
    print(numbers_2[az])

    given_array = np.random.randint(1, 6, 5)
    given_array_squared = given_array ** 2

    print(given_array)
    print(given_array_squared)

    #-----------------------------------------------

    given_array = np.array(np.random.randint(1, 101, 12).reshape((4, 3)))
    print(given_array)

    ax = sum(given_array)
    print(f"\nSum: {ax}")

    ay = given_array.min()
    print(ay)

    az = given_array.max()
    print(az)

    print(f"\n{given_array.mean()} - > {given_array.std()} - > {given_array.var()}")

    print(f"\nAverage per exam/column: {given_array.mean(axis=0)}")
    print(f"\nAverage per student: {given_array.mean(axis=1)}")

    #------------------------------------------------------------------

    grades_from_exams = np.array(np.random.randint(60, 101, 12).reshape((3, 4)))
    print(f"\n* Grades from the exams:")

    def calc_average(given_array, type_of_axis):
        for k in given_array.mean(axis=type_of_axis):
            print(f"{k:.2f}", end=" ")

    for i in range(len(grades_from_exams)):
        print(f"{' ' * 1}", end="")
        for j in range(len(grades_from_exams[i])):
            print(f"{grades_from_exams[i][j]:>3}", end=" ")
        print()

    print(f"\n - > Average per each exam:", end=" ")
    calc_average(grades_from_exams, type_of_axis=0)

    print(f"\n - > Average per student:", end=" ")
    calc_average(grades_from_exams, type_of_axis=1)

    #------------------------------------------------------------

    numbers = np.arange(1, 11)
    print(numbers)

    sqrt_numbers = np.sqrt(numbers)
    print(sqrt_numbers)

    az = np.add(numbers, sqrt_numbers)
    print(az)

    print(np.multiply(numbers, 2))

    numbers_2 = np.array(numbers.reshape((2, 5)))
    print(numbers_2)

    numbers_3 = np.full(5, 2, dtype=int)
    az = np.multiply(numbers_2, numbers_3)

    print(az)

    #---------------------------------
    given_arr = np.arange(1, 6)
    result_power = np.power(given_arr, 3)

    print(result_power)

    #---------------------------------

    grades = np.array(np.random.randint(40, 101, 12).reshape((4, 3)))

    print(f"\n{grades}\n")

    first_two_rows = grades[0:2]
    print(first_two_rows)

    last_two_columns = grades[:, 1:3]
    print(last_two_columns)

    first_two_columns_on_last_two_rows = grades[2:4, 0:2]
    print(f"{first_two_columns_on_last_two_rows}")

    first_row_third_row = grades[[0, 2]]
    print(first_row_third_row)

    #---------------------------------------------

    given_array = np.arange(1, 16).reshape((3, 5))
    print(f"\n{given_array}")

    second_row = given_array[1]
    print(f"\n{second_row}")

    first_third_row = given_array[[0, 2]]
    print(f"\n{first_third_row}")

    three_columns = given_array[:, 1:4]
    print(three_columns)

    #--------------------------------

    numbers = np.arange(1, 6)
    numbers2 = numbers.view()

    print(f"{numbers}\n{numbers2}")

    numbers[2] = 100
    print(f"{numbers}\n{numbers2}")

    #-------------------------------

    numbers2 = numbers[0:3]
    #print(f"{numbers}\n{numbers2}")

    numbers2[1] = 1000
    print(numbers)

    #-------------------------------

    numbers = np.arange(1, 6)

    numbers2 = numbers.copy()

    #-------------------------------

    grades = np.array([[87, 96, 70], [100, 87, 90]])
    print(grades)

    grades.resize(1, 6)
    print(grades)

    ay = grades.ravel()
    ax = grades.flatten()
    print(ay)

    print(grades.transpose())

    grades2 = np.array([[94, 77, 90], [100, 81, 82]])

    stacking_h = np.hstack((grades, grades2))
    print(stacking_h)

    stacking_v = np.vstack((grades2, grades))
    print(f"\n{stacking_v}")

    #------------------------------------------------

    given_arr = np.arange(1, 7).reshape((2, 3))

    stacking = np.hstack((given_arr, given_arr))
    stacking2 = np.vstack((stacking, stacking))

    print(stacking2)

    #-----------------------------------------


def exercises_3():
    grades = pd.Series([87, 100, 94], index=['Maria', 'Vali', 'Andrei'])
    print(grades['Maria'])

    numbers = pd.Series(np.random.randint(50, 100, 3), range(1, 4))
    print(numbers)

    print(grades['Vali':'Andrei'])

    print(grades.count())
    print(grades.mean())
    print(min(grades))

    print(grades.describe())

    #--------------------------------------

    grades = pd.Series([87, 100, 94], index=['Maria', 'Valentin', 'Violeta'])
    print(grades)

    given_dict_grades = {'Andrei': 89, 'Andreea': 90, 'Rares': 87, 'Ionut': 96}

    to_series = pd.Series(given_dict_grades)

    for i in to_series.index:
        print(to_series[i])

    extract_values = to_series.values
    print(extract_values)

    extract_index = to_series.index
    print(extract_index)

    #----------------------------------------------------------

    hardware = pd.Series(['hammer', 'saw', 'wrench'])

    ax = hardware.str.contains('a')
    print(ax)

    ay = hardware.str.capitalize()
    print(ay)

    #-----------------------------------------------
    temperatures = np.random.randint(60, 100, 5)

    print(f"\n * Summertime temperatures:", end=" ")
    for i in temperatures: print(i, end=" ")

    temperatures_to_series = pd.Series(temperatures)

    print(f"\n\n ** Array to Series:\n{temperatures_to_series}")
    print(f"\n *** Descriptive statistics:\n{temperatures_to_series.describe()}")

    #----------------------------------------------

    grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90], 'Sam': [94, 77, 90],
                   'Katie': [100, 81, 82], 'Bob': [83, 65, 85]}

    grades_to_df = pd.DataFrame(grades_dict.values(), columns=['Math', 'English', 'Physics'], index=list(grades_dict.keys()))
    print(grades_to_df)

    #---------------------------------------------

    print(grades_to_df.iloc[0:2, 0:2])

    print(grades_to_df.loc['Wally':'Sam'])

    print(grades_to_df.loc[['Wally', 'Sam', 'Bob']])

    #----------------------------------------------
    print(grades_to_df.loc['Eva':'Katie', ['Math', 'Physics']])
    print(grades_to_df.iloc[[0, 2, 4], 0:2])

    #------------------------------------------

    ax = grades_to_df[(grades_to_df >= 80)]
    print(ax)

    ay = grades_to_df[(grades_to_df >= 80) & (grades_to_df < 90)]
    ay.fillna("None", inplace=True)

    print(ay)
    #-----------------------------------------

    print(grades_to_df.at['Wally', 'Math'])
    print(grades_to_df.iat[0, 2])

    grades_to_df.at['Wally', 'Math'] = 99

    grades_to_df.loc['Wally', 'Math':'Physics'] = [100, 100, 100]

    print(grades_to_df)

    #----------------------------------------

    pd.set_option('display.precision', 2)

    print(grades_to_df.transpose().describe())

    print(f"\n{grades_to_df.describe()}")

    #--------------------------------------

    az = grades_to_df.transpose().describe()
    print(f"\n{az.loc[:, 'Wally']}")

    print(grades_to_df.loc[:, 'Math'].describe())

    az = grades_to_df.sort_values(by='English', axis=0, ascending=False)
    print(az)

    #-------------------------------------------------

    temps = {'Mon': [68, 89], 'Tue': [71, 93], 'Wed': [66, 82],
             'Thu': [75, 97], 'Fri': [62, 79]}

    convert_to_df = pd.DataFrame(temps, index=['Low', 'High'])
    print(f"\n{convert_to_df}")

    from_mon_through_wed = convert_to_df.loc[:, 'Mon':'Wed']
    print(from_mon_through_wed)

    low_temps = convert_to_df.loc['Low']
    print(low_temps)

    avg_each_day = convert_to_df.mean(axis=0)
    print(avg_each_day)

    avg_low_high = convert_to_df.mean(axis=1)
    print(avg_low_high)



first_category: dict = {
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
}

second_category: dict = {
    2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
    7: 'seventy', 8: 'eighty', 9: 'ninety'
}

third_category: dict = {
    1: 'thousand', 2: 'million', 3: 'billion', 4: 'trillion', 5: 'quadrillion',
    6: 'quintillion', 7: 'sextillion', 8: 'septillion', 9: 'octillion',
    10: 'nonillion', 11: 'decillion'
}


def joining_elements(*args):
    return ' '.join(filter(bool, args))


def divide(dividend, divisor, magnitude):
    return joining_elements(process_number(dividend // divisor), magnitude, process_number(dividend % divisor))


def process_number(i):
    if i < 20:
        return first_category[i]
    if i < 100:
        return joining_elements(second_category[i // 10], first_category[i % 10])
    if i < 1000:
        return divide(i, 100, 'hundred')
    for k, z in third_category.items():
        if i < 1000**(k + 1):
            break
    return divide(i, 1000**k, z)


def catch_number(i):
    if i < 0:
        return joining_elements('negative', process_number(-i))
    if i == 0:
        return 'zero'
    return process_number(i)


def main():
    #exercises_1()
    #exercises_2()
    #exercises_3()
    ax = catch_number(1987)
    print(ax)


if __name__ == '__main__':
    main()
