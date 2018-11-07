import csv
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.neural_network import MLPClassifier

window = "4" # Change for each window
io_path = 'D:/Courses/18755/M2/Data/nodeVector/window'+window+'/XY_class.csv'
input_data = []
output_data = []

with open(io_path, mode="r") as f:
    reader = csv.reader(f)
    for line in reader:
        vector_input = line[1].split(',')
        vector_input[-1] = vector_input[-1][:-1]
        vector_input[0] = vector_input[0][1:]
        vector_output = line[2]

        input_data.append(list(map(float, vector_input)))
        output_data = output_data + list((vector_output))#(list(map(int, vector_output)))

X = np.array(input_data, dtype=float)
y = np.array(output_data, dtype=int)


x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

mlp = MLPClassifier(hidden_layer_sizes=(100,), max_iter=50, alpha=1e-4,
                    solver='sgd', verbose=10, tol=1e-4, random_state=1,
                    learning_rate_init=.1)


mlp.fit(x_train, y_train)

print(mlp.predict(x_test))
print("Training set score: %f" % mlp.score(x_train, y_train))
print("Test set score    : %f" % mlp.score(x_test, y_test))
