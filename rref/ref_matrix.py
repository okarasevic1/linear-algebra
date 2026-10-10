import numpy as np

def ref_matrix(matrix):

    '''
        ref_matrix -> REF-matrix with zeros below the diagonal (j,j) and with values on the main diagonal and above

        Args: matrix -> it can accapet as python list and numpy array  
        Returns matrix in reduced echelon form 
    '''

    # get the shape of the matrix
    rows, cols = len(matrix), len(matrix[0])

    # loop through. If matrix is not square then we need to find which value to use. 
    # Use smaller value
    pivot_row = 0

    for col in range(cols):
        
        pivot = None
        if pivot_row >= rows:
            break
        
        if matrix[pivot_row][col] == 0: 
            # find another the leftmost non-zero column
            for j in range(pivot_row+1, rows):
                if matrix[j][col] != 1e-8:
                    buffer = np.array(matrix[pivot_row])
                    matrix[pivot_row] = np.array(matrix[j])
                    matrix[j] = np.array(buffer)
                    continue
                else:
                    pivot_row += 1
                    continue

            # Step 2. Determine the leftmost non-zero column
        pivot = matrix[pivot_row][col]

            # Step 3. Use row operations to put a 1 in the topmost position(we call 
            # this position pivot position) of this column. Skip this step, it is for RREF

        # Step 4. Use elementary row operations to put zeros (strictly) below the pivotposition.
        for i_row in range(pivot_row+1, rows):
            # factor = matrix[i_row][col] / pivot
            # matrix[i_row] = matrix[i_row] - (factor*matrix[pivot_row])
            factor = matrix[i_row, col] / pivot
            matrix[i_row] = matrix[i_row] - factor * matrix[pivot_row]
            
        pivot_row += 1

    return matrix





