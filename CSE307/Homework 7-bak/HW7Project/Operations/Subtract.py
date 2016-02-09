# Aditya Balwani
# SBUID: 109353920

from Nodes import Node
from Exceptions import SemanticError

class Subtract(Node.Node):
    """
    A Node representing subtraction
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
        return left - right
