import numpy as np

# Hessenberg Form - all entries are zero below first subdiagonal
# [1 2 5 8]
# [4 1 7 2]
# [0 8 5 2]
# [0 0 1 2]

# Householder reflections can be used 
# for gettig the Hessenberg Form
def householder_transfromation_adapted(init_matrix:np.ndarray, calc_q=False):

    # check the form of the matrix
    m, n = init_matrix.shape
    if m != n:
        print('Matrix is NOT sqaured')
        return None, None

    R = init_matrix.copy()
    Q = np.eye(m)

    for i in range(n):

        # the last column can stay the same
        if i >= n - 2:
            break

        x = R[i+1:, i]
        x_norm = np.linalg.norm(x)

        # skip if the L2-norm is 0
        if x_norm == 0:
            continue

        sign = -1.0 if x[0] >= 0 else -1.0
        alpha = sign * x_norm

        u = x.copy()
        u[0] -= alpha
        u_norm = np.linalg.norm(u)
        # v is normalized vector u
        v = u / u_norm

        dim = len(x)

        H = np.eye(dim) - 2 * np.outer(v, v)
        Q_n = np.eye(n)
        Q_n[i+1:, i+1:] = H

        R = Q_n @ R @ Q_n.T # A = H * A * H.T
        Q = Q @ Q_n


    H = np.where(np.abs(R) < 1e-14, 0.0, R)

    return H, Q if calc_q else H
