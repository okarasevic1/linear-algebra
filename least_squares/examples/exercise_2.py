import numpy as np
import matplotlib.pyplot as plt

# the distance away from Time Square
distances = [2, 7, 8, 16, 27, 47, 67, 82, 102, 120]
ones = np.ones_like(distances)

matrix = np.vstack([ones, distances]).T


# Cost of tolls USD (Y)
tolls = [6.00, 6.00, 6.00, 6.50, 2.50, 1.00, 1.00, 1.00, 1.00, 1.00]

# calculate the line of the best fit
vector_best_fit = np.linalg.inv(matrix.T @ matrix) @ matrix.T @ np.array(tolls)

# get parameters
intercept = vector_best_fit[0]
slope = vector_best_fit[1]
print('Intercept: ', intercept)
print('Slope: ', slope)

# get the predictions
tolls_pred = matrix @ vector_best_fit

# Calculate the R2 score
residuals = np.array(tolls) - np.array(tolls_pred)
SS_pred = np.sum((np.array(tolls) - np.array(tolls_pred))**2)
SS_total = np.sum((np.array(tolls) - np.array(tolls).mean())**2)

R2_score = 1 - (SS_pred / SS_total)
print('R2 Score: ', R2_score)

figure = plt.figure(figsize=(14, 8))

plt.scatter(distances, tolls, color='purple', s=70, label='Original Data')
plt.plot(distances, tolls_pred, color='red', label='Predicted Tolls')

plt.legend()
plt.xlabel('Distances')
plt.ylabel('Tolls')
plt.show()

plt.scatter(tolls, residuals, color='purple', s=100, label='Original Data')

plt.legend()
plt.xlabel('Distances')
plt.ylabel('Residuals')
plt.show()
