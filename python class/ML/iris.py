from sklearn.datasets import load_iris
from sklearn.svm import LinearSVC
import pandas as pd 

x_new = [[3, 3, 2, 1]]

iris = load_iris()
x = iris.data
y = iris.target
clf = LinearSVC()
clf.fit(x, y)
print clf.predict(x_new)
print iris.target_names
# print clf.coef_
# print clf.intercept_


# print iris['DESCR']