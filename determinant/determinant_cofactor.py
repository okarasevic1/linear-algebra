import numpy as np
import time
import scipy

def determinant_cofactor(matrix): 

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

q_non = np.array([
    [1, 1, -1, -1],
    [1, -1, -1, 1],
    [1, 1, 1, 1],
    [1, -1, 1, -1],
])

Q = q_non * 1/2

print('Determinant of unnormalized Q: ', determinant_cofactor(q_non))
print('Determinant of  normalized Q : ', determinant_cofactor(Q))


# t_general = time.process_time()

# for i in range(2, 11): 
#     t = time.process_time()

#     generated_matrix = matrix_generator(i, i)
#     determinant = determinant_cofactor(generated_matrix)
#     print(determinant)

#     print(f'Epoch-{i} time: ', time.process_time() - t)

# print('Total loop time: ', time.process_time() - t_general)


# t_general = time.process_time()

# for i in range(2, 11): 
#     t = time.process_time()

#     generated_matrix = matrix_generator(i, i)
#     determinant = np.linalg.det(generated_matrix)
#     # determinant = np.linalg.slogdet(generated_matrix)
#     print(determinant)

#     print(f'Epoch-{i} time: ', time.process_time() - t)

# print('Total loop time with numpy: ', time.process_time() - t_general)

# for i in range(2, 11): 
#     t = time.process_time()

#     generated_matrix = matrix_generator(i, i)
#     determinant = scipy.linalg.det(generated_matrix)
#     print(determinant)

#     print(f'Epoch-{i} time: ', time.process_time() - t)

# print('Total loop time with numpy: ', time.process_time() - t_general)
                

