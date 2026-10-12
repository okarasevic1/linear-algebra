import numpy as np
from scipy.linalg import hessenberg



np.set_printoptions(precision=3, suppress=True)


class FrancisShift:

    def __init__(self, matrix:np.ndarray):
        self.matrix = matrix
        
    # eigenvalues for 2x2 matrix can experessed Characteristic equation:
    # µ^2 - (a + d) * µ + (a * d) - (b * c) = 0
    def eigenvalues_2x2(self, matrix2x2:np.ndarray):

        a, b = matrix2x2[0]
        c, d = matrix2x2[1]

        trace = a + d
        determinant = (a * d) - (b * c)

        try:
            des = np.sqrt((trace**2) - (4 * (determinant)))
        except Exception as e:
            print(e)
            return []

        l1 = (trace + des) / 2
        l2 = (trace - des) / 2

        return [l1, l2]


    def given_rotations(self, el_1, el_2):

        G = np.eye(2, dtype=float)

        i, j = [0, 1]

        r = np.sqrt(np.power(el_1, 2) + np.power(el_2, 2))
        # normalize entries 
        c = el_1 / r
        s = el_2 / r

        G[[i, j], [i, j]] = c
        G[i, j] = -s
        G[j, i] = s

        return G


    def introduce_bulge(self, hessenberg_form:np.ndarray):

        H = hessenberg_form.copy()
        m_rows, n_cols = H.shape

        e_matrix = H[np.ix_([-2, -1], [-2, -1])]
        eigens_2x2 = self.eigenvalues_2x2(e_matrix)

        id_matrix = np.eye(m_rows, n_cols, dtype=float)

        # f(A) = (A−ρmI)···(A−ρ1I)
        fA = id_matrix[0, :].copy()

        for m in eigens_2x2:
            S = H.copy().flatten()
            S[0::m_rows+1] -= m
            S = np.reshape(S, H.shape)

            fA = S @ fA

        # fA is equal to x-vector
        # and then we apply Given Rotations Algo to get zeros besides first entry 
        x = fA.copy()
        x = np.where(np.abs(x) < 1e-10, 0.0, x)
        m = np.count_nonzero(x)

        for i in range(m-1, 0, -1):

            x_el, y_el = x[i-1], x[i]
            Gm = self.given_rotations(el_1=x_el, el_2=y_el)
            Gm_stack = id_matrix.copy()

            Gm_stack[i-1:i+1, i-1:i+1] = Gm
            x = Gm_stack @ x 

            H[i-1:i+1] = Gm.T @ H[i-1:i+1]
            H[:, i-1:i+1] = H[:, i-1:i+1] @ Gm

        return H

    def francies_shift(self, max_iter=1000):

        # Calculate the eigenvalues of the 2x2 lower right-hand h_matrix
        m_rows, n_cols = self.matrix.shape

        H_new = self.matrix.copy()

        if m_rows != n_cols:
            print('Matrix is not square')
            raise ValueError

        n = 0

        while n < max_iter:

            # Introduce the bulge
            H_new = self.introduce_bulge(H_new)

            # count zero with tolerance: 
            start_row = 4
            end_row = 1

            tol = 1e-16

            # chase the bulge 
            for j_col in range(n_cols):

                if j_col == n_cols - 3:

                    i_row = start_row - 2
                    # get the elements, which shlould be zero after Given rotations
                    x_el, y_el = H_new[i_row-1, j_col], H_new[i_row, j_col]
                    Gm = self.given_rotations(x_el, y_el)

                    # perform Given rotations only on specific two rows frist and then on two columns 
                    H_new[i_row-1:i_row+1] = Gm.T @ H_new[i_row-1:i_row+1]
                    H_new[:, i_row-1:i_row+1] = H_new[:, i_row-1:i_row+1] @ Gm
                    break

                for i_row in range(start_row-1, end_row, -1):
                    # get the elements, which shlould be zero after Given rotations
                    x_el, y_el = H_new[i_row-1, j_col], H_new[i_row, j_col]
                    Gm = self.given_rotations(x_el, y_el)
        
                    H_new[i_row-1:i_row+1] = Gm.T @ H_new[i_row-1:i_row+1]
                    H_new[:, i_row-1:i_row+1] = H_new[:, i_row-1:i_row+1] @ Gm
                                
                start_row += 1
                end_row += 1

            if n % 54 == 0: 

                pre_last = np.abs(H_new[-1, -2])
                diag_check = np.abs([H_new[-2, -2], H_new[-1, -1]])
                tol_v = tol * np.prod(diag_check)
                print(pre_last)
                print(tol_v)

                if pre_last <= tol_v:
                    print(True)

                print(f'Number of iteration: {n}')


            n += 1
            

    

def pd_matrix_gen(rows, cols):
    matrix = np.random.randint(-10, 10, (rows, cols))
    pd_matrix = matrix.T @ matrix

    return pd_matrix

matrix = pd_matrix_gen(7, 7)
h_matrix = hessenberg(matrix)

fr = FrancisShift(h_matrix)
fr.francies_shift(max_iter=50)


