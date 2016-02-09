# Aditya Balwani
# SBUID: 109353920

import sys
import tpg

from Nodes import *
from Exceptions import *
from Operations import *
from Statements import *

import CodeFormatter

# This is the TPG Parser that is responsible for turning our language into
# an abstract syntax tree.
class Parser(tpg.Parser):
    """
    token int "\d+" $ IntLiteral.IntLiteral $;
    separator space "\s";
    token variable '[A-Za-z][A-Za-z0-9]*' $ Variable.Variable $;
    token str '\"[^\"]*\"' $ StringLiteral.StringLiteral$;

    START/a -> block/a | (statementList/a $ a = Block.Block(a) $);

    block/a -> "{" statementList/a "}" $ a = Block.Block(a) $
    ;

    statementList/a -> statement/a statementList/b $ a = StatementList.StatementList(a, b) $
    | statement/a $ a = StatementList.StatementList(a) $
    ;

    expression/a -> orBool/a
    ;

    orBool/a -> andBool/a
    ( "or" andBool/b $ a = Boolean.Or(a,b) $ )*
    ;

    andBool/a -> notBool/a
    ( "and" notBool/b $ a = Boolean.And(a,b) $ )*
    ;

    notBool/a -> "not" notBool/a $ a = Boolean.Not(a) $
    | "not" comparison/a $ a = Noolean.Not(a) $
    | comparison/a
    ;

    comparison/a -> xor/a
    ( "\>" xor/b $ a = Comparison.Greater(a,b)
    | "\<" xor/b $ a = Comparison.Less(a,b)
    | "==" xor/b $ a = Comparison.Equal(a,b)
    )*;

    xor/a -> addsub/a
    ( "xor" addsub/b $ a = Xor(a,b) $)*
    ;

    statement/a -> (
    "while" expression/a block/b $ a = While.WhileStatement(a, b) $
    |"if" expression/a block/b $ a = If.IfStatement(a, b) $
    | variable/l "=" expression/r ";" $ a = Assign.Assign(l, r) $
    | variable/l indeces/i "=" expression/r ";" $ a = Assign.AssignList(l,i,r)$
    | "\(" variable/l "\)[ ]*=" expression/r ";" $ a = Assign.Assign(l, r) $
    | "\(" variable/l indeces/i "\)[ ]*=" expression/r ";" $ a = Assign.AssignList(l,i,r)$
    | "print\(" expression/e "\);" $ a = Print.Print(e) $
    | block/a
    )
    ;

    addsub/a -> muldiv/a
    ( "\+" muldiv/b $ a = Add.Add(a,b) $
    | "-" muldiv/b $ a = Subtract.Subtract(a,b) $
    )*
    ;

    muldiv/a -> parens/a
    ( "\*" parens/b $ a = Multiply.Multiply(a, b) $
    | "/"  parens/b $ a = Divide.Divide(a, b) $
    )* ;

    parens/a -> "\(" expression/a "\)" | literal/a
    ;

    literal/a -> index/a | int/a | variable/a | str/a | list/a;

    index/a -> indexable/a indeces/b $ a = List.Index(a,b) ;
    ;

    indexable/a -> list/a | str/a | variable/a
    ;

    indeces/a -> "\[" expression/a "\]" indeces/b $ a = List.Indeces(a,b) $
    | "\[" expression/a "\]" $ a = List.Indeces(a) $
    ;

    list/a -> "\[" elementList/a "\]" $ a = List.ListLiteral(a) $
    ;

    elementList/a -> expression/a "," elementList/b $ a = List.ElementList(a,b) $
    | expression/a $ a = List.ElementList(a) $
    ;
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

# code = CodeFormatter.formatCode(f)

code = f.read()

# print(code)

# For each line in f
try:
    # Try to parse the expression.
    node = parse(code)

    # Try to get a result.
    result = node.execute()

    # Print the representation of the result
# If an exception is thrown, print the appropriate error.
except tpg.Error:
    print("SYNTAX ERROR")
    # Uncomment the next line to re-raise the syntax error,
    # displaying where it occurs. Comment it for submission.
    # raise

except SemanticError.SemanticError:
    print("SEMANTIC ERROR")
    # Uncomment the next line to re-raise the semantic error,
    # displaying where it occurs. Comment it for submission.
    # raise

except SyntaxError.SyntaxError:
    print("SYNTAX ERROR")

f.close()
