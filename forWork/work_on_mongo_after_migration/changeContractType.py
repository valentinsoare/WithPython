#!/usr/bin/python

import pymongo
import pandas as pd


def header(given_message):
    message_processed = ' ### '
    message_processed += ' '.join(given_message)
    message_processed += ' ### '
    length_of_message = len(message_processed)

    print(f"\n{' ' * int(length_of_message * 0.5)}{message_processed}")
    print(f"{' ' * int(length_of_message * 0.25)}{'-' * int(length_of_message * 1.5)}")


def import_document(given_document):
    to_work_on = pd.read_csv(given_document, encoding='latin-1', engine='c')
    return to_work_on


def open_db_connection(**kwargs):
    user_name, passwd, host_name, used_port = tuple(kwargs.values())
    connection_address = f"mongodb://{user_name}:{passwd}@{host_name}:{used_port}"

    client = pymongo.MongoClient(connection_address)
    return client['beapi2']


def extract_relevant_fields(given_df):
    developer_id = pd.Series(given_df.iloc[:, 0])
    country = pd.Series(given_df.iloc[:, 3])
    offer_name = pd.Series(given_df.iloc[:, 4])

    return developer_id, country, offer_name


def printing_missing_lines(lines_missing):
    print(f"\n{' ' * 15}{'Lines that were not in DB:':}\n")
    for element in range(len(lines_missing)):
        print(f"{' ' * 12}{element + 1:>3}. {lines_missing[element][0]:<35}"
              f"{lines_missing[element][1]:<7}{lines_missing[element][2]}")


def check_and_act_on_type_in_db_from_imported_lines(developer_id, country_name, offer_name, flag=0):
    lines_not_found = []
    beapi = open_db_connection(user_name='rwuser', passwd='Anrw9avx!', host_name='10.228.216.136', used_port='8635')
    beapi_contracts_collection = beapi['contracts']

    for i in range(len(developer_id)):
        query_to_execute = {"developerId": f"{developer_id[i]}", "country": f"{country_name[i]}", "offerName": f"{offer_name[i]}"}

        if beapi_contracts_collection.count_documents(query_to_execute) != 0:
            result = beapi_contracts_collection.find(query_to_execute)
            for line in result: print(f"{' ' * 12}{(i + 1):>3}. {line['developerId']:<30} {line['country']:<7} {line['offerName']:<15} {line['type']} ")
        else:
            lines_not_found.append(tuple(query_to_execute.values()))

        if flag == 1:
            new_type = {"$set": {"type": "BROKER"}}
            beapi_contracts_collection.update_one(query_to_execute, new_type)

    return lines_not_found if flag == 1 else False


def main():
    # Print header message
    header('Updating Contract Type')

    # Read csv into panda dataframe
    data_to_process = import_document('to_extract_lines.csv')

    # Extract from dataframe 3 pandas series.
    developer_id, country_name, offer_name = extract_relevant_fields(data_to_process)

    # Read, print and then modify. In order to modify we used flag equal to 1 at the end of the arguments.
    print(f"\n{' ' * 15}{'Developer ID':<29}{'Country':<8}{'Offer Name':<12}{'Type / Will be changed to BROKER'}\n")
    missing_lines = check_and_act_on_type_in_db_from_imported_lines(developer_id, country_name, offer_name, 1)

    # Read and print to check if type values have been modified.
    print(f"\n{' ' * 15}{'Developer ID':<29}{'Country':<8}{'Offer Name':<12}{'Type Value after the Change'}\n")
    check_and_act_on_type_in_db_from_imported_lines(developer_id, country_name, offer_name, 0)

    # Print missing lines that were not in BeApi DB.
    printing_missing_lines(missing_lines)


if __name__ == '__main__':
    main()
