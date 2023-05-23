#!/usr/bin/env python
# coding: utf-8

# In[37]:


import numpy as np
import statistics 
import math


# In[38]:


arr = np.arange(1,50)


# In[39]:


arr


# In[40]:


scores = np.random.randint(1,300,50)
scores


# In[8]:


np.median(scores)


# In[9]:


np.mean(scores)


# In[11]:


np.var(scores)


# In[12]:


np.std(scores)


# In[23]:


statistics.harmonic_mean(scores)


# In[24]:


statistics.mean(scores)


# In[25]:


statistics.median(scores)


# In[26]:


statistics.median_grouped(scores)


# In[27]:


statistics.median_high(scores)


# In[28]:


statistics.median_low(scores)


# In[29]:


statistics.mode(scores)


# In[30]:


statistics.pstdev(scores)


# In[31]:


statistics.stdev(scores)


# In[32]:


statistics.pvariance(scores)


# In[33]:


statistics.variance(scores)


# In[ ]:





# In[41]:


x = 23.45
print(math.ceil(x))


# In[42]:


math.copysign(4, -1)


# In[44]:


math.fabs(-12.23)


# In[45]:


math.factorial(5)


# In[47]:


val = np.random.uniform(1,223,10)
for i in val:
    print(math.ceil(i),end=" ")
val


# In[49]:


math.floor(15.84708)


# In[51]:


math.fmod(11,2)


# In[54]:


math.frexp(12)


# In[55]:


math.fsum([100, 400, 340, 500])


# In[63]:


math.isfinite(1435454645768757857)


# In[64]:


math.isinf(23)


# In[68]:


math.isnan(123)


# In[72]:


math.modf(3)


# In[73]:


math.exp(3)


# In[76]:


math.expm1(3)


# In[81]:


math.log(0.9)


# In[82]:


math.log1p(3)


# In[83]:


math.log2(3)


# In[84]:


math.log10(3)


# In[85]:


math.pow(2,4)


# In[86]:


math.sqrt(23)


# In[ ]:





# In[87]:


import numpy as np
import pandas as pd


# In[94]:


a = pd.read_excel('1234.xlsx')
a


# In[95]:


a.head()


# In[96]:


a.tail()


# In[100]:


a.loc[:,['Name','RateofMurder']]


# In[114]:


a['RateofMurder'].max()


# In[108]:


a['RateofMurder'].min()


# In[111]:


b=a['RateofMurder'].max()
pd.DataFrame([b])


# In[121]:


a.loc[:,['Name','RateofMurder','midPopulation']]


# In[127]:



a.iloc[[4],:]


# In[132]:


a = pd.read_excel('1234.xlsx')
a['midPopulation'] = a['midPopulation'].fillna(0)
a


# In[ ]:




