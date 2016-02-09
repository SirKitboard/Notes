# Aditya Balwani
# SBUID: 109353920

from Nodes import Node
from Nodes import Functions

class ReturnStatement(Node.Node):
    """
    If statement
    """

    def __init__(self, expression):
        self.expression = expression

    def evaluate(self):
        expression = self.expression.evaluate()
        return expression
        # if(isinstance(expression, int)):
        #     if(expression != 0):
        #         return True
        #     else:
        #         return False
        # raise SemanticError.SemanticError()

    def execute(self):
        # if(self.evaluate()):
        # self.block.execute()
        raise Functions.ReturnException(self.expression.evaluate())
        # raise self.expression.evaluate()
