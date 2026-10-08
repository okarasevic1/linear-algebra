import numpy as np
import matplotlib.pyplot as plt

matrix = np.array([
    [0.7, 0.15, 0.15,],
    [0.2, 0.8, 0.15],
    [0.1, 0.05, 0.7]
])

vector_n1 = np.array([15000/100000, 20000/100000, 65000/100000,])

years=3

vector_n_m = []

for itter in range(1, years+1):
    if itter == 1:
        vector_n_m = np.dot(matrix, vector_n1)
    else:
        vector_buffer = np.dot(matrix, vector_n_m)
        vector_n_m = vector_buffer

    print(f'Number of itteration {itter}; Number of Customers: {vector_n_m}')

# figure = plt.figure(figsize=(14, 8))

# plt.plot(range(1, n), probanilities, color='orange', linewidth=2, label='Probabilities')
# plt.axhline(np.array(probanilities).mean(), color='red', linewidth=0.5, linestyle='--', label='Minimum')
# plt.legend()
# plt.xlabel('Number')
# plt.ylabel('Prob on the win: ')

# plt.tight_layout()
# plt.show()

print(np.dot(matrix.__pow__(years-1), vector_n1) * 100000)
