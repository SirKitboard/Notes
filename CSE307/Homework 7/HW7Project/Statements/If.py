# Aditya Balwani
# SBUID: 109353920

from Nodes import Node

class IfStatement(Node.Node):
    """
    If statement
    """

    def __init__(self, expression, block):
        self.expression = expression
        self.block = block

    def evaluate(self):
        expression = self.expression.evaluate()
        if(isinstance(expression, int)):
            if(expression != 0):
                return True
            else:
                return False
        raise SemanticError.SemanticError()

    def execute(self):
        if(self.evaluate()):
            self.block.execute()
