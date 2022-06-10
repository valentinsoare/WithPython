#!/usr/bin/python

from stackWithArrays import StacksArray
from queueArray import QueueArray


class Node:
    __slots__ = '_element', '_left', '_right'

    def __init__(self, element, left, right):
        self._element = element
        self._left = left
        self._right = right

    @property
    def element(self):
        return self._element

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right


class BinarySearchTree:
    def __init__(self, element, left, right):
        if None in (left, right):
            self._root = Node(element, None, None)
        else:
            self._root = Node(element, left.root, right.root)

    @property
    def root(self):
        return self._root

    def iterative_search(self, given_value):
        tnode = self.root

        while tnode.element is not None:
            if given_value is tnode.element:
                return True
            elif given_value < tnode.element:
                tnode = tnode.left
            elif given_value > tnode.element:
                tnode = tnode.right

        return False

    def recursive_search(self, given_value, given_node):
        temp_root = given_node.element

        if temp_root is None:
            return False

        if given_value == temp_root:
            return True
        elif given_value > temp_root:
            return self.recursive_search(given_value, given_node.right)
        else:
            return self.recursive_search(given_value, given_node.left)

    def iterative_traverse_binary_search_tree(self):
        temp_root = self.root
        given_stack = StacksArray()

        while True:
            if temp_root.element is not None:
                given_stack.push(temp_root)
                temp_root = temp_root.left
            elif not given_stack.is_empty():
                temp_root = given_stack.pop()
                yield temp_root.element
                temp_root = temp_root.right
            else:
                break

    def recursive_traverse_binary_search_tree(self, given_node, given_list):
        if given_node.element:
            self.recursive_traverse_binary_search_tree(given_node.left, given_list)
            given_list.append(given_node.element)
            self.recursive_traverse_binary_search_tree(given_node.right, given_list)

        return given_list
