import json

business_data = []
# Path where Rishabh's data is stored
for line in open('D:\Courses\\18755\yelp_dataset\yelp_academic_dataset_business.json', 'r', encoding="utf8"):
    business_data.append(json.loads(line))

# Path where Farrelin's data is stored
# for line in open('yelp_academic_dataset_business.json', 'r'):
#    business_data.append(json.loads(line))

pittsburgh_list = []
user_list = []
sub_cat = []
sub_cat_u = []
for i in range(len(business_data)):
    if business_data[i]["city"] == "Pittsburgh":
        cat = business_data[i]["categories"]    # Type of cat is 'str' and 'NoneType'

        # Extract unique sub categories within the categories tab.
        if not (cat is None):
            if"Restaurants" not in cat.split(','):
                for sub_cat in cat.split(','):
                    if sub_cat.lstrip().rstrip() not in sub_cat_u:
                        sub_cat_u.append(sub_cat.lstrip().rstrip())
        # Conclusion: We should add the key words "Restaurants", "Restaurant" and "Food" to capture more of the data.

        if not (cat is None):
            if "Restaurants" or "Restaurant" or "Food" in cat:
                pittsburgh_list.append(business_data[i])
                user_list.append(business_data[i]["review_count"])

print("Unique Sub-categories : ", sub_cat_u)
print("Number of unique Sub-categories :", len(sub_cat_u))
print("Number of business :", len(pittsburgh_list))
print("Number of user comments to Analyze:", sum(user_list))
