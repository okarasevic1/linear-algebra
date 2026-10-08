import numpy as np

def l1_norm(arr: np.ndarray):

    print('Shape:', arr.shape)
    
    norm = 0
    for i in range(len(arr)):
        norm += abs(arr[i])

    return norm


print(l1_norm(np.array([-3, 4])))