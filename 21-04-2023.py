#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing numpy array
import numpy as np


# In[128]:


# creating empty numpy array
np.array([]) 


# In[3]:


# creating numpy array with some elements one-dimensional
np.array([1,2,3,4,5])


# In[7]:


# creating numpy array with some elements two-dimensional
np.array([[1,2,3],[4,5,6],[7,8,9]])


# In[8]:


# printing 1-9 using arange function
np.arange(10)


# In[9]:


# printing only even numbers
np.arange(0,10,2)


# In[10]:


# print 4 zeros using zeros function in 1-D
np.zeros(4)


# In[13]:


# print 4 by 5 matricies of zeros using zeros function in 2-D
np.zeros((4,5))


# In[14]:


# print 4 zeros using ones function in 1-D
np.ones(4)


# In[15]:


# print 3 by 4 matricies of ones using zeros function in 2-D
np.ones((3,4))


# In[18]:


# find the linespaces between 2 numbers how many parts you want
np.linspace(1,10,20)


# In[19]:


# printing 50 random numbers from 10 to 300 range using random function 
np.random.randint(10,300,50)


# In[22]:


# Find minimum and maximum values in numpy arrays
minimum = np.random.randint(10,300,50)
print(minimum)
minimum.min()


# In[24]:


maximum = np.random.randint(10,300,50)
print(maximum)
maximum.max()


# In[26]:


# Find indices of minimum and maximum values in numpy arrays
maximum = np.random.randint(10,300,50)
print(maximum)
print("maximum value index is : ",maximum.argmax())


# In[27]:


minimum = np.random.randint(10,300,50)
print(minimum)
print("minimum value index is : ",minimum.argmin())


# In[30]:


# list
list1 = [3, 4, 5, 6]
print(type(list1))
print(list1)
print()

# conversion
array1 = np.asarray(list1)
print(type(array1))
print(array1)
print()


# In[62]:


# tuple
tuple = (3, 4, 5, 6)
print(type(tuple))
print(tuple)
print()

# conversion
array2 = np.asarray(tuple)
print(type(array2))
print(array2)
print()


# In[31]:


np.linspace(0,5,10)


# In[34]:


arr = np.array([[1,2,3,10],[4,5,6,11],[7,8,9,12]])
arr.reshape(12)


# In[130]:


arr = np.array([ 1,  2,  3, 10,  4,  5,  6, 11,  7,  8,  9, 12])
arr.reshape((3,4))


# In[41]:


a = np.arange(0,30,5)
a


# In[46]:


np.zeros((3,4))


# In[48]:


b = np.random.randint(0,17,16)
b.shape


# In[49]:


b.dtype


# In[50]:


b = np.dtype(np.int16)


# In[52]:


b.type


# In[63]:


b = np.random.randint(10,30,size=(5, 5))
b


# In[64]:


a = np.random.randint(0,16,size=(4, 4))
a


# In[69]:


array1 = np.array([ 1,  2,  3, 10,  4,  5,  6, 11,  7,  8,  9, 12])
print(array1[3])


# In[70]:


print(array1[::-1])


# In[71]:


print(array1[4:9:])


# In[73]:


print(array1[13:0:-2])


# In[74]:


print(array1[::-3])


# In[95]:


array2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array2[0][0])


# In[96]:


print(array2[2][0])


# In[97]:


print(array2[:2][:3])


# In[107]:


print(array2[:0][:0])


# In[111]:


print(array2[2:5, 1:3])


# In[102]:


print(array2[:3][:3])


# In[81]:


v = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])
v


# In[131]:


array1 = np.array([1,2,3,4,5])


# In[114]:


print(array1 + 2)


# In[133]:


print(array1 - 2)


# In[117]:


print(array1 * 5)


# In[124]:


print(array1 * array1)


# In[125]:


trans = np.array([[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])
np.transpose(trans)


# In[129]:


np.linspace(0,30,5)


# In[ ]:




