#!/usr/bin/env python
# coding: utf-8
UNIVERSAL FUNCTIONS

ufunc Intro-zip, add
ufunc Create Function
ufunc Simple Arithmetic
ufunc Rounding Decimals
ufunc Logs
ufunc Summations
ufunc Products
ufunc Differences

Mathematical Methods

math.ceil() Rounds a number up to the nearest integer
math.exp()  Returns E raised to the power of x
math.fabs() Returns the absolute value of a number
math.factorial()Returns the factorial of a number
math.floor()      Rounds a number down to the nearest integer
math.fmod() Returns the remainder of x/y
math.fsum() Returns the sum of all items in any iterable (tuples, arrays, lists, etc.)
math.gcd()  Returns the greatest common divisor of two integers
math.isclose()    Checks whether two values are close to each other, or not
math.isfinite()   Checks whether a number is finite or not
math.isinf()      Checks whether a number is infinite or not
math.isnan()      Checks whether a value is NaN (not a number) or not
math.log()  Returns the natural logarithm of a number, or the logarithm of number to base
math.perm() Returns the number of ways to choose k items from n items with order and without repetition
math.pow()  Returns the value of x to the power of y
math.prod() Returns the product of all the elements in an iterable
math.remainder()Returns the closest value that can make numerator completely divisible by the denominator
math.sqrt() Returns the square root of a number
math.trunc()      Returns the truncated integer parts of a number

statistical methods in Pandas

minimum value
maximum value
mean
median
standard deviation
mode
Describe Method
count
cumsum
cumprod


comparison methods

df = pd.DataFrame({'Tops':    [15, 20, 25],
                   'Coats':   [36, 88, 89],
                   'Pants':   [21, 56, 94],
                   'Tanks':   [11, 10, 19],
                   'Sweats':  [27, 21, 35]})
result = df.lt(45)
print(result)


DataFrame.lt(other, axis='columns', level=None)
DataFrame.gt(other, axis='columns', level=None)
DataFrame.le(other, axis='columns', level=None)
DataFrame.ge(other, axis='columns', level=None)
DataFrame.eq(other, axis='columns', level=None)
DataFrame.ne(other, axis='columns', level=None)


# In[101]:


import numpy as np
import pandas as pd
import statistics as sp


# In[4]:


file = pd.read_csv('Student_Marks.csv')
file


# In[5]:


file.tail()


# In[84]:


file.head()


# In[85]:


file.head(1)


# In[86]:


file.tail(1)


# In[88]:


file.max()


# In[89]:


file.min()


# In[90]:


file.mean()


# In[91]:


file.median()


# In[94]:


file.std()


# In[95]:


file.mode()


# In[96]:


file.describe()


# In[97]:


file.count()


# In[98]:


file.cumsum()


# In[99]:


file.cumprod()


# In[ ]:





# In[7]:


import math
print(math.ceil(12.34))


# In[9]:


print(math.exp(3))


# In[10]:


math.fabs(5)


# In[11]:


print(math.floor(12.34))


# In[12]:


math.factorial(5)


# In[15]:


math.fmod(13,3)


# In[16]:


ls = [1,2,3,4,5,6]
print(math.fsum(ls))


# In[20]:


math.gcd(2,4,6,8,2)


# In[22]:


math.isclose(23.9,26)


# In[23]:


math.isclose(23.89,24)


# In[24]:


math.isfinite(21)


# In[26]:


math.isfinite(-123423452342545645456566.45625)


# In[28]:


math.isinf(23453453434.534534)


# In[31]:


math.isnan(76)


# In[32]:


math.log(1)


# In[34]:


math.log(5)


# In[35]:


math.perm(12)


# In[36]:


math.pow(2,3)


# In[37]:


math.prod([12,34,2])


# In[38]:


math.remainder(12,5)


# In[39]:


math.sqrt(16)


# In[40]:


math.trunc(12.34234234)


# In[ ]:





# In[41]:


import statistics as sp
import math 
import numpy as np
import pandas as pd


# In[42]:


scores = np.random.randint(1,300,50)
scores


# In[43]:


np.median(scores)


# In[44]:


np.var(scores)


# In[45]:


np.std(scores)


# In[47]:


sp.harmonic_mean(scores)


# In[48]:


sp.mean(scores)


# In[49]:


sp.median(scores)


# In[50]:


sp.median_grouped(scores)


# In[51]:


sp.median_high(scores)


# In[53]:


sp.median_low(scores)


# In[54]:


sp.mode(scores)


# In[55]:


sp.pstdev(scores)


# In[56]:


sp.stdev(scores)


# In[57]:


sp.pvariance(scores)


# In[59]:


sp.variance(scores)


# In[65]:


a = pd.DataFrame({'Name': ['Shobhit', 'Vaibhav',
                            'Vimal', 'Sourabh',
                            'Rahul', 'Shobhit'],
                          'Physics': [11, 12, 13, 14, 13, 11],
                          'Chemistry': [10, 14, 20, 18, 20, 10],
                          'Math': [13, 10, 15, 19, 20, 13]})
 


# In[66]:


a


# In[67]:


a.count()


# In[68]:


df = pd.DataFrame({'Tops':    [15, 20, 25],
                   'Coats':   [36, 88, 89],
                   'Pants':   [21, 56, 94],
                   'Tanks':   [11, 10, 19],
                   'Sweats':  [27, 21, 35]})
result = df.lt(45)
print(result)


# In[69]:


df.max()


# In[70]:


df.min()


# In[71]:


df1 = pd.DataFrame({'X': [25, 120, 120, 10],
                   'Y': [25, 350, 200, 35]},
                  index=['A', 'B', 'C', 'D'])


df2 = pd.DataFrame({'X': [150, 90, 350, 120, 130, 330],
                             'Y': [160, 450, 30, 560, 235, 356]},
                            index=[['R1', 'R1', 'R1', 'R2', 'R2', 'R2'],
                                   ['A', 'B', 'C', 'A', 'B', 'C']])
df1
df2


# In[72]:


print(df1.lt(df2, level=1))


# In[73]:


print(df1.lt(df2, level=0))


# In[74]:


print(df2.lt(df1, level=1))


# In[75]:


print(df2.lt(df1, level=0))


# In[77]:


print(df2.gt(df1, level=1))


# In[79]:


print(df1.gt(df2, level=0))


# In[80]:


print(df1.le(df2, level=1))


# In[81]:


print(df1.ge(df2, level=1))


# In[82]:


print(df1.eq(df2, level=1))


# In[83]:


print(df1.ne(df2, level=1))


# In[ ]:




