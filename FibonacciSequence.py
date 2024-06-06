#!/usr/bin/env python
# coding: utf-8

# In[7]:


#This is a program to print the fibonacci sequence upto nth term
fib = [0, 1]
n = int(input("Enter the number of terms to be displayed in the Fibonacci sequence:"))
for i in range(2,n):
    fib.append(fib[i-1]+fib[i-2])
for i in range(n):
    print(fib[i])


# In[ ]:




