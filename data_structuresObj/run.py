#!/usr/bin/python

#import string
#import random
#import dynArray
#import fixedArray
#import stackArray
import collections
import string
import queueArray
#import dequeArray
#import numpy as np
#import pandas as pd
#import simpleLinkedList
#import stackWithLinkedList
#import queueWithSingleLinkedList
#import queueWithCircularlyLinkedList
#from doubleLinkedList import DoubleLinkedList
#from circularLinkedList import CircularLinkedList
#from stackWithArrays import StacksArray
#from stacksLinkedList import StacksLinkedLists
#import queueWithArray
#import queueWithTheCircularLinkedList
#import dequeWithArray
#from deQueWithDoubleLinkedList import DEqueueDoubleLinkedList
#import doublyLinkedBase
#from binaryTreeWithLinkedList import BinaryTree

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

    #given_queue
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

    #circ_list = CircularLinkedList()
    #circ_list.add_item_end(404)
    #circ_list.add_item_end(20)
    #circ_list.add_item_end(11)
    #print(circ_list)
    #circ_list.rotate()
    #print(circ_list)

    #circ_list.add_item_beginning(8)
    #circ_list.add_item_beginning(2)

    #print(circ_list.head)
    #print(circ_list.tail)
    #print(circ_list)

    #circ_list.insert_item_anywhere(3, 1000)
    #print(circ_list)

    #circ_list.insert_item_anywhere(0, 666)
    #print(circ_list)

    # ax = circ_list.remove_item_beginning()
    # print(circ_list)
    # print(ax)
    # print(circ_list.head)
    # print(circ_list.tail)

    # ay = circ_list.remove_item_end()
    # print(ay)
    # print(circ_list)

    #az = circ_list.remove_item_anywhere(2)
    #print(circ_list)
    #print(az)

    #-------------------------------------
    #double linkedlist

    #d_list = DoubleLinkedList()

    #d_list.add_item_start(40)
    #d_list.add_item_start(22)
    #d_list.add_item_start(100)
    #d_list.add_item_start(44)
    #d_list.add_item_start(20)
    #d_list.add_item_start(9)
    #d_list.add_item_start(234)
    #d_list.add_item_start(12)
    #d_list.add_item_start(89)
    #d_list.add_item_start(91)
    #print(d_list)

    #d_list.insert_element(2, 1001)
    #print(d_list)

    #ax = d_list.remove_item_beginning()
    #print(ax)
    #print(d_list)

    #xx = d_list.remove_item_end()
    #print(xx)

    #print(d_list)
    #pp = d_list.remove_element(0)

    #print(pp)

    #d_list.add_item_start(57)
    #print(d_list)

    #aaa = d_list.remove_element(1)
    #print(aaa)

    #print(d_list)

    #-------------------------------------------------
    #stacksArray explainedVideo

    #given_stack = StacksArray()

    #given_stack.push(20)
    #given_stack.push(12)
    #given_stack.push(99)
    #given_stack.push(2)

    #print(given_stack)

    #given_stack.pop()
    #print(given_stack.top())
    #print(given_stack)

    #---------------------------------------------
    #stacks with LinkedList

    #given_stack_with_linked = StacksLinkedLists()
    #given_stack_with_linked.push(20)
    #given_stack_with_linked.push(123)
    #given_stack_with_linked.push(99)
    #given_stack_with_linked.push(11)

    #print(given_stack_with_linked)
    #ax = given_stack_with_linked.pop()
    #print(ax)
    #print(given_stack_with_linked)
    #print(given_stack_with_linked.bottom())

    #-------------------------------------------
    #Queue with Arrays

    #Q = queueWithArray.QueueArray()
    #Q.enqueue(44)
    #Q.enqueue(21)
    #Q.enqueue(98)
    #Q.enqueue(12)
    #Q.enqueue(101)
    #Q.enqueue(123)
    #Q.enqueue(942)

    #print(Q)
    #ax = Q.dequeue()
    #print(ax)
    #print(Q)
    #------------------------------

    #given_queue = queueWithTheCircularLinkedList.QueueCircularLinkedList()

    #given_queue.enqueue(44)
    #given_queue.enqueue(12)
    #given_queue.enqueue(100)
    #given_queue.enqueue(6)

    #print(given_queue)
    #given_queue.rotate()
    #print(given_queue)

    # extract_element_front = given_queue.dequeue()
    # print(extract_element_front)
    # print(given_queue)

    #------------------------------
    #double ended queues, DEques with array

    #given_q = dequeWithArray.DequeArray()

    #given_q.add_last(4)
    #given_q.add_last(20)
    #given_q.add_last(78)
    #given_q.add_first(100)
    #given_q.add_first(52)
    #given_q.add_last(123)
    #given_q.add_last(99)
    #given_q.add_first(67)

    #print(given_q.first())
    #print(given_q.last())

    #print(given_q)
    #extract_first = given_q.remove_first()
    #given_q.rotate()
    #given_q.rotate()

    #print(given_q)

    #print(given_q[7])

    #--------------------------------------------------------
    #double ended queue with double linked list

    #given_q = DEqueueDoubleLinkedList()

    #given_q.add_first(40)
    #given_q.add_first(21)
    #given_q.add_first(67)
    #given_q.add_first(19)
    #given_q.add_last(100)
    #given_q.add_last(4)
    #given_q.add_last(99)
    #given_q.insert(7, 1000)
    #given_q.insert(0, 400)
    #given_q.insert(2, 4000)
    #given_q.insert(6, 999)
    #print(given_q)
    #given_q.insert_between(55, 21, 67)
    #print(len(given_q))
    #print(given_q)

    ##----------------------
    #deque with double linkedlist with header and trailer as empty nodes

    #given_deque = doublyLinkedBase.LinkedDeque()

    #given_deque.insert_first(40)
    #given_deque.insert_first(5)
    #given_deque.insert_first(99)

    #print(f'Size: {len(given_deque)}')
    #print(given_deque)

    #ax = given_deque.delete_last()
    #print(given_deque)
    #print(f'Deleted Element from the list: {ax}')

    #given_positional_list = doublyLinkedBase.PositionalList()
    #given_positional_list.add_last(40)
    #given_positional_list.add_last(2)
    #given_positional_list.add_first(100)

    #aa = list(given_positional_list)
    #print(aa)

    #--------------------------------------------------------
    ##Binary trees

    #x = BinaryTree()
    #y = BinaryTree()
    #z = BinaryTree()
    #a = BinaryTree()     # it will be null for when a node has no children. This is for leaf nodes.

    #x.make_tree(20, a, a)
    #y.make_tree(30, a, a)
    #z.make_tree(10, x, y)

    # Binary tree traversal
    #z.inorder(z.root)    # A + B
    #print()
    #z.preorder(z.root)   # +AB
    #print()
    #z.postorder(z.root)  # AB+
    #print()

    #---------------------------------

    #null_node = BinaryTree()
    #a = BinaryTree()
    #b = BinaryTree()
    #c = BinaryTree()
    #d = BinaryTree()
    #e = BinaryTree()
    #f = BinaryTree()
    #g = BinaryTree()
    #h = BinaryTree()
    #i = BinaryTree()
    #j = BinaryTree()
    #k = BinaryTree()

    #creating leaf nodes
    #a.make_tree(40, null_node, null_node)
    #b.make_tree(10, null_node, null_node)
    #c.make_tree(10, null_node, null_node)
    #d.make_tree(25, null_node, null_node)
    #e.make_tree(15, null_node, null_node)

    #creating internal nodes
    #f.make_tree(200, a, null_node)
    #g.make_tree(100, null_node, b)
    #h.make_tree(60, d, e)
    #i.make_tree(50, g, h)
    #j.make_tree(90, i, null_node)
    #k.make_tree(80, f, j)        #root node for the entire tree structure

    #k.preorder(k.root)
    #print()
    #k.inorder(k.root)
    #print()
    #k.postorder(k.root)
    #print()
    #print()
    #k.levelorder()
    #print()
    #i.levelorder()  #partial tree, subtree

    #print(f'- > Our binary tree has {k.count_elements(k.root)} elements')

    #print(f'- > In Order Iter Traversal')
    #for p in k.inorder_iter():
    #    print(f'{p}', end=" ")

    #print(k)   # print the tree with inorder iterative traversal

    #print(f'The height of the K tree is {k.height(k.root) - 1}')   # find the height of a binary tree. Height starts from 0.
    #for p in k.preorder_iter():
    #    print(p, end=" ")

    #for p in k.postorder_iter():
    # print(p, end=" ")
    #-----------------------------------------------




if __name__ == '__main__':
    main()

