from cofactor_matrix import cofactor_matrix
import numpy as np

def adjoint_matrix(square_matrix:np.ndarray):
    # calculate the cofactor_matrix
    cofactor_matrix_step = np.array(cofactor_matrix(square_matrix))
    
    # Adjoint is the same cofactor matrix only transposed 
    n_rows, m_cols = cofactor_matrix_step.shape

    # create zero_matrix
    adjoint = [[0 for _ in range(m_cols)] for _ in range(n_rows)]

    for i in range(n_rows):
        for j in range(m_cols):
            adjoint[j][i] = cofactor_matrix_step[i][j]

    return adjoint 