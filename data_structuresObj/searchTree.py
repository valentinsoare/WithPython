#!/usr/bin/python

from stackWithArrays import StacksArray
from queueWithArray import QueueArray


class Node:
    __slots__ = '_element', '_left', '_right', '_parent'

    def __init__(self, element, left, right, parent):
        self._element = element
        self._left = left
        self._right = right
        self._parent = parent

    @property
    def element(self):
        return self._element

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def parent(self):
        return self._parent

    @right.setter
    def right(self, value):
        self._right = value

    @left.setter
    def left(self, value):
        self._left = value

    @parent.setter
    def parent(self, value):
        self._parent = value


class BinarySearchTree:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, value):
        self._root = value

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

    def recursive_search(self, given_value, given_node, type_of_return=0):

        if not given_node:
            return False

        if given_value == given_node.element:
            if type_of_return == 0:
                return True
            else:
                return given_node
        elif given_value > given_node.element:
            return self.recursive_search(given_value, given_node.right, type_of_return)
        elif given_value < given_node.element:
            return self.recursive_search(given_value, given_node.left, type_of_return)

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

    def iterative_preorder_traverse(self):
        temp_root = self.root
        given_stack = StacksArray()

        given_stack.push(temp_root)

        while not given_stack.is_empty():
            temp_root = given_stack.pop()
            yield temp_root.element

            if temp_root.right:
                given_stack.push(temp_root.right)

            if temp_root.left:
                given_stack.push(temp_root.left)

    def iterative_level_order(self):
        temp_root = self.root
        given_queue = QueueArray()

        if not temp_root:
            return -1

        given_queue.enqueue(temp_root)

        while not given_queue.is_empty():
            temp_root = given_queue.dequeue()
            yield temp_root.element

            if temp_root.left:
                given_queue.enqueue(temp_root.left)

            if temp_root.right:
                given_queue.enqueue(temp_root.right)

    def iterative_postorder(self):
        temp_root = self.root

        if not temp_root:
            return -1

        process_stack = StacksArray()
        printing_stack = StacksArray()

        process_stack.push(temp_root)

        while not process_stack.is_empty():
            temp_root = process_stack.pop()
            printing_stack.push(temp_root)

            if temp_root.left:
                process_stack.push(temp_root.left)

            if temp_root.right:
                process_stack.push(temp_root.right)

        while len(printing_stack) > 0:
            temp_root = printing_stack.pop()
            yield temp_root.element

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

    def insert_iterative(self, t_root, given_element, parent_node=None):
        temporary_root = None

        while t_root:
            temporary_root = parent_node = t_root
            if given_element == t_root.element:
                return
            elif given_element < t_root.element:
                t_root = t_root.left
            elif given_element > t_root.element:
                t_root = t_root.right

        new_node = Node(given_element, None, None, parent_node)

        if self.root:
            if new_node.element < temporary_root.element:
                temporary_root.left = new_node
            else:
                temporary_root.right = new_node
        else:
            self._root = new_node

    def insert_recursive(self, t_root, given_element, parent_node=None):
        if t_root:
            parent_node = t_root
            if given_element < t_root.element:
                t_root.left = self.insert_recursive(t_root.left, given_element, parent_node)
            elif given_element > t_root.element:
                t_root.right = self.insert_recursive(t_root.right, given_element, parent_node)
        else:
            new_element = Node(given_element, None, None, parent_node)
            t_root = new_element

            if not self.root:
                self.root = new_element

        return t_root

    def is_leaf_node(self, t_root, given_node_value):
        temp_root = t_root

        if not temp_root:
            return None

        if given_node_value == t_root.element and (not t_root.right and not t_root.left):
            return True
        elif given_node_value < temp_root.element:
            return self.is_leaf_node(t_root.left, given_node_value)
        elif given_node_value > temp_root.element:
            return self.is_leaf_node(t_root.right, given_node_value)
        else:
            return False

    def largest_element(self, t_root):
        temp_root = t_root

        while temp_root.right:
            temp_root = temp_root.right

        return temp_root.element

    def smallest_element(self, t_root):
        temp_root = t_root

        while temp_root.left:
            temp_root = temp_root.left

        return temp_root.element

    #def delete_iterative_way(self, given_value):
    #    t_root = self.root

    #    while t_root and given_value != t_root.element:
    #        parenting = t_root
    #        if given_value < t_root.element:
    #            t_root = t_root.left
    #        elif given_value > t_root.element:
    #            t_root = t_root.right

    #    if not t_root:
    #        return False

    #    #if t_root.right:

    def subtree_first_recursive(self, given_node):
        if given_node.left:
            return self.subtree_first_recursive(given_node.left)
        return given_node.element

    def subtree_last_recursive(self, given_node):
        if given_node.right:
            return self.subtree_last_recursive(given_node.right)
        return given_node.element

    def successor(self, given_element):
        t_root = self.root

        if not t_root:
            return False

        given_node = self.recursive_search(given_element, t_root, 1)

        if not given_node:
            return -1
        elif self.subtree_last_recursive(t_root) == given_node.element:
            return f'Value given is the last element of the tree!'

        if given_node.right:
            return self.subtree_first_recursive(given_node.right)
        else:
            while given_node != given_node.parent.left:
                given_node = given_node.parent

            return given_node.parent.element

    def __str__(self):
        str_to_print = '['
        given_root = self.root
        number_of_elements = self.count(given_root)
        for_traversing = self.recursive_inorder_traverse_binary_search_tree(given_root, [])

        for i in range(number_of_elements - 1):
            str_to_print += str(for_traversing[i]) + ', '

        str_to_print += str(for_traversing[number_of_elements - 1]) + ']'
        return str_to_print
