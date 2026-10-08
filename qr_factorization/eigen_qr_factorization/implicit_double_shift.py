import numpy as np
from hessenberg_form import householder_transfromation_adapted as hessenberg


class Impilicit_Double_Shift:

    def __init__(self, init_matrix):
        self.init_matrix = init_matrix


    # get the last block of the matrix 2x2 and calculate it's eigenvalues
    # s = a + d -> sum of trace of 2x2
    # p = ad - bc * µ2 -> determinant of 2x2 
    # H_new = H^2 - sH + pI
    def introduce_bulge(self, hessenberg_matrix:np.ndarray): 

        # get the shape and check 
        m_rows, n_cols = hessenberg_matrix.shape

        H_new = hessenberg_matrix.copy()

        if m_rows != n_cols:
            print('Matrix is NOT sqaure')
            raise ValueError

        tbt_block = np.array([
            [hessenberg_matrix[-2, -2], hessenberg_matrix[-2, -1]], 
            [hessenberg_matrix[-1, -2], hessenberg_matrix[-1, -1]], 
        ])

        # p, s calculation 
        s = tbt_block[0, 0] + tbt_block[1, 1]
        p = (tbt_block[0, 0] * tbt_block[1, 1]) + (tbt_block[0, 1] * tbt_block[1, 0])

        v = hessenberg_matrix[:, 0]
        x = hessenberg_matrix @ v - s * v
        x[0] += p

        H_new[:, 0] = x

        return H_new


    def introduce_bulge_comp(self, hessenberg_matrix:np.ndarray): 

        # get the shape and check 
        m_rows, n_cols = hessenberg_matrix.shape

        H = hessenberg_matrix.copy()

        if m_rows != n_cols:
            print('Matrix is NOT sqaure')
            raise ValueError

        tbt_block = np.array([
            [hessenberg_matrix[-2, -2], hessenberg_matrix[-2, -1]], 
            [hessenberg_matrix[-1, -2], hessenberg_matrix[-1, -1]], 
        ])

        # p, s calculation 
        s = tbt_block[0, 0] + tbt_block[1, 1]
        p = (tbt_block[0, 0] * tbt_block[1, 1]) + (tbt_block[0, 1] * tbt_block[1, 0])

        H_new = (H @ H) - (s * H) - (p * np.eye(m_rows))

        return H_new


    def given_rotations(self, matrix, out_size, row_i:int, col_j:int):

        G = np.eye(out_size, dtype=float)
        x = matrix[row_i, col_j]
        y = matrix[row_i+1, col_j]

        v_norm = np.linalg.norm([x, y])
        s = x / v_norm
        c = y / v_norm

        G[row_i, col_j+1] = s
        G[row_i, col_j+2] = c
        G[row_i+1, col_j+1] = -c
        G[row_i+1, col_j+2] = s

        return G


    def bulge_chasing(self, hessenberg_form:np.ndarray):

        rows = hessenberg_form.shape[0]

        output_m = None

        test_num = 20

        for i in range(test_num): 
            test_matrix = self.introduce_bulge_comp(hessenberg_form)
            if i == 0:
                print(np.around(test_matrix, 2))

            for k in range(rows-2):
                G = self.given_rotations(test_matrix, rows, k+1, k)

                test_matrix = G @ test_matrix @ G.T

            # print(np.around(test_matrix, 2))

            output_m = test_matrix

        return output_m  

    



def pd_matrix(rows, cols):
    matrix = np.random.randint(0, 3, (rows, cols))
    pd_matrix = (matrix.T @ matrix).astype(float)

    return pd_matrix


m1 = pd_matrix(5, 5)
ids = Impilicit_Double_Shift(m1)
hess = hessenberg(m1)

out_m = ids.bulge_chasing(hess)
print(np.around(out_m, 2))