import numpy as np
from sklearn.linear_model import LinearRegression

num_rows_ar = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]).reshape(-1, 1)
seconds_ar = np.array([0, 0.0162539482117, 
                       0.0808238983154, 0.248152971268, 
                       0.555531978607, 1.05453586578, 
                       1.77881097794, 2.75969099998, 
                       4.10647988319, 5.81125879288, 7.86893582344])

ones_ar = np.ones_like(num_rows_ar)

# matrix = np.vstack([ones_ar, num_rows_ar]).T
matrix = num_rows_ar

inverse = np.linalg.inv(matrix.T @ matrix) 
print(inverse)
slope = inverse @ matrix.T @ seconds_ar
print(slope)

model = LinearRegression(fit_intercept=False)
model.fit(num_rows_ar, seconds_ar)
print(model.coef_)


