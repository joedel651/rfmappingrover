import csv
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as nd
import matplotlib.pyplot as plt
from statistics import median
from sklearn.preprocessing import MinMaxScaler

filename = 'median114.csv'
filename2 = 'mycsv.csv'
#62:01:94:38:03:df AP1
#62:01:94:38:06:43 AP2
#86:f3:eb:b3:15:b5. AP3
#86:f3:eb:b2:a0:75. AP4

data = pd.read_csv(filename, index_col = None)
data2 = pd.read_csv(filename2, index_col = None)

feature_cols = ["BaseStation1","RSSI1","BaseStation2","RSSI2","BaseStation3","RSSI3","BaseStation4","RSSI4"]
# use the list to select a subset of the original DataFrame
X_train = data[feature_cols]

#select a series from the dataFrame
y_train = data['Position']

# split the set
#default split is 75% for training and 25% for testing
#X_train,X_test,y_train,y_test = train_test_split(X, y, random_state = 1)

X_test = data2[feature_cols]
#y_test = data2['Position']




# instantiate learning model (k = 1)
knn = KNeighborsClassifier(n_neighbors=1)

# fitting the model
modle = knn.fit(X_train, y_train)
# predict the response
pred = knn.predict(X_test)


# evaluate accuracy
print("the accuracy is")
#print (metrics.accuracy_score(y_test, pred))
print(X_test.columns)
print("The predicted position is")
print(pred)

