# Import scikit-learn dataset library
from sklearn import datasets
import numpy as np

# Load dataset
cancer = datasets.load_breast_cancer()

# Print the label types of cancer ("malignant", "benign")
print("Labels:", cancer.target_names)

# Print data (features) shape
print(cancer.data.shape)

# Print the cancer data (features)
print(cancer.data[0:5])

# Print the cancer labels (0: malignant, 1: benign)
print(cancer.target)

# Import train_test_split function
from sklearn.model_selection import train_test_split

# Split dataset into training set and test set
x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.3, random_state=109)
print(x_train)

# Import SVM model
from sklearn import svm

# Create SVM Classifier
clf = svm.SVC(kernel='rbf')  # RBF kernel

# Train the model using the training sets
clf.fit(x_train, y_train)

# Predict the response for test dataset
y_pred = clf.predict(x_test)
print(y_pred)

# Import scikit-learn metrics for accuracy calculation
from sklearn import metrics

# Model accuracy: how often is the classifier correct?
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

# Plotting test data
import matplotlib.pyplot as plt
plt.scatter(x_test[:, 0], x_test[:, 1], c='pink', alpha=0.4)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Scatter plot of test data')
plt.show()

# Plotting trained data
plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Scatter plot of training data')
plt.show()
