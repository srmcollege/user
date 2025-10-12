#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from sklearn import datasets
wine=datasets.load_wine()
print(wine)


# In[2]:


print(wine.feature_names)

print(wine.target_names)


# In[3]:


x=pd.DataFrame(wine['data'])
print(x.head())


# In[5]:


y=print(wine.target)


# In[5]:


X_train, X_test, y_train, y_test = train_test_split(wine.data,wine.target,test_size=0.30, random_state=100)
X_train, X_test, y_train, y_test 


# In[6]:


#import naive bayes classifire
from sklearn.naive_bayes import GaussianNB
gnb=GaussianNB()
gnb.fit(X_train,y_train)
y_pred=gnb.predict(X_test)
print(y_pred)


# In[7]:


#accuracy
from sklearn import metrics
print(metrics.accuracy_score(y_test,y_pred))


# In[8]:


from sklearn.metrics import confusion_matrix
cm=np.array(confusion_matrix(y_test,y_pred))
cm


# In[ ]:




