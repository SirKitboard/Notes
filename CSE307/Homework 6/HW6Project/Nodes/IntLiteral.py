# Aditya Balwani
# SBUID: 109353920

from Nodes import Node

class IntLiteral(Node.Node):
    """
    A node representing integer literals.
    """

    def __init__(self, value):
        self.value = int(value)

    def evaluate(self):
        return self.value
