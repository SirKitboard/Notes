# Aditya Balwani
# SBUID: 109353920

from Nodes import Node
from Exceptions import SemanticError

class Add(Node.Node):
    """
    A Node representing addition
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if type(left) != type(right):
            raise SemanticError.SemanticError()
        elif not isinstance(left, int) and not isinstance(left, str):
            raise SemanticError.SemanticError()
        return left + right
