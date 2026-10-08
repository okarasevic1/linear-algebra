import numpy as np
import matplotlib.pyplot as plt

matrix = np.array([
    [1.0, 0.5, 0, 0, 0, 0],
    [0, 0, 0.5, 0, 0, 0],
    [0, 0.5, 0, 0.5, 0, 0],
    [0, 0, 0.5, 0, 0.5, 0],
    [0, 0, 0, 0.5, 0, 0],
    [0, 0, 0, 0, 0.5, 1.0],
])

vector_n1 = np.array([0, 0, 0, 0, 1, 0])

probability_vector = np.dot(matrix, vector_n1)
print(probability_vector)

n=100
vector_n_m = []

probanilities = []

for itter in range(1, n):
    if itter == 1:
        vector_n_m = np.dot(matrix, vector_n1)
    else:
        vector_buffer = np.dot(matrix, vector_n_m)
        vector_n_m = vector_buffer

    print(f'Number of itteration {itter}; Probability: {vector_n_m}; Probability of the game is over: {vector_n_m[0] + vector_n_m[-1]}')
    probanilities.append(vector_n_m[-1])

figure = plt.figure(figsize=(14, 8))

plt.plot(range(1, n), probanilities, color='orange', linewidth=2, label='Probabilities')
plt.axhline(np.array(probanilities).mean(), color='red', linewidth=0.5, linestyle='--', label='Minimum')
plt.legend()
plt.xlabel('Number')
plt.ylabel('Prob on the win: ')

plt.tight_layout()
plt.show()


