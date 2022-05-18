from sklearn.ensemble import AdaBoostClassifier

import Code.Draw


def adaBoost(X_train, y_train, X_test, y_test, images, index):
    boost = AdaBoostClassifier()
    # Train the model on training data
    boost.fit(X_train, y_train)
    acc = boost.score(X_test, y_test) * 100
    Code.Draw.drawPredict(boost, X_test, y_test, images, index)
    return acc
