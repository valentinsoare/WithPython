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


class LinkedList:
    _MESSAGE_IF_EMPTY = 'Linked list is empty!'

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        current = self._head

        while current:
            yield current.element
            current = current.next_node

    def __getitem__(self, item):
        if self.is_empty():
            raise Empty(LinkedList._MESSAGE_IF_EMPTY)
        elif not 0 <= item < self._size:
            raise ValueError('Wrong element location, outside range!')

        count = 0
        current = self._head

        while count < self._size:
            if item == count:
                return current.element

            count += 1
            current = current.next_node

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            return Empty(LinkedList._MESSAGE_IF_EMPTY)

        return self._head.element

    def last(self):
        if self.is_empty():
            return Empty(LinkedList._MESSAGE_IF_EMPTY)

        return self._tail.element

    def add_item_beginning(self, element):
        new_node = _Node(element, None)

        if self.is_empty():
            self._tail = new_node
        else:
            new_node._next_node = self._head

        self._head = new_node
        self._size += 1

    def insert_element(self, given_element, position):
        if position == 0:
            self.add_item_beginning(given_element)
        elif (position - 1) == self._size - 1:
            self.add_item_end(given_element)
        else:
            new_node = _Node(given_element, None)
            current = self._head
            count = 0

            while count < position - 1:
                current = current.next_node
                count += 1

            new_node._next_node = current.next_node
            current._next_node = new_node
            self._size += 1

    def add_item_end(self, element):
        new_node = _Node(element, None)

        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next_node = new_node

        self._tail = new_node
        self._size += 1

    def get_location(self, req_element):
        if self.is_empty():
            raise Empty(LinkedList._MESSAGE_IF_EMPTY)

        count = 0
        current = self._head

        while current:
            if req_element == current.element:
                return count

            current = current.next_node
            count += 1

        return -1

    def remove_item_beginning(self):
        if self.is_empty():
            raise Empty(self._MESSAGE_IF_EMPTY)

        current = self._head.element
        self._head = self._head.next_node
        self._size -= 1

        if self.is_empty():
            self._tail = None

        return current

    def remove_item_end(self):
        if self.is_empty():
            raise Empty(self._MESSAGE_IF_EMPTY)

        count = 0
        current = self._head
        end_element = self._tail.element

        till_end = self._size - 2
        while count < till_end:
            current = current.next_node
            count += 1

        self._tail = current
        self._tail._next_node = None
        self._size -= 1

        if self.is_empty():
            self._head = None

        return end_element

    def remove_element_from_between(self, position):
        if self.is_empty():
            raise Empty(self._MESSAGE_IF_EMPTY)
        elif not 0 <= position < self._size:
            raise IndexError('Position value not inside proper range.')

        count = 0
        current = self._head

        while count < position - 1:
            current = current.next_node
            count += 1

        last_iter = current.next_node
        current._next_node = last_iter.next_node
        self._size -= 1

        return last_iter.element

    def __str__(self):
        to_print = '['
        current = self._head

        while current != self._tail:
            to_print += str(current.element) + ', '
            current = current.next_node

        to_print += str(current.element) + ']'
        return to_print
