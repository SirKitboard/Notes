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

        print(self.name)
        raise SemanticError()

    def location(self):
        for stack in reversed(glob.variables):
            if self.name in stack.keys():
                def setter(value):
                    stack[self.name] = value
                return setter

        def setter(value, arguments=None):
            if(arguments is None):
                glob.variables[-1][self.name] = value
            else:
                glob.variables[0][self.name] = {
                    "statements" : value,
                    "arguments" : arguments
                }
        return setter

    def execute(self, arguments = []):
        function = glob.variables[0][self.name]
        if(len(arguments) != len(function["arguments"])):
            raise SemanticError()
        argumentsDict = {}
        for index, name in enumerate(function['arguments']):
            argumentsDict[name] = arguments[index]
        # print(argumentsDict)
        # print(function["statements"])
        function["statements"].execute(argumentsDict)

    def getName(self):
        return self.name
