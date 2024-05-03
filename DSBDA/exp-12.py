#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np


# In[7]:


df=pd.read_csv("C:\\Users\\Pranali\\Downloads\\records.csv")


# In[8]:


#3. Filling the Missing Values – Imputation
updated_df = df
updated_df['Salary']=updated_df['Salary'].fillna(updated_df['Salary'].mean())
print(updated_df)


# In[9]:


#4. Imputation with an additional column
updated_df = df
updated_df['Salaryismissing'] = updated_df['Salary'].isnull()
print(updated_df)


# In[10]:


#5. Filling with a Regression Model
testdf = df[df['Salary'].isnull()==True]
traindf = df[df['Salary'].isnull()==False]
traindf.drop("Salary",axis=1,inplace=True)
testdf.drop("Salary",axis=1,inplace=True)
print(traindf)


# In[ ]:




