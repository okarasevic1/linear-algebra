import numpy as np 
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

plt.style.use('seaborn-v0_8-notebook')

# data from Wikipedia: https://en.wikipedia.org/wiki/Mile_run_world_record_progression
dates = np.array([
    1885.3333, 1889.4167, 1890.1667, 1892.1667, 1895.9167, 1906.0833, 1906.25,   1909.1667, 
    1912.1667, 1913.1667, 1913.1667, 1917.25,   1919.3333, 1925.0833, 1925.1667, 1925.25,   
    1925.25,   1932.1667, 1932.1667, 1933.25,   1934.25,   1938.25,   1938.25,   1940.1667, 
    1940.1667, 1941.1667, 1941.1667, 1944.25,   1944.25,   1948.0833, 1954.1667, 1955.0833, 
    1955.1667, 1958.25,   1959.1667, 1959.25,   1962.1667, 1963.1667, 1964.1667, 1964.25,   
    1971.1667, 1974.1667, 1978.0833, 1979.1667, 1981.1667
])

seconds = np.array([
    279.2, 279.2, 271.4, 268.4, 266.0, 265.2, 263.8, 259.8, 259.8, 258.8, 
    258.2, 256.0, 254.6, 253.6, 253.4, 252.0, 252.0, 251.2, 250.0, 249.8, 
    248.4, 244.4, 247.4, 247.4, 247.4, 247.4, 247.4, 247.3, 246.4, 245.3, 
    244.9, 243.8, 243.6, 243.4, 242.5, 241.4, 238.9, 238.6, 236.6, 236.4, 
    236.4, 235.0, 235.0, 232.6, 230.6
])

# Create the matrix
ones = np.ones_like(dates)
matrix = np.vstack([ones, dates]).T
print(matrix)

# Calculate the vector of the best fit
vector_best_fit = np.linalg.inv(matrix.T @ matrix) @ matrix.T @ seconds
intercept = vector_best_fit[0]
slope = vector_best_fit[1]

print('Intercept: ', round(intercept, 4))
print('Slope: ', round(slope, 4))

# Predict the result
seconds_predicted = np.dot(matrix, vector_best_fit)
print(seconds_predicted)

# Calculate the Residuals and R2_score
residuals = seconds - seconds_predicted
SS_residuals = np.sum(residuals**2)

SS_total = np.sum((seconds - seconds.mean())**2)
R_2 = 1 - (SS_residuals / SS_total)
print('R2 Score:', R_2)
print('SKlearn R2 Score:', r2_score(seconds, seconds_predicted))

# plot the results 
figure = plt.figure(figsize=(14, 8))

plt.scatter(dates, seconds, color='blue', label='Original Data')
plt.plot(dates, seconds_predicted, color='red', label='Predicted result')

plt.legend()
plt.xlabel('Dates')
plt.ylabel('Seconds')
plt.grid(True)
plt.show()

y_cross = 224
year_crossed = (y_cross - intercept) / slope
print('Year when 220 seconds mark will be crossed: ', year_crossed)

print(np.linalg.lstsq(matrix, seconds))

# plot residuals 
plt.scatter(seconds, residuals, color='green', marker='o', s=100, label='Residuals')
plt.legend()
plt.xlabel('Seconds')
plt.ylabel('Residuals')
plt.grid(True)
plt.show()