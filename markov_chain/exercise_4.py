import numpy as np

matrix = np.array([
    [0.9, 0.01],
    [0.1, 0.99]
])

vector_n1 = np.array([0.2, 0.8])

epochs = 10

vector_n_m = []

for epoch in range(epochs):
    if epoch == 0:
        vector_n_m = np.dot(matrix, vector_n1)
    else:
        vector_buffer = np.dot(matrix, vector_n_m)
        vector_n_m = vector_buffer

    print(f'Number of itteration {epoch+1}; Number of Customers: {np.array(vector_n_m)}')