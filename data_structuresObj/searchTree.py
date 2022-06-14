#!/usr/bin/python

from stackWithArrays import StacksArray


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

    @right.setter
    def right(self, value):
        self._right = value

    @left.setter
    def left(self, value):
        self._left = value


class BinarySearchTree:
    def __init__(self):
        self._root = None

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

        if given_node:
            return False

        if given_value == given_node.element:
            return True
        elif given_value > given_node.element:
            return self.recursive_search(given_value, given_node.right)
        else:
            return self.recursive_search(given_value, given_node.left)

    def iterative_inorder_traverse_binary_search_tree(self):
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

    def recursive_inorder_traverse_binary_search_tree(self, given_node, given_list):
        if given_node:
            self.recursive_inorder_traverse_binary_search_tree(given_node.left, given_list)
            given_list.append(given_node.element)
            self.recursive_inorder_traverse_binary_search_tree(given_node.right, given_list)

        return given_list

    def count(self, temp_root):
        if temp_root:
            x = self.count(temp_root.left)
            y = self.count(temp_root.right)
            return x + y + 1
        return 0

    def height(self, temp_root):
        if temp_root:
            x = self.height(temp_root.left)
            y = self.height(temp_root.right)
            if x > y:
                return x + 1
            else:
                return y + 1
        return -1

    def insert_iterative(self, t_root, given_element):
        temporary_root = None

        while t_root:
            temporary_root = t_root
            if given_element == t_root.element:
                return
            elif given_element < t_root.element:
                t_root = t_root.left
            elif given_element > t_root.element:
                t_root = t_root.right

        new_node = Node(given_element, None, None)

        if self.root:
            if new_node.element < temporary_root.element:
                temporary_root.left = new_node
            else:
                temporary_root.right = new_node
        else:
            self._root = new_node

    def __str__(self):
        str_to_print = '['
        given_root = self.root
        number_of_elements = self.count(given_root)
        for_traversing = self.recursive_inorder_traverse_binary_search_tree(given_root, [])

        for i in range(number_of_elements - 1):
            str_to_print += str(for_traversing[i]) + ', '

        str_to_print += str(for_traversing[number_of_elements - 1]) + ']'
        return str_to_print
