#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#stop word remove
#lemmatisation
#steaming

import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
example_text = "Hello Mr. Pravin, how are you doing today? The weather in lonavala israiny. The sky is full of cloud."
print(sent_tokenize(example_text))
print(word_tokenize(example_text))

# In[1]:


import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
print(stop_words)


# In[2]:


import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
lemmatizer = WordNetLemmatizer()
input_str = "There are several cities with mice."
input_str = nltk.word_tokenize(input_str)
print (input_str)
for word in input_str:
 print(lemmatizer.lemmatize(word))


# In[3]:


import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
stemmer = PorterStemmer()
input_str = "There are several types of stemming algorithms."
input_str = nltk.word_tokenize(input_str)
print (input_str)
for word in input_str:
 print(stemmer.stem(word))


# In[ ]:




