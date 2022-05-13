#!/usr/bin/python

class DoubleLinkedListBase:
    class _Node:
        def __init__(self, element, previous_element, next_element):
            self._element = element
            self._previous_element = previous_element
            self._next_element = next_element

        @property
        def previous_element(self):
            return self._previous_element

        @property
        def next_element(self):
            return self._next_element



