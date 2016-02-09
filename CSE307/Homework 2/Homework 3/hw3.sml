fun lengthString(L) = Int.toString(length(L));

(* Function 1 : Find last element of list
  Get tail of list until only one element left*)
fun one(L) = if L=nil then 0
else if tl(L)=nil then hd(L)
else one(tl(L));

(*------------------------------------------------------------------------------------------------------------*)

(* Function 2 : Find kth element of list
  Get Tail of list and decrement k until k is 0 or list is empty*)
fun two(a:int, L) = if(L=nil) then 0
else if a=0 then hd(L)
else two(a-1,tl(L));

(*------------------------------------------------------------------------------------------------------------*)

(* Function 3 : Reverse List
  Append head of list to tail until end of list recursively *)
fun three(L) = if L=nil then nil
else three(tl(L)) @ [hd(L)];

(*------------------------------------------------------------------------------------------------------------*)

(* Function 4 : Check if list is palindrome
  Reverse list using function three and then check for equality *)
fun four(a) = if a=nil then true
else if tl(a)=nil then true
else if a=three(a) then true
else false;

(*------------------------------------------------------------------------------------------------------------*)

(* Function 5 : Flatten list
  Take head and append to root list
  NOTE: Only works for 2 level lists *)
fun five(L) = if L = [] then []
else hd(L) @ five(tl(L));

(*------------------------------------------------------------------------------------------------------------*)

(* Function 6 : Remove duplicates
  If head of list is equal to next, then all this method again on just the tail*)
fun six(L) = if L=[] then []
else if length(L)=1 then L
else if hd(L)=hd(tl(L)) then six(tl(L))
else [hd(L)] @ six(tl(L));

(*------------------------------------------------------------------------------------------------------------*)

(* Function 7 Helper : Parameters : Result List (initially empty), List to group, Temp list
 If list is empty, check if temp is empty and return temp + result
 else if temp is empty, add first element of List to temp
 else if first element of list is equal to first of temp, add element to temp and remove from list
 else concactonate temp with result and call again*)
fun sevenHelper(a,b,c) = if b=nil then if c = nil then a else c::a
else if c=[] then sevenHelper(a,tl(b),[hd(b)])
else if hd(b)=hd(c) then sevenHelper(a,tl(b),hd(b)::c)
else sevenHelper(c::a,tl(b),[hd(b)]);

(* Function 7 : Group consecutive identical elements*)
fun seven(L) = sevenHelper([],three(L),[]);

(*------------------------------------------------------------------------------------------------------------*)

(* Function 8 Helper : Run length on ever group of element
  and create a new list with length and element *)
fun eightHelper(a,b) = if b=nil then a
else eightHelper([length(hd(b)),hd(hd(b))]::a,tl(b));

(* Function 8 : Length encode list
  Uses SevenHelper to group elements*)
fun eight(L) = eightHelper([],sevenHelper([],L,[]));

(*------------------------------------------------------------------------------------------------------------*)

(* Function 9 helper :
  Parameters : Result list, List, count (initially -1), element to count (initially -1)
  If list is empty, return result
  else if count is -1 then call method with result, and head of list as count and elememt
  else if count is 0, then call method with result, tail of list and -1,-1
  else append element to result and decrememnt count*)
fun nineHelper(a,b,count,element) = if b = nil then a
else if count = ~1 then nineHelper(a,b,hd(hd(b)),hd(tl(hd(b))))
else if count = 0 then nineHelper(a,tl(b),~1,~1)
else nineHelper(a @ [element], b, count-1, element)

(*Function 9 : Decode length encoded list*)
fun nine(L) = nineHelper([],L,~1,~1);

(*------------------------------------------------------------------------------------------------------------*)

(*Function 10 : Create list of specified range*)
fun ten(a,b) = if a=b then [b]
else [a] @ ten(a+1,b);

(*--------------------------------------------Function Call---------------------------------------------------*)

one([1,2,3,4,5]);
two(2,[1,2,3,4,5]);
three([1,2,3,4,5,6]);
four([1,2,3,2,1]);
five([[1,2,3],[1,2,3,4],[6,7,8,9]]);
six([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,5,5,6,6,6,7]);
seven([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,5,5,6,6,6,7]);
eight([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,5,5,6,6,6,7]);
nine([[4,1],[4,2],[4,3],[3,4],[4,5],[3,6],[1,7]]);
ten(1,10);
