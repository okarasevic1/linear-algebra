import numpy as np
import scipy


def PLU_decomposition(matrix:np.ndarray):

    # checck whether the matrix is sqaure 
    num_rows, num_cols = matrix.shape

    if num_rows != num_cols:
        print('Matrix is NOT sqaure!')
        return None

    # set out initial matrices 
    U = matrix.astype(float).copy() # upper triangular matrix 
    L = np.identity(n=num_cols) # lower triangular matrix with one's on the diagonal 
    P = np.identity(n=num_cols) # for recording the row exchanges 

    pivot_row = 0 # tracks in which row the pivot entry

    for j_col in range(num_cols):

        # find the index of the greatest value in current column
        max_idx = np.argmax(np.abs(U[pivot_row:, j_col])) + pivot_row 

        # skip if all coumns contains only zeros 
        if np.isclose(U[max_idx, j_col], 0, atol=1e-8):
            continue

        # exchange the rows, if max value exists and record all transformations into P
        if max_idx != pivot_row:
            U[[pivot_row, max_idx]] = U[[max_idx, pivot_row]]
            P[[pivot_row, max_idx]] = P[[max_idx, pivot_row]]

            if j_col > 0:
                L[[pivot_row, max_idx], :j_col] = L[[max_idx, pivot_row], :j_col]

        pivot_entry = U[pivot_row, j_col]

        # reduce the rows 
        for i_row in range(pivot_row+1, num_rows):
            factor = U[i_row, j_col] / pivot_entry
            U[i_row] = U[i_row] - (factor * U[pivot_row])
            L[i_row, j_col] = factor

        pivot_row += 1

    answer = [P.T, L, U]
    for matrix in answer:
        print(f'{matrix}\n{"="*100}')

    return answer


def squre_matrix_generator(size):
    random_matrix = [[np.random.randint(-10, 10) for _ in range(size)] for _ in range(size)]
    return random_matrix


random_matrix = np.array(squre_matrix_generator(5))
print(random_matrix)
answer = PLU_decomposition(random_matrix)
sci_answer = scipy.linalg.lu(random_matrix)

print(np.dot(np.dot(answer[0], answer[1]), answer[2]))
print(np.dot(np.dot(sci_answer[0], sci_answer[1]), sci_answer[2]))