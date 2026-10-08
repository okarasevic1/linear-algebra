import numpy as np
from hessenberg_form import householder_transfromation_adapted as hessenberg
import sys
sys.path.append('/Users/okarasevic1/Documents/Linear Algebra /qr_factorization')
from householder_transformation import householder_transformation as qr
import time

def make_similiar(H:np.ndarray, eigen:float):

    m, n = H.shape
    # H - (µ * I) = QR
    H_shifted = H.flatten()
    H_shifted[0::m+1] -= eigen
    H_shifted = np.reshape(H_shifted, (m,n))

    Q, R = qr(H_shifted)

    # H_k+1 = R * Q = Q.T * H * Q
    H_sim = Q.T @ H @ Q

    return H_sim


def eigenvalues_calculation(init_matrix:np.ndarray, index_eig:int=-1):

    # check the form
    m, n = init_matrix.shape
    if m != n:
        print('Matrix is NOT square')
        return None

    # reduce the matrix to Hessenberg matrix 
    H, _ = hessenberg(init_matrix, calc_q=False)
    last_eigen = np.array(H)[-1, -1]
    
    tolerance = 1e-16
    max_iter = 1000
    n_iter = 0
    eigenvalues = []

    while n_iter < max_iter: 
        H = make_similiar(H, last_eigen)
        last_eigen = H[index_eig, index_eig]


        # deflation logic
        if H.shape[0] > 2 and H.shape[0] > 2:
            H_nm1 = H[index_eig, index_eig-1] # if < tolerance then deflate it out

            if np.abs(H_nm1) < tolerance: 
                eigenvalues.append(last_eigen)
                H = H[:index_eig, :index_eig]

        elif H.shape[0] == 2 and H.shape[0] == 2:
            H_nm1 = H[index_eig, index_eig-1]

            if np.abs(H_nm1) < tolerance:
                eigenvalues.extend([H[l, l] for l in range(2)])
                break

        n_iter += 1
    else:
            print("Увага: досягнуто максимальну кількість ітерацій без повної збіжності!")

    print(f'Number of totel iterations: {n_iter}')

    return eigenvalues



def test(A): 

    my_time_s = time.time()
    eigen_values_m = eigenvalues_calculation(A)
    my_time_e = time.time()
    my_time_diff = my_time_e - my_time_s

    np_time_s = time.time()
    eigen_values_np = np.linalg.eigvalsh(A)
    np_time_e = time.time()
    np_time_diff = np_time_e - np_time_s

    print(f'My execution time: {my_time_diff},\nNumpy execution time: {np_time_diff},\nRatio: {my_time_diff / np_time_diff}')
    
    eigen_values_m = np.sort(eigen_values_m)
    pass_test = np.isclose(eigen_values_m, eigen_values_np, atol=1e-14).all()
    print(f'Passed? -> {'Yes' if pass_test else 'No'}')
    # print(f'My calculations: \n', eigen_values_m)
    # print(f'Numpy calculations: \n', eigen_values_np)


N = 50
matrix = np.random.randn(N, N)
spd_matrix = matrix.transpose() @ matrix

test(spd_matrix)