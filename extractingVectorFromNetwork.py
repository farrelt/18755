import networkx as nx
import csv
import numpy
import matplotlib.pyplot as plt
from node2vec import Node2Vec
import glob
import re
import ntpath

# INPUT PARAMETERS #
#--------------------------------------------------------------------------------------------------------------------#
window = 1  # Set the time window being analyzed
output_vector_dimension = 64
walk_length = 30
hyperParameter_p = 1
inoutParameter_q = 0.5
num_walk = 200
workers_parallel = 1
#--------------------------------------------------------------------------------------------------------------------#
fileName = glob.glob('D:/Courses/18755/M2/Data/window+'+window+'/*.csv') # Complie list of all similarity matrices.
pathName = str("D:/Courses/18755/M2/Data/nodeVector/window"+window+"/")

for csvFile in fileName:
    head, tail = ntpath.split(csvFile)  # Extract file name from path
    graph = nx.read_adjlist(csvFile)    # Creating graph from adjacency matrix (Scope for clean up and fine tuning here)
    node2vec = Node2Vec(graph, dimensions=output_vector_dimension,
                        walk_length=walk_length, num_walks=num_walk,
                        p=hyperParameter_p, q=inoutParameter_q,
                        workers=workers_parallel)
# Embed nodes
    model = node2vec.fit(window=10, min_count=1, batch_words=4)
    # Any keywords acceptable by gensim.Word2Vec can be passed, `diemnsions` and `workers`
    # are automatically passed (from the Node2Vec constructor)

# Save embeddings for later use
    model.wv.save_word2vec_format(pathName+"/embedding/"+tail[:-3]+"emb")

# Save model for later use
    model.save(pathName+"/model/"+tail[:-3]+"model")