import pickle
from sklearn.datasets import load_iris
from sklearn import tree


def train():
    X, y = load_iris(return_X_y=True)
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, y)
    with open("./model.pkl", "wb") as f:
        pickle.dump(clf, f)


def score(x: list) -> list:
    with open("./model.pkl", "rb") as f:
        clf = pickle.load(f)
    _y = clf.predict_proba(x)[0]
    return list(_y)