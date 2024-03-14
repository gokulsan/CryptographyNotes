## Timeline

- Seminal work of Ajtai - Lattices with O(n^2) complexity
- Innovations by Micciancio - Cyclic Lattices with O(n) complexity using ring Z(x)/(x^n-1)
- Creation of collision resistant hash functions based on the Micciancio scheme
- Lyubashevsky and Micciancio constructed a one-time signature where verificaiton can be done in O(n)
- 

## Hard Lattice Problems

Detecting Short Non Zero Lattice Vectors (Gap) SVP, SIVP, 
For poly(m), solving appears to require 2^ohm(m) time and space. 
Need clarity on the proof of these hard lattice problems.

## Short Integer Solution

Zsubscript(q), Superscript(n) is an n-dimensional integer vector modulo q
Goal is to find a non-trivial z1, ..., z(m) such that z(1)a(1)+ z(2)a(2)+...+z(m)a(m) = 0

Collission Resistant Hash Functions and Short Integer Solutions 
Set m > nlogq, define shrinking fA : {0,1} superscript(m) -> zQN
