import numpy as np
from vector_projection import vector_projection


# Matrix Orhogonalization using Classical Gramm-Shmidt process
def orthogonal_matrix(init_matrix:np.ndarray):

    # get the shape of the matrix and check whether it is square 
    rows, cols = init_matrix.shape

    if rows != cols:
        print('Matrix is NOT square!')
        return None

    index_col = 0 # current vector which is projected
    U = np.zeros_like(init_matrix, dtype=float) 
    Q = init_matrix.copy() # matrix with orhogonal vectors to each other and lenght of 1
    

    # find orthogonal vectors using projection formula: 
    for n in range(cols): 

        # the first vector stays the same 
        if index_col == 0:
            U[:, n] = init_matrix[:, n]
            Q[:, n] = U[:, n] / np.linalg.norm(U[:, n]) # normalize vector into unit-vector, lenght = 1
            index_col += 1
            continue

        vector = init_matrix[:, n].copy()

        # the non-fisrt columns must been calculated using projection formula
        for p in range(0, index_col):
            u = U[:, p]
            vector = vector - vector_projection(u=u, v=vector)

        # append vector 
        U[:, n] = vector
        Q[:, n] = U[:, n] / np.linalg.norm(U[:, n]) # normalize vector into unit-vector
        index_col += 1

    return Q

    
