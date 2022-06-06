#!/usr/bin/python

# instead of stack and deque we can use a simple list to simulate these without all the bells and whistles.

from stackArray import StackArray
from queueArray import QueueArray        # deque can be found in collections, but I like the one that I made :D


class Node:
    __slots__ = '_left_child', '_right_child', '_element'

    def __init__(self, element, left_child=None, right_child=None):
        self._element = element
        self._right_child = right_child
        self._left_child = left_child

    @property
    def element(self):
        return self._element

    @property
    def left_child(self):
        return self._left_child

    @property
    def right_child(self):
        return self._right_child

    @element.setter
    def element(self, value):
        if value:
            self._element = value
        else:
            raise ValueError('No proper value was given!')

    @left_child.setter
    def left_child(self, value):
        if value:
            self._left_child = value
        else:
            raise ValueError('No proper value was given!')

    @right_child.setter
    def right_child(self, value):
        if value:
            self._right_child = value
        else:
            raise ValueError('No proper value was given')


class BinaryTree:
    def __init__(self, given_element, left_child=None, right_child=None):
        if None in (left_child, right_child):
            self._root = Node(given_element, left_child, right_child)
        else:
            self._root = Node(given_element, left_child.root, right_child.root)

    @property
    def root(self):
        return self._root

    #def make_tree(self, element, left, right):
    #    self._root = _Node(element, left.root, right.root)

    def depth_first_preorder_iterative(self):
        given_stack = StackArray()
        given_node = self.root

        if given_node.element is None:
            return -1

        given_stack.push(given_node)

        while not given_stack.is_empty():
            given_node = given_stack.pop()
            yield given_node.element

            if given_node.right_child.element is not None:
                given_stack.push(given_node.right_child)

            if given_node.left_child.element is not None:
                given_stack.push(given_node.left_child)

    def depth_first_preorder_recursive(self, given_root, given_list):
        if given_root:
            if given_root.element is not None:
                given_list.append(given_root.element)
            self.depth_first_preorder_recursive(given_root.left_child, given_list)
            self.depth_first_preorder_recursive(given_root.right_child, given_list)

        return given_list

    def breadth_first_levelorder_iterative(self):
        given_deque = QueueArray()
        given_node = self.root

        if given_node.element is not None:
            return -1

        given_deque.enqueue(given_node)

        while not given_deque.is_empty():
            given_node = given_deque.dequeue()
            yield given_node.element

            if given_node.left_child.element is not None:
                given_deque.enqueue(given_node.left_child)

            if given_node.right_child.element is not None:
                given_deque.enqueue(given_node.right_child)

    def inorder_iterative(self):
        given_node = self.root
        given_stack = StackArray()

        while True:
            if given_node.element:
                given_stack.push(given_node)
                given_node = given_node.left_child
            elif not given_stack.is_empty():
                given_node = given_stack.pop()
                yield given_node.element
                given_node = given_node.right_child

    def inorder_recursive(self, given_root, given_list):
        if given_root:
            self.inorder_recursive(given_root.left_child, given_list)
            if given_root.element is not None:
                given_list.append(given_root.element)
            self.inorder_recursive(given_root.right_child, given_list)

        return given_list

    def postorder_iterative(self):
        given_node = self.root

        if given_node.element is None:
            return -1

        processing_stack = StackArray()
        printing_stack = StackArray()
        processing_stack.push(given_node)

        while not processing_stack.is_empty():
            given_node = processing_stack.pop()
            printing_stack.push(given_node)

            if given_node.left_child.element is not None:
                processing_stack.push(given_node.left_child)

            if given_node.right_child.element is not None:
                processing_stack.push(given_node.right_child)

        while not printing_stack.is_empty():
            given_node = printing_stack.pop()
            yield given_node.element

    def postorder_recursive(self, given_root, given_list):
        if given_root:
            self.postorder_recursive(given_root.left_child, given_list)
            self.postorder_recursive(given_root.right_child, given_list)
            if given_root.element is not None:
                given_list.append(given_root.element)

        return given_list

    def count(self, given_root):
        if given_root.element is not None:
            x = self.count(given_root.left_child)
            y = self.count(given_root.right_child)
            return x + y + 1
        return 0

    def height(self, given_root):
        if given_root.element is not None:
            x = self.height(given_root.left_child)
            y = self.height(given_root.right_child)

            if x > y:
                return x + 1
            else:
                return y + 1
        return 0

    # recursive search function
    def search(self, given_value, given_node):
        if given_node.element is None:
            return

        if given_value == given_node.element:
            return given_node
        elif given_value < given_node.element:
            return self.search(given_value, given_node.left_child)
        else:
            return self.search(given_value, given_node.right_child)

    def insert(self, given_value, given_node):
        if given_value < given_node.element:
            if given_node.left_child.element is None:
                given_node.left_child = Node(given_value, None, None)
            else:
                self.insert(given_value, given_node.left_child)
        elif given_value > given_node.element:
            if given_node.right_child.element is None:
                given_node.right_child = Node(given_value, None, None)
            else:
                self.insert(given_value, given_node.right_child)

    def __str__(self):
        count = 0
        string_to_print = '['
        number_of_elements = self.count(self.root)

        for p in self.inorder_iterative():
            if count != number_of_elements - 1:
                string_to_print += str(p) + ', '
                count += 1
            else:
                string_to_print += str(p) + ']'

        return string_to_print
