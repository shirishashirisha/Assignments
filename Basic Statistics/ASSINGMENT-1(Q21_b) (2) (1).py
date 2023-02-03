#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


wcat=pd.read_csv('wc-at.csv')
wcat


# In[6]:


# plotting distribution for Waist Circumference (Waist) 
sns.distplot(wcat.Waist)
plt.ylabel('density');
import warnings
warnings.filterwarnings('ignore')


# In[9]:


# plotting distribution for Adipose Tissue (AT) 
sns.distplot(wcat.AT)
plt.ylabel('density');
import warnings
warnings.filterwarnings('ignore')


# In[10]:


# WC
wcat.Waist.mean() , wcat.Waist.median()


# In[11]:


# AT
wcat.AT.mean() , wcat.AT.median()


# In[ ]:




