from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import numpy as np

np.random.seed(42)
X = np.sort(5 * np.random.rand(80, 1), axis=0)
y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=3)
regr_3 = DecisionTreeRegressor(max_depth=4)
regr_4 = DecisionTreeRegressor(max_depth=5)

regr_1.fit(X_train, y_train)
regr_2.fit(X_train, y_train)
regr_3.fit(X_train, y_train)
regr_4.fit(X_train, y_train)

y1_pred = regr_1.predict(X_test)
y2_pred = regr_2.predict(X_test)
y3_pred = regr_3.predict(X_test)
y4_pred = regr_4.predict(X_test)

print('Regresseion max_depth=2: ', mean_squared_error(y_test, y1_pred))
print('Regresseion max_depth=3: ', mean_squared_error(y_test, y2_pred))
print('Regresseion max_depth=4: ', mean_squared_error(y_test, y3_pred))
print('Regresseion max_depth=5: ', mean_squared_error(y_test, y4_pred))

X_line = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y1_line = regr_1.predict(X_line)
y2_line = regr_2.predict(X_line)
y3_line = regr_3.predict(X_line)
y4_line = regr_4.predict(X_line)

figure = plt.figure(figsize=(14, 8))

plt.scatter(X, y, edgecolors='black', c='darkorange', label="Реальні дані (з шумом)")
# plt.plot(X_line, y1_line, color="cornflowerblue", label="max_depth=2 (проста модель)", linewidth=1)
plt.plot(X_line, y2_line, color="orange", label="max_depth=3", linewidth=1)
plt.plot(X_line, y3_line, color="green", label="max_depth=4", linewidth=1)
# plt.plot(X_line, y4_line, color="yellowgreen", label="max_depth=5 (глибока модель)", linewidth=1)

plt.xlabel("Ознака X")
plt.ylabel("Цільова змінна Y")
plt.title("Дерево рішень для регресії: як глибина впливає на результат")
plt.legend()
plt.show()