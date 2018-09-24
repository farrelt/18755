import json
from pprint import pprint

business_data = []
for line in open('yelp_academic_dataset_business.json', 'r'):
    business_data.append(json.loads(line))

pittsburgh_list = []
user_list = []
'print(type(business_data[9]["categories"]))'
for i in range(len(business_data)):
    if (business_data[i]["city"] == "Pittsburgh"):
        cat = business_data[i]["categories"]
        if not (cat is None):
            if ("Restaurants" in cat):
                pittsburgh_list.append(business_data[i])
                user_list.append(business_data[i]["review_count"])

'pprint(pittsburgh_list)'
print(len(pittsburgh_list))
print(sum(user_list))
