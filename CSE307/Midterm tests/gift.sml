(*fun pyramidNumHelper(num, n) = if n = 1 then num
else concat([num, pyramidNumHelper(num, n-1)]);

fun pyramidSpaceHelper(n) = if n = 1 then " "
else concat([" ", pyramidSpaceHelper(n-1)]);

fun pyramidHelper(num, n, i) = if(i = n) then concat([pyramidNumHelper(num, n),"\n"])
else concat([pyramidSpaceHelper(n-i),pyramidNumHelper(num,i),"\n",pyramidHelper(num,n,i+1)]);

fun pyramid(a:int) = print(pyramidHelper(Int.toString(a),a,1));
*)
fun makeBoxHelper(num, n) = if n = 1 then num
  else concat([num,makeBoxHelper(num,n-1)]);

fun makeBox(num, n, i) = if i = n then concat(["|",makeBoxHelper(num, n),"|\n"])
  else concat(["|",makeBoxHelper(num, n),"|\n",makeBox(num,n,i+1)]);

fun makeTopperHelper(n) = if n = 0  then ""
else concat(["-",makeTopperHelper(n-1)]);

fun makeTopper(n) = concat(["/",makeTopperHelper(n),"\\ \n"]);

fun makeBottom(n) = concat(["\\",makeTopperHelper(n),"/\n"]);

fun boxHelper(num, n) = concat([makeTopper(n),makeBox(num, n, 1),makeBottom(n)]);

fun box(a:int) = print(boxHelper(Int.toString(a),a));
