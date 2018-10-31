from analyze1 import loadingData
import gensim
import nltk
from nltk import RegexpTokenizer
from nltk.corpus import stopwords
from os import listdir
from os.path import isfile, join
import re
import numpy
import os



#running using Python 2.7

#label sentence object
class LabeledLineSentence(object):
    def __init__(self, doc_list, labels_list):
        self.labels_list = labels_list
        self.doc_list = doc_list
    def __iter__(self):
        for idx, doc in enumerate(self.doc_list):
              yield gensim.models.doc2vec.LabeledSentence(doc,
              [self.labels_list[idx]])
        
# network creating layer
class commentsLayer(object):
    def __init__(self):
        self.bus_id = []
        self.review = []
        self.folderPath = "C:/Users/Farreltin/Documents/fall2018/CourseData/result/"
        #print('prepare docLabels...')
        #self.docLabels = [f for f in listdir(self.folderPath)]
        #print('prepare data...')
        #self.data = self.readDoc()
        #print('finished initialization...')
        # two libraries used to preprocess the comment
        #self.tokenizer = RegexpTokenizer(r'\w+')
        #self.stopword_set = set(stopwords.words('english'))
    
    def initVariables(self):
        l = loadingData()
        self.bus_id = l.business_id
        self.review = l.review

        
    def readDoc(self):
        data = []
        for doc in self.docLabels:
            data.append(open(self.folderPath + doc).read())
        return data
    
    #create comment txt files
    def com2txt(self):
        business_c = []
        self.initVariables()
        print('Writing comments to txt...')

        for i in range(len(self.review)):
            text = self.review[i]["text"]
            busid = self.review[i]["business_id"]
            id = self.review[i]["review_id"]
            business_c.append(text)
            osPath = self.folderPath+ busid + 'comment[' + id+'].txt'
            with open(osPath,'w') as file:
                file.write("%s\n" % text.encode('utf-8'))
        print('finished writing txt!')
        return 0
    
    # preprocess the words
    def nlp_clean(self, data):
        new_data = []
        for d in data:
            new_str = d.lower()
            dlist = self.tokenizer.tokenize(new_str)
            dlist = list(set(dlist).difference(self.stopword_set))
            new_data.append(dlist)
        return new_data
    
    # training the model
    def createModel(self):
        self.initVariables()
        #self.com2txt()
        
        print('creating models....')
        self.data = self.nlp_clean(self.data)
        it = LabeledLineSentence(self.data, self.docLabels)
        # 50 features should be good enough?
        model = gensim.models.Doc2Vec(size=50, min_count=0, 
                            alpha=0.025, min_alpha=0.025)
        model.build_vocab(it)
        #training of model
        for epoch in range(100):
            print('iteration '+str(epoch+1))
            model.train(it, total_examples=model.corpus_count, epochs=model.iter)
            model.alpha -= 0.002
            model.min_alpha = model.alpha
            #saving the created model
        model.save("commentLayer.model")
        print("model saved")
        return 0
    
    def createNetwork(self):
        model = gensim.models.doc2vec.Doc2Vec.load('commentLayer.model')
        index = lambda nums: int(''.join(str(i) for i in nums)) 
        #generating index for each comments
        size = len(self.docLabels)
        G = numpy.zeros((size,size))
        print('Making Network....')
        for i in range(size):
            #using Regex to get the number of the two document we are comparing
            m = re.findall(r"\d", self.docLabels[i])
            m = index(m)
            for j in range(i+1, size):
                n = re.findall(r"\d", self.docLabels[j])
                n = index(n)
                sim_doc = model.docvecs.similarity(i,j)
                G[m][n] = sim_doc
                G[n][m] = sim_doc
        
        numpy.savetxt("firstLayer.csv", G, delimiter= ",")
        print('NetWork saved.')
        return 0

c = commentsLayer()
c.com2txt()
#c.createNetwork()







    
