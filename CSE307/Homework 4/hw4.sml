(*
  Aditya Balwani. SBU ID : 109353920
*)

(*Get Row from a list.
  Arguments :
    L -- List of List
    a -- Index of row*)
fun getRow(L, a:int) = if L=[] then []
  else if a=0 then hd(L)
  else getRow(tl(L),a-1)

(*--------------------------------------------------------------------------------------------------*)

(*Get element from a row
  Arguments :
    L -- List
    a -- Index of element to be retrieved*)
fun getElementFromRow(L, a:int) = if(L=[]) then 0
  else if a=0 then hd(L)
  else getElementFromRow(tl(L),a-1)

(*--------------------------------------------------------------------------------------------------*)

(*Get element from a 2D Array
  Arguments :
    sudoku -- The 2D Array
    row -- Row of element to be retrieved
    col -- Col of element to be retrieved
*)
fun getElement(sudoku,row,col) = getElementFromRow(getRow(sudoku,row),col)

(*--------------------------------------------------------------------------------------------------*)

(*Helper for the insert method, inserts and element into a row
  Arguments :
    num -- The number to be inserted
    rowList -- The row in which element will be inserted
    col -- The index at which element would be inserted int the row
*)
fun insertHelper(num,rowList,col) = if col = 0  then num::tl(rowList)
  else hd(rowList) :: insertHelper(num,tl(rowList),col-1)

(*--------------------------------------------------------------------------------------------------*)

(*Inserts an element at the specified position in a 2D Array
  Arguments :
    num -- the number to be inserted
    sudoku -- The 2D Array
    row -- X coordinate of insert position
    col -- Y coordinate of insert position*)
fun insertElement(num,sudoku,row,col) = if row = 0 then insertHelper(num, hd(sudoku),col) :: tl(sudoku)
  else hd(sudoku)::insertElement(num,tl(sudoku),row-1,col)

(*--------------------------------------------------------------------------------------------------*)

(*Check if element fits at specified position in its row and column
  Arguments :
    i -- the index which is being tested in the row and col.*)
fun checkValidRowAndCol(num,sudoku,row,col,i) = if i = 6 then true
  else if getElement(sudoku,i,col) = num then false
  else if getElement(sudoku,row,i) = num then false
  else checkValidRowAndCol(num,sudoku, row, col, i+1)

(*--------------------------------------------------------------------------------------------------*)

(*Checks if element fits at specified position. Checks the box and then call the
  method that checks the row and column
  Arguments : Num, sudoku, row, col, and all the indices required to do the math*)
fun checkValidHelper(num,sudoku,row,col,secRow:int,secCol:int,row1:int,col1:int,col2:int) =
  if getElement(sudoku,row1+secRow,col1+secCol) = num then false
  else if getElement(sudoku,row1+secRow,col1+secCol) = num then false
  else checkValidRowAndCol(num,sudoku,row,col,0)

(*--------------------------------------------------------------------------------------------------*)

(*Checks if the specified number fits at specified position. Calculetes all the required
  indices and then calls the helper methods which checks everything*)
fun checkValid(num,sudoku,row,col) = checkValidHelper(num,sudoku,row,col,2*floor(real(row)/2.0),3*floor(real(col)/3.0),(row+1) mod 2,(col+2) mod 3, (col+4) mod 3)

(*--------------------------------------------------------------------------------------------------*)

(*Checks if the sudoku is valid*)
fun solveSudoku(i,sudoku,row,col) = if i = 0 then (
    (* Check if already at end of sudoku *)
    if row = 6 then sudoku
    (*Check if position is empty, if it is, move onto the next element*)
    else if not(getElement(sudoku,row,col) = ~1) then (
      (* If at end of row, move on to next row else continue in row *)
      if col = 5 then solveSudoku(0,sudoku,row+1,0)
      else solveSudoku(0,sudoku,row,col+1)
    )
    else solveSudoku(1,sudoku, row, col)
  )
  (* Iterate through all possibilties at position, and check if they are valid. *)
  else (
    if checkValid(i,sudoku,row,col) then (
      if col = 5 then solveSudoku(0, insertElement(i,sudoku,row,col), row+1, 0)
      else solveSudoku(0,insertElement(i,sudoku,row,col), row, col+1)
    )
    else solveSudoku(i+1,sudoku,row,col)
  )

(* Check if input sudoku is a valid 6x6 sudoku. Checks individual rows for length 6 *)
fun isValidEmptyHelper(sudoku) = if sudoku = [] then true
  else if not(length(hd(sudoku)) = 6) then false
  else isValidEmptyHelper(tl(sudoku))

(* Check if input sudoku is a valid 6x6 sudoku. Checks the number of rows and
  then moves on to columns*)
fun isValidEmpty(sudoku) = if not(length(sudoku) = 6) then false
  else isValidEmptyHelper(sudoku)

fun hw4(sudoku) = solveSudoku(0, sudoku, 0, 0)

val SolvedSudoku = hw4([[2,1,~1,~1,4,3],[~1,~1,~1,~1,~1,~1],[~1,~1,6,2,~1,~1],[~1,~1,3,4,~1,~1],[~1,~1,~1,~1,~1,~1],[3,4,~1,~1,5,6]])
