# Aditya Balwani
# SBUID: 109353920

from Nodes import Node

class StringLiteral(Node.Node):
    """
    A node representing String literals
    """

    def __init__(self,value):
        self.value = str(value)
        self.value = self.value[1:len(self.value)-1]

    def evaluate(self):
        # print("EV STR")
        return self.value
