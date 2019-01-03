import csv
import pandas as pd

#A = -90
#B = -60
#C = -80
#D = -66
#P = 0
def make_the_csv(A,B,C,D):
    with open('mycsv.csv', 'w', newline='') as f:
        thewriter = csv.writer(f)

        thewriter.writerow(['BaseStation1','RSSI1','BaseStation2','RSSI2','BaseStation3','RSSI3','BaseStation4','RSSI4'])
        thewriter.writerow([ 1 ,A, 2 , B, 3 , C, 4 , D])

    filename = 'mycsv.csv'
    data = pd.read_csv(filename, index_col=None)
    print(data)

make_the_csv(-90,-60,-80,-66)