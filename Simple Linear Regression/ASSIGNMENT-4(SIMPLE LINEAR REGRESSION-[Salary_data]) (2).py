#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
# reading a csv file using pandas library
df =pd.read_csv("Salary_Data.csv")
df
pd.set_option('display.min_rows', None) 


# In[2]:


df.shape    


# In[31]:


df


# In[6]:


df.head()


# In[5]:


df.describe()   


# In[33]:


df.info() 


# In[34]:


df.columns 


# In[35]:


plt.boxplot(df.YearsExperience) 
plt.show() 


# In[36]:


plt.hist(df.YearsExperience) 
plt.show() 


# In[ ]:





# In[37]:


plt.boxplot(df.Salary) 
plt.xlabel("Salary") 
plt.ylabel("No of Observations")
plt.title("Boxplot of Salary") 
plt.show()    


# In[38]:


plt.hist(df.Salary)
plt.show()   


# In[39]:


import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
sns.distplot(df['Salary']) 
plt.show()  


# In[40]:


sns.distplot(df['YearsExperience']) 


# In[41]:


import matplotlib.pyplot as plt
plt.plot(df.YearsExperience,df.Salary,"rs")
plt.xlabel("YearsExperience")
plt.ylabel("Salary")
plt.title("ScatterPlot")   


# In[42]:


# correlation


# In[43]:


df.corr() 


# In[ ]:





# In[44]:


# building model


# In[45]:


import statsmodels.formula.api as smf
model=smf.ols("Salary~YearsExperience",data=df).fit()
model.params 


# In[46]:


model.summary() 


# In[47]:


model.resid  


# In[48]:


model.resid_pearson


# In[49]:


pred = model.predict(df.YearsExperience)
#pred = model.predict(df.iloc[:,0]) 
pred  


# In[ ]:





# In[ ]:





# In[50]:


#print(model.conf_int(0.05))


# In[51]:


rmse_lin = np.sqrt(np.mean((np.array(df['Salary'])-np.array(pred))**2))
rmse_lin   


# In[52]:


import matplotlib.pyplot as plt
plt.scatter(x=df['YearsExperience'],y=df['Salary'],color='red')
plt.plot(df['YearsExperience'],pred,color='black')
plt.xlabel('YE')
plt.ylabel('Salary') 


# In[53]:


model2=smf.ols("Salary~np.log(YearsExperience)",data=df).fit()


# In[54]:


model2.summary()


# In[56]:


model2.params


# In[57]:


model2.tvalues


# In[58]:


model2.pvalues


# In[59]:


model2.resid


# In[60]:


model2.resid_pearson


# In[61]:


pred2 = model2.predict(pd.DataFrame(df['YearsExperience'])) 
pred2  


# In[62]:


pred2
rmse_log = np.sqrt(np.mean((np.array(df['Salary'])-np.array(pred2))**2))
rmse_log   


# In[63]:


pred2.corr(df.Salary)


# In[65]:


import matplotlib.pyplot as plt
plt.scatter(x=df['YearsExperience'],y=df['Salary'],color='red')
plt.plot(df['YearsExperience'],pred2,color='black')
plt.xlabel('YE')
plt.ylabel('Salary') 


# In[ ]:





# In[69]:


#exponential model
model3 = smf.ols('np.log(Salary)~YearsExperience',data=df).fit()
model3.params
model3.summary()


# In[70]:


pred_log = model3.predict(pd.DataFrame(df['YearsExperience']))


# In[71]:


pred_log


# In[72]:


pred3=np.exp(pred_log)  # as we have used log(AT) in preparing model so we need to convert it back
pred3


# In[73]:


rmse_exp = np.sqrt(np.mean((np.array(df['Salary'])-np.array(pred3))**2)) 
rmse_exp 


# In[74]:


import matplotlib.pyplot as plt
plt.scatter(x=df['YearsExperience'],y=df['Salary'],color='red')
plt.plot(df['YearsExperience'],pred3,color='black')
plt.xlabel('YE')
plt.ylabel('Salary') 


# In[75]:


plt.plot(df['YearsExperience'],df['Salary'], 'bo')  
plt.plot(df.YearsExperience,pred3,color='red')


# In[76]:


student_resid = model3.resid_pearson 
student_resid


# In[77]:


plt.plot(model3.resid_pearson,'o')
plt.axhline(y=0,color='green')
plt.xlabel("Observation Number")
plt.ylabel("Standardized Residual") 


# In[79]:


plt.scatter(x=pred3,y= df.Salary)
plt.xlabel("Predicted")
plt.ylabel("Actual")


# In[81]:


df["YearsExperience_Sq"] = df.YearsExperience*df.YearsExperience


# In[82]:


df


# In[85]:


model_quad = smf.ols("np.log(Salary)~YearsExperience+YearsExperience_Sq",data=df).fit()
model_quad.params


# In[86]:


model_quad.summary()


# In[88]:


pred_quad = model_quad.predict(df)
pred4=np.exp(pred_quad)  # as we have used log(AT) in preparing model so we need to convert it back
pred4


# In[89]:


rmse_quad = np.sqrt(np.mean((np.array(df['Salary'])-np.array(pred4))**2))
rmse_quad 


# In[90]:


plt.scatter(df.YearsExperience,df.Salary,c="b")
plt.plot(df.YearsExperience,pred4,"r") 


# In[94]:


model_quad.resid


# In[95]:


model_quad.resid_pearson


# In[97]:


plt.plot(np.arange(30),model_quad.resid_pearson)
plt.axhline(y=0,color='red')
plt.xlabel("Observation Number")
plt.ylabel("Standardized Residual") 


# In[98]:


plt.scatter(np.arange(30),model_quad.resid_pearson)
plt.axhline(y=0,color='red')
plt.xlabel("Observation Number")
plt.ylabel("Standardized Residual")  


# In[99]:


plt.hist(model_quad.resid_pearson)
plt.show()


# In[100]:


data = {"MODEL":pd.Series(["rmse_lin","rmse_log","rmse_exp","rmse_quad"]),
        "RMSE_Values":pd.Series([rmse_lin,rmse_log,rmse_exp,rmse_quad]),
        "Rsquare":pd.Series([model.rsquared,model2.rsquared,model3.rsquared,model_quad.rsquared])}
table=pd.DataFrame(data)
table 


# In[101]:


print(plt.style.available)  


# In[102]:


import matplotlib.pyplot as plt
plt.style.use('classic')     


# In[103]:


plt.hist(model_quad.resid_pearson)  
plt.show() 


# In[104]:


plt.scatter(df.YearsExperience,df.Salary,c="b")
plt.plot(df.YearsExperience,pred4,"r")

