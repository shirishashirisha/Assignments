#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy import stats
from scipy.stats import norm


# In[2]:


# Assume Null Hypothesis is: Ho = Avg life of Bulb >= 260 days
# Alternate Hypothesis is: Ha = Avg life of Bulb < 260 days


# In[3]:


# find t-scores at x=260; t=(s_mean-P_mean)/(s_SD/sqrt(n))
t=(260-270)/(90/18**0.5)
t


# In[4]:


# Find P(X>=260) for null hypothesis


# In[5]:


# p_value=1-stats.t.cdf(abs(t_scores),df=n-1)... Using cdf function
p_value=1-stats.t.cdf(abs(-0.4714),df=17)
p_value


# In[6]:


#  OR p_value=stats.t.sf(abs(t_score),df=n-1)... Using sf function
p_value=stats.t.sf(abs(-0.4714),df=17)
p_value


# In[ ]:




