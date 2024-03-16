## Timeline

- Guass and Lagrange uses lattices for the quadratic reciprocity and four square theorems.
- Minkowski advances the study of lattices
- Lenstra, Lenstra and Lovasz discover the famous “LLL” basis-reduction algorithm
- Ajtai shows a “worst-case to average-case reduction” for lattice problems, yielding a one-way function
- Hoffstein, Pipher and Silverman introduce the NTRU public-key encryption scheme and  digital signature scheme
- Innovations by Micciancio - Cyclic Lattices with O(n) complexity using ring Z(x)/(x^n-1)
- Creation of collision resistant hash functions based on the Micciancio scheme
- Lyubashevsky and Micciancio constructed a one-time signature where verificaiton can be done in O(n)

## Basics
- An n-dimensional lattice L is a discrete additive subgroup of R^(n).
- The rank k of a lattice L ⊂ R(^n) is the dimension of its linear span.
- When k = n, the lattice is said to be full rank
- Except for the degenerate case {0}, a lattice is always an infinite set.
- However, a basic fact is that a lattice can always be finitely represented by a basis.
- A basis B of a lattice L is a set of linearly independent vectors whose integer linear combinations generate the lattice.
- Any lattice can be obtained by applying some nonsingular linear transformation to the integer lattice
- Essentially, the existence of multiple lattice bases is what makes lattice-based cryptography possible!

## Hard Lattice Problems

Detecting Short Non Zero Lattice Vectors (Gap) SVP, SIVP, 
For poly(m), solving appears to require 2^ohm(m) time and space. 
Need clarity on the proof of these hard lattice problems.

## Short Integer Solution

Zsubscript(q), Superscript(n) is an n-dimensional integer vector modulo q
Goal is to find a non-trivial z1, ..., z(m) such that z(1)a(1)+ z(2)a(2)+...+z(m)a(m) = 0

Collission Resistant Hash Functions and Short Integer Solutions 
Set m > nlogq, define shrinking fA : {0,1} superscript(m) -> zQN
