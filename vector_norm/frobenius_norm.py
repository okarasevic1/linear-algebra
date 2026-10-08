import numpy as np

def frobenius_norm(arr:np.ndarray):
    norm = 0

    for i in range(len(arr)):
        row_norm = np.sum(arr[i] ** 2)
        norm += row_norm
    
    return np.sqrt(norm)


print(frobenius_norm(np.array([[1, 2], [5, 2]])))