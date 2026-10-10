import numpy as np


def gauss_method_determinant(matrix):
    '''
        Perform Gauss's Method on matrix. This code is for illustration only
        and should not be used in practice.
        m list of lists of numbers; each included list is a row
    '''
    num_rows, num_cols = len(matrix), len(matrix[0])

    # Step 1. Begin with an m × n matrix A. If A = 0, go to Step 7.
    TOL = 1e-10

    if num_rows != num_cols:
        print('It is not square matrix!')
        return None

    ref_matrix = []
    pivot_row, pivot_col = 0, 0

    det_ref = 1

    # Reduce the matrix to the RREF or REF
    for col in range(num_cols):

        for i_row in range(num_rows):
            pivot_entry = matrix[pivot_row][pivot_col]
            
            factor = 0

            if pivot_entry != TOL:
                matrix[pivot_row] = matrix[pivot_row] / pivot_entry # reduce pivot entry to one 
                det_ref *= pivot_entry # det(kp) = k * det(p)
            
            if pivot_entry == TOL:
                buffer = np.array(matrix[i_row])
                matrix[i_row] = matrix[i_row+1]
                matrix[i_row+1] = buffer
                det *= (-1) # det(p, l) = -1 * det (l, p); change the sign

            # for j_row in range(i_row+1, num_rows+1):
            #     factor = 
            #     m[j_row] = 
    
    # ref_matrix = np.array(ref_matrix)
    # return ref_matrix



matrix = np.array([[1, 2], [3, 4]], dtype=np.float16)
index = 1, 0
print(matrix)
buffer = np.array(matrix[0])
matrix[0] = matrix[1]
matrix[1] = buffer
print(matrix)