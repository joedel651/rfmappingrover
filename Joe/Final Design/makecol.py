from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
import csv
import pandas as pd

P = 0

with open('median114copy.csv', 'r+') as csvFile:
    reader = csv.reader(csvFile, delimiter=',', quotechar='"')
    writer = csv.writer(csvFile, delimiter=',', quotechar='"')

    for row in reader:
        row[1] = [0,1,2,3,4,'bacon','taste']
        writer.writerow(row)


#ilename = 'median114copy.csv'
#data = pd.read_csv(filename, index_col=None)

