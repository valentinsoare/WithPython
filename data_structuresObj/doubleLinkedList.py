#!/usr/bin/python

class Empty(Exception):
    pass


class _Node:
    __slots__ = '_element', '_next_node', '_previous_node'

    def __init__(self, element, next_node, previous_node):
        self._element = element
        self._next_node = next_node
        self._previous_node = previous_node

    @property
    def element(self):
        return self._element

    @property
    def next_node(self):
        return self._next_node

    @property
    def previous_node(self):
        return self._previous_node


class DoubleLinkedList:

    _EMPTY_MESSAGE = 'Double Linked List is empty!'

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    @property
    def head(self):
        return self._head.element

    @property
    def tail(self):
        return self._tail.element

    def add_item_start(self, element):
        new_element = _Node(element, None, None)

        if self.is_empty():
            self._tail = new_element
        else:
            self._head._previous_node = new_element
            new_element._next_node = self._head

        self._head = new_element
        self._size += 1

    def add_item_end(self, element):
        new_element = _Node(element, None, None)

        if self.is_empty():
            self._head = new_element
        else:
            self._tail._next_node = new_element
            new_element._previous_node = self._tail

        self._tail = new_element
        self._size += 1

    def print_reverse_list(self):
        if self.is_empty():
            raise Empty(self._EMPTY_MESSAGE)

        var_for_printing = '['
        current = self._tail

        while current != self._head:
            var_for_printing += str(current.element) + ', '
            current = current.previous_node

        var_for_printing += str(current.element) + ']'
        return var_for_printing

    def __str__(self):
        if self.is_empty():
            raise Empty(self._EMPTY_MESSAGE)

        current = self._head
        double_list_to_print = '['

        while current != self._tail:
            double_list_to_print += str(current.element) + ', '
            current = current.next_node

        double_list_to_print += str(current.element) + ']'
        return double_list_to_print
