from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
import csv
import pandas as pd

x=0
y=0
z=0

def compare(x,y):
    if x==y:
        return 1
    else:
        return 0


def drivetopostion(Finish):
    z = compare(0, 1)



    filename = 'median114.csv'
    filename2 = 'mycsv.csv'

    data = pd.read_csv(filename, index_col=None)
    data2 = pd.read_csv(filename2, index_col=None)

    feature_cols = ["BaseStation1", "RSSI1", "BaseStation2", "RSSI2", "BaseStation3", "RSSI3", "BaseStation4", "RSSI4"]
    # use the list to select a subset of the original DataFrame
    X_train = data[feature_cols]

    # select a series from the dataFrame
    y_train = data['Position']

    # split the set
    # default split is 75% for training and 25% for testing
    # X_train,X_test,y_train,y_test = train_test_split(X, y, random_state = 1)

    X_test = data2[feature_cols]
    y_test = data2['Position']

    # instantiate learning model (k = 1)
    knn = KNeighborsClassifier(n_neighbors=1)

    # fitting the model
    modle = knn.fit(X_train, y_train)
    # predict the response
    pred = knn.predict(X_test)

    # evaluate accuracy
    print("the accuracy is")
    print(metrics.accuracy_score(y_test, pred))
    print(X_test.columns)
    print("The predicted position is")
    print(pred)
    if z==0:
        if Finish > pred:
            print("move forward")
            x=1
            return 1
        elif Finish < pred:
            print("move backward")
            y=1
            return 0
        elif Finish == pred:
            print("stop")
            return 100
        z = compare(x, y)

    elif z==1:
        if Finish > pred:
            print("move 1/2 forward")
            x = 0
            return 3
        elif Finish < pred:
            print("move 1/2 backward")
            y = 0
            return 4
        elif Finish == pred:
            print("stop")
            return 100
        z = compare(x, y)

if __name__ == '__main__':
    x = 0
    y = 0
    z = 0

    b=drivetopostion(6)
    print(b)

#drivetopostion(5)