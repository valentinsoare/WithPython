#!/usr/bin/python

import mysql.connector


def printing_header(input_message):
    message_as_a_list = input_message.split()
    message_processed = ' * '.join(map(lambda i: i, message_as_a_list))
    length_of_processed_message = len(message_processed)

    print(f"\n{' ' * 6}{' ' * (length_of_processed_message // 2)}{message_processed}")
    print(f"{' ' * 6}{'-' * (length_of_processed_message * 2)}")


def init_beapi_db(our_host=None, db_name=None, use_user=None, our_passwd=None):
    try:
        return mysql.connector.connect(host=our_host,
                                       database=db_name,
                                       user=use_user,
                                       password=our_passwd)
    except mysql.connector.Error:
        print(f"{' ' * 7} * ERROR connection cannot be made to DB.")
        exit(0)


def sanity_checks_and_make_connection(host_to_use=None, db_name_from_user=None, user_to_use=None, passwd=None):
    missing_args = []
    str_rep = ['host_to_use', 'db_name_from_user', 'user_to_use', 'passwd']

    for i in range(len(str_rep)):
        if not eval(str_rep[i]):
            missing_args.append(str_rep[i])

    length_of_missing_args = len(missing_args)

    if length_of_missing_args != 0:
        print(f"\n {' ' * 6} * ERROR - You need to have 4 input arguments"
              f" in order to connect to DB: host, db_name, user and password.",end="")
        print(f"\n{' ' * 7} ** {length_of_missing_args} missing arguments:", end=" ")

        for i in missing_args:
            print(f"{i}", end=" ")

        print(f"\n{' ' * 7} * Try again to make PDK proud!\n")
        exit(0)
    else:
        connection = init_beapi_db(our_host=host_to_use, db_name=db_name_from_user, use_user=user_to_use, our_passwd=passwd)
        return connection


def obtain_cursor(connection_to_db):
    try:
        connection_to_db.ping(reconnect=True, attempts=2, delay=2)
    except mysql.connector.Error:
        connection_to_db = sanity_checks_and_make_connection(host_to_use='10.228.216.136', db_name_from_user='beapidb01', user_to_use='root', passwd='beapidb01update')
    return connection_to_db.cursor()


def reading_the_file_txt(given_file):
    open_file = ''
    list_with_lines = []
    try:
        open_file = open(given_file, mode='r+')
    except FileNotFoundError:
        print(f'{" " * 7}{" * ERROR - file not found"}\n')
        exit(0)

    with open_file:
        entire_text = open_file.read().splitlines()
        for line in entire_text:
            list_with_lines.append(line)

    return list_with_lines


def main():
    count = 0
    message_to_use = 'Cleaning Mysql BeAPI DB'

    printing_header(message_to_use)
    connection_to_db = sanity_checks_and_make_connection(host_to_use='10.228.216.136', db_name_from_user='beapidb01',
                                                         user_to_use='root', passwd='beapidb01update')
    cursor = obtain_cursor(connection_to_db)

    processed_list = reading_the_file_txt('queries_for_db.txt')
    length_of_list = len(processed_list)
    list_with_vars = ['table_name', 'query_for_count_deleted', 'query_for_count_all', 'query_for_delete']
    length_of_list_var = len(list_with_vars)

    while count < length_of_list - 1:
        query_for_count_deleted = processed_list[count].replace('delete', 'select COUNT(*)')
        query_for_count_all = query_for_count_deleted.rsplit(' where')[0]
        table_name = query_for_count_all[query_for_count_all.find('from'):].lstrip('from')
        query_for_delete = processed_list[count]

        print(f"{' ' * 7}{(count + 1):>3}", end=".")

        for i in range(length_of_list_var):
            if i == 0:
                print(f"{table_name:<31}", end=" ")
            elif i == 3:
                cursor.execute(eval(list_with_vars[i]))
                connection_to_db.commit()
            else:
                cursor.execute(eval(list_with_vars[i]))
                output_record = cursor.fetchone()
                print(f"{'|':<2}{output_record[0]:<5}", end=" ")

        print(" |")

        count += 1

    connection_to_db.close()


if __name__ == '__main__':
    main()
