import os
import glob
import ntpath

fileName_w1 = glob.glob('D:/Courses/18755/M2/Data/nodeVector/window1/embedding/*.emb')
fileName_w2 = glob.glob('D:/Courses/18755/M2/Data/nodeVector/window2/embedding/*.emb')
fileName_w3 = glob.glob('D:/Courses/18755/M2/Data/nodeVector/window3/embedding/*.emb')
fileName_w4 = glob.glob('D:/Courses/18755/M2/Data/nodeVector/window4/embedding/*.emb')

business_id_w1 = []
for file in fileName_w1:
    head, tail = ntpath.split(file)
    business_id_w1.append(tail[:-4])

business_id_w2 = []
for file in fileName_w2:
    head, tail = ntpath.split(file)
    business_id_w2.append(tail[:-4])

business_id_w3 = []
for file in fileName_w3:
    head, tail = ntpath.split(file)
    business_id_w3.append(tail[:-4])

business_id_w4 = []
for file in fileName_w4:
    head, tail = ntpath.split(file)
    business_id_w4.append(tail[:-4])
print("--------------------------------------------------------------------------------------------------------------")
print("No. of business in Window 1", len(business_id_w1))
print("No. of business in Window 2", len(business_id_w2))
print("No. of business in Window 3", len(business_id_w3))
print("No. of business in Window 4", len(business_id_w4))
print("--------------------------------------------------------------------------------------------------------------")
counter_same = 0
counter_dropped = 0
for name_w1 in business_id_w1:

    if name_w1 in business_id_w2:
        counter_same = counter_same + 1
    else:
        counter_dropped = counter_dropped + 1
print("Same businesses     ( 1 -> 2 ) : ", counter_same)
print("Dropped businesses  ( from 1 ) : ", counter_dropped)
print("New businesses      (  In 2  ) : ", len(business_id_w2) - counter_same)
print("--------------------------------------------------------------------------------------------------------------")
counter_same = 0
counter_dropped = 0
for name_w2 in business_id_w2:

    if name_w2 in business_id_w3:
        counter_same = counter_same + 1
    else:
        counter_dropped = counter_dropped + 1
print("Same businesses     ( 2 -> 3 ) : ", counter_same)
print("Dropped businesses  ( from 2 ) : ", counter_dropped)
print("New businesses      (  In 3  ) : ", len(business_id_w3) - counter_same)
print("--------------------------------------------------------------------------------------------------------------")
counter_same = 0
counter_dropped = 0
for name_w3 in business_id_w3:

    if name_w3 in business_id_w4:
        counter_same = counter_same + 1
    else:
        counter_dropped = counter_dropped + 1
print("Same businesses     ( 3 -> 4 ) : ", counter_same)
print("Dropped businesses  ( from 3 ) : ", counter_dropped)
print("New businesses      (  In 4  ) : ", len(business_id_w4) - counter_same)
print("--------------------------------------------------------------------------------------------------------------")
counter_same = 0
counter_dropped = 0
for name_w1 in business_id_w1:

    if name_w1 in business_id_w2 and name_w1 in business_id_w3 and name_w1 in business_id_w4:
        counter_same = counter_same + 1
    else:
        counter_dropped = counter_dropped + 1
print("Same businesses     ( 1 -> 4 ) : ", counter_same)
print("Dropped businesses  ( from 1 ) : ", counter_dropped)
print("New businesses      (  In 4  ) : ", len(business_id_w4) - counter_same)
print("--------------------------------------------------------------------------------------------------------------")
