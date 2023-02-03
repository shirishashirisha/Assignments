#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv('Q9_b.csv')


# In[3]:


df2=df.iloc[:,1:]
df2
           


# In[4]:


#skewness
df2.skew()


# In[5]:


#kurtosis
df2.kurt()


# In[6]:


f,ax=plt.subplots(figsize=(15,5))
plt.subplot(1,3,1)
plt.boxplot(df.SP)
plt.title('SP')
plt.subplot(1,3,2)
plt.boxplot(df.WT)
plt.title('WT')
plt.subplot(1,3,3)
plt.show()


# In[ ]:





# In[ ]:




