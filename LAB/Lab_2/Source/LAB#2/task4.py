from sklearn import neighbors, datasets

# import data
iris = datasets.load_iris()
one = iris.data[:, :]
two = iris.target

# Splitting the dataset into the training set and test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(one, two, test_size = 0.2, random_state = 123)


from sklearn import metrics
neighbours =  [1,10,15,25,50]
for n in neighbours:
    clf = neighbors.KNeighborsClassifier(n)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print("Accuracy Score for K = ",n)
    print(metrics.accuracy_score(y_test, y_pred))