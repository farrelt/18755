import gensim
import nltk

from nltk import RegexpTokenizer
from os import listdir
from os.path import isfile, join
import re
import numpy
import os

HOMEDIR = "/Users/yif/Documents/GitHub/18755/"

folderPath1 = HOMEDIR + "result/" + '2016-01-01'
folderPath2 = HOMEDIR + "result/" + '2016-07-01'
folderPath3 = HOMEDIR + "result/" + '2017-01-01'
folderPath4 = HOMEDIR + "result/" + '2017-07-01'



tokenizer = RegexpTokenizer(r'w+')
stopword_set = set(line.strip() for line in open('english'))

# label sentence object
class LabeledLineSentence(object):
    def __init__(self, doc_list, labels_list):
        self.labels_list = labels_list
        self.doc_list = doc_list

    def __iter__(self):
        for idx, doc in enumerate(self.doc_list):
            yield gensim.models.doc2vec.TaggedDocument(doc,
                                                        [self.labels_list[idx]])


    # training the model
def createModel():

    print('creating models....')
    path = listdir(folderPath1)
    for folder in path:
        folderPath = folderPath1 + '/' + folder
        docLabels = [f for f in listdir(folderPath)]
        print(folderPath)
        data = readDoc(folderPath, docLabels)
        data = nlp_clean(data)
        it = LabeledLineSentence(data, docLabels)
        # 10 features should be good enough?
        model = gensim.models.Doc2Vec(size=10, min_count=0,
                                      alpha=0.025, min_alpha=0.025)
        model.build_vocab(it)
        # training of model
        for epoch in range(100):
            #print('iteration ' + str(epoch + 1))
            model.train(it, total_examples=model.corpus_count, epochs=model.epochs)
            model.alpha -= 0.002
            model.min_alpha = model.alpha

        # saving the created model
        model.save(folder + ".model")
        print("model saved")

        size = len(docLabels)
        G = numpy.zeros((size, size))
        print(size)
        print('Making Network....')
        for i in range(size):
            # using Regex to get the number of the two document we are comparing
            for j in range(i + 1, size):
                sim_doc = model.docvecs.similarity(i, j)
                G[m][n] = sim_doc
                G[n][m] = sim_doc
        numpy.savetxt(folder + ".csv", G, delimiter=",")
        print('NetWork saved.')

    return 0

def readDoc(folderPath, docLabels):
    data = []
    for doc in docLabels:
        data.append(open(folderPath+ '/' + doc).read())
    return data

    # preprocess the words

def nlp_clean(data):
    new_data = []
    for d in data:
        new_str = d.lower()
        dlist = tokenizer.tokenize(new_str)
        dlist = list(set(dlist).difference(stopword_set))
        new_data.append(dlist)
    return new_data

createModel()

