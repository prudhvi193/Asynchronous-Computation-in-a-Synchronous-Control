#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Problem-2 
# Finding the solution for Probability of P(i) when size of block is adaptive
# Team Member Names: Hai Huynh, Prudhviraj Sheela, Aman Masipeddi

# Below are the input configuration values
import math
import sys
import random
lambd = int(input("Arrival Rate: ")) # Arrival Rate
mu = int(input("Service Rate: ")) # Service Rate
c = 1
r = lambd/mu

max_block_size = random.randint(0,sys.maxsize) # Takes the maximum block size
number_of_blocks = random.randint(0,sys.maxsize) # Number of blocks


# In[2]:


# M/M/1/K Model
# The probability function for individual block
def prob_function (i, k):
    P_0 = (1 - r)/(1-r**(k+1))
    P_n = 0
    n = i
    if n == 0:
        P_n = P_0
    elif n <= k:
        P_n = ((1-r)/(1-r**(k+1)))*(r**n)
    else:
        P_n = 0
    return P_n


# In[4]:


# The below step generates the random block sizes
import random
random_block_sizes = [random.randrange(1, max_block_size) for iter in range(number_of_blocks)]

max_i = -99

# The below condition is used to get the maximum block size from the available blocks
for block in random_block_sizes: 
    if block >= max_i:
        max_i = block


# In[5]:


avg_pi = [] # Average Probability for each value of 'i'
accu_pi = [] # Accumulated Probabilit for each value of 'i'

total = 0
for i in range(max_i+1):
    a_pi = 0
    for k in random_block_sizes:
        a_pi += prob_function(i, k)
    avg_pi.append(a_pi/len(random_block_sizes))
    total += avg_pi[i]
    accu_pi.append(total)


# In[7]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

xs = np.arange(max_i+1)
bar = sns.barplot(xs, avg_pi)
line = sns.lineplot(xs, accu_pi)
plt.xlabel("Slots in block")
plt.ylabel("Probablity")
plt.show()

print("There are {} blocks of sizes {}".format(number_of_blocks, random_block_sizes))


# In[10]:


z = [print('P({}): {}'.format(i, avg_pi[i])) for i in range(len(avg_pi))]


# In[ ]:




