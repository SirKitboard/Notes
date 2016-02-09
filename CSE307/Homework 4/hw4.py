#pylint: disable=W0312,C

# Aditya Balwani, SBUID : 109353920

# Sudoku Solver
import fileinput


def checkValid(num, sudoku, row, col):
    """Check if the number fit at the specified position in a sudoku.

    Key arguments:
        num -- Integer. The number being inserted into the sudoku
        sudoku -- Array of Arrays. The sudoku in which the number will be inserted
        row -- Integer. The row in which num will be inserted
        col -- INteger. the column in which the num will be inserted

    Returns:
        Boolean -- True if valid
    """

    # Calculate all the indices
    secRow = 2*int(row/2)
    secCol = 3*int(col/3)
    row1 = (row+1)%2
    col1 = (col+2)%3
    col2 = (col+4)%3

    #Check if num exists in row or column
    for i in range(0,6):
        if sudoku[i][col] == num:
            return False
        if sudoku[row][i] == num:
            return False

    # Check if num exists in box
    if sudoku[row1+secRow][col1+secCol] == num:
        return False
    if sudoku[row1+secRow][col2+secCol] == num:
        return False
    return True


def sudokuHelper(sudoku,row,col) :
    """The method that solves the sudoku.
    It uses recursive back tracking to insert a number into the sudoku and then check if its valid.
    If something is invalid then it backtracks up the branch and tries different values.

    Key arguments:
        sudoku : The sudoku to be solved
        row : the row currently being tested
        col : the column currently being tested
    """

    # Check if already at end of sudoku
    if row == 6:
        return True

    # Check if position is empty, if it is, move onto the next element
    if sudoku[row][col] != -1:
        # If at end of row, move on to next row else continue in row
        if(col == 5):
            if sudokuHelper(sudoku,row+1,0):
                return True
        elif sudokuHelper(sudoku, row, col+1):
            return True
        return False

    # Iterate through all possibilties at position, and check if they are valid.
    for num in range(1,7):
        if checkValid(num, sudoku, row, col):
            sudoku[row][col] = num
            if(col == 5):
                if sudokuHelper(sudoku,row+1,0):
                    return True
            elif sudokuHelper(sudoku, row, col+1):
                return True
            sudoku[row][col] = -1

def isValidEmpty(sudoku):
    """ Check if input sudoku is a valid 6x6 sudoku

    Key Arguments :
        sudoku : the sudoku to be tested
    Return :
        Boolean. True if valid.
    """
    if len(sudoku) != 6:
        return False
    for row in sudoku:
        if len(row) != 6:
            return False
        for val in row:
            if val != -1 and not(val > 0 and val < 7):
                return False
    return True


def main() :
    sudokuGrid = []
    # Read all the lines in the file and make a sudoku out of it
    for row in fileinput.input():
        #print(row)
        row=row.strip().split(" ")
        if(len(row) == 1):
            continue
        intArray = []
        for num in row:
            if num == '-':
                intArray.append(-1)
            else:
                intArray.append(int(num))
        sudokuGrid.append(intArray)
    # Solve if valid
    if(isValidEmpty(sudokuGrid)):
        print("Solving sudoku... \n")
        sudokuHelper(sudokuGrid, 0, 0)
        print("Solution : \n")
        for row in sudokuGrid:
            print(row)
    else:
        print("Invalid sudoku inserted")

main()
