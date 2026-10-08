import numpy as np

matrix = np.array([
    [0.787, 0, 0, 0.111, 0.102],
    [0, 0.966, 0.034, 0, 0],
    [0, 0.063, 0.937, 0, 0],
    [0, 0, 0.074, 0.612, 0.314],
    [0.021, 0.009, 0.005, 0.010, 0.954],
])

matrix = matrix.T

vector_n1 = np.array([0.025, 0.025, 0.025, 0.025, 0.900])

epochs = 52

vector_n_m = []

for epoch in range(epochs):
    if epoch == 0:
        vector_n_m = np.dot(matrix, vector_n1)
    else:
        vector_buffer = np.dot(matrix, vector_n_m)
        vector_n_m = vector_buffer

    print(f'Number of itteration {epoch+1}; Number of Customers: {np.array(vector_n_m)}')