from Nodes import Node
import glob

class Function(Node.Node):
    """
    The function node
    """

    def __init(self, a):
        print('HIII')
        print(a)

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
        self.arg = arg
        self.argList = argList

    def evaluate(self):
        if self.argList is None:
            return [self.arg.evaluate()]
        else:
            return [self.arg.evaluate()] + self.argList.evaluate()

    def getNames(self):
        if self.argList is None:
            return [self.arg.getName()]
        else:
            return [self.arg.getName()] + self.argList.getNames()

class CallFunction(Node.Node):
    """
    HI
    """

    def __init__(self, function, arguments = None):
        self.function = function
        self.arguments = arguments

    def evaluate(self):
        try:
            self.function.execute(self.arguments.evaluate())
        except ReturnException as e:
            return e.getValue()

    def execute(self):
        # print(self.arguments.evaluate())
        self.function.execute(self.arguments.evaluate())

class ReturnException(Exception):
    """
    This is the class of the exception that is raised when a semantic error
    occurs.
    """
    def __init__(self, value):
        super(ReturnException, self).__init__("")
        self.value = value

    def getValue(self):
        return self.value
