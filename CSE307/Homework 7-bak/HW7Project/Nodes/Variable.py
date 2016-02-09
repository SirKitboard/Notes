# Aditya Balwani
# SBUID: 109353920

from Nodes import Node
from Exceptions import SemanticError
import glob


class Variable(Node.Node):
    """
    A node representing access to a variable.
    """
    def __init__(self, name):
        self.name = name

    def evaluate(self):
        for stack in reversed(glob.variables):
            if self.name in stack.keys():
                return stack[self.name]
        raise SemanticError()

    def location(self):
        for stack in reversed(glob.variables):
            if self.name in stack.keys():
                def setter(value):
                    stack[self.name] = value
                return setter

        def setter(value):
            glob.variables[-1][self.name] = value
        return setter

    def getName(self):
        return self.name
