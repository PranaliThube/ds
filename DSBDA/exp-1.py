#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


data={"Roll-num": [10,20,30,40,50,60,701], "Age":[12,14,13,12,14,13,15],"NAME":['John', 'Camill','Rheana','Joseph', 'Amanti','Alexa','Siri']}


# In[9]:


block = pd.DataFrame(data)


# In[18]:


print("Original Data frame:\n", block)


# In[11]:


print(block)


# In[12]:


print(block.loc[[0,1,3]])


# In[13]:


print(block.loc[0:3])


# In[14]:


print(block.loc[0:2,['Age','NAME']])


# In[17]:


print(block.iloc[[0,1,3,6],[0,2]])


# In[ ]:


##Merging


# In[19]:


import pandas as pd 


# In[20]:


d1 = {'Name': ['Pankaj', 'Meghna', 'Lisa'], 'Country': ['India', 'India', 'USA'], 'Role': ['CEO','CTO','CTO']}


# In[21]:


df1 =pd.DataFrame(d1)


# In[22]:


print('Datafreame 1:\n',df1)


# In[24]:


df2 =pd.DataFrame({'ID':[1,2,3],'Name':['Pankaj','Anupam','Amit']})


# In[25]:


print('Datafreame 2:\n',df2)


# In[26]:


df_merged = df1.merge(df2)


# In[28]:


print('Result Inner join:\n',df_merged)


# In[30]:


print('Result left join:\n',df1.merge(df2,how='left'))


# In[31]:


print('Result right join:\n',df1.merge(df2,how='right'))


# In[34]:


print('Result outer join:\n',df1.merge(df2,how='outer'))

