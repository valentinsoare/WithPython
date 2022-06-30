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

    @element.setter
    def element(self, value):
        self._element = value


class BinarySearchTree:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, value):
        self._root = value

    def __len__(self):
        return self.count(self.root)

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
            given_list.append(given_node)
            self.recursive_inorder_traverse_binary_search_tree(given_node.right, given_list)

        return given_list

    def get_leaf_nodes(self, given_node, given_list):
        if given_node:
            self.get_leaf_nodes(given_node.left, given_list)

            if not given_node.left and not given_node.right:
                given_list.append(given_node.element)

            self.get_leaf_nodes(given_node.right, given_list)

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

    def largest_element(self, t_root):
        while t_root.right:
            t_root = t_root.right

        return t_root.element

    def smallest_element(self, t_root):
        while t_root.left:
            t_root = t_root.left

        return t_root.element

    def subtree_first_iterative(self, given_node):
        while given_node.left:
            given_node = given_node.left
        return given_node.element

    def subtree_last_iterative(self, given_node):
        while given_node.right:
            given_node = given_node.right
        return given_node.element

    def subtree_first_recursive(self, given_node):
        if given_node.left:
            return self.subtree_first_recursive(given_node.left)
        return given_node

    def subtree_last_recursive(self, given_node):
        if given_node.right:
            return self.subtree_last_recursive(given_node.right)
        return given_node

    def is_root_node(self, given_val):
        t_root = self.root

        if not t_root:
            return None

        given_node = self.recursive_search(given_val, t_root, 1)

        if given_node.left or given_node.right:
            return True
        else:
            return False

    def number_of_children(self, given_value):
        count = 0
        t_root = self.root

        if not t_root:
            return False

        given_node = self.recursive_search(given_value, t_root, 1)

        if given_node:
            if given_node.left:
                count += 1

            if given_node.right:
                count += 1
        else:
            raise -1

        return count

    def is_leaf_node(self, given_node_value):
        temp_root = self.root

        if not temp_root:
            raise ValueError('There is no element in the tree')

        find_out_num_children = self.number_of_children(given_node_value)

        if find_out_num_children == -1:
            raise ValueError("Given element doesn't exists!")
        elif find_out_num_children in [1, 2]:
            return False
        else:
            return True

    def children_of_a_node(self, given_value):
        t_root = self.root
        tuple_to_return = []

        if not t_root:
            raise ValueError('There is no element in the tree')

        given_node = self.recursive_search(given_value, t_root, 1)

        if not given_node:
            raise ValueError("Given element doesn't exists!")

        for i in given_node.left, given_node.right:
            if i:
                tuple_to_return.append(i.element)
            else:
                tuple_to_return.append(i)

        return tuple_to_return

    def sibling(self, given_value):
        t_root = self.root

        if not t_root:
            raise ValueError('There is no element in the tree')

        given_node = self.recursive_search(given_value, t_root, 1)

        if not given_node:
            raise ValueError("Element doesn't exists!")
        else:
            p_node = given_node.parent

            if p_node.left and p_node.left.element != given_value:
                return p_node.left.element
            elif p_node.right and p_node.right.element != given_value:
                return p_node.right.element
            else:
                return None

    def left_node(self, given_value):
        t_root = self.root

        if not t_root:
            raise ValueError('There is no element in the tree')

        given_node = self.recursive_search(given_value, t_root, 1)

        if not given_node:
            raise ValueError("Element doesn't exists!")
        else:
            if given_node.left:
                return given_node.left.element
            else:
                return None

    def right_node(self, given_value):
        t_root = self.root

        if not t_root:
            raise ValueError('There is no element in the tree')

        given_node = self.recursive_search(given_value, t_root, 1)

        if not given_node:
            raise ValueError("Element doesn't exists!")
        else:
            if given_node.right:
                return given_node.right.element
            else:
                return None

    def successor(self, given_element):
        t_root = self.root

        if not t_root:
            return False

        given_node = self.recursive_search(given_element, t_root, 1)

        if not given_node:
            return -1
        elif self.subtree_last_recursive(t_root).element == given_node.element:
            return f'Value given is the last element of the tree!'

        if given_node.right:
            return self.subtree_first_recursive(given_node.right).element
        else:
            while given_node != given_node.parent.left:
                given_node = given_node.parent

            return given_node.parent

    def predecessor(self, given_element):
        t_root = self.root

        if not t_root:
            return False

        given_node = self.recursive_search(given_element, t_root, 1)

        if not given_node:
            return -1
        elif given_node.element == self.subtree_last_recursive(t_root).element:
            return given_node.parent

        if given_node.left:
            return self.subtree_last_recursive(given_node.left)

    def insert_after(self, given_node_value, new_element):
        t_root = self.root

        if t_root:
            given_node = self.recursive_search(given_node_value, t_root, 1)
            if not given_node.right:
                new_node = Node(new_element, None, None, given_node)
                given_node.right = new_node
            else:
                given_node = self.subtree_first_recursive(given_node.right)
                new_node = Node(new_element, None, None, given_node)
                given_node.left = new_node
        else:
            new_node = Node(new_element, None, None, None)
            self.root = new_node

    def insert_before(self, given_node_value, new_element):
        t_root = self.root

        if t_root:
            given_node = self.recursive_search(given_node_value, t_root, 1)
            if not given_node.left:
                new_node = Node(new_element, None, None, given_node)
                given_node.left = new_node
            else:
                temp = given_node.left
                new_node = Node(new_element, temp, None, given_node)
                given_node.left = new_node
                new_node.left.parent = new_node
        else:
            new_node = Node(new_element, None, None, None)
            self.root = new_node

    def delete_recursive(self, given_value, option_to_search=0):
        t_root = self.root

        if not t_root:
            return False

        if option_to_search == 1:
            given_node = self.recursive_search(given_value, t_root, 1)
        else:
            given_node = given_value

        if given_node.right:
            successor_node = self.subtree_first_recursive(given_node.right)
            temp_node = successor_node.element
            successor_node.element = given_node.element
            given_node.element = temp_node

            self.delete_recursive(successor_node)
        elif given_node.left:
            predecessor_node = self.subtree_last_recursive(given_node.left)
            temp_node = predecessor_node.element
            predecessor_node.element = given_node.element
            given_node.element = temp_node

            self.delete_recursive(predecessor_node)
        else:
            if given_node.parent.left == given_node:
                given_node.parent.left = None
            elif given_node.parent.right == given_node:
                given_node.parent.right = None

    def delete_iterative(self, given_value):
        t_root = self.root

        while t_root and t_root.element != given_value:
            if given_value < t_root.element:
                t_root = t_root.left
            elif given_value > t_root.element:
                t_root = t_root.right

        if not t_root:
            return False

        if t_root.left and t_root.right:
            choose_side = t_root.left

            while choose_side.right:
                choose_side = choose_side.right

            successor = choose_side
            t_root.element = successor.element

            if successor.parent.right.element == successor.element:
                successor.parent.right = None
            elif successor.parent.left.element == successor.element:
                successor.parent.left = None
        elif t_root.left:
            temp_node = t_root.parent
            t_root.parent.left = t_root.left
            t_root.left.parent = temp_node
        elif t_root.right:
            temp_node = t_root.parent
            t_root.parent.right = t_root.right
            t_root.right.parent = temp_node
        elif not t_root.left and not t_root.right:
            if t_root.parent.left.element == t_root.element:
                t_root.parent.left = None
            elif t_root.parent.right.element == t_root.element:
                t_root.parent.right = None

            t_root.parent = None

    def sum_of_all_leafs(self, given_node):
        all_leaf_nodes = self.get_leaf_nodes(given_node, [])
        return sum(all_leaf_nodes)

    def __str__(self):
        str_to_print = '['
        given_root = self.root
        number_of_elements = self.count(given_root)
        for_traversing = self.recursive_inorder_traverse_binary_search_tree(given_root, [])

        for i in range(number_of_elements - 1):
            str_to_print += str(for_traversing[i].element) + ', '

        str_to_print += str(for_traversing[number_of_elements - 1].element) + ']'
        return str_to_print
