# Aditya Balwani
# SBUID: 109353920

from Nodes import Node
from Exceptions import SemanticError

class Equal(Node.Node):
    """
    A node represening the boolean Equal
    """

    def __init__(self, a, b):
        self.left = a
        self.right = b

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError.SemanticError()
        if not isinstance(right, int):
            raise SemanticError.SemanticError()
        return 1 if left == right else 0

class Greater(Node.Node):
    """
    A node represening the boolean Equal
    """

    def __init__(self, a, b):
        self.left = a
        self.right = b

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError.SemanticError()
        if not isinstance(right, int):
            raise SemanticError.SemanticError()
        return 1 if left > right else 0

class Less(Node.Node):
    """
    A node represening the boolean Equal
    """

    def __init__(self, a, b):
        self.left = a
        self.right = b

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError.SemanticError()
        if not isinstance(right, int):
            raise SemanticError.SemanticError()
        return 1 if left < right else 0
