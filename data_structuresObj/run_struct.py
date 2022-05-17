#!/usr/bin/python

import string
import random
import dynArray
import fixedArray
import stackArray
import queueArray
import dequeArray
import numpy as np
import pandas as pd
import simpleLinkedList
import stackWithLinkedList
import queueWithSingleLinkedList
import queueWithCircularlyLinkedList
from circularLinkedList import CircularLinkedList
from doubleLinkedList import DoubleLinkedList


def main():
    #classes = fixedArray.FixedArray(['math', 'physics', 'chemistry', 'object oriented programming', 'english'])
    #classes_to_dict = {j.title(): i for i, j in classes.fixed_to_dict(given_keys=[classes[i][0] for i in range(len(classes))]).items()}
    #grades = fixedArray.FixedArray([[9, 10, 6.4, 8, 7, 9, 8.6], [10, 8, 6, 9.4, 7, 10], [8, 6, 10, 8, 9, 9, 6],
                                    #[10, 9, 7, 8, 9, 10], [8, 6, 10, 10, 9, 7, 8, 9]])

    #classes_grades_df = pd.DataFrame({i: grades[i] for i in range(len(grades))}.values(), index=classes_to_dict.keys(),
                                     #columns=['Andrew', 'Michele', 'Valentin', 'Jack', 'Richard', 'Kim', 'Kelly', 'David'])
    #initial_data_frame = classes_grades_df
    #classes_grades_df = classes_grades_df.transpose()

    #print(f'\n\033[1m{"**Classes and Grades**":>45}\033[0m\n')
    #print(f'{classes_grades_df}')

    #print(f'\n\n\033[1m{"**Stats on given table**":>47}\033[0m\n')
    #print(f' - Number of students: {len(classes_grades_df.keys()):>2}')
    #print(f' - Number of classes: {len(classes_grades_df.values):>3}')

    #print(f' - Average per student:', end="")
    #print(f'\n   {"-" * 45}', end="")

    #count = 0
    #for i, j in initial_data_frame.items():
    #    if count % 3 == 0:
    #        print()
    #    print(f'{" ":>3}{i}{": "}{j.values.mean()}', end=" ")
    #    count += 1

    #print(f'\n   {"-" * 45}', end="\n\n")

    ###-------------------------queue running

    #print(f'{"=" * 80}', end="\n\n")

    #given_queue = queueArray.QueueArray()

    #n = 0
    #while n < 9:
    #    number_to_add = random.randint(0, 100)
    #    given_queue.enqueue(number_to_add)
    #    n += 1

    #print(f'{given_queue}', end="\n\n")

    #value_x = given_queue.dequeue()
    #print(value_x)
    #print(f'{given_queue}', end="\n\n")

    #value_y = given_queue.dequeue()
    ##print(value_y)
    #print(f'{given_queue}', end="\n\n")

    ###-----------------------deque running

    #given_deck = dequeArray.Deque()

    #given_deck.add_first(10)
    #given_deck.add_first(40)
    #given_deck.add_first(25)

    #listing_transform = list(given_deck)
    #given_deck[0] = 23

    #print(f'Deque array: {given_deck}')
    #print(f'Converted to list: {listing_transform}')

    #print(given_deck.remove_first())
    #given_deck.add_last(201)

    #given_deck.add_first(33)
    #print(given_deck)

    ###------------------------stack with single linkedlist

    #given_linked_list = stackWithLinkedList.LinkedStack()

    #given_linked_list.push(20)
    #given_linked_list.push(101)
    #given_linked_list.push(44)

    #print(given_linked_list)
    #given_linked_list.push_last(50)

    #print(given_linked_list)

    ###-------------------------Queue with Single Linkedlist

    #queue_with_linked_list = queueWithSingleLinkedList.QueueLinkedList()

    #queue_with_linked_list.enqueue(4)
    #queue_with_linked_list.enqueue(22)
    #queue_with_linked_list.enqueue(123)
    #queue_with_linked_list.enqueue(4762)
    #queue_with_linked_list.enqueue(9999)
    #xx = queue_with_linked_list.get_position(123)

    #print(xx)
    #print(queue_with_linked_list)

    ###-----------------------
    #counting = 0
    #given_stack = stackWithLinkedList.LinkedStack()

    #while counting < 20:
    #    given_stack.push(random.randint(1, 101))
    #    given_stack.push_last(random.randint(400, 999))
    #    counting += 1

    #print(f'{given_stack}')

    #---------------------------------------
    #given_queue = queueWithCircularlyLinkedList.QueueCircularlyLinkedList()
    #given_queue.enqueue_back(4)
    #given_queue.enqueue_back(2)
    #given_queue.enqueue_back(100)

    #print(given_queue)
    #given_queue.enqueue_front(1)
    #print(given_queue)

    #given_queue.rotate()
    #given_queue.enqueue_back(35)

    #print(given_queue)

    #----------------------------------------
    #Single linked list

    #start_linked_list = simpleLinkedList.LinkedList()

    #start_linked_list.insert_element(100, 0)
    #start_linked_list.add_item_beginning(44)
    #start_linked_list.add_item_end(202)

    #xx = start_linked_list.get_location(44)

    #print(xx)

    #start_linked_list.insert_element(4444, 3)
    #print(start_linked_list)

    #ax = start_linked_list.remove_item_beginning()
    #print(ax)

    #print(start_linked_list)

    #axx = start_linked_list.remove_element_from_between(1)
    #print(axx)

    #print(start_linked_list)
    #---------------------------------------------------
    #Circular linked list

    circ_list = CircularLinkedList()
    circ_list.add_item_end(404)
    circ_list.add_item_end(20)
    circ_list.add_item_end(11)
    print(circ_list)
    circ_list.rotate()
    print(circ_list)

    #circ_list.add_item_beginning(8)
    #circ_list.add_item_beginning(2)

    #print(circ_list.head)
    #print(circ_list.tail)
    #print(circ_list)

    #circ_list.insert_item_anywhere(2, 1000)
    #print(circ_list)

    #circ_list.insert_item_anywhere(0, 666)
    #print(circ_list)

    #ax = circ_list.remove_item_beginning()
    #print(circ_list)
    #print(ax)
    #print(circ_list.head)
    #print(circ_list.tail)

    #ay = circ_list.remove_item_end()
    #print(ay)
    #print(circ_list)

    #az = circ_list.remove_item_anywhere(2)
    #print(circ_list)
    #print(az)

    #-------------------------------------
    #double linkedlist

    d_list = DoubleLinkedList()

    d_list.add_item_start(40)
    d_list.add_item_start(22)
    d_list.add_item_start(100)
    #print(d_list)

    d_list.add_item_end(20)
    d_list.add_item_end(9)
    #print(d_list)

    #print(f'{d_list.print_reverse_list()}')


if __name__ == '__main__':
    main()
