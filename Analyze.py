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
user_list = []
sub_cat = []
sub_cat_u = []
list_of_business_id = []
for i in range(len(business_data)):
    if business_data[i]["city"] == "Pittsburgh":
        cat = business_data[i]["categories"]    # Type of cat is 'str' and 'NoneType'

        # Extract unique sub categories within the categories tab.
        """
        if not (cat is None):
            if "Restaurants" not in cat.split(','):
                for sub_cat in cat.split(','):
                    if sub_cat.lstrip().rstrip() not in sub_cat_u:
                        sub_cat_u.append(sub_cat.lstrip().rstrip())
        # Conclusion: We should add the key words "Restaurants", "Restaurant" and "Food" to capture more of the data.
        """
        if not (cat is None):
            if "Restaurants" in cat and business_data[i]["business_id"] not in list_of_business_id:
                pittsburgh_list.append(business_data[i])
                user_list.append(business_data[i]["review_count"])
                list_of_business_id.append(business_data[i]["business_id"])

"""
print("Unique Sub-categories : ", sub_cat_u)
print("Number of unique Sub-categories :", len(sub_cat_u))
print("Number of business :", len(pittsburgh_list))
print("Number of user comments to Analyze:", sum(user_list))
print(list_of_business_id)
"""

d = defaultdict(list)
number_of_comments = 0
with open('Review.csv', 'w', newline='', encoding="utf-8") as csvfile:
    print("Writing to CSV File")
    writer = csv.writer(csvfile)
    for i in range(len(review_data)):
        if (review_data[i]["business_id"] in list_of_business_id) and parse(review_data[i]["date"]) > parse("2016/01/01"):
            number_of_comments = number_of_comments + 1
            writer.writerow([review_data[i]["text"]])

print("Number of Comments to analyze : ", number_of_comments)
