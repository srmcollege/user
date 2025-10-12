#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing models
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import AdaBoostClassifier
import pandas as pd

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

import warnings
warnings.filterwarnings("ignore")


# In[10]:


import os
os.listdir("E:\Backup 24\D Backup 24\College stuff\T.Y.C.S")


# In[3]:


df=pd.read_csv("E:\Backup 24\D Backup 24\College stuff\T.Y.C.S\heart.csv")
df
rows=df.shape[0]
columns=df.shape[1]
print(rows,columns)   #input variable x and y

y=df['target']
print(y)

x=df.drop('target',axis=1)
print(x)


# In[4]:


X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=.25,random_state=42323232)
X_train, X_test, y_train, y_test 


# In[19]:


log_clf=LogisticRegression()
rnd_clf=RandomForestClassifier()
svm_clf=SVC()
nbg_clf=GaussianNB()

for clf in(log_clf,rnd_clf,svm_clf,nbg_clf):
    clf.fit(X_train,y_train)
    
    y_pred=clf.predict(X_test)
    print(clf.__class__.__name__,accuracy_score(y_test,y_pred))
    


# In[5]:


from sklearn.svm import SVC
svc_clf=SVC(probability=True,kernel='linear')


# In[6]:


# AdaboostClassifier with SVM
boost=AdaBoostClassifier(base_estimator=svc_clf,n_estimators=500,algorithm='SAMME',learning_rate=0.5)
boost.fit(X_train,y_train)

y_pred=boost.predict(X_test)
print("Boosting with SVM classifire",accuracy_score(y_test,y_pred))    


# In[26]:


#training score
boost.score(X_train,y_train)


# In[28]:


#testing score
boost.score(X_test,y_test)


# In[ ]:




####################### Inbuilt Dataset ########################

more for (eg. load_digits(),load_breast_cancer() )


#!/usr/bin/env python
# coding: utf-8

# Importing models
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import warnings
warnings.filterwarnings("ignore")

# Load built-in Breast Cancer dataset
data = load_iris()
x = data.data
y = data.target

print("Feature shape:", x.shape)
print("Labels:", data.target_names)

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

# Define classifiers
log_clf = LogisticRegression()
rnd_clf = RandomForestClassifier()
svm_clf = SVC()
nbg_clf = GaussianNB()

# Train and evaluate each classifier
for clf in (log_clf, rnd_clf, svm_clf, nbg_clf):
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(clf.__class__.__name__, "Accuracy:", accuracy_score(y_test, y_pred))

# AdaBoost with SVM
svc_clf = SVC(probability=True, kernel='linear')
boost = AdaBoostClassifier(estimator=svc_clf, n_estimators=50, algorithm='SAMME', learning_rate=0.5)
boost.fit(X_train, y_train)
y_pred = boost.predict(X_test)
print("Boosting with SVM classifier:", accuracy_score(y_test, y_pred))

# Training and testing scores
print("Training Score:", boost.score(X_train, y_train))
print("Testing Score:", boost.score(X_test, y_test))


######################### Create your own Binary Dataset (Inbuilt) #####################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score, classification_report

# -----------------------------
# Create a custom binary dataset
# -----------------------------
data = {
    'Age':        [25, 45, 52, 23, 40, 60, 35, 48, 55, 30],
    'BloodPressure':[120, 140, 130, 110, 135, 150, 125, 145, 138, 128],
    'Cholesterol':[180, 220, 210, 190, 200, 230, 195, 215, 225, 185],
    'Diabetes':   [0, 1, 0, 0, 1, 1, 0, 1, 1, 0],
    'HeartDisease':[0, 1, 1, 0, 1, 1, 0, 1, 1, 0]  # Target variable (binary)
}

df = pd.DataFrame(data)
print("Custom Dataset:")
print(df)

# -----------------------------
# Split features and target
# -----------------------------
X = df.drop('HeartDisease', axis=1)
y = df['HeartDisease']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# -----------------------------
# Train AdaBoost with Decision Tree (weak learner)
# -----------------------------
weak_clf = DecisionTreeClassifier(max_depth=1)
ada_clf = AdaBoostClassifier(estimator=weak_clf, n_estimators=10, learning_rate=1.0, algorithm='SAMME.R')
ada_clf.fit(X_train, y_train)

y_pred = ada_clf.predict(X_test)

# -----------------------------
# Evaluate Performance
# -----------------------------
print("\nAdaBoost Ensemble Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))




######################### Create your own Binary Dataset (Different .csv file) #####################
import pandas as pd

# Create custom binary dataset
data = {
    'Age':         [25, 45, 52, 23, 40, 60, 35, 48, 55, 30, 42, 50, 28, 46, 38, 57, 33, 49, 36, 54],
    'BloodPressure':[120, 140, 130, 110, 135, 150, 125, 145, 138, 128, 132, 142, 118, 136, 126, 148, 124, 143, 129, 139],
    'Cholesterol':[180, 220, 210, 190, 200, 230, 195, 215, 225, 185, 198, 218, 182, 205, 192, 223, 187, 217, 193, 212],
    'Diabetes':    [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    'HeartDisease':[0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)
df.to_csv("binary_dataset.csv", index=False)
df.head()


******
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

# Load the CSV dataset
df = pd.read_csv("binary_dataset.csv")

# Split features and target
X = df.drop('HeartDisease', axis=1)
y = df['HeartDisease']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# AdaBoost with Decision Tree as weak learner
weak_clf = DecisionTreeClassifier(max_depth=1)
ada_clf = AdaBoostClassifier(estimator=weak_clf, n_estimators=10, learning_rate=1.0)
ada_clf.fit(X_train, y_train)

# Predict and evaluate
y_pred = ada_clf.predict(X_test)

print("AdaBoost Ensemble Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
