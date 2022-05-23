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


class DEqueueDoubleLinkedList:
    _EMPTY_MESSAGE = 'Double queue is empty!'
    _NOT_VALID_MESSAGE = 'Value outside the valid range!'

    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None

    def __len__(self):
        return self._size

    def __getitem__(self, item):
        if self.is_empty():
            raise Empty(self._EMPTY_MESSAGE)
        elif not 0 <= item < self._size:
            raise IndexError(self._NOT_VALID_MESSAGE)

        if item > self.size // 2:
            count = self._size - 1
            current = self._tail

            if count == item:
                return current.element

            while count > item + 1:
                current = current.previous_node
                count -= 1

            element_to_return = current.previous_node.element
            return element_to_return
        else:
            count = 0
            current = self._head

            if item == count:
                return current.element

            while count < item - 1:
                current = current.next_node
                count += 1

            element_to_return = current.next_node.element
            return element_to_return

    @property
    def head(self):
        return self._head.element

    @property
    def tail(self):
        return self._tail.element

    @property
    def size(self):
        return self._size

    def is_empty(self):
        return self.size == 0

    def add_first(self, element):
        new_element = _Node(element, None, None)

        if self.is_empty():
            self._tail = new_element
        else:
            self._head._previous_node = new_element
            new_element._next_node = self._head

        self._head = new_element
        self._size += 1

    def add_last(self, element):
        new_element = _Node(element, None, None)

        if self.is_empty():
            self._head = new_element
        else:
            self._tail._next_node = new_element
            new_element._previous_node = self._tail

        self._tail = new_element
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            raise Empty(self._EMPTY_MESSAGE)
        else:
            current = self._head
            self._head = self._head.next_node
            self._head._previous_node = None

        self._size -= 1

        if self.is_empty():
            self._tail = None

        return current.element

    def remove_last(self):
        if self.is_empty():
            raise Empty(self._EMPTY_MESSAGE)
        else:
            current = self.tail
            self._tail = self.tail.previous_node
            self._tail._next_node = None

        self._size -= 1

        if self.is_empty():
            self._head = None

        return current.element

    def search(self, element):
        if self.is_empty():
            raise Empty(self._EMPTY_MESSAGE)

        count = 0
        current = self._head

        while current:
            if current.element == element:
                return count
            current = current.next_node
            count += 1

    def insert(self, position, element):
        new_element = _Node(element, None, None)

        if self.is_empty():
            raise Empty(self._EMPTY_MESSAGE)
        elif not 0 <= position <= self._size:
            raise IndexError(self._NOT_VALID_MESSAGE)
        elif position == self._size:
            self.add_last(element)
        elif position == 0:
            self.add_first(element)
        elif position > self._size // 2:
            count = self._size - 1
            current = self._tail

            while count > position:
                current = current.previous_node
                count -= 1

            new_element._previous_node = current.previous_node
            current.previous_node._next_node = new_element
            new_element._next_node = current
            current._previous_node = new_element
            self._size += 1
        else:
            count = 0
            current = self._head

            while count < position - 1:
                current = current.next_node
                count += 1

            new_element._next_node = current.next_node
            current.next_node._previous_node = new_element
            new_element._previous_node = current
            current._next_node = new_element
            self._size += 1

    def __str__(self):
        string_for_printing = '['
        current_node = self._head

        while current_node != self._tail:
            string_for_printing += str(current_node.element) + ', '
            current_node = current_node.next_node

        string_for_printing += str(current_node.element) + ']'
        return string_for_printing
