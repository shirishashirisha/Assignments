#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import norm


# In[2]:


df=pd.read_csv('Cars.csv')
df


# In[3]:


sns.boxplot(df.MPG)


# In[4]:


# P(MPG>38)
1-stats.norm.cdf(38,df.MPG.mean(),df.MPG.std())


# In[5]:


# P(MPG<40)
stats.norm.cdf(40,df.MPG.mean(),df.MPG.std())


# In[9]:


# P (20
stats.norm.cdf(0.50,df.MPG.mean(),df.MPG.std())-stats.norm.cdf(0.20,df.MPG.mean(),df.MPG.std())          

 


# In[ ]:





# In[ ]:




