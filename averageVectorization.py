import os
import glob
import numpy
import csv
import ntpath
from operator import add


window = "1" # Change for each window
results_XY = open('D:/Courses/18755/M2/Data/nodeVector/window'+window+'/XY.csv', 'a', newline='')
fileName_emb = glob.glob('D:/Courses/18755/M2/Data/nodeVector/window'+window+'/embedding/*.emb')

avg_vector = []
datafancy = []
with results_XY:
    for file in fileName_emb:
        head, tail = ntpath.split(file)
        writer = csv.writer(results_XY)
        data = open(file, 'r')  # Open file in read mode
        next(data)  # Skip first line containing irrelevant data
        sum_vector = [0]*64
        counter = 0
        for line in data:
            vector = (line.split(',')[-1]).split(" ")[1:]   # Extract the actual vector
            vector[-1] = vector[-1].strip() # Get rid of trailing \n
            vector_float = list(map(float, vector)) # Convert to float from string
            sum_vector =list(map(add, sum_vector, vector_float))    # Add all the vectors
            counter = counter + 1   # Keep track for averaging
        avg_vector = list(map(lambda x: x / counter, sum_vector))   # Calculate average
        datafancy.append([tail[:-4], avg_vector])   # Write to file
    writer.writerows(datafancy)
