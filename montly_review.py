import json
import os
from dateutil.parser import parse

HOMEDIR = "/Users/yif/Documents/GitHub/18755/"

folderPath1 = HOMEDIR + "result/" + '2016-01-01'
folderPath2 = HOMEDIR + "result/" + '2016-07-01'
folderPath3 = HOMEDIR + "result/" + '2017-01-01'
folderPath4 = HOMEDIR + "result/" + '2017-07-01'


def getRev():

    date1 = parse('2016/01/01')
    date2 = parse('2016/07/01')
    date3 = parse('2017/01/01')
    date4 = parse('2017/07/01')
    date5 = parse('2018/01/01')

    print(folderPath1)
    

    os.makedirs(folderPath1)
    os.makedirs(folderPath2)
    os.makedirs(folderPath3)
    os.makedirs(folderPath4)


    file = 'yelp_academic_dataset_review.json'
    print("loading all the review......")
    for line in open(HOMEDIR + file, 'r'):
        r = json.loads(line)
        date = parse(r["date"])

        if(date > date1):
            if date < date2:
                with open(folderPath1 + '/data.json', 'a') as fp:
                    json.dump(r, fp)
                    fp.write('\n')
            elif date < date3:
                with open(folderPath2 + '/data.json', 'a') as fp:
                    json.dump(r, fp)
                    fp.write('\n')
            elif date < date4:
                with open(folderPath3 + '/data.json', 'a') as fp:
                    json.dump(r, fp)
                    fp.write('\n')
            elif date < date5:
                with open(folderPath4 + '/data.json', 'a') as fp:
                    json.dump(r, fp)
                    fp.write('\n')

    print("finished!")
    return

def reduce_review():
    print('start time window 1')
    review_count = dict()
    for line in open(folderPath1 + '/data.json', 'r'):
        r = json.loads(line)
        busid = r["business_id"]
        if busid in review_count:
            (info, count) = review_count[busid]
            count += 1
            info.append(r)
            review_count[busid] = (info, count)
        else:
            review_count[busid] = ([r], 1)

    print("reducing the number of comments...")
    final_review = dict()
    for res in review_count:
        (info, count) = review_count[res]
        print(count)
        if count > 30:
            final_review[res] = info
    print("finished reducing")

    print("dumping in a json file....")
    for e in final_review:
        (info, count) = review_count[e]
        for e in info:
            with open(folderPath1 + '/reduced_data.json', 'a') as fp:
                json.dump(e, fp)
                fp.write('\n')
    print("finish dumping")

    print("start time window2 ...")
    review_count = dict()
    for line in open(folderPath2 + '/data.json', 'r'):
        
        r = json.loads(line)
        #print(r)
        busid = r["business_id"]
        if busid in review_count:
            (info, count) = review_count[busid]
            count += 1
            info.append(r)
            review_count[busid] = (info, count)
        else:
            review_count[busid] = ([r], 1)

    print("reducing the number of comments...")
    final_review = dict()
    for res in review_count:
        (info, count) = review_count[res]
        if count > 30:
            final_review[res] = info
    print("finished reducing")

    print("dumping in a json file....")
    for e in final_review:
        (info, count) = review_count[e]
        for e in info:
            with open(folderPath2 + '/reduced_data.json', 'a') as fp:
                json.dump(e, fp)
                fp.write('\n')
    print("finish dumping")

    print('start time window3')
    review_count = dict()
    for line in open(folderPath3 + '/data.json', 'r'):
        
        r = json.loads(line)
        #print(r)
        busid = r["business_id"]
        if busid in review_count:
            (info, count) = review_count[busid]
            count += 1
            info.append(r)
            review_count[busid] = (info, count)
        else:
            review_count[busid] = ([r], 1)

    print("reducing the number of comments...")
    final_review = []
    for res in review_count:
        (info, count) = review_count[res]
        if count > 100:
            final_review.extend(info)
    print("finished reducing")

    print(final_review)
    print("dumping in a json file....")
    for e in final_review:
        print(e)
        with open(folderPath3 + '/reduced_data.json', 'a') as fp:
            json.dump(e, fp)
            fp.write('\n')
    print("finish dumping")

    print('start time window4')
    review_count = dict()
    for line in open(folderPath4 + '/data.json', 'r'):
        
        r = json.loads(line)
        #print(r)
        busid = r["business_id"]
        if busid in review_count:
            (info, count) = review_count[busid]
            count += 1
            info.append(r)
            review_count[busid] = (info, count)
        else:
            review_count[busid] = ([r], 1)

    print("reducing the number of comments...")
    final_review = dict()
    for res in review_count:
        (info, count) = review_count[res]
        if count > 30:
            final_review[res] = info
    print("finished reducing")

    print("dumping in a json file....")
    for e in final_review:
        (info, count) = review_count[e]
        for e in info:
            with open(folderPath4 + '/reduced_data.json', 'a') as fp:
                json.dump(e, fp)
                fp.write('\n')
    print("finish dumping")

    return

def com2txt():
    business_c = []
    print("writing comments to txt ...")

    
    for line in open(folderPath3 + '/reduced_data.json', 'r'):
        
        r = json.loads(line)
        for e in r:
            print(e)
        #busid = r["business_id"]
        #rid = r["review_id"]
        #text = r["text"]
        #if not os.path.exists(folderPath1 + '/' + busid):
         #   os.makedirs(busid)
        #osPath = folderPath1 + '/' + busid + '/comment[' + rid + '].txt'
        #with open(osPath, 'a') as file:
        #    file.write('%s\n' % text.encode('utf-8'))

          
          
            

    return

'''
        if (parse(r["date"]) > parse(date1)) and (parse(r["date"]) < parse(date2)):
            busid = r["business_id"]
            if busid in review_count:
                (info, count) = review_count[busid]
                count += 1
                info.append(r)
                review_count[busid] = (info, count)
            else:
                review_count[busid] = ([r], 1)
    print("finished loading all reviews")

    print("reducing the number of comments...")
    final_review = dict()
    for res in review_count:
        (info, count) = review_count[res]
        if count > 100:
            final_review[res] = info
    print("finished reducing")

    print("dumping in a json file....")
    with open(folderPath + '/data.json', 'w') as fp:
        json.dump(final_review, fp)
    print("finish dumping")


    for res in final_review:
        (info, count) = final_review[res]
        path = folderPath + '/' + res
        if not os.path.exists(path):
            os.makedirs(path)
        count = 0
        for comment in info:
            count += 1
            text = comment["text"]
            osPath = path + '/comment[' + str(count) + '].txt'
            with open(osPath, 'w') as file:
                file.write("%s" % text.encode('utf-8'))

    print("finished!")'''
reduce_review()
#com2txt()
 #folderPath = "C:/Users/Farreltin/Documents/fall2018/CourseData/result/" + busid
            #if not os.path.exists(folderPath):
            #    os.makedirs(folderPath)
            #id = r["review_id"]
            #osPath = folderPath + '/comment[' + id + '].json'
            #with open(osPath, 'w') as file:
            #    json.dump(r, file)
            #review.append(r)
