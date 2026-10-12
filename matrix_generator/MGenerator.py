import numpy as np

class MGenerator:

    def generate_matrix(size:tuple, spd_matirx:bool, low:int, high:int) -> np.ndarray:
        '''
            size -> 1st value is rows and 2nd is columns 
            dtype -> float/int/double/etc.
            spd_matrix -> true: it is positive definite matrix (A^T * A); false: random matrix 

            Returns either matrix with givan size and random entries or similiar positive definite matrix
        '''

        matrix = None

        if (low == 0) & (high == 1): 
            matrix = np.random.rand(size[0], size[1])
        else:
            matrix = np.random.randint(
                low=low, high=high, 
                size=size
            )

        if len(matrix) > 0:
            if spd_matirx:
                pd_matrix = matrix.T @ matrix

                return pd_matrix

            else:
                return matrix

        else:
            raise ValueError

        