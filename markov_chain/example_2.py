import numpy as np
import matplotlib.pyplot as plt
import scipy

matrix = np.array([
    [0.1, 0.06, 0.03],
    [0.05, 0.08, 0.04],
    [0.85, 0.86, 0.93]
])

vector_n1 = np.array([300/1000, 400/1000, 300/1000,])

nights=25

vector_n_m = []

for itter in range(1, nights+1):
    if itter == 1:
        vector_n_m = np.dot(matrix, vector_n1)
    else:
        vector_buffer = np.dot(matrix, vector_n_m)
        vector_n_m = vector_buffer

    print(f'Number of itteration {itter}; Number of Customers: {np.array((vector_n_m)*1000)}')

# figure = plt.figure(figsize=(14, 8))

# plt.plot(range(1, n), probanilities, color='orange', linewidth=2, label='Probabilities')
# plt.axhline(np.array(probanilities).mean(), color='red', linewidth=0.5, linestyle='--', label='Minimum')
# plt.legend()
# plt.xlabel('Number')
# plt.ylabel('Prob on the win: ')

# plt.tight_layout()
# plt.show()

p = np.array([
    [-0.9, 0.06, 0.03, 0],
    [0.05, -0.92, 0.04, 0],
    [0.85, 0.86, -0.07, 0],
    [1, 1, 1, 1]
])

b = np.array([0, 0, 0, 0])

print(np.linalg.solve(p, b))
print(scipy.linalg.solve(p))
