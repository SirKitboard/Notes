(* Function 1 : Find last element of list *)
fun one(L) = if tl(L)=nil then hd(L)
else one(tl(L));
one([1,2,3,4,5]);

(* Function 2 : Find kth element of list *)
fun two(a:int, L) =  if a=0 then hd(L)
else two(a-1,tl(L));

(* Function 3 : Reverse List *)
fun three(L) = if L=nil then nil
else three(tl(L)) @ [hd(L)];

(* Function 4 : Check if list is palindrome *)
fun four(a) = if a=nil then true
else if tl(a)=nil then true
else if a=three(a) then true
else false;

(*Function 10 : Create list of specified range*)
fun ten(a,b) = if a=b then [b]
else [a] @ ten(a+1,b);
