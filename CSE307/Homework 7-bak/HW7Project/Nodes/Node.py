# Aditya Balwani
# SBUID: 109353920

from Exceptions import SemanticError

# These are the nodes of our abstract syntax tree.
class Node(object):
    """
    A base class for nodes. Might come in handy in the future.
    """
    def execute(self):
        """
        Executes this node.
        """
        raise SemanticError.SemanticError()

    def evaluate(self):
        """
        Called on children of Node to evaluate that child.
        """
        raise Exception("Not implemented.")

    def location(self):
        """
        Evaluates this node for a location.
        """
        print("2")
        raise SemanticError.SemanticError()
