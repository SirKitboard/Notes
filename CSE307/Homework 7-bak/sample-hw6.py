class Node(object):
    """
    A base class for nodes. Might come in handy in the future.
    """
    def execute(self):
        """
        Executes this node.
        """
        raise SemanticError()
    def evaluate(self):
        """
        Evaluates this node for an r-value.
        """
        raise SemanticError()
    def location(self):
        """
        Evaluates this node for a location.
        """
        raise SemanticError()
class Variable(Node):
    """
    A node representing access to a variable.
    """
    def __init__(self, name):
        self.name = name
# Statements.
class Block(Node):
    """
    A node representing the block statement.
    """
    def __init__(self):
        self.statements = [ ]
class If(Node):
    """
    A node representing the if statement.
    """
    def __init__(self, expression, statement):
        self.expression = expression
        self.statement = statement
class While(Node):
    """
    A node representing the while statement.
    """
    def __init__(self, expression, statement):
        self.expression = expression
        self.statement = statement
class Assign(Node):
    """
    A node representing the assignment statement.
    """
    def __init__(self, left, right):
        self.left = left
        self.right = right
class Print(Node):
    """
    A node representing the print statement.
    """
    def __init__(self, expression):
        self.expression = expression
    def execute(self):
        print repr(self.expression.evaluate())
class Parser(tpg.Parser):
    """
    token variable '[A-Za-z][A-Za-z0-9]*' Variable;
    START/a -> statement/a
    ;
    statement/a ->
     "if" "\(" expression/e "\)" statement/s $ a = If(e, s) $
    | "while" "\(" expression/e "\)" statement/s $ a = While(e, s) $
    | expression/l "=(?!=)" expression/r ";" $ a = Assign(l, r) $
    | "print\(" expression/e "\)” “;" $ a = Print(e) $
    );
...
    """
parse = Parser()
f = file(sys.argv[1], "r")
code = f.read()
f.close()
try:
    # Try to parse the expression.
    node = parse(code)
    # Execute the node.
    node.execute()
# If an exception is thrown, print the appropriate error.
except tpg.Error:
    print "SYNTAX ERROR"
    # Uncomment the next line to re-raise the syntax error,
    # displaying where it occurs. Comment it for submission.
    # raise
except SemanticError:
    print "SEMANTIC ERROR"
    # Uncomment the next line to re-raise the semantic error,
    # displaying where it occurs. Comment it for submission.
    # raise
