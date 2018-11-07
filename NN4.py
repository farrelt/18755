import csv
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score

window = "1" # Change for each window
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

print(X)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=1)

logisticRegr = LogisticRegression(solver='lbfgs', multi_class='multinomial')

logisticRegr.fit(x_train, y_train)

predictions = logisticRegr.predict(x_test)

score = logisticRegr.score(x_test, y_test)
score = logisticRegr.score(X, y)
print("SCORE : ",score)

print("F1 Score : ", f1_score(y_test, predictions, average='micro'))

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics

print(y_test)
print(predictions)
cm = metrics.confusion_matrix(y_test, predictions)
print(cm)

plt.figure(figsize=(4,4))
sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square = True, cmap = 'Blues_r');
plt.ylabel('Actual label');
plt.xlabel('Predicted label');
all_sample_title = 'Accuracy Score: {0}'.format(score)
plt.title(all_sample_title, size = 15);
plt.show()