import numpy as np

import sys
sys.path.append('/Users/okarasevic1/Documents/Linear Algebra /qr_factorization')
from householder_transformation import householder_transformation as qr
import time

def shift_makesimiliar(B, eigen):
    
    m, n = B.shape
    shift_matrix = eigen * np.eye(m)

    B = B - shift_matrix
    Q, R = qr(B)

    B_n = R @ Q 
    B_n = B_n + shift_matrix
    return B_n


def eigenvalues_shift_qr(init_matrix:np.ndarray, index_eig=-1):

    # check the shape of the matrix 
    m, n = init_matrix.shape
    if m != n:
        print('Matrix is not squared')
        return None

    B = init_matrix.copy()
    last_eigen = B[index_eig, index_eig]
    tolerance = 1e-14
    max_iter = 1000
    n_iter = 0
    eigenvalues = []

    while n_iter < max_iter:
        B = shift_makesimiliar(B, last_eigen)
        last_eigen = B[index_eig, index_eig]

        # deflation
        if B.shape[0] > 2 and B.shape[1] > 2:
            B_nm1 = B[index_eig, index_eig-1]# if B(n_rows, n-1_cols) < tolerance, then we need deflate it out

            if np.abs(B_nm1) < tolerance:
                eigenvalues.append(last_eigen)
                B = B[:index_eig, :index_eig]

        elif B.shape[0] == 2 and B.shape[1] == 2:
            B_nm1 = B[index_eig, index_eig-1]
            if np.abs(B_nm1) < tolerance:
                eigenvalues.extend([B[l, l] for l in range(2)])
                break

        n_iter += 1
    else:
        print("Увага: досягнуто максимальну кількість ітерацій без повної збіжності!")

    return eigenvalues



def test(A): 

    my_time_s = time.time()
    eigen_values_m = eigenvalues_shift_qr(A)
    my_time_e = time.time()
    my_time_diff = my_time_e - my_time_s

    np_time_s = time.time()
    eigen_values_np = np.linalg.eigvalsh(A)
    np_time_e = time.time()
    np_time_diff = np_time_e - np_time_s

    print(f'My execution time: {my_time_diff},\nNumpy execution time: {np_time_diff},\nRatio: {my_time_diff / np_time_diff}\n')
    # print('My calculations: ', eigen_values_m)
    # print('Numpy calculations', eigen_values_np)


N = 100
a = np.random.randn(N, N)
matrix = a.T @ a

test(matrix)