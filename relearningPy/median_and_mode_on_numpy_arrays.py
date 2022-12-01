#!/usr/bin/python

import numpy as np


def exec_mode(array_from_user_work_with):
    list_with_indices = []
    values_to_return_most_freq = []

    values_from_array, freq_of_values = np.unique(array_from_user_work_with, return_counts=True)
    most_frequent_appearance = max(freq_of_values)

    if list(freq_of_values).count(most_frequent_appearance) > 1:
        for i in range(len(freq_of_values)):
            if freq_of_values[i] == most_frequent_appearance:
                list_with_indices.append(i)

        for j in range(len(list_with_indices)):
            values_to_return_most_freq.append(values_from_array[list_with_indices[j]])

        return values_to_return_most_freq

    else:
        value_to_returned_index = list(freq_of_values).index(most_frequent_appearance)
        mode_value = values_from_array[value_to_returned_index]

        return mode_value


def find_out_mode(array_from_user, axis=1, entire_array=True):
    if not isinstance(array_from_user, np.ndarray):
        raise ValueError("Ths method will work only on numpy arrays.")

    array_from_user_work_with = np.array(array_from_user)

    # part of mode method for the entire array is more complex and we use axis to parse raw by raw or column by column
    if axis == 0:
        array_from_user_work_with = np.array(array_from_user_work_with.transpose())

    if len(array_from_user_work_with) == 0:
        return None
    elif entire_array:
        return exec_mode(array_from_user_work_with)
    else:                         # this part is to find out mode for each row or each column.
        list_with_modes_per_column_row = []
        for i in range(len(array_from_user_work_with)):
            list_with_modes_per_column_row.append(exec_mode(array_from_user_work_with[i]))

        return list_with_modes_per_column_row


def exec_median(array_to_work_with):
    if len(array_to_work_with.shape) == 2:
        array_to_work_with = array_to_work_with.ravel()

    if len(array_to_work_with) == 2:
        return array_to_work_with[0]
    elif len(array_to_work_with) % 2 == 0:
        return [array_to_work_with[(len(array_to_work_with) // 2) - 1],
                array_to_work_with[(len(array_to_work_with) // 2)]]
    elif len(array_to_work_with) % 2 != 0:
        return array_to_work_with[len(array_to_work_with) // 2]


def find_out_median(given_array, axis=1, entire_array=True):
    if not isinstance(given_array, np.ndarray):
        raise ValueError("Ths method will work only on numpy arrays.")

    list_with_medians = []
    array_to_work_with = np.array(given_array)

    if len(given_array) == 0:
        return None
    elif len(given_array) == 1:
        return given_array[0]
    else:
        if axis == 0:
            array_to_work_with = array_to_work_with.transpose()

        if entire_array:
            return exec_median(array_to_work_with)
        else:
            for i in range(len(array_to_work_with)):
                list_with_medians.append(exec_median(array_to_work_with[i]))

            return list_with_medians


def main():
    array_work = np.array(np.random.randint(1, 10, 6).reshape(2, 3))

    calc_mode = find_out_mode(array_work, axis=1, entire_array=False)
    print(f"{array_work.ravel()}\n\n{calc_mode}")

    median_calc = find_out_median(array_work, axis=0, entire_array=False)
    print(f"{array_work}\n{median_calc}")


if __name__ == '__main__':
    main()
