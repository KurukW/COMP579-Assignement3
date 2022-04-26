import itertools
import numpy as np 
from matplotlib import pyplot as plt 
from numpy.random import normal


data1 = []
data2 = []
data3 = []

for i in range(100000):
    #Pr(N(1,2))
    data1.append(normal(1,2))

    #Pr(N(2/3,4/3))
    data2.append(normal(2/3.0 + 0.5,4/3.0))

#Data 3 = data 2
#for elt in data1:
#    data3.append(elt*2/3.0)

data = data1 + data2

fig, axs = plt.subplots(1,2)
axs[0].hist(data1,bins= 500)
axs[0].title.set_text("Normal(1, 2) = Z")
axs[0].set_xlim([-7.5,7.5])
axs[1].hist(data2,bins= 500)
axs[1].title.set_text("Normal(2/3+0.5, 4/3) = Pr(R+gamma*Z)")
axs[1].set_xlim([-7.5,7.5])
#axs[2].hist(data2,bins= 500)
#axs[2].title.set_text("Normal(1,2) * 2/3")


plt.show()