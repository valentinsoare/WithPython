#!/usr/bin/python

import os
import mysql.connector


def printing_header(input_message):
    message_as_a_list = input_message.split()
    message_processed = ' * '.join(map(lambda i: i, message_as_a_list))
    length_of_processed_message = len(message_processed)

    print(f"\n{' ' * 6}{' ' * (length_of_processed_message // 2)}{message_processed}")
    print(f"{' ' * 6}{'-' * (length_of_processed_message * 2)}")


def sanity_checks_connect_db(host_to_use=None, db_name_from_user=None, user_to_use=None, passwd=None):
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

    try:
        connection_to_db = mysql.connector.connect(host=host_to_use,
                                                   database=db_name_from_user,
                                                   user=user_to_use,
                                                   password=passwd)
        if connection_to_db.is_connected():
            db_info = connection_to_db.get_server_info()
            print(f"Connected to MySQL Server version ", db_info)
            cursor = connection_to_db.cursor()
            cursor.execute("select database();")
            record_line = cursor.fetchone()
            print(f"You're connected to database: ", record_line)

    except mysql.connector.Error:
        print(f"\n{' ' * 6} * ERROR Error while connecting to MySQL DB.\n")
        os.system('sleep 2')


def main():
    printing_header('Cleaning Mysql BeAPI DB')
    sanity_checks_connect_db(host_to_use='localhost', db_name_from_user='beapidb01', user_to_use='root', passwd='beapidb01update')


if __name__ == '__main__':
    main()
