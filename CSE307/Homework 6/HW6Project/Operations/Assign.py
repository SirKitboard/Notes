# Aditya Balwani
# SBUID: 109353920

import types

from Nodes import Node
from Exceptions import SemanticError

class Assign(Node.Node):
    """
    A node representing the assignment statement.
    """
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def execute(self):
        left = self.left.location()
        right = self.right.evaluate()
        if not isinstance(left, types.FunctionType):
            raise SemanticError.SemanticError()
        if not isinstance(right, int) and not isinstance(right, str) and not isinstance(right, list):
            raise SemanticError.SemanticError()
        left(right)


class AssignList(Node.Node):
    """
    A node for assigning values in a list
    """

    def __init__(self, left, index, right):
        self.left = left
        self.index = index
        self.right = right

    def execute(self):
        locationSetter = self.left.location()
        arrayValue = self.left.evaluate()
        value = self.right.evaluate()
        index = self.index.evaluate()

        arrayValue = self.setValue(arrayValue, index, value)

        locationSetter(arrayValue)

    def setValue(self, array, index, value):
        if not isinstance(index[0], int):
            raise SemanticError.SemanticError()
        if len(index) == 1:
            array[index[0]] = value
            return array
        else:
            temp = array[index[0]]
            temp = self.setValue(temp, index[1:], value)
            array[index[0]] = temp
            return array
