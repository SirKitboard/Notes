# pylint: disable=W,C

# Aditya Balwani, SBUID : 109353920

import sys
import tpg

im

variables = {}

# class VariableManager:
#     def __init__(self):
#         self.variables = {}
#
#     def addVariable(self, key, value):
#         self.variables[key] = value
#
#     def getVariable(self, key):
#         if key in self.variables.keys():
#             return self.variables

class SemanticError(Exception):
    """
    This is the class of the exception that is raised when a semantic error
    occurs.
    """

# These are the nodes of our abstract syntax tree.
class Node(object):
    """
    A base class for nodes. Might come in handy in the future.
    """

    def evaluate(self):
        """
        Called on children of Node to evaluate that child.
        """
        raise Exception("Not implemented.")

class IntLiteral(Node):
    """
    A node representing integer literals.
    """

    def __init__(self, value):
        # print("INT")
        self.value = int(value)

    def evaluate(self):
        # print("EV INT")
        return self.value

class StringLiteral(Node):
    """
    A node representing String literals
    """

    def __init__(self,value):
        # print("STR")
        self.value = str(value)
        self.value = self.value[1:len(self.value)-1]
        # print(self.value);


    def evaluate(self):
        # print("EV STR")
        return self.value

class ListLiteral(Node):
    """
    A node representing List literals
    """

    def __init__(self, values):
        # print("LIST", values)
        values = str(values)[1:len(str(values))-1]
        valArray = str(values).split(",")
        parsed = []
        try:
            for element in valArray:
                # print("list element", element)
                tempParse = Parser()
                parsed.append(tempParse(element))
        except tpg.Error:
            print("SYNTAX ERROR")
        self.values = parsed

    def evaluate(self):
        # print("EV LIST")
        tempArr = []
        for element in self.values:
            tempArr.append(element.evaluate())
        return tempArr

# class CreateVariable(Node):
#     def __init__(self, key, value):
#         variables[key] =

class Add(Node):
    """
    A Node representing addition
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if type(left) != type(right):
            raise SemanticError()
        elif not isinstance(left, int) and not isinstance(left, str):
            raise SemanticError()
        return left + right

class Subtract(Node):
    """
    A Node representing subtraction
    """

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError()
        if not isinstance(right, int):
            raise SemanticError()
        return left - right

class Multiply(Node):
    """
    A node representing multiplication.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError()
        if not isinstance(right, int):
            raise SemanticError()
        return left * right

class Divide(Node):
    """
    A node representing division.
    """

    def __init__(self, left, right):
        # The nodes representing the left and right sides of this
        # operation.
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError()
        if not isinstance(right, int):
            raise SemanticError()
        if right == 0:
            raise SemanticError()
        return int(left / right)

class Equal(Node):
    """
    A node represening the boolean Equal
    """

    def __init__(self, a, b):
        self.left = a
        self.right = b

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError()
        if not isinstance(right, int):
            raise SemanticError()
        return 1 if left == right else 0

class Greater(Node):
    """
    A node represening the boolean Equal
    """

    def __init__(self, a, b):
        self.left = a
        self.right = b

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError()
        if not isinstance(right, int):
            raise SemanticError()
        return 1 if left > right else 0

class Less(Node):
    """
    A node represening the boolean Equal
    """

    def __init__(self, a, b):
        self.left = a
        self.right = b

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError()
        if not isinstance(right, int):
            raise SemanticError()
        return 1 if left < right else 0



class Not(Node):
    """
    A node representing the boolean NOT
    """
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        value = self.value.evaluate()
        if not isinstance(value, int):
            raise SemanticError()
        return 1 if (value == 0) else 0

class And(Node):
    """
    A node representing the boolean and
    """

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError()
        if not isinstance(right, int):
            raise SemanticError()
        return 1 if (left!=0) & (right!=0) else 0

class Xor(Node):
    """
    A node representing the boolean and
    """

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError()
        if not isinstance(right, int):
            raise SemanticError()
        return left ^ right

class Or(Node):
    """
    A node representing the boolean Or
    """

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if not isinstance(left, int):
            raise SemanticError()
        if not isinstance(right, int):
            raise SemanticError()
        return 1 if (left!=0) | (right!=0) else 0

class Index(Node):
    """
    A node representing the List Index
    """

    def __init__(self, val, index):
        # print("INDEX")
        self.val = val
        self.index = index

    def evaluate(self):
        left = self.val.evaluate()
        right = self.index.evaluate()
        if not isinstance(left, str) and not isinstance(left, list):
            raise SemanticError()
        if not isinstance(right, list) or len(right) != 1:
            raise SemanticError()
        if len(left) < right[0] + 1:
            raise SemanticError()
        return left[right[0]]

# This is the TPG Parser that is responsible for turning our language into
# an abstract syntax tree.
class Parser(tpg.Parser):
    """
    token int "\d+" IntLiteral;
    token str '\"[^\"]*\"' StringLiteral;
    token list '\[*\]' ListLiteral;
    separator space "\s";

    START/a -> expression/a
    ;

    expression/a -> orBool/a | parens/a
    ;

    orBool/a -> andBool/a
    ( "or" andBool/b $ a = Or(a,b) $ )*
    ;

    andBool/a -> notBool/a
    ( "and" notBool/b $ a = And(a,b) $ )*
    ;

    notBool/a -> ("not") comparison/a $ a = Not(a) $ | comparison/a
    ;

    notBool/a -> "not" notBool/a $ a = Not(a) $
    | "not" comparison/a $ a = Not(a) $
    | comparison/a
    ;

    comparison/a -> xor/a
    ( "\>" xor/b $ a = Greater(a,b)
    | "\<" xor/b $ a = Less(a,b)
    | "==" xor/b $ a = Equal(a,b)
    )*;

    xor/a -> addsub/a
    ( "xor" addsub/b $ a = Xor(a,b) $)*
    ;

    addsub/a -> muldiv/a
    ( "\+" muldiv/b $ a = Add(a,b) $
    | "-" muldiv/b $ a = Subtract(a,b) $
    )*
    ;

    muldiv/a -> parens/a
    ( "\*" parens/b $ a = Multiply(a,b) $
    | "/" parens/b $ a = Divide(a,b)
    )*
    ;

    parens/a ->  "\(" expression/a "\)" | literal/a
    ;

    literal/a -> (str/a list/b $ a = Index(a,b) $ ) | (list/a list/b $ a = Index(a,b) $) | int/a | str/a | list/a;
    """

# Make an instance of the parser. This acts like a function.
parse = Parser()

# This is the driver code, that reads in lines, deals with errors, and
# prints the output if no error occurs.

# Open the file containing the input.
try:
    f = open(sys.argv[1], "r")
except(IndexError, IOError):
    f = open("input1.txt", "r")

code = Code

# For each line in f
for l in f:
    try:
        # Try to parse the expression.
        node = parse(l)

        # Try to get a result.
        result = node.evaluate()

        # Print the representation of the result.
        print(repr(result))

    # If an exception is thrown, print the appropriate error.
    except tpg.Error:
        print("SYNTAX ERROR")
        # Uncomment the next line to re-raise the syntax error,
        # displaying where it occurs. Comment it for submission.
        # raise

    except SemanticError:
        print("SEMANTIC ERROR")
        # Uncomment the next line to re-raise the semantic error,
        # displaying where it occurs. Comment it for submission.
        # raise

f.close()
