#!/usr/bin/env python
# coding: utf-8

# In[1]:


# plot1
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r--')
plt.show()


# In[2]:


import matplotlib.pyplot as plt
names = ['a', 'b', 'c']
values = [1, 10, 100]
plt.subplot(141)
plt.bar(names, values)
plt.subplot(142)
plt.scatter(names, values)
plt.subplot(143)
plt.plot(names, values, linewidth=5.0)
plt.subplot(144)
plt.plot(names, values, '--')
plt.show()


# In[3]:


import matplotlib.pyplot as plt
import numpy as np
# Creating dataset
sub = ['m1', 'm2', 'm3', 'bxe']
data = [23, 17, 35, 29]
# Creating plot
fig = plt.figure(figsize =(10, 7))
plt.pie(data, labels = sub)
plt.show()


# In[ ]:




