import numpy as np


# Calculate the determinant using Cofactor Expansion
def determinant_cofactor(square_matrix:np.ndarray): 

    n_rows, m_cols = square_matrix.shape

    # Chech whether it square or not
    if n_rows != m_cols:
        return None
    
    # If a matrix is 2x2 then apply standard formula |2x2| = ad - cb
    if n_rows == 2 and m_cols == 2:
        det = (square_matrix[0][0] * square_matrix[1][1]) - (square_matrix[0][1] * square_matrix[1][0])
        return det
    
    determinant_result = 0
    current_element = [0, 0]

    # Itter through each column and its first element
    for j_col in range(m_cols):
        
        minor_matrix = [] # minor matrix it is a submatrix of a given square matrix but without j_col and i_row
        for i_row in range(n_rows):
            if i_row == current_element[0]:
                continue
            
            row = [] # this row will be added to the minor matrix

            for k_col in range(m_cols):
                if k_col == current_element[1]:
                    continue
                
                row.append(square_matrix[i_row][k_col])
            
            minor_matrix.append(row)
        
        cofactor_sign = (-1) ** (j_col+i_row) # if the i+j is odd -> Negative, else -> Positive 
        cofactor_element = square_matrix[current_element[0]][current_element[1]]
        determinant_result += cofactor_sign * cofactor_element * determinant_cofactor(np.array(minor_matrix))

        current_element[1] += 1
    
    return determinant_result








def cofactor_matrix(square_matrix:np.ndarray):

    n_rows, m_cols = square_matrix.shape

    # Chech whether it square or not
    if n_rows != m_cols:
        return None
    
    # Each entry of Cofactor Matrix is a Determinant of its Minor Matrix
    cofactor_matrix = [[0 for _ in range(m_cols)] for _ in range(n_rows)]

    # Itter through each entry, get its minor and calculate determinant
    for i_row in range(n_rows):

        for j_col in range(m_cols):
            minor_matrix = []

            for k_row in range(n_rows):
                # If index of row from Current element equals to i_row, then we skip this row
                if k_row == i_row:
                    continue

                row = []

                for l in range(m_cols):
                    # If index of column from Current element equals to j_col, then we skip this column
                    if l == j_col:
                        continue
            
                    row.append(square_matrix[k_row][l])
            
                minor_matrix.append(row)

            # if the sum of the entries is odd then the sign of the determinant entry in negative 
            sign = (-1)**(i_row + j_col)
            cofactor_entry = sign * determinant_cofactor(np.array(minor_matrix))
            cofactor_matrix[i_row][j_col] = cofactor_entry
    
    return cofactor_matrix
            

                    
                
    
