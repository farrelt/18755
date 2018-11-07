import numpy as np
import os
import glob
import csv
#import ntpat
from operator import add
# X = (hours studying, hours sleeping), y = score on test, xPredicted = 4 hours studying & 8 hours sleeping (input data for prediction)

window = "1" # Change for each window
#input_path = 'D:/Courses/18755/M2/Data/nodeVector/window'+window+'/XY.csv'
output_path = 'D:/Courses/18755/M2/Data/nodeVector/window'+window+'/star.csv'
results_oneHot = open('D:/Courses/18755/M2/Data/nodeVector/window'+window+'/oneHot.csv', 'a', newline='')
#input_data = []
output_data = []
writer = csv.writer(results_oneHot)
one_hot = []
with open(output_path, "r") as f:
    reader = csv.reader(f)
    for line in (reader):
        #print(line[0])
        vector = line[1].split(',')
        output_data.append(float(vector[0]))
        rating = float(vector[0])
        if (rating >= 0.0 and rating <= 1.0):
            one_hot.append([line[0],[1,0,0,0,0]])
        elif (rating > 1.0 and rating <= 2.0):
            one_hot.append([line[0],[0,1,0,0,0]])
        elif (rating > 2.0 and rating <= 3.0):
            one_hot.append([line[0],[0,0,1,0,0]])
        elif (rating > 3.0 and rating <= 4.0):
            one_hot.append([line[0],[0,0,0,1,0]])
        elif (rating > 4.0 and rating <= 5.0):
            one_hot.append([line[0],[0,0,0,0,1]])
        else:
            print("Error")
print(one_hot)
writer.writerows(one_hot)

y = np.array(output_data, dtype=float)