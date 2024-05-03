#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("C:\\Users\\Pranali\\Downloads\\records.csv")


# In[3]:


print(df)


# In[4]:


print(df.T)


# In[5]:


print(df.shape)


# In[6]:


print(df.size)


# In[7]:


import numpy as np


# In[8]:


import numpy as np

# Creating a 1D array
arr = np.array([1, 2, 3, 4])

# Reshaping the array to a 2D array with 5 rows and 2 columns
reshape_arr = arr.reshape(2, 2)

# Displaying the original and reshaped arrays
print("Original array:")
print(arr)
print("\nReshaped array:")
print(reshape_arr)


# In[ ]:




