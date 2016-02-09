# Aditya Balwani
# SBUID: 109353920

import glob

from Nodes import Node
from Exceptions import SemanticError


class ListLiteral(Node.Node):
    """
    List Node
    """

    def __init__(self, elementList):
        self.elementList = elementList

    def evaluate(self):
        return self.elementList.evaluate()


class ElementList(Node.Node):
    """
    Helper for ListLiteral
    """

    def __init__(self, element, elementList=None):
        self.element = element
        self.elementList = elementList

    def evaluate(self):
        if self.elementList is None:
            return [self.element.evaluate()]
        else:
            return [self.element.evaluate()] + self.elementList.evaluate()


class Index(Node.Node):
    """
    Index Node
    """

    def __init__(self, list, indeces):
        self.list = list
        self.indeces = indeces

    def evaluate(self):
        left = self.list.evaluate()
        right = self.indeces.evaluate()
        if not isinstance(left, str) and not isinstance(left, list):
            raise SemanticError()
        if not isinstance(right, list):
            raise SemanticError()
        for element in right:
            if not isinstance(element, int):
                raise SemanticError.SemanticError()
            if len(left) < element + 1:
                raise SemanticError.SemanticError()
            left = left[element]
        return left

class Indeces(Node.Node):
    """
    Index Helper
    """

    def __init__(self, index, indeces=None):
        self.index = index
        self.indeces = indeces

    def evaluate(self):
        if self.indeces is None:
            return [self.index.evaluate()]
        else:
            return [self.index.evaluate()] + self.indeces.evaluate()
