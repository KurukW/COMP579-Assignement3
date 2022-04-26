import itertools
import numpy as np 
from matplotlib import pyplot as plt 
from numpy.random import normal


data1 = []
data2 = []
for i in range(100000):
    #Pr(N(1+2/3,4/3))
    data1.append(normal(1+2/3.0,4/3.0))

    #Pr(N(2/3,4/3))
    data2.append(normal(2/3.0,4/3.0))

#Data 3 = data 2
#for elt in data1:
#    data3.append(elt*2/3.0)
data1_b = list(map(lambda x: x*3/4.0, data1))
data2_b = list(map(lambda x: x*1/4.0, data2))
data =  data1_b + data2_b 

fig, axs = plt.subplots(1,3)
axs[0].hist(data1_b,bins= 500)
axs[0].title.set_text("Normal(1+2/3,4/3) * 3/4")
axs[0].set_xlim([-4,4])
axs[1].hist(data2_b,bins= 500)
axs[1].title.set_text("Normal(2/3,4/3) * 1/4")
axs[1].set_xlim([-4,4])
axs[2].hist(data,bins= 500)
axs[2].title.set_text("Sum")
axs[2].set_xlim([-4,4])
plt.show()