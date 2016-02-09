# CSE 305 Homework 3

## Aditya Balwani, SBUID : 109353920

### Question 6.18

The projection of dependencies on ADE includes E → A, A → D and D → E however, B → E is not included anywhere hence this is not dependency-preserving.

Let r be a relation over ABCDE, and rAB, rBCD, rADE be its projections on the corresponding sets of attributes. We need to show that rAB JOIN rBCD JOIN rADE ⊆ r.

Every tuple can now be represented as abcde, where ab ∈ rAB, bcd ∈ rBCD and ade ∈ rADE.

The tuple ab must be a projection of some tuple abc<sub>1</sub>d<sub>1</sub>e<sub>1</sub>. ade must be a projection of some ab<sub>2</sub>c<sub>2</sub>de and bcd must be a projection of some a<sub>3</sub>bcde<sub>3</sub>

Now since,  B → E, e<sub>1</sub> = e<sub>3</sub>. Since E → A and since e<sub>1</sub> = e<sub>3</sub>, the tuples must agree on A as well, hence a = a<sub>3</sub>. Since A → D, d = d<sub>1</sub> and since D → E, e = e<sub>1</sub> = e<sub>3</sub>

Using all these, we have abc<sub>1</sub>d<sub>1</sub>e<sub>1</sub> = abcde, hence this is lossless

### Question 6.23

Provided FDs:
* BG → CD
* G → F
* CD → GH
* C → FG
* F → D

<div class="page-break"></div>

To convert this into a minimal cover, we first split all the right hand sides into FD with a single RHS :

* BG → C
* BG → D
* G → F
* CD → H
* CD → G
* C → F
* C → G
* F → D

Next we reduce the left hand sides. CD → H reduces to C → H and CD → G reduces to C → G (Which is elimintaed) and BG → D reduces to G → D. After this we elimnate all redundant FDs which leaves us with

* BG → C
* G → F
* C → H
* C → G
* F → D

This gives us the decomposition into 3NF :
(BGC; {BG → C, C → G}), (GF; {G → F}), (CGH ; {C → GH }), (FD; {F → D})

Out of this, (BGC; {BG → C, C → G}) is not a BCNF. A decomposition with respect to C → G gives us (CG; {C → G}) and (CB; {}) which makes it BCNF but it loses the BG → C FD
