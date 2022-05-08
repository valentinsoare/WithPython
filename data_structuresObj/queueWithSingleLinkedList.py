#!/usr/bin/python

class Empty(Exception):
    pass


class QueueLinkedList:
    class _Node:
        __slots__ = '_element', '_next_object'

        def __init__(self, element, next_object):
            self._element = element
            self._next_object = next_object

        @property
        def element(self):
            return self._element

        @property
        def next_object(self):
            return self._next_object

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False

    @property
    def top(self):
        return self._head.element

    @property
    def last(self):
        return self._tail.element

    def enqueue(self, element):
        new_element = self._Node(element, None)

        if self.is_empty():
            self._head = new_element
        else:
            self._tail._next_object = new_element

        self._tail = new_element
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue array is empty')

        value_to_return = self._head.element
        self._head = self._head.next_object
        self._size -= 1

        if self.is_empty():
            self._tail = None

        return value_to_return

    def __str__(self):
        to_print = '['

        current_element = self._head

        count = 0
        while current_element:
            if count == self._size - 1:
                to_print += str(current_element.element) + ']'
                return to_print

            to_print += str(current_element.element) + ', '
            current_element = current_element.next_object
            count += 1

        return to_print






