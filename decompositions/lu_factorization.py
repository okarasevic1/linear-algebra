import numpy as np

# LU decomposition with no row exchange 
# with square matrix
# A = LU
def LU_decomposition(matrix: np.ndarray): 

    '''
        The algo reduces matrix to: 
        L - lower-triangular form, with zeros above the diagonal
        U - upper-triangular form, with zeros below the diagonal
        A = LU

        Args:
            it takes numpy array for numerical stability 

        Returns two matrices: L, U 
    '''

    # check whether it is square 
    row_len, col_len = matrix.shape

    if row_len != col_len:
        print('Non-square Matrix: ', matrix)
        return None

    L = np.identity(row_len) # Lower-triangular matrix with one's on its main diagonal 
    U = matrix # Upper-triangular matrix, or reduced form of given matrix

    pivot_row = 0 # for tracking which row we use as pivot 

    # itter trhough each column
    for j_col in range(col_len):

        # define pivot entry
        pivot_entry = None
        if U[pivot_row, j_col] != 0:
            pivot_entry = U[pivot_row, j_col]
        else: 
            pivot_row += 1
            continue

        # reduce row that are lower than row with its pivot entry
        for i_row in range(pivot_row+1, row_len):
            factor = U[i_row, j_col] / pivot_entry
            U[i_row] = U[i_row] - (factor * U[pivot_row])
            L[i_row, j_col] = factor

        # increase pivot_row variable, so that it doesn't use the same 
        pivot_row += 1

    return L, U



