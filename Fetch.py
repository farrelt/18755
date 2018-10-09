import json
from collections import defaultdict
from dateutil.parser import parse
import csv

business_data = []
review_data = []
# Path where Rishabh's data is stored
print("Reading Business JSON")
for line_business in open('D:\Courses\\18755\yelp_dataset\yelp_academic_dataset_business.json', 'r', encoding="utf8"):
    business_data.append(json.loads(line_business))

print("Reading Review JSON")
for line_review in open('D:\Courses\\18755\yelp_dataset\yelp_academic_dataset_review.json', 'r', encoding="utf8"):
    review_data.append(json.loads(line_review))


# Path where Farrelin's data is stored
# for line in open('yelp_academic_dataset_business.json', 'r'):
#    business_data.append(json.loads(line))

pittsburgh_list = []
list_of_business_id = []
for i in range(len(business_data)):
    if business_data[i]["city"] == "Pittsburgh":
        cat = business_data[i]["categories"]    # Type of cat is 'str' and 'NoneType'
        if not (cat is None):
            if "Restaurants" in cat and business_data[i]["business_id"] not in list_of_business_id:
                pittsburgh_list.append(business_data[i])
                list_of_business_id.append(business_data[i]["business_id"])


number_of_comments_Jun = 0

with open('Review_June.csv', 'w', newline='', encoding="utf-8") as csvfile:
    print("Writing to CSV File")
    writer = csv.writer(csvfile)
    for i in range(len(review_data)):
        if (review_data[i]["business_id"] in list_of_business_id) and parse("2018/06/30") > parse(review_data[i]["date"]) > parse("2018/06/01"):
            number_of_comments_Jun = number_of_comments_Jun + 1
            writer.writerow([review_data[i]["text"]])


print("Number of Comments to analyze J: ", number_of_comments_Jun)
