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

    @property
    def head(self):
        return self._head

    @property
    def size(self):
        return self._size

    @property
    def tail(self):
        return self._tail

    def __len__(self):
        return self._size

    def __getitem__(self, item):
        if self.is_empty():
            raise Empty('Stack with linked list is empty!')

        count = 0
        element_to_get = self._head

        while count < self._size:
            if count == item:
                return str(element_to_get.element)
            element_to_get = element_to_get.next_object
            count += 1

    def __iter__(self):
        element_for_parse = self._head

        while element_for_parse:
            yield element_for_parse.element
            element_for_parse = element_for_parse.next_object

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
        if self.is_empty():
            raise Empty('Stack is empty, nothing to print!')

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
