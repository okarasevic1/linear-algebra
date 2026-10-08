import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

plt.style.use('seaborn-v0_8-notebook')


year = np.array([1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950])
secs = np.array([268.8, 264.5, 258.4, 255.6, 255.6, 252.6, 250.4, 246.4, 241.4])

ones_np = np.ones_like(year)

# Stack columns vertically to form the matrix
matrix = np.vstack([ones_np, year]).T

# Find the vector of the best fit
vector_of_best_fit = np.linalg.inv(matrix.T @ matrix) @ matrix.T @ secs
# Project (Predict) the vector onto the line/plane
secs_predicted = np.dot(matrix, vector_of_best_fit)

# Coefficients
intercept = vector_of_best_fit[0]
slope = vector_of_best_fit[1]
print('Intercept: ', round(intercept, 3))
print('Slope: ', round(slope, 3))

# Calculate the year, when 4min mark will be crossed
y_cross = 240
year_cross = (y_cross - intercept) / slope
print(year_cross)

# calculate the Sum of squared Residuals 
residuals = secs - secs_predicted
squared_residuals = residuals**2
sse = squared_residuals.sum()
print(squared_residuals)
print(sse/len(secs))

# calculate the R2 score
SS_residual = sse
SS_total = ((secs - secs.mean())**2).sum()
r2_score = 1 - (SS_residual / SS_total)
print('R2 Score: ', r2_score)

figure = plt.figure(figsize=(14, 8))

plt.scatter(year, secs, color='blue', label='Original Data')
plt.plot(year, secs_predicted, color='red', label='Predicted Result')

plt.axhline(y=y_cross, color='green', linestyle='--', label=f'{y_cross} Seconds Mark')
plt.axvline(x=year_cross, color='purple', linestyle=':', label=f'Year Crossed ({y_cross}s)')
plt.scatter(year_cross, y_cross, color='yellow', marker='o', s=100, zorder=5)
plt.text(year_cross + 5, y_cross - 5, f' {int(year_cross)}', color='red', fontsize=12, ha='left')

plt.legend()
plt.xlabel('Year')
plt.ylabel('Seconds')
plt.title('Line of Best Fit and 240 Seconds Mark')
plt.grid(True)
plt.show()

# plot residuals 
plt.scatter( secs, residuals, color='green', marker='o', s=100, label='Residuals')
plt.legend()
plt.xlabel('Seconds')
plt.ylabel('Residuals')
plt.grid(True)
plt.show()
