from sklearn.tree import DecisionTreeClassifier
import Code.Draw


def decisionTreeClassifier(X_train, y_train, X_test, y_test, images, index):
    DtreeClf = DecisionTreeClassifier()
    DtreeClf.fit(X_train, y_train)
    acc = DtreeClf.score(X_test, y_test) * 100
    Code.Draw.drawPredict(DtreeClf, X_test, y_test, images, index)
    return acc
