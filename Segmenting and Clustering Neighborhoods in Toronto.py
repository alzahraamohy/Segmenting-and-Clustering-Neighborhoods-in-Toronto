#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import requests


# In[2]:


wiki = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
wiki_page = requests.get(wiki)

wiki_raw = pd.read_html(wiki_page.content, header = 0)[0]
df = wiki_raw[wiki_raw.Neighborhood != 'Not assigned']
df.reset_index(inplace = True)
df.head()


# In[3]:


df.groupby(['Postal Code']).first()


# In[4]:


len(df['Postal Code'].unique())


# In[5]:


df[df['Borough'] == 'Not assigned']


# In[6]:


df.shape


# In[ ]:




