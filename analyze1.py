import json
import os
from dateutil.parser import parse




HOMEDIR = "C:/Users/Farreltin/Documents/fall2018/CourseData/"

#creating an object to get each variable easier and don't have to change a lot of code
class loadingData(object):
    def __init__(self):
        print('loading bus_id...')
        self.business_id = self.getBid()
        print('load review for all of restaurants ...')
        self.review = self.getRev()
    
    def getBid(self):
        business_data = []
        file = 'yelp_academic_dataset_business.json'
        for line in open(HOMEDIR + file, 'r', encoding="utf8"):
            business_data.append(json.loads(line))
        
        pittsburgh_list = []
        business_id = []

        count = 0

        while count < 2000
            for i in range(len(business_data)):
                cat = business_data[i]["categories"]
                if not (cat is None):
                    if ("Restaurants" in cat):
                        pittsburgh_list.append(business_data[i])
                        business_id.append(business_data[i]["business_id"])
        business_id = business_id[0:2000]
        print('done!')
        return business_id
    
    def getRev(self):
        review = []
        file = 'yelp_academic_dataset_review.json'
        for line in open(HOMEDIR + file, 'r', encoding="utf8"):
            r = json.loads(line)
            if r["business_id"] in self.business_id:
                if (parse(r["date"]) > parse("2017/01/01")) and (parse(r["date"]) < parse("2017/07/01")):
                    busid = r["business_id"]
                    folderPath = "C:/Users/Farreltin/Documents/fall2018/CourseData/result/" + busid
                    if not os.path.exists(folderPath):
                        os.makedirs(folderPath)
                    id = r["review_id"]
                    osPath = folderPath + '/comment[' + id + '].json'
                    with open(osPath, 'w') as file:
                        json.dump(r, file)
                    review.append(r)
        return review
    
    def run(self):
        return 0

a = loadingData()
a.run()