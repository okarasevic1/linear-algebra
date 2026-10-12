import numpy as np

import sys
sys.path.append('/Users/okarasevic1/Documents/Linear Algebra /qr_factorization')
from householder_transformation import householder_transformation as qr

def makesimiliar(B):
    Q, R = qr(B)
    B = R @ Q
    return B

# Standard approach for finding eigenvalues using 
# QR-factorization with Householder Transformation
# A_n = Q_n * R_n
# A_n+1 = R_n * Q_n

def eigen_qr_standard(init_matrix:np.ndarray):

    # get the shape of matrix
    m, n = init_matrix.shape
    if m != n:
        print('Matrix is NOT squared!')
        return None

    B = init_matrix.copy()
    tolerance = 1e-19
    max_iter = 10000
    n_iter = 0

    while n_iter < max_iter:
        B = makesimiliar(B)
        
        # Перевірка стану матриці
        sub_diagonal = np.tril(B, k=-1)
        max_sub_el = np.max(np.abs(sub_diagonal))
        
        # Якщо досягли точності — виходимо з циклу
        if max_sub_el < tolerance:
            break
            
        n_iter += 1
    else:
        print("Увага: досягнуто максимальну кількість ітерацій без повної збіжності!")
    
    print(f'Init mattrix: \n', init_matrix)
    print(f'A_n mattrix after #{n_iter} operations: \n', B)

    eigens = [B[ind, ind] for ind in range(m)]
    eigens = np.sort(eigens)
    print(eigens)

    return B


def squre_matrix_generator(size):
    random_matrix = np.array([[np.random.randint(-10, 10) for _ in range(size)] for _ in range(size)])
    return random_matrix

matrix = squre_matrix_generator(2)

B_n = eigen_qr_standard(matrix)
print(np.linalg.eigvalsh(matrix))

