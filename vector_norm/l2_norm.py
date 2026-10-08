import numpy as np

def l2_norm(arr: np.ndarray):
    norm = np.sum(arr ** 2)
    return norm

print(l2_norm(np.array([-3, 4])))