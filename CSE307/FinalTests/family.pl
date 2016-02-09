parent(pam, bob).
parent(bob, ann).
parent(tom, bob).
parent(bob, pat).
parent(tom, liz).
parent(pat, jim).
parent(liz, nauman).
male(tom).
male(jim).
male(bob).
female(pam).
female(pat).
female(ann).
female(liz).

mother(X,Y):-parent(X,Y), female(X).

father(X,Y):-parent(X,Y), male(X).

grandparent(X,Y):-parent(X,Z), parent(Z,Y).

grandmother(X,Y):-grandparent(X,Y), female(X).

grandfather(X,Y):-grandparent(X,Y), male(X).

sibling(X,Y):-parent(Z,X), parent(Z,Y), X\=Y.

cousin(X,Y):-parent(Z,X), parent(W,Y), sibling(Z,W).

greatgrandparent(X,Y):-parent(X,Z), grandparent(Z,Y).

greatgreatgrandparent(X,Y):-parent(X,Z), greatgrandparent(Z,Y).

ancestor(X,Y):-parent(X,Y).
ancestor(X,Y):-parent(X,Z), ancestor(Z,Y).
