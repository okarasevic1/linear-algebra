import numpy as np
import scipy
from vector_projection import vector_projection


# QR-factorization using Classical Gramm-Schmidt orthogonalization
def qr_decomposition(init_matrix:np.ndarray): 

    # check whether it is square
    rows, cols = init_matrix.shape

    if rows != cols:
        print('Matrix is NOT sqaured!')
        return None

    index_col = 0
    U = np.zeros_like(init_matrix, dtype=float)
    Q = init_matrix.copy() # orthogonal matrix and ||v_k|| = 1

    for j in range(cols): 

        if index_col == 0:
            U[:, j] = init_matrix[:, j]
            Q[:, j] = U[:, j] / np.linalg.norm(U[:, j])
            index_col += 1
            continue

        vector = init_matrix[:, j]

        for k in range(0, j): 
            u = U[:, k]
            vector = vector - vector_projection(u, vector)

        U[:, j] = vector.copy()
        Q[:, j] = U[:, j] / np.linalg.norm(U[:, j])
        index_col += 1

    # A=QR -> Q^T*QR=Q^T*A -> R=Q^T*A
    Q_t = Q.T
    R = np.dot(Q_t, init_matrix)

    return Q, R
