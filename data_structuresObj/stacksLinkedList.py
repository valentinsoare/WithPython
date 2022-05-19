#!/usr/bin/python

class Empty(Exception):
    pass


class _Node:
    __slots__ = '_element', '_next_node'

    def __init__(self, element, next_node):
        self._element = element
        self._next_node = next_node

    @property
    def element(self):
        return self._element

    @property
    def next_node(self):
        return self._next_node


class StacksLinkedLists:
    _MESSAGE_EMPTY = 'Stack is empty!'

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def top(self):
        if self.is_empty():
            raise Empty(self._MESSAGE_EMPTY)

        return self._head.element

    def bottom(self):
        if self.is_empty():
            raise Empty(self._MESSAGE_EMPTY)

        return self._tail.element

    def push(self, element):
        new_element = _Node(element, None)

        if self.is_empty():
            self._tail = new_element
        else:
            new_element._next_node = self._head

        self._head = new_element
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Empty(self._MESSAGE_EMPTY)
        else:
            to_retrieve = self._head
            self._head = to_retrieve.next_node
            self._size -= 1

        return to_retrieve.element

    def __str__(self):
        string_to_print = '['
        current = self._head

        while current != self._tail:
            string_to_print += str(current.element) + ', '
            current = current.next_node

        string_to_print += str(current.element) + ']'
        return string_to_print
