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

    def __iter__(self):
        if self.is_empty():
            raise Empty(self._EMPTY_MESSAGE)

        current = self._head

        while current:
            yield current.element
            current = current.next_node

    def is_empty(self):
        return self._size == 0

    @property
    def head(self):
        return self._head.element

    @property
    def tail(self):
        return self._tail.element

    def reverse_iter(self):
        if self.is_empty():
            raise Empty(self._EMPTY_MESSAGE)

        current = self._tail

        while current:
            yield current.element
            current = current.previous_node

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

    def remove_item_beginning(self):
        if self.is_empty():
            raise Empty(self._EMPTY_MESSAGE)
        else:
            to_return = self._head.element
            self._head = self._head.next_node
            self._head._previous_node = None

            self._size -= 1

        if self.is_empty():
            self._tail = None

        return to_return

    def remove_item_end(self):
        if self.is_empty():
            raise Empty(self._EMPTY_MESSAGE)
        else:
            to_return = self._tail.element
            self._tail = self._tail.previous_node
            self._tail._next_node = None
            self._size -= 1

        if self.is_empty():
            self._head = None

        return to_return

    def insert_element(self, position, element):
        new_element = _Node(element, None, None)

        if not 0 <= position <= self._size:
            raise IndexError('Position value outside of valid range.')

        if position == 0:
            self.add_item_start(element)
        elif position == self._size:
            self.add_item_end(element)
        elif position > self._size // 2:
            current = self._tail
            count = self._size - 1

            while count > position:
                current = current.previous_node
                count -= 1

            new_element._previous_node = current.previous_node
            current._previous_node._next_node = new_element
            new_element._next_node = current
            current._previous_node = new_element
            self._size += 1
        else:
            current = self._head
            count = 0

            while count < position - 1:
                current = current.next_node
                count += 1

            new_element._next_node = current.next_node
            current.next_node._previous_node = new_element
            current._next_node = new_element
            new_element._previous_node = current
            self._size += 1

    def remove_element(self, position):
        if self.is_empty():
            raise Empty(self._EMPTY_MESSAGE)
        elif not 0 <= position <= self._size:
            raise IndexError('Position value outside of valid range.')

        if position == 0:
            return self.remove_item_beginning()
        elif position == self._size - 1:
            return self.remove_item_end()
        elif position > self._size // 2:
            current = self._tail
            count = self._size - 1

            while count > position + 1:
                current = current.previous_node
                count -= 1

            node_to_remove = current.previous_node
            current._previous_node = node_to_remove.previous_node
            current._previous_node._next_node = current
            self._size -= 1

            return node_to_remove.element
        else:
            current = self._head
            count = 0

            while count < position - 1:
                current = current.next_node
                count += 1

            node_to_remove = current.next_node
            current._next_node = node_to_remove.next_node
            node_to_remove.next_node._previous_node = current
            self._size -= 1

            return node_to_remove.element

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
