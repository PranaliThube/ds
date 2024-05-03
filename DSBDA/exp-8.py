#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# In[9]:


data=pd.read_csv("C:\\Users\\Pranali\\Desktop\\DSBDA\\house (1).csv")


# In[10]:


print(data.columns) # This will show all the column names
print(data.head(10)) # Show first 10 records of dataframe
print(data.describe()) #You can look at summary of numerical fields by using de
print(data.shape)
print(data.isnull().sum())


# In[11]:


sns.relplot(x='median_house_value', y= 'total_bedrooms', data=data)


# In[12]:


sns.relplot(x='median_house_value', y= 'total_rooms', data=data)


# In[13]:


sns.relplot(x='median_house_value', y= 'population', data=data)


# In[14]:


sns.relplot(x='median_house_value', y= 'median_income', data=data)


# In[15]:


sns.relplot(x='median_house_value', y= 'households', data=data)


# In[16]:


sns.relplot(x='median_house_value', y= 'median_income', hue= 'total_rooms', data=data)
plt.show()


# In[17]:


train =data.drop(['median_house_value','longitude','latitude','housing_median_age'], axis=1)
test =data['median_house_value']


# In[18]:


x_train, x_test,  y_train, y_test = train_test_split(train, test, test_size=0.3, random_state=2)


# In[19]:


regr= LinearRegression()
regr.fit(x_train, y_train)
pred = regr.predict(x_test)
print(pred)
print(regr.score(x_test, y_test))


# In[ ]:




