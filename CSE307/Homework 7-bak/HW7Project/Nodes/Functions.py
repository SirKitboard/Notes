from Nodes import Node
import glob


class Function(Node.Node):
    """
    The function node
    """

    def __init(self, name):
        print("HI")
        self.name = name

    def exectute(self):
        print("execute")

    def location(self):
        for stack in reversed(glob.functions):
            if self.name in stack.keys():
                def setter(defin, argLength):
                    stack[self.name] = {
                        'def': defin,
                        'argsLen': argLength
                    }
                return setter

        def setter(defin, argLength):
            glob.functions[-1][self.name] = {
                'def': defin,
                'argsLen': argLength
            }
        return setter

class ArgumentList(Node.Node):
    """
    Argument List for a function
    """

    def __init__(self, arg, argList=None):
        self.argument = arg
        self.argList = argList

    def evaluate(self):
        if self.argList is None:
            return [self.arg.name()]
        else:
            return [self.arg.name()] + self.argList.evaluate()
