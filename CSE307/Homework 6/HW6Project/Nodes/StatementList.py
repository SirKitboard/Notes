# Aditya Balwani
# SBUID: 109353920

from Nodes import Node


class StatementList(Node.Node):
    """
    A node representing the block statement.
    """
    def __init__(self, statement, statementList=None):
        self.statement = statement
        self.statementList = statementList

    def evaluate(self):
        if self.statementList is None:
            return [self.statement]
        else:
            return [self.statement] + self.statementList.evaluate()
