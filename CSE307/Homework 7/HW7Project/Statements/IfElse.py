# Aditya Balwani
# SBUID: 109353920

from Nodes import Node

class IfElseStatement(Node.Node):
    """
    If statement
    """

    def __init__(self, expression, ifStatement, elseStatement):
        # print("IFELSE")
        self.expression = expression
        self.ifS = ifStatement
        self.elseS = elseStatement

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
            self.ifS.execute()
        else:
            self.elseS.execute()
