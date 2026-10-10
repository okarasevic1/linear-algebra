import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.
    
    Args: 
    arr: Input numpy array (1D or 2D) 
    norm_type: Type of norm ('l1', 'l2', or 'frobenius')
    
    Returns: The computed norm as a float
    """
    norm = 0

    if norm_type == 'l1': 
        for i in range(len(arr)):
            norm += abs(arr[i])
    elif norm_type == 'l2': 
        norm = np.sqrt(np.sum(arr ** 2))
    elif norm_type == 'frobenius': 
        matrix_norm = 0
        for i in range(len(arr)):
            row_norm = np.sum(arr[i] ** 2)
            matrix_norm += row_norm

        norm = np.sqrt(matrix_norm)
    else:
        return None
    
    return norm

print(compute_norm(np.array([1, -2, 3]), 'l1'))