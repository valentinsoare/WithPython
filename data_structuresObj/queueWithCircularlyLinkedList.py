#!/usr/bin/python

class Empty(Exception):
    pass


class QueueCircularlyLinkedList:
    class _Node:
        __slots__ = '_element', '_next_object'

        def __init__(self, element, next_object):
            self._element = element
            self._next_object = next_object

        @property
        def element(self):
            return self._element

        @property
        def next_object(self):
            return self._next_object

    MESSAGE_IF_EMPTY = 'Queue is empty'

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        current = self.tail

        while current.next_object != self.tail:
            current = current.next_object
            yield current.element

        yield current.next_object.element

    def __getitem__(self, item):                               # not efficient or recommended for a queue
        if self.is_empty():
            raise Empty(self.MESSAGE_IF_EMPTY)
        elif not 0 <= item < self.size:
            raise IndexError('Index not within range')

        count = 0
        current_for_parse = self.tail.next_object

        while count < self.size:
            if count == item:
                value_to_return = current_for_parse.element
                return value_to_return

            current_for_parse = current_for_parse.next_object
            count += 1

    @property
    def tail(self):
        return self._tail

    @property
    def size(self):
        return self._size

    def first(self):
        if self.is_empty():
            raise Empty(self.MESSAGE_IF_EMPTY)

        element_to_return = self.tail.next_object
        return element_to_return.element

    def last(self):
        if self.is_empty():
            raise Empty(self.MESSAGE_IF_EMPTY)

        element_to_return = self.tail.element
        return element_to_return

    def is_empty(self):
        return self._size == 0

    def dequeue_front(self):
        if self.is_empty():
            raise Empty(self.MESSAGE_IF_EMPTY)
        elif self.size == 1:
            heading = self.tail.element
            self._tail = None
        else:
            heading = self.tail.next_object                # save old head
            self._tail._next_object = heading.next_object  # set new head

        self._size -= 1
        return heading.element

    def dequeue_back(self):
        #no efficient to dequeue from the
        #back of a queue with a single linked list, we need a double

        if self.is_empty():
            raise Empty(self.MESSAGE_IF_EMPTY)
        elif self._size == 1:
            backing = self.tail.element
            self._tail = None
        else:
            backing = self.tail.element
            head = parse_element = self.tail.next_object

            while parse_element != self.tail:
                parse_element = parse_element.next_object

            self._tail = parse_element
            self._tail._next_object = head

        return backing

    def enqueue_back(self, element):
        new_item = self._Node(element, None)
        if self.is_empty():
            self._tail = new_item                  # header and tail set
            self._tail._next_object = self.tail    # header definition
        else:
            new_item._next_object = self.tail.next_object
            self._tail._next_object = new_item

        self._tail = new_item
        self._size += 1

    def enqueue_front(self, element):
        new_item = self._Node(element, None)

        if self.is_empty():
            self._tail = new_item
            self._tail._next_object = self.tail
        else:
            new_item._next_object = self.tail.next_object
            self._tail._next_object = new_item

        self._size += 1

    def rotate(self):
        if self.is_empty():
            raise Empty(self.MESSAGE_IF_EMPTY)
        else:
            self._tail = self.tail.next_object    # tail value becomes old head value

    def __str__(self):
        value_to_print = '['
        current = self.tail

        while current.next_object != self.tail:
            current = current.next_object
            value_to_print += str(current.element) + ', '

        value_to_print += str(self.tail.element) + ']'
        return value_to_print
