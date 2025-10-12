#!/usr/bin/env python
# coding: utf-8

# In[2]:


dataset=[['milk','onion','nutmeg','kidney beans','eggs','yogurt'],
       ['dill','onion','nutmeg','kidney beans','eggs','yogurt'],
       ['milk','apple','kidney beans','eggs'],
       ['milk','unicorn','corn','kidney beans','yogurt'],
       ['corn','onion','onion','kidney beans','ice cream','eggs']]


# In[3]:


import mlxtend
from mlxtend.frequent_patterns import apriori


# In[5]:


import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
dataset
te=TransactionEncoder()
te_ary=te.fit(dataset).transform(dataset)

df=pd.DataFrame(te_ary,columns=te.columns_)
df


# In[7]:


from mlxtend.frequent_patterns import apriori
frequent_itemset=apriori(df,min_support=0.6,use_colnames=True)
frequent_itemset


# In[11]:


#association rule mining
from mlxtend.frequent_patterns import association_rules
res=association_rules(frequent_itemset,metric="confidence",min_threshold=0.7)
res


# In[12]:


res1=res[['antecedents','consequents','support','confidence','lift']]
res1


# In[14]:


res2=res1[res1['confidence']>=1]
res2


# In[ ]:




