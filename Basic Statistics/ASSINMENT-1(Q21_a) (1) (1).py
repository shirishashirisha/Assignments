#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv('Cars.csv')


# In[3]:


df


# In[8]:


sns.distplot(df.MPG, label='df-MPG')
plt.xlabel('MPG')
plt.ylabel('Density')
plt.legend();
import warnings
warnings.filterwarnings('ignore')


# In[9]:


df.MPG.mean()


# In[10]:


df.MPG.median()


# In[ ]:




