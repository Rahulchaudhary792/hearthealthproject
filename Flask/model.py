#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('Heart.csv')
df


# In[3]:


df.columns


# In[4]:


df.ChestPain.nunique


# In[5]:


f = df.Ca.fillna(df.Ca.mean())
f


# In[6]:


l = df.Thal.fillna('normal')
l


# In[7]:


merge = pd.concat([df.drop(['Ca', 'Thal'], axis='columns'), f, l], axis='columns')
merge


# In[8]:


merge.isnull().sum()


# In[9]:


dummies1 = pd.get_dummies(merge.ChestPain)
dummies1


# In[10]:


dummies2 = pd.get_dummies(merge.Thal)
dummies2


# In[11]:


dummies3 = pd.get_dummies(merge.AHD)
dummies3


# In[12]:


final = pd.concat([merge.drop(['ChestPain', 'Thal', 'AHD'], axis='columns'), dummies1, dummies2, dummies3], axis='columns')
final


# In[13]:


final.isnull().sum()


# In[14]:


x = final.drop(['Unnamed: 0', 'No', 'Yes', 'Sex', 'Slope', 'RestECG', 'ExAng', 'Oldpeak'], axis='columns')
y = final.No


# In[15]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)


# In[16]:


x_train


# In[17]:


y_train


# In[18]:


from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression


# In[19]:


scores1 = cross_val_score(LinearRegression(), x, y, cv=10)
np.average(scores1)


# In[20]:


scores2 = cross_val_score(LogisticRegression(), x, y, cv=10)
np.average(scores2)


# In[21]:


from sklearn.svm import SVC


# In[22]:


scores3 = cross_val_score(SVC(C=50, gamma='auto'), x, y, cv=10)
np.average(scores3)


# In[23]:


from sklearn.tree import DecisionTreeClassifier


# In[24]:


scores4 = cross_val_score(DecisionTreeClassifier(), x, y, cv=10)
np.average(scores4)


# In[25]:


from sklearn.ensemble import RandomForestClassifier


# In[26]:


scores5 = cross_val_score(RandomForestClassifier(n_estimators=15), x, y, cv=10)
np.average(scores5)


# In[27]:


model = LogisticRegression()
model.fit(x_train, y_train)


# In[28]:


model.score(x_test, y_test)


# In[29]:


model.predict([[18, 57, 0, 159, 0.0, 0, 0, 1.0, 1, 0, 0, 1, 0]])


# In[30]:


from sklearn.metrics import confusion_matrix
y_pred = model.predict(x_test)
cm = confusion_matrix(y_test, y_pred)
cm


# In[31]:


import seaborn as sn


# In[32]:


sn.heatmap(cm, annot=True)


# In[34]:


from joblib import dump


# In[36]:


dump(model, 'hearthealth')


# In[37]:


from joblib import load
l = load('hearthealth')


# In[38]:


import pickle


# In[39]:


pickle.dump(model, open('model.pkl', 'wb'))


# In[40]:


model = pickle.load(open('model.pkl', 'rb'))


# In[ ]:




