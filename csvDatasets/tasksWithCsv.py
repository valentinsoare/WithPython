#!/usr/bin/python

import re
import pandas as pd


def loading_the_datasets_static():
    diamonds_ds = pd.read_csv('diamonds.csv', index_col=0)
    return diamonds_ds


def printing_basic_output(data_processing):
    print(f'\n *First seven rows:\n{data_processing.head(7)}', end="\n\n")
    print(f' *Last seven rows:\n{data_processing.tail(7)}', end="\n\n")


def descriptive_statistics(given_data_frame):
    calc_value = given_data_frame.describe()

    print(f'\n *Descriptive statistics on the given data:', end="\n")
    print(f'{calc_value}', end="\n\n")


def stats_for_selected_columns(given_data):
    with_selected_columns = ['cut', 'color', 'clarity', 'depth', 'table', 'price', 'x', 'y', 'z']

    print(f'*Stats on selected columns:', end="\n")

    for select in with_selected_columns:
        print(f'\n{"- >":>7} Stats for {select}:', end="\n\n")
        series_selected = pd.Series(given_data[select], dtype=str)
        if select in ['cut', 'color', 'clarity']:
            print(f' - Descriptive stats:\n{series_selected.describe()}', end="\n\n")
            print(f' - Uniq values:\n{series_selected.unique()}', end="\n\n")
        else:
            print(f' - Uniq values:\n{series_selected.unique()}', end="\n\n")

    print()


def main():
    pd.set_option('precision', 2)
    data_to_process = loading_the_datasets_static()
    printing_basic_output(data_to_process)

    descriptive_statistics(data_to_process)
    stats_for_selected_columns(data_to_process)


main()
