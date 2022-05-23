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


class _DoubleBaseLinkedList:
    def __init__(self):
        self._head = _Node(None, None, None)
        self._tail = _Node(None, None, None)
        self._head._next_node = self._tail
        self._tail._previous_node = self._head
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, element, successor, predecessor):
        new_element = _Node(element, successor, predecessor)
        predecessor._next_node = new_element
        successor._previous_node = new_element

        self._size += 1
        return new_element

    def _delete_node(self, element):
        predecessor = element.previous_node
        successor = element.next_node
        predecessor._next_node = successor
        successor._previous_node = predecessor

        self._size -= 1
        return element


class LinkedDeque(_DoubleBaseLinkedList):

    _EMPTY_MESSAGE = 'Deque is empty!'

    def first(self):
        if self.is_empty():
            raise Empty(self._EMPTY_MESSAGE)

        return self._head.next_node.element

    def last(self):
        if self.is_empty():
            raise Empty(self._EMPTY_MESSAGE)

        return self._tail.next_node.element

    def insert_first(self, element):
        self._insert_between(element, self._head.next_node, self._head)

    def insert_last(self, element):
        self._insert_between(element, self._tail, self._tail.previous_node)

    def delete_first(self):
        if self.is_empty():
            raise Empty(self._EMPTY_MESSAGE)

        return self._delete_node(self._head.next_node).element

    def delete_last(self):
        if self.is_empty():
            raise Empty(self._EMPTY_MESSAGE)

        return self._delete_node(self._tail.previous_node).element

    def __str__(self):
        string_to_return = '['

        current = self._head.next_node

        while current != self._tail.previous_node:
            string_to_return += str(current.element) + ', '
            current = current.next_node

        string_to_return += str(current.element) + ']'
        return string_to_return


class PositionalList(_DoubleBaseLinkedList):
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node.element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, pos):
        if not isinstance(pos, self.Position):
            raise TypeError('Pos must pe proper Position type!')
        if pos._container is not self:
            raise ValueError('pos does not belong to this computer!')
        if pos._node.next_node is None:
            raise ValueError('pos is not longer valid!')
        return pos._node

    def _make_position(self, node):
        if node is self._head or node is self._tail:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._head.next_node)

    def last(self):
        return self._make_position(self._tail.previous_node)

    def before(self, pos):
        node = self._validate(pos)
        return self._make_position(node.previous_node)

    def after(self, pos):
        node = self._validate(pos)
        return self._make_position(node.next_node)

    def __iter__(self):
        cursor = self.first()
        while cursor:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, element, successor, predecessor):
        node = super()._insert_between(element, predecessor, successor)
        return self._make_position(node)

    def add_first(self, element):
        return self._insert_between(element, self._head, self._head.next_node)

    def add_last(self, element):
        return self._insert_between(element, self._tail.previous_node, self._tail)

    def add_before(self, pos, element):
        original = self._validate(pos)
        return self._insert_between(element, original.previous_node, original)

    def add_after(self, pos, element):
        original = self._validate(pos)
        return self._insert_between(element, original, original.next_node)

    def delete(self, pos):
        original = self._validate(pos)
        return self._delete_node(original)

    def replace(self, pos, element):
        original = self._validate(pos)
        old_value = original.element
        original._element = element
        return old_value
