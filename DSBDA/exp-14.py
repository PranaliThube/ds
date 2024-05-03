#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install textblob


# In[2]:


from textblob import TextBlob


# In[3]:


f1= "The Food at Radison was awesome"
f2 = "The Food at Radison was very good"


# In[8]:


b1=TextBlob(f1)
b2=TextBlob(f1)


# In[9]:


b1.sentiment


# In[10]:


b2.sentiment


# In[ ]:




