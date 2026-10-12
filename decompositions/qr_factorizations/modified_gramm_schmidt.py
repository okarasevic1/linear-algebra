import numpy as np
from vector_projection import vector_projection
import scipy

# QR-factorization using Modified Gramm-Schmidt process (MGS)
def mgs_qr_factorization(init_matix:np.ndarray):

    # check whether the matrix is singular
    rows, cols = init_matix.shape

    if rows < cols:
        print('Matrix MUST be square or vertical matrix')
        return None

    index_col = 0
    modified_matrix = init_matix.copy() # we need original vector for R=Q^T*A
    U = np.zeros_like(init_matix, dtype=float)
    Q = init_matix.copy()

    # u_index = a_index 
    # a_index+1 = a_index+1 - Proj_u_index(a_index+1)
    for j in range(cols):

        if index_col == j:
            u = modified_matrix[:, index_col] # set already perpendicular vector 
            U[:, j] = u
            # normalize vector
            Q[:, j] = u / np.linalg.norm(u)

            for l in range(j+1, cols):
                vector = modified_matrix[:, l]
                vector = vector - vector_projection(u, vector)
                modified_matrix[:, l] = vector

        index_col += 1

    Q_t = Q.T
    # R = Q^T * A
    R = Q_t @ init_matix

    return Q, R

M = np.array([
    [1, 4, 6], 
    [5, 2, 0], 
    [0, 4, 1],
    [6, 7, 1],
], dtype=float)

q, r = mgs_qr_factorization(M)
print(q)
print(scipy.linalg.qr(M)[0])
print(r)
print(scipy.linalg.qr(M)[1])        