#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df=pd.read_csv("Q7.csv")
df


# In[5]:


# mean
df.mean()


# In[7]:


# Median
df.median()


# In[8]:


# Mode
df.Points.mode() 


# In[11]:


df.Score.mode()


# In[12]:


df.Weigh.mode()


# In[13]:


#variance
df.var()


# In[14]:


#Standard deviation
df.std()


# In[15]:


#range
df.describe()


# In[18]:


Points_Range=df.Points.max()-df.Points.min()
Points_Range


# In[19]:



Score_Range=df.Score.max()-df.Score.min()
Score_Range


# In[20]:


Weigh_Range=df.Weigh.max()-df.Weigh.min()
Weigh_Range


# In[24]:


f,ax=plt.subplots(figsize=(15,5))
plt.subplot(1,3,1)
plt.boxplot(df.Points)
plt.title('Points')
plt.subplot(1,3,2)
plt.boxplot(df.Score)
plt.title('Score')
plt.subplot(1,3,3)
plt.boxplot(df.Weigh)
plt.title('Weigh')
plt.show()


# In[ ]:




