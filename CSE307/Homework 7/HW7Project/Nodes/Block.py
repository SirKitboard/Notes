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

    def execute(self, arguments = {}):
        glob.variables.append({})
        for key in arguments:
            glob.variables[-1][key] = arguments[key]
        statementList = self.evaluate()
        # print(statementList)
        for statement in statementList:
            # print(statement)
            # print(statement)
            statement.execute()
        glob.variables.pop()

    # def execute(self, arguments):
    #     glob.variables.append({})
    #     statementList = self.evaluate()
    #     # print(statementList)
    #     for statement in statementList:
    #         # print(statement)
    #         statement.execute()
    #     glob.variables.pop()
