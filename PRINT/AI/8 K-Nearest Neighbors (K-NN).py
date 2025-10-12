#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split


# In[5]:


#Load the Dataset
from sklearn.datasets import load_iris
iris = load_iris()

df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target
df
df['target']


# In[6]:


#Split the Data into Training and Test Sets
X_train, X_test, y_train, y_test = train_test_split(df[iris.feature_names], df['target'], random_state=0)
X_train, X_test, y_train, y_test 


# In[9]:


from sklearn.preprocessing import StandardScaler
scalar=StandardScaler()
scalar.fit(X_train)
X_train=scalar.transform(X_train)
X_test=scalar.transform(X_test)


from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train,y_train)

y_pred=classifier.predict(X_test)
y_pred


# In[12]:


from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))


# In[ ]:




