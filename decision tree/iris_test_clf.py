from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

dataset = load_iris()
X = dataset.data
y = dataset.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print('Accuracy score: ', accuracy_score(y_test, y_pred))

figure = plt.figure(figsize=(14, 8))

plot_tree(
    clf, 
    feature_names=dataset.feature_names, 
    class_names=dataset.target_names, 
    filled=True, 
    rounded=True
)

plt.show()