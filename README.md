# Linear Algebra (WIP)
## Idea:
The main idea of this project is to develop an algorithmic understanding of matrix operations. You can find Gilbert Strang's video lectures [here](https://youtube.com/playlist?list=PL49CF3715CB9EF31D&si=wb4o5ifcZoVbPUre).
However, some algorithms are computationally inefficient for large matrices. For example, calculating the determinant of a 10×10 matrix using the cofactor expansion method takes approximately 7 seconds on my computer. **But what if our dataset contains 2 million rows and 20 features?**
**The answer is to use more efficient algorithms for matrix operations or modified versions of the original methods.**
In other words, what works well for humans doesn't necessarily work efficiently for computers.


### Tasks

#### 1. Linear Algebra Fundamentals
- [x] Vectors and vector norms
- [x] Matrices and matrix operations
- [x] Orthogonal and orthonormal bases
- [x] Classical Gram-Schmidt orthogonalization
- [x] Modified Gram-Schmidt orthogonalization
- [x] Determinant calculation using cofactor expansion
- [x] Determinant calculation using Gaussian elimination

#### 2. Matrix Decompositions
- [x] LU decomposition: A = LU
- [x] Cholesky decomposition: A = LLᵀ
- [x] QR decomposition: A = QR
- [x] Householder reflections
- [x] Givens rotations

#### 3. Singular Value Decomposition
- [ ] Singular Value Decomposition (SVD)

#### 4. Eigenvalues and Eigenvectors
- [x] Eigenvalue computation using the QR algorithm
- [x] Improved QR algorithms for eigenvalue computation
- [ ] Francis implicit double-shift QR algorithm

#### 5. Optimization and Stochastic Processes
- [x] Least Squares and Linear Regression using normal equations
- [ ] Least Squares optimization using SVD
- [x] Markov chains and steady-state distributions

#### 6. Practical Applications
- [ ] Market crash correlation analysis using eigenvalues
- [ ] Principal Component Analysis (PCA)