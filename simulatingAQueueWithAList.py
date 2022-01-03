#!/usr/bin/python

import random
import sys


def generated_list(how_many_elements_to_generate):
    output_list = [random.randrange(1, 51) for i in range(1, how_many_elements_to_generate)]
    return output_list


def put_elements_in_queue(given_queue, elements_to_add):
    if isinstance(elements_to_add, list):
        given_queue.extend(elements_to_add)
    else:
        given_queue.append(elements_to_add)

    return given_queue


def remove_elements_from_queue(given_queue, number_of_elements):
    i = 0
    if len(given_queue) < number_of_elements:
        print(f"\n - > Number of elements in queue is smaller than number of elements to remove.", end="\n\n")
        sys.exit(0)

    while i < number_of_elements:
        given_queue.pop(0)
        i += 1

    return list(given_queue)


def main():
    list_to_be_process = generated_list(20)
    print(f"\n - > Queue to work on: {list_to_be_process}", end="\n")

    elements_to_add = [1, 10, 4]
    queue_after_added = put_elements_in_queue(list_to_be_process, elements_to_add)
    print(f"\n - > Queue after added: {queue_after_added} ", end="\n")

    elements_to_add = [55, 100, 44, 23]
    queue_after_added = put_elements_in_queue(list_to_be_process, elements_to_add)
    print(f"\n - > Queue after added: {queue_after_added} ", end="\n")

    elements_after_removing = remove_elements_from_queue(queue_after_added, 12)
    print(f"\n - > Elements after removing: {elements_after_removing}", end="\n")


main()
