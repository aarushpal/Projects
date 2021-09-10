from scipy.sparse import data
from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt

boston = datasets.load_boston()

X = boston.data
y = boston.target

X_train , X_test , y_train , y_test = train_test_split(X , y , test_size=0.2)

l_reg = linear_model.LinearRegression()
model = l_reg.fit(X_train , y_train)

predictions = model.predict(X_test)
print(predictions)
print('R^2 value:' , l_reg.score(X,y)) # Accuracy
print('Coefficients:',l_reg.coef_) # Weights
print('Intercept:',l_reg.intercept_) # Bias

