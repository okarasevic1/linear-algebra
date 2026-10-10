import numpy as np
import time


def determinant_cofactor(matrix): 

    '''
        The determinant of the given matrix is calculated by using cofactor method: 
        if matrix has 5rows/columns then it has 5 cofactors with size (5-1)rows/columns (sub-matrix)
        then algo calculate the determinant of its submatrix and multiplies it by factor. 
        The sigh of the factor is defined as (-1)^(i+j)

        Notes: this procedure is very expensive from time and calculation point of view 

        Returns the numerical values, the determinant of the matirx 
    '''

    matrix = np.array(matrix)
    rows, cols = matrix.shape

    if cols != rows: 
        print('The matrix is not square!')
        return None
    
    if rows == 2 and cols == 2: 
        determinant_2_2 = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        return determinant_2_2
    
    determinant = 0
    cofactor_element = [0, 0]

    for col in range(cols):
        minor_matrix = []
        
        for row in range(rows):
            if row == cofactor_element[0]:
                continue

            minor_row = []

            for j_col in range(cols):
                if j_col == cofactor_element[1]:
                    continue

                minor_row.append(matrix[row][j_col])
            
            minor_matrix.append(minor_row)

        sign = (-1)**sum(cofactor_element)
        # print(f'Row: {cofactor_element[0]}, Column: {cofactor_element[1]} Sign: {sign}')
        element = matrix[cofactor_element[0]][cofactor_element[1]]
        determinant += sign * element * determinant_cofactor(minor_matrix)

        cofactor_element[1] = col + 1

    return determinant


def bench_comprassion(g_matrix, my_func, np_func):
    
    t_general = time.process_time()
    mdet = my_func(g_matrix)
    print('My function execution time: ', time.process_time() - t_general)

    t_general = time.process_time()
    npdet = np_func(g_matrix)
    print('My function execution time: ', time.process_time() - t_general)


    print(f'My result of calculation: {mdet};\nNumpy result of calculation: {npdet}')


matrix = np.random.rand(10, 10)
bench_comprassion(matrix, determinant_cofactor, np.linalg.det)

                

