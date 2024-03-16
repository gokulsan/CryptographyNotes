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
