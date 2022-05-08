#!/usr/bin/python

class Empty(Exception):
    pass


class LinkedStack:
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
        self._size = 0
        self._head = None
        self._tail = None

    def __len__(self):
        return self._size

    @property
    def head(self):
        return self._head

    @property
    def size(self):
        return self._size

    @property
    def tail(self):
        return self._tail

    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty!')

        return self.head.element

    def last(self):
        if self.is_empty():
            raise Empty('Stack is empty')

        return self.tail.element

    def push(self, given_element):
        new_element = self._Node(given_element, self._head)
        self._head = new_element
        self._size += 1

        if self.size == 1:
            self._tail = new_element

    def push_last(self, given_element):
        new_element = self._Node(given_element, None)

        self._tail._next_object = new_element

        self._tail = new_element
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty!')

        var_to_return = self.head.element

        self._head = self.head.next_object
        self._size -= 1

        return var_to_return

    def __str__(self):
        value_to_return = '['
        present_object = self.head

        count = 0
        while present_object:
            if count == self._size - 1:
                value_to_return += str(present_object.element) + ']'
                return value_to_return

            value_to_return += str(present_object.element) + ', '
            present_object = present_object.next_object
            count += 1
