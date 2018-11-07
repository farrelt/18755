# importing necessary libraries
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import csv
import numpy as np

# loading the iris dataset



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


# dividing X, y into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# training a DescisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier

dtree_model = DecisionTreeClassifier(max_depth=2).fit(X_train, y_train)
dtree_predictions = dtree_model.predict(X_test)
print(score)
# creating a confusion matrix
cm = confusion_matrix(y_test, dtree_predictions)
