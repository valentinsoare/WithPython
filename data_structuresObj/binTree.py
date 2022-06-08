#!/usr/bin/python

from stackWithArrays import StacksArray
from queueArray import QueueArray


class Node:
    __slots__ = '_element', '_left_child', '_right_child'

    def __init__(self, element, left_child, right_child):
        self._element = element
        self._left_child = left_child
        self._right_child = right_child

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
        self._element = value

    @left_child.setter
    def left_child(self, value):
        self._left_child = value

    @right_child.setter
    def right_child(self, value):
        self._right_child = value


class BinaryTree:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def make_tree(self, element, left_child, right_child):
        self._root = Node(element, left_child.root, right_child.root)

    def depth_first_preorder_iterative(self):
        given_stack = StacksArray()
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

        if given_node.element is None:
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
        given_stack = StacksArray()

        while True:
            if given_node is not None:
                given_stack.push(given_node)
                given_node = given_node.left_child
            elif not given_stack.is_empty():
                given_node = given_stack.pop()
                yield given_node.element
                given_node = given_node.right_child
            else:
                break

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

        processing_stack = StacksArray()
        printing_stack = StacksArray()
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
        if given_root:
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
            return False

        if given_value == given_node.element:
            return True
        elif given_value < given_node.element:
            return self.search(given_value, given_node.left_child)
        else:
            return self.search(given_value, given_node.right_child)

    def insert(self, given_value, given_node):
        if given_value < given_node.element:
            if given_node.left_child is None:
                given_node.left_child = Node(given_value, None, None)
            else:
                self.insert(given_value, given_node.left_child)
        elif given_value > given_node.element:
            if given_node.right_child is None:
                given_node.right_child = Node(given_value, None, None)
            else:
                self.insert(given_value, given_node.right_child)

    def delete(self, delete_value, given_node):
        if given_node is None:
            return None
        elif delete_value < given_node.element:
            given_node.left_child = self.delete(delete_value, given_node.left_child)
            return given_node
        elif delete_value > given_node.element:
            given_node.right_child = self.delete(delete_value, given_node.right_child)
            return given_node
        elif delete_value == given_node.element:
            if given_node.left_child is None:
                return given_node.right_child
            elif given_node.right_child is None:
                return given_node.left_child
            else:
                given_node.right_child = self.lift(given_node.right_child, given_node)
                return given_node

    def lift(self, given_node, node_to_delete):
        if given_node.left_child:
            given_node.left_child = self.lift(given_node.left_child, node_to_delete)
            return given_node
        else:
            node_to_delete.element = given_node.element
            return given_node.right_child

    #for inorder traversal iterative, first node in inorder traversal
    def subtree_first_iterative(self, given_node):
        while given_node.left_child is not None:
            given_node = given_node.left_child
        return given_node.element

    #first node in inorder traversal recursive
    def subtree_first_recursive(self, given_node):
        if given_node.left_child is not None:
            return self.subtree_first_recursive(given_node.left_child)
        return given_node.element

    #last node inorder traversal iterative
    def subtree_last_iterative(self, given_node):
        while given_node.right_child is not None:
            given_node = given_node.right_child
        return given_node.element

    #last node inorder traversal recursive
    def subtree_last_recursive(self, given_node):
        if given_node.right_child is not None:
            return self.subtree_last_recursive(given_node.right_child)
        return given_node.element

    #find successor node in inorder traversal binary trees
    def successor(self, given_node):
        if given_node.right_child is not None:
            return self.subtree_first_recursive(given_node.right_child)
        return given_node
       # under development :( not easy

    def __str__(self):
        count = 0
        string_to_print = '['
        number_of_elements = self.count(self.root)

        for p in self.inorder_iterative():
            if count != number_of_elements - 1 and p is not None:
                string_to_print += str(p) + ', '
                count += 1
            elif p is not None:
                string_to_print += str(p) + ']'

        return string_to_print
