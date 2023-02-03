#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv("Q9_a.csv")


# In[3]:


df


# In[4]:


# Skewness
df.skew()


# In[5]:


# Kurtosis
df.kurt()


# In[6]:


f,ax=plt.subplots(figsize=(15,5))
plt.subplot(1,3,1)
plt.boxplot(df.speed)
plt.title('speed')
plt.subplot(1,3,2)
plt.boxplot(df.dist)
plt.title('dist')
plt.show()


# In[ ]:





# In[ ]:




