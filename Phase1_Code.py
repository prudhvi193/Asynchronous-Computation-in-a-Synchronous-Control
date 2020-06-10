#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Program for asynchronous computation in a synchronous control
#Team Member Names: Hai Huynh, Prudhviraj Sheela, Aman Masipeddi

import math
c=1 #Default as it is a single waiting queue model
k=int(input("Queue size:")) # Queue size
lambda1=int(input("Arrival Rate: ")) # Arrival Rate
mu1=int(input("Service Rate: ")) #Service Rate
r = lambda1 / mu1 # Utilization Rate


# In[19]:


# M/M/1/K Model
# This is the one that we have described in the report
P_0 = (1 - r)/(1-r**(k+1)) # The inital probability when the queue is empty
P_n = 0 # The probability P_n means the proabability at the position 'n' when traversed through
def prob_function (i):
    n = i
    if n == 0:
        P_n = P_0
    elif n <= k:
        P_n = ((1-r)/(1-r**(k+1)))*(r**n)
    else:
        P_n = 0
    return P_n


# In[14]:


# The below model is an extension to the M/M/1/K model if we wanted to use multiple servers
# M/M/C/K Model (Multiple servers)
R0 = lambda1 / (c*mu1) # Utilization Rate for each server but in this case we are considering the value of (c=1)
P0=0
if R0 != 1:
    for i in range(0,c):
        P0= pow(r,i) / math.factorial(i)
    P0 += pow(r, c) * (1 - pow(R0, k - c + 1)) / (math.factorial(c) * (1 - R0))
    P0 = pow(P0, -1)
else:
    for i in range(0,c):
        P0 = pow(r,i)/math.factorial(i)
    P0 += pow(r, c) * (k - c + 1) / (math.factorial(c))
    P0 = pow(P0, -1)
# print(P0) # The initial probability when the queue is empty


# In[15]:


# M/M/C/K Model (Multiple servers)
def ProbabFunc(i):
    n=i
    if n==0:
        Pn = P0
    elif 1<=n and n<=c:
         Pn = pow(r, n) * P0 / pow(n, k - c)
    else:
        Pn = pow(r, n) * P0 / (math.factorial(c) * pow(c, n - c))
    return Pn
#Pn --> Probability while the queue is traversed through the 'n'th state


# In[18]:


discreteCategories=[]
discreteProbabilities=[]
accumulatedProbabilities=[]
def discrete():
    value = None
    for i in range(0,k+1):
        discreteCategories.append(i)
        n=i
        # pi1 = ProbabFunc(i) if value is None else value
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


# In[20]:


import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax=fig.gca()
xs=np.arange(len(dC))
ax.bar(xs,dP)
ax.plot(xs,aP)
plt.ylabel('Probability')
plt.xlabel('Slots in the queue served')
plt.show()


# In[22]:


z = [print('P({}): {}'.format(i, dP[i])) for i in range(len(dP))]


# In[ ]:




