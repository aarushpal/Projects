from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()

X = iris.data
y = iris.target

classes = ['Iris Setosa','Iris Versicolour','Iris Virginica']

X_train , X_test , y_train , y_test = train_test_split(X , y , test_size=0.2)

model = svm.SVC() # Creating the model
model.fit(X_train , y_train) # Training the model
print(model)

# print(X_train.shape)
# print(y_train.shape)
# print(X_test.shape)
# print(y_test.shape)

predictions = model.predict(X_test) # Predicting on y_test
accuracy = accuracy_score(y_test , predictions) # Finding accuracy by comparing predictions and y_test

print(predictions)
print(accuracy)