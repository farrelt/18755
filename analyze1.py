import json

#creating an object to get each variable easier and don't have to change a lot of code
class loadingData(object):
    def __init__(self):
        print('loading bus_id...')
        self.business_id = self.getBid()
        print('load review for all of restaurants ...')
        self.review = self.getRev()
    
    def getBid(self):
        business_data = []
        for line in open('yelp_academic_dataset_business.json', 'r'):
            business_data.append(json.loads(line))
        
        pittsburgh_list = []
        business_id = []
        #star = []

        #print(business_data[0])
        for i in range(len(business_data)):
            if (business_data[i]["city"] == "Pittsburgh"):
                cat = business_data[i]["categories"]
                if not (cat is None):
                    if ("Restaurants" in cat):
                        pittsburgh_list.append(business_data[i])
                        business_id.append(business_data[i]["business_id"])
                        #star.append(business_data[i]["stars"])
        return business_id
    
    def getRev(self):
        review = []
        for line in open('yelp_academic_dataset_review.json', 'r'):
            review.append(json.loads(line))
        #print(review[0])
        return review
    
    def run(self):
        #print(self.business_id[0])
        return 0

'''a = Thai()
a.run()'''