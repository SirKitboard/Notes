# Aditya Balwani
# SBUID: 109353920

from Nodes import Node

class Print(Node.Node):
    """
    A node representing the print function
    """

    def __init__(self, expression):
        self.expression = expression

    def execute(self):
        expression = self.expression.evaluate()
        print(repr(expression))
