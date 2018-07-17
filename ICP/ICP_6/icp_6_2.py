from sklearn import datasets, metrics
from sklearn import cross_validation as cv
from sklearn.naive_bayes import GaussianNB

# Loading the dataset
irisdataset = datasets.load_iris()

# use the Gaussiannm model
model = GaussianNB()
# # getting the data and response of the dataset
x = irisdataset.data
y = irisdataset.target
splits = cv.train_test_split(x,y,test_size=0.2)
# load the date into training and testing
X_train, X_test, y_train, y_test =splits
#print(splits)
model.fit(X_train,y_train)
# set the expected value to perform cross validation
expected = y_test
predicted = model.predict(X_test)
print("----")
print(metrics.classification_report(expected,predicted))
print("----")
#print the expected and predicted values
print(metrics.confusion_matrix(expected,predicted))
print("----")
# the average of all
print(metrics.f1_score(expected,predicted, average='micro'))