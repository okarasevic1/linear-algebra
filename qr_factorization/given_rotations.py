import numpy as np
import numpy.linalg as la

# zero out the entries by using Given Rotations
# Given Rotation 2x2 unitary matrix
def given_rotaions(size, x, y, indexes:list):

    G = np.eye(size, dtype=float)
    i, j = indexes[0], indexes[1]

    r = np.sqrt(np.power(x, 2) + np.power(y, 2))

    # it will give us two by two vector 
    # with L2-norm on it's main entry and all other zero's
    c = x / r
    s = y / r

    G[j, j] = c
    G[i, i] = c
    G[i, j] = -s 
    G[j, i] = s 

    return G


def qr_given_r(init_matrix:np.ndarray):

    # check the form
    m, n = init_matrix.shape

    R = init_matrix.copy().astype(float)
    Q = np.eye(m, dtype=float)
    tolerance = 1e-14

    for j in range(n):

        for i in range(j+1, m):
            el1 = R[j, j] # element on the diagonal
            el2 = R[i, j] # elements below the diagonal

            # if the value is zero or very close to it -> skip
            if el2 == 0 or np.abs(el2) < tolerance:
                continue

            G = given_rotaions(m, el1, el2, [i, j])
            R = G @ R
            Q = Q @ G.T

    return Q, R
