# Aditya Balwani
# SBUID: 109353920

from Nodes import Node
import glob

class Block(Node.Node):
    """
    A node representing the block statement.
    """
    def __init__(self, statementList):
        self.statements = statementList

    def evaluate(self):
        return self.statements.evaluate()

    def execute(self):
        glob.variables.append({})
        statementList = self.evaluate()
        for statement in statementList:
            statement.execute()
        glob.variables.pop()
