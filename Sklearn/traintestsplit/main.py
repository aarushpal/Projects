from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split

iris = datasets.load_iris() # Loading the iris dataset

# Splitting data into features and labels
X = iris.data # features
y = iris.target # labels

X_train , X_test , y_train , y_test = train_test_split(X , y , test_size=0.2)
# Splits the data into training and test sets
# test size refers to the fraction of the data to be taken for testing

