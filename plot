import csv

with open('firstNetwork.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    with open('FN_r3510c.csv', mode='a') as csv_network:
        csv_network = csv.writer(csv_network, delimiter=',')
        for row in csv_reader:
            row = list(map(float, row))
            for x in range(0, len(row)):
                if row[x] == 0.0:
                    row[x] = 0
                elif (row[x] > 0.75 ):
                    row[x] = 1
                else:
                    row[x] = 0
            # print(len(row))
            csv_network.writerow(row)
        #print(row)
csv_file.close()


import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
def show_graph_with_labels(adjacency_matrix):
    rows, cols = np.where(adjacency_matrix == 1)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    gr.add_edges_from(edges)
    nx.draw_random(gr)
    plt.show()
input_data = pd.read_csv('FN_r3510c.csv')

show_graph_with_labels(input_data)
print('done')
#import pandas as pd
#import networkx as nx
#input_data = pd.read_csv('FN.csv')
#G = nx.DiGraph(input_data.values)
#nx.draw(G)
