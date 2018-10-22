import json
from collections import defaultdict
import csv
from pathlib import Path

business_data = []
review_data = []
# Path where Rishabh's data is stored
print("Reading Business JSON")
for line_business in open('D:\Courses\\18755\yelp_dataset\yelp_academic_dataset_business.json', 'r', encoding="utf8"):
    business_data.append(json.loads(line_business))

print("Reading Review JSON")
for line_review in open('D:\Courses\\18755\yelp_dataset\yelp_academic_dataset_review.json', 'r', encoding="utf8"):
    review_data.append(json.loads(line_review))

list_of_business_id = []
for i in range(len(business_data)-2300):
    if business_data[i]["city"] == "Pittsburgh":
        cat = business_data[i]["categories"]    # Type of cat is 'str' and 'NoneType'

        # List of business id which are classified as "Restaurants"
        if not (cat is None):
            if "Restaurants" in cat and business_data[i]["business_id"] not in list_of_business_id:
                list_of_business_id.append(business_data[i]["business_id"])

print("Number of businesses: ", len(list_of_business_id))

print("Writing to CSV Files . . .")
path_to_csv = "D:\Courses\\18755\projectYelp\starRating"

for i in range(len(review_data)):
    bid = review_data[i]["business_id"]
    if bid in list_of_business_id:
        my_file = Path(path_to_csv+"\\"+str(bid)+".csv")
        if my_file.is_file():
            with open(my_file,'a', newline='') as fd:
                ff = csv.writer(fd)
                ff.writerow([review_data[i]["date"], review_data[i]["stars"] ])
        else:
            with open(my_file,'w', newline='') as fd:
                ff = csv.writer(fd)
                ff.writerow([review_data[i]["date"], review_data[i]["stars"] ])
