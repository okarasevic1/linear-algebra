# Theory of the Cofactor Matrix

## Definition

Given a square matrix A of size n×n, the cofactor of the entry a_{ij} is

C_{ij} = (-1)^{i+j} M_{ij}

where M_{ij} is the determinant of the (n-1)×(n-1) matrix obtained by deleting row i and column j from A. The sign factor (-1)^{i+j} alternates in a checkerboard pattern.

## Cofactor Matrix

The cofactor matrix of A is the n×n matrix C whose entries are the cofactors C_{ij} of A:

C = [C_{ij}].

## Adjugate and Inverse

The adjugate (or classical adjoint) of A is the transpose of the cofactor matrix:

adj(A) = C^{T}.

When A is invertible, its inverse can be written using the adjugate:

A^{-1} = \frac{1}{\det(A)} adj(A).

This formula is useful for theoretical work and for matrices of small size.

## Properties

- If A is singular, det(A) = 0 and the matrix of cofactors still exists, but A^{-1} does not.
- The determinant of A can be computed by expanding along any row or column using cofactors:

\det(A) = \sum_{j=1}^{n} a_{ij} C_{ij} = \sum_{i=1}^{n} a_{ij} C_{ij}.

- The cofactor matrix relates to minors and signed minors: each entry is the signed minor for its position.

## Example

For a 3×3 matrix

A = \begin{pmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{pmatrix},

one cofactor is

C_{12} = (-1)^{1+2} \det\begin{pmatrix} d & f \\
g & i \end{pmatrix} = - (di - fg).

The full cofactor matrix is

C = \begin{pmatrix}
+\det\begin{pmatrix} e & f \\
h & i \end{pmatrix} & -\det\begin{pmatrix} d & f \\
g & i \end{pmatrix} & +\det\begin{pmatrix} d & e \\
g & h \end{pmatrix} \\
-\det\begin{pmatrix} b & c \\
h & i \end{pmatrix} & +\det\begin{pmatrix} a & c \\
g & i \end{pmatrix} & -\det\begin{pmatrix} a & b \\
g & h \end{pmatrix} \\
+\det\begin{pmatrix} b & c \\
e & f \end{pmatrix} & -\det\begin{pmatrix} a & c \\
d & f \end{pmatrix} & +\det\begin{pmatrix} a & b \\
d & e \end{pmatrix}
\end{pmatrix}.

## Use in Linear Algebra

The cofactor matrix is a key tool in:

- determinant expansion,
- computing matrix inverses by adjugate,
- understanding how each element of A contributes to det(A),
- deriving formulas for matrix derivatives and cofactors in theoretical work.

By organizing signed minors, the cofactor matrix bridges the matrix entries and determinant-based operations.
