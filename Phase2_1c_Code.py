#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Problem-3
# Program for Pseudo Asynchronous Block Processing where each transaction is served immediately once it is arrived into the block
# Team Member Names: Hai Huynh, Prudhviraj Sheela, Aman Masipeddi

# Below are the input configuration values
import math
import sys
import random
c=1 #Default as it is a single waiting queue model
lambda1=int(input("Arrival Rate: ")) # Arrival Rate
mu1=int(input("Service Rate: ")) #Service Rate
r = lambda1 / mu1 # Utilization Rate


# In[2]:


P_0 = (1 - r) # The inital probability when the queue is empty
P_n = 0 # The probability P_n means the proabability at the position 'n' when traversed through
def block_size():
    k = random.randint(0,sys.maxsize) # This gives a block with a varied size until a range of infinity
    return k
def prob_function (i):
    n = i
    if n == 0:
        P_n = P_0
    else:
        P_n = (P_0)*(r**n)
    return P_n


# In[3]:


import itertools
discreteCategories=[]
discreteProbabilities=[]
accumulatedProbabilities=[]
def discrete():
    value = None
    b_size = block_size() # This variable stores the block size which can vary until infinite
    for i in range(0,b_size+1):
        discreteCategories.append(i)
        n=i
        pi1 = prob_function(i)
        pi2 = round(pi1,4) if value is None else value
        discreteProbabilities.append(pi2)
        if i==0:
            accumulatedProbabilities.append(pi2)
        else:
            pi3 = round(pi2+accumulatedProbabilities[i-1],4)
            accumulatedProbabilities.append(pi3)
    return discreteCategories,discreteProbabilities,accumulatedProbabilities
dC,dP,aP = discrete()
# print(dC) # Stores the each slot value in the queue
# print(dP) # It specifies the discrete probability of events that occur within that particular time frame which is the poisson distribution
# print(aP) # It specifies the accumulated probability of events that are uniformly distributed


# In[5]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
xs=np.arange(len(dC))
sns.barplot(xs,dP)
sns.lineplot(xs,aP)
plt.ylabel('Probability')
plt.xlabel('Slots in the queue served')
plt.show()


# In[6]:


z = [print('P({}): {}'.format(i, dP[i])) for i in range(len(dP))]


# In[ ]:




