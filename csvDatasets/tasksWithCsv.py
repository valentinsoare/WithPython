#!/usr/bin/python

import pandas as pd


def loading_the_datasets_static():
    diamonds_ds = pd.read_csv('diamonds.csv', index_col=0)
    return diamonds_ds


def printing_basic_output(data_processing):
    print(f'\n *First seven rows:\n{data_processing.head(7)}', end="\n\n")
    print(f' *Last seven rows:\n{data_processing.tail(7)}', end="\n\n")


def main():
    data_to_process = loading_the_datasets_static()
    printing_basic_output(data_to_process)


main()
