import numpy as np


def gauss_method_determinant(np_matrix:np.ndarray[np.float32]):
    '''
        Perform Gauss's Method on matrix. This code is for illustration only
        and should not be used in practice.
        m list of lists of numbers; each included list is a row.

        Reduce to the upper triangulat matrix -> 
        store operations -> 
        compute determinant of the upper-triangular matrix (product of its entires on the main diagonal)
        -> multiply det with stored operations -> the result will be it's determinant.
    '''

    matrix = np_matrix.copy()
    num_rows, num_cols = matrix.shape

    # Step 1. Begin with an m × n matrix A. If A = 0, go to Step 7.
    TOL = 1e-14

    if num_rows != num_cols:
        print('It is not square matrix!')
        return None

    pivot_row = 0

    det_op = 1
    n_row_swaps = 0

    # Reduce the matrix to the RREF or REF
    for col in range(num_cols):

        if pivot_row == num_rows:
            break

        swap_rows = False

        if np.isclose(matrix[pivot_row, col], 0, atol=TOL, rtol=0):

            for j in range(pivot_row + 1, num_rows):
                if abs(matrix[j, col]) > TOL:
                    matrix[[pivot_row, j]] = matrix[[j, pivot_row]]
                    n_row_swaps += 1
                    swap_rows = True
                    break

            if not swap_rows:
                continue


        pivot_entry = matrix[pivot_row][col]

        for i_row in range(pivot_row+1, num_rows):
            factor = matrix[i_row, col] / pivot_entry
            matrix[i_row] -= factor * matrix[pivot_row]

        # accumulate the products of pivot entries
        det_op *= pivot_entry

        pivot_row += 1
    
    # set the right sign
    det_op = ((-1)**n_row_swaps) * det_op
                
    return det_op
