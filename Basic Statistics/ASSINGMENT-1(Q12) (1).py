#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


x=pd.Series([34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56])


# In[3]:


#mean
x.mean()


# In[4]:


#median
x.median()


# In[5]:


#variance
x.var()


# In[6]:


#standard Deviation
x.std()


# In[7]:


plt.boxplot(x)


# In[ ]:




