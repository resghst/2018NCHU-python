from sklearn.datasets import load_iris
from sklearn.svm import LinearSVC
import pandas as pd 
from sklearn.linear_model import LogisticRegression

x_new = [[113, 3, 2, 3]]

iris = load_iris()
x = iris.data
y = iris.target
# clf = LinearSVC()
# clf.fit(x, y)
# print clf.predict(x_new)
# print iris.target_names


clf2 = LogisticRegression().fit(x, y)
print clf2.predict_proba(x_new)
