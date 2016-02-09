# CSE 307 Homework 1

## Problem 1.1 :

Using the example of Java : 
a) Hi! //Invalid Tokens
b) float a //no semicolon
c) { int x = 0; int x = 5; } //Double Declaration of int
d) Person person = new Person(); (Student) person; //Casting parent to child
e) array[randomMethod()] //Could create index out of bound

## Problem 1.4
The given program generates the correct output with the following modification : 

    while (i != j && i > 0 && j > 0) {
        if (i > j) i = i % j;
        else j = j % i;
    }
    if(i != 0) {
        printf("GCD = %d\n",i); 
    }
    else {
        printf("GCD = %d\n",j);
    }

Version 2 is faster when the the difference between the 2 numbers is small, but version 1 is faster for a bigger difference.

## Problem 1.6
Since make uses the timestamp of the file to decide whether a file needs to be recompiled, trivial changes like adding comments will also cause the timestamp to change and cause unneeded compilations.
Also, since its the programmers job to declare the dependencies, if they are not delared properly, the program will not recompile even if the dependency is changed