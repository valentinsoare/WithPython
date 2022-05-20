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


class QueueCircularLinkedList:
    _MESSAGE_EMPTY = 'Queue is empty!'

    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, element):
        new_element = _Node(element, None)

        if self.is_empty():
            new_element._next_node = new_element
            self._head = new_element
        else:
            self._tail._next_node = new_element
            new_element._next_node = self._head

        self._tail = new_element
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty(self._MESSAGE_EMPTY)
        else:
            element_to_remove = self._head.element
            self._head = self._head.next_node
            self._tail._next_node = self._head
            self._size -= 1

        return element_to_remove

    def first(self):
        if self.is_empty():
            raise Empty(self._MESSAGE_EMPTY)

        return self._head.element

    def rotate(self):
        if self.is_empty():
            raise Empty(self._MESSAGE_EMPTY)
        else:
            self._tail = self._head
            self._head = self._head.next_node
            self._tail._next_node = self._head

    def __str__(self):
        if self.is_empty():
            raise Empty(self._MESSAGE_EMPTY)

        list_to_print = '['
        current = self._head

        while current != self._tail:
            list_to_print += str(current.element) + ', '
            current = current.next_node

        list_to_print += str(current.element) + ']'
        return list_to_print
