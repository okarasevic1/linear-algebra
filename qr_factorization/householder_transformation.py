import numpy as np
import scipy

# QR-decomposition using Householder-transformation and Householder-matrix (H)
# H = I - 2 * v.v^T
def householder_transformation(init_matrix:np.ndarray): 

    # get the shape and check whether it is not a horizontal 
    # (number of columns is greater than number of rows)
    rows, cols = init_matrix.shape

    if rows < cols:
        print('Matrix is NOR square NEITHER vertical')
        return None, None

    R = init_matrix.copy()
    Q = np.eye(rows)

    for i in range (cols):

        # the last column doesn't need to be changed
        if i >= rows - 1:
            break

        x = R[i:, i]
        x_norm = np.linalg.norm(x)
        # skip if norm is equal t0 zero
        if x_norm == 0:
            continue

        alpha = -np.sign(x[0]) * x_norm
        y = np.zeros_like(x, dtype=float)
        y[0] = alpha
        u = x - y
        u_norm = np.linalg.norm(u)

        v = u/u_norm

        dim = len(x)

        H_sub = np.eye(dim) - (2 * np.outer(v, v))
        Q_n = np.block([
            [np.eye(i), np.zeros((i, dim))],
            [np.zeros((dim, i)), H_sub]
        ])

        R = Q_n @ R
        Q = Q @ Q_n.T

    return Q, R