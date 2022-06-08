#!/usr/bin/python

class Position:
    _ERROR_MESSAGE = 'must be implemented by subclass'

    def element(self):
        raise NotImplementedError(self._ERROR_MESSAGE)

    def __eq__(self, other):
        raise NotImplementedError(self._ERROR_MESSAGE)

    def __ne__(self, other):
        if self != other:
            return True
        else:
            return False


class Tree:
    _ERROR = 'you need to implement this in subclass'

    # abstract methods implemented in this base class

    def root(self):
        raise NotImplementedError(self._ERROR)

    def parent(self, given_position):
        raise NotImplementedError(self._ERROR)

    def number_of_children(self, given_position):
        raise NotImplementedError(self._ERROR)

    def children(self, given_position):
        raise NotImplementedError(self._ERROR)

    def __len__(self):
        raise NotImplementedError(self._ERROR)

    # concrete methods implemented in this class.

    def is_root(self, given_position):
        if given_position == self.root:
            return True
        else:
            return False

    def is_leaf(self, given_position):
        if self.number_of_children(given_position) == 0:
            return True
        else:
            return False

    def is_empty(self):
        if len(self) == 0:
            return True
        else:
            return False

    def depth(self, given_position):
        if self.is_root(given_position):
            return 0
        else:
            return 1 + self.depth(self.parent(given_position))

    def _height1(self):
        list_with_depths = []
        for p in self.positions():
            if self.is_leaf(p):
                list_with_depths += self.depth(p)

        return max(list_with_depths)

    def _height2(self, given_position):
        if self.is_leaf(given_position):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(given_position))



