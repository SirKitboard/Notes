# Aditya Balwani
# SBUID: 109353920

from Nodes import Node
from Exceptions import *


class Xor(Node.Node):
    """
    A node representing the boolean and
    """

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError.SemanticError()
        if not isinstance(right, int):
            raise SemanticError.SemanticError()
        return left ^ right


class Or(Node.Node):
    """
    A node representing the boolean Or
    """

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError.SemanticError()
        if not isinstance(right, int):
            raise SemanticError.SemanticError()
        return 1 if (left != 0) | (right != 0) else 0


class Not(Node.Node):
    """
    A node representing the boolean NOT
    """
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        value = self.value.evaluate()
        if not isinstance(value, int):
            raise SemanticError.SemanticError()
        return 1 if (value == 0) else 0


class And(Node.Node):
    """
    A node representing the boolean and
    """

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError.SemanticError()
        if not isinstance(right, int):
            raise SemanticError.SemanticError()
        return 1 if (left != 0) & (right != 0) else 0
