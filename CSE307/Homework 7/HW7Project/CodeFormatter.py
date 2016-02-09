# Aditya Balwani
# SBUID: 109353920

import sys
from Exceptions import SyntaxError


def formatCode(code):
    indentStack = []
    savedCode = ""
    for i, line in enumerate(code):
        if(line.strip() != ""):
            numSpaces = countSpaces(line)
            if(numSpaces % 4 != 0):
                print("Incorrect indentation on line ", i+1, "\n", line)
                return("SYNTAX ERROR")
            if(len(indentStack) != numSpaces/4):
                if(len(indentStack) > numSpaces/4):
                    toStrip = len(indentStack) - int(numSpaces/4)
                    braces = ''
                    for i in range(0, toStrip):
                        braces += '}'
                        indentStack.pop()
                    line = braces + line
                    # line = '}' + line
                    # indentStack.pop()
                else:
                    toInsert = int(numSpaces/4) - len(indentStack)
                    braces = ''
                    for i in range(0, toInsert):
                        braces += '{'
                        indentStack.append(' ')
                    line = braces + line
            savedCode = savedCode + line
    if len(indentStack) != 0:
        braces = ''
        for i in range(0, len(indentStack)):
            braces += '}'
            indentStack.pop()
        savedCode = savedCode + braces

    return savedCode


def countSpaces(line):
    return len(line) - len(line.lstrip(' '))
