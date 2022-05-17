#!/usr/bin/python

####t5-4-buc10-e

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


class CircularLinkedList:
    _MESSAGE_EMPTY = 'Circular Linked List is empty!'

    def __init__(self):
        self._tail = None
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        count = 0
        current = self._head

        while count < self._size:
            yield current.element
            current = current.next_node
            count += 1

    @property
    def head(self):
        return self._head.element

    @property
    def tail(self):
        return self._tail.element

    def is_empty(self):
        return self._size == 0

    def add_item_end(self, element):
        new_element = _Node(element, None)

        if self.is_empty():
            new_element._next_node = new_element
            self._head = new_element
        else:
            new_element._next_node = self._head   # or new_element._next_node = self._tail.next_node
            self._tail._next_node = new_element

        self._tail = new_element
        self._size += 1

    def insert_item_anywhere(self, position, element):
        if not 0 <= position <= self._size:
            raise IndexError('Position outside valid range!')
        elif position == 0:
            self.add_item_beginning(element)
        elif position == self._size:
            self.add_item_end(element)
        else:
            new_element = _Node(element, None)

            count = 0
            current = self._head

            while count < position - 1:
                current = current.next_node
                count += 1

            new_element._next_node = current.next_node
            current._next_node = new_element
            self._size += 1

    def add_item_beginning(self, element):
        if self.is_empty():
            raise Empty(self._MESSAGE_EMPTY)

        new_element = _Node(element, None)

        if self.is_empty():
            new_element._next_node = new_element
            self._tail = new_element
        else:
            new_element._next_node = self._head
            self._tail._next_node = new_element

        self._head = new_element
        self._size += 1

    def remove_item_beginning(self):
        if self.is_empty():
            raise Empty(self._MESSAGE_EMPTY)

        current = self._head
        self._head = current.next_node
        self._tail._next_node = self._head
        self._size -= 1

        if self.is_empty():
            self._tail = self._head = None

        return current.element

    def remove_item_end(self):
        if self.is_empty():
            raise Empty(self._MESSAGE_EMPTY)

        count = 0
        current = self._head
        value_to_return = self._tail.element

        while count < self._size - 2:
            current = current.next_node
            count += 1

        current._next_node = self._head
        self._tail = current
        self._size -= 1

        if self.is_empty():
            self._head = self._tail = None

        return value_to_return

    def remove_item_anywhere(self, position):
        if self.is_empty():
            raise Empty(self._MESSAGE_EMPTY)
        elif not 0 <= position < self._size:
            raise IndexError('Position value outside range!')
        elif position == 0:
            return self.remove_item_beginning()
        elif position == self._size - 1:
            return self.remove_item_end()
        else:
            count = 0
            current = self._head

            while count < position - 1:
                current = current.next_node
                count += 1

            element_to_remove = current.next_node
            current._next_node = element_to_remove.next_node
            self._size -= 1

            if self.is_empty():
                self._head = None
                self._tail = None

            return element_to_remove.element

    def __str__(self):
        if self.is_empty():
            raise Empty(self._MESSAGE_EMPTY)

        print_output = '['
        current = self._head

        while current != self._tail:
            print_output += str(current.element) + ', '
            current = current.next_node

        print_output += str(current.element) + ']'
        return print_output
