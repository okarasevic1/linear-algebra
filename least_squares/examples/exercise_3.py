import numpy as np
import matplotlib.pyplot as plt

"""
ЗАДАЧА СТАТИСТИЧНОГО АНАЛІЗУ: Катастрофа шатла 'Челленджер' (1986)

Контекст:
Перед запуском шатла за рекордно низької температури (31°F) інженери NASA 
намагалися оцінити ризик відмови ущільнювальних O-кілець. 

Суть помилки аналізу:
(а) Спочатку розглядалися ЛИШЕ ті 7 польотів, де сталася хоча б одна відмова. 
    Через відкидання нульових значень зразок даних виявився викривленим, а тренд — непомітним.
(б) Якщо взяти ПОВНИЙ набір даних (усі 24 польоти), стає очевидно, що при високих 
    температурах відмов взагалі не було, а з похолоданням їхня кількість стрімко зростає.

Мета: Побудувати дві лінії найкращого наближення (МНК) для обох випадків 
      та зробити прогноз для критичної температури 31°F.
"""

temp = 31

# Лише ті рейси, де кількість відмов >= 1
failed_temps = np.array([53, 75, 57, 58, 63, 70, 70])
failed_failures = np.array([3, 2, 1, 1, 1, 1, 1])

# Температура в градусах Фаренгейта (X)
all_temps = np.array([
    53, 75, 57, 58, 63, 70, 70, 66, 67, 67, 67,
    68, 69, 70, 70, 72, 73, 75, 76, 76, 78, 79, 80, 81
])

# Кількість пошкоджених O-кілець (Y)
all_failures = np.array([
    3,  2,  1,  1,  1,  1,  1,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0
])

# Part A
ones_a = np.ones_like(failed_temps)
matrix_a = np.vstack([ones_a, failed_temps]).T

best_fit_a = np.linalg.inv(matrix_a.T @ matrix_a) @ matrix_a.T @ failed_failures

intercept_a = best_fit_a[0]
slope_a = best_fit_a[1]

ff_predicted = np.dot(matrix_a, best_fit_a)

residuals_a = failed_failures - ff_predicted
SS_pred_a = np.sum(residuals_a**2)
SS_total_a = np.sum((failed_failures - failed_failures.mean())**2)
R2_score_a = 1 - (SS_pred_a / SS_total_a)

print('R2 score from part A: ', R2_score_a)

f, (ax1, ax2) = plt.subplots(1, 2)

ax1.scatter(failed_temps, failed_failures, color='purple', label='Original Data')
ax1.plot(failed_temps, ff_predicted, color='red', label='Line of the best Fit')
ax1.set_title('Failed Failures')
ax1.set_xlabel('Terperature')
ax1.set_ylabel('№ of Failures')
ax1.legend()

ax2.scatter(failed_failures, residuals_a, color='green', s=100, label='Residuals')
ax2.set_title('Failed Failures')
ax2.set_xlabel('№ of Failures')
ax2.set_ylabel('Residuals')
ax2.legend()

plt.tight_layout()
plt.show()

part_a_failures = intercept_a + (slope_a * temp)
print('Number of failures for part A: ', part_a_failures)

# Part B
ones_b = np.ones_like(all_temps)
matrix_b = np.vstack([ones_b, all_temps]).T

best_fit_b = np.linalg.inv(matrix_b.T @ matrix_b) @ matrix_b.T @ all_failures

intercept_b = best_fit_b[0]
slope_b = best_fit_b[1]

af_predicted = np.dot(matrix_b, best_fit_b)

residuals_b = all_failures - af_predicted
SS_pred_b = np.sum(residuals_b**2)
SS_total_b = np.sum((all_failures - all_failures.mean())**2)
R2_score_b = 1 - (SS_pred_b / SS_total_b)

print('R2 score from part B: ', R2_score_b)

f, (ax1, ax2) = plt.subplots(1, 2)

ax1.scatter(all_temps, all_failures, color='purple', label='Original Data')
ax1.plot(all_temps, af_predicted, color='red', label='Line of the best Fit')
ax1.set_title('Failed Failures')
ax1.set_xlabel('Terperature')
ax1.set_ylabel('№ of Failures')
ax1.legend()

ax2.scatter(failed_failures, residuals_a, color='green', s=100, label='Residuals')
ax2.set_title('Failed Failures')
ax2.set_xlabel('№ of Failures')
ax2.set_ylabel('Residuals')
ax2.legend()

plt.tight_layout()
plt.show()

part_b_failures = intercept_b + (slope_b * temp)
print('Number of failures for part A: ', part_b_failures)