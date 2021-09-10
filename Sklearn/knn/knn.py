import numpy as np
import pandas as pd
from sklearn import neighbors , metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('knn\car.data')
# print(data.head())

X = data[['buying' , 'maint' , 'safety']].values
y = data[['class']]


# Converting the values(label encoding)
Le = LabelEncoder()
for i in range(len(X[0])):
    X[:,i] = Le.fit_transform(X[:,i])


# Converting labels
label_maping = {
    'unacc':0,
    'acc':1,
    'good':2,
    'vgood':3
}

y['class'] = y['class'].map(label_maping)
y = np.array(y)

# Creating model

knn = neighbors.KNeighborsClassifier(n_neighbors=25 , weights='uniform') # Creating knn object
X_train , X_test , y_train , y_test = train_test_split(X , y , test_size=0.2) 

knn.fit(X_train , y_train) # Training the model

prediction = knn.predict(X_test) # Predicting the labels from test features

accurary = metrics.accuracy_score(y_test , prediction) # Finding the accuracy of the model
print(accurary)

