# CSE337 Homework 1

## Aditya Balwani, SBUID: 109353920

### Question 3 output:

```
#Output1
>>> a = [1,2]
>>> b = [a,3]
>>> c = b[:]
>>> a[0]=7
>>> b[1]=8
>>> c
[[7, 2], 3]
>>> import copy
>>> c = copy.deepcopy(b)
>>> c
[[7, 2], 8]
>>> a[0]=5
>>> c
[[7, 2], 8]


#Output2

>>> import copy
>>> a = [[[1,2,3],2],4]
>>> b = copy.deepcopy(a)
>>> a[0][0][2] = 11
>>> a[0][1] = 5
>>> b
[[[1, 2, 3], 2], 4]
>>> a
[[[1, 2, 11], 5], 4]
>>> exit()

```


### Question 4:

1. &nbsp;
  1. if n=2 and r=1 then the condition n>r will succeed and break the loop, printing out "Better luck next time"
  2. if n=1 and r=1 then the condition n==r will succeed and continue the loop without printing "x"
  3. if n=2 and r=2 then the condition n==r will succeed and continue the loop without printing "x" but since thats the last iteration, it will print out "Wow you are lucky"
  4. if n=0 and r=2 then the condition n>r will fail and so "x" will be printed out and the next iteration of loop will start
2. In general, "Wow you are lucky" will be printed if r is less than or equal to n for all three iterations of the loop
