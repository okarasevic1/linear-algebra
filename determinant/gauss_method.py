import numpy as np

def matrix_generator(m_rows, n_cols):
    normalized_matrix = np.random.rand(m_rows, n_cols)
    matrix = normalized_matrix * np.random.randint(5, 20, (m_rows, n_cols))

    return matrix

print(matrix_generator(4, 4))

def gauss_method_determinant(m):
    """Perform Gauss's Method on m. This code is for illustration only
    and should not be used in practice.
    m list of lists of numbers; each included list is a row
    """
    num_rows, num_cols = len(m), len(m[0])

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
            pivot_entry = m[pivot_row][pivot_col]

            
            factor = 0

            if pivot_entry != TOL:
                m[pivot_row] = m[pivot_row] / pivot_entry # reduce pivot entry to one 
                det_ref *= pivot_entry # det(kp) = k * det(p)
            
            if pivot_entry == TOL:
                buffer = np.array(m[i_row])
                m[i_row]
                m[i_row+1] = m[i_row+1], m[i_row]
                det *= (-1) # det(p, l) = -1 * det (l, p); change the sign

    #         for j_row in range(i_row+1, num_rows+1):
    #             # m[j_row] = 
    
    # ref_matrix = np.array(ref_matrix)
    # return ref_matrix



matrix = np.array([[1, 2], [3, 4]], dtype=np.float16)
index = 1, 0
print(matrix)
buffer = np.array(matrix[0])
matrix[0] = matrix[1]
matrix[1] = buffer
print(matrix)