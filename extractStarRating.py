import os
import glob
import ntpath
import json
from collections import defaultdict
import csv
from pathlib import Path

data = []
business_id = []

dict = {}
fileName_emb = glob.glob('D:/Courses/18755/M2/Data/nodeVector/window4/embedding/*.emb')
results_XY = open('D:/Courses/18755/M2/Data/nodeVector/window4/star.csv', 'a', newline='')

for file in fileName_emb:
    head, tail = ntpath.split(file)
    business_id.append(tail[:-4])
    dict[str((tail[:-4]))] = []
print(business_id)
review_data = []
print("Reading Data JSON")
for line_business in open('D:/Courses/18755/M2/drive-download-20181104T230128Z-001/2017-07-01/data.json', 'r', encoding="utf8"):
    data.append(json.loads(line_business))


for i in range(len(data)):
    if data[i]["business_id"] in business_id:
        if str(data[i]["business_id"]) in dict:
            dict[str(data[i]["business_id"])].append(data[i]["stars"])

datafancy = []
star = []

writer = csv.writer(results_XY)
for k in dict.keys():
    star = dict.get(k)
    s = float((sum(star)))
    l = float((len(star)))
    if(l == 0.0):
        datafancy.append([k, 0])
    else:
        datafancy.append([k, (s/l)])
writer.writerows(datafancy)
print(datafancy)
