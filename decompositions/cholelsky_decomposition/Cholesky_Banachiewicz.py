import numpy as np
import time

# Cholesky decomposition
# The formula to find the entries on the main diagonal: 
# L_ii = sqrt(A_ii - sum(L_in<i))
# The formula for subdiagonal
# L_ij = 1/L_ii * A_ij
def cholelsky(init_matrix:np.ndarray):

    # check whether it is square
    m, n = init_matrix.shape
    if m != n:
        print('Matrix is NOT sqaure')
        raise ValueError

    L = np.eye(m)

    for j in range(n):
        # find the diagonal entry
        s = np.sum([L[j, k]**2 for k in range(0, j)])
        
        diff = init_matrix[j, j] - s

        if diff < 0:
            print('Matrix is not Positive definite')
            return None

        l_jj = np.sqrt(diff)
        L[j, j] = l_jj
        inv_L_ij = l_jj ** -1 # 1/L_jj

        # calculate the entries under the diagonal 
        for i in range(j+1, m):
            A_ij = init_matrix[i, j]

            prod = 0
            for k in range(0, j):
                prod += np.prod(L[[j, i], k])

            l_ij = inv_L_ij * (A_ij - prod)
            L[i, j] = l_ij

    return L


# Testing ====================================================

def test(my_func, np_func, matrix_A:np.ndarray): 
    my_time_s = time.time()
    l = my_func(matrix_A)

    my_time_e = time.time()
    my_time_diff = my_time_e - my_time_s

    # print(f'My algo: \n', l)

    np_time_s = time.time()
    np_l = np_func(matrix_A)

    np_time_e = time.time()
    np_time_diff = np_time_e - np_time_s
    # print(f'Numpy algo: \n', np_l)

    # print(f'A=L*L^T: \n', l@l.T)
    print(f'My execution time: {my_time_diff};\nNumpy execution time: {np_time_diff};\nRatio: {my_time_diff / np_time_diff}')


