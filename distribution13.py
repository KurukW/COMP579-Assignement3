import itertools
import numpy as np 
from matplotlib import pyplot as plt 
from numpy.random import normal


data1 = []
data2 = []

for i in range(100000):
    #Pr(N(0,1))
    data1.append(normal(0,1))

    #Pr(N(1,4/3))
    data2.append(normal(1,4/3.0))

data = data1 + data2

fig, axs = plt.subplots(3)
axs[0].hist(data1,bins= 500)
axs[0].title.set_text("Normal(0,1)")
axs[1].hist(data2, bins= 500)
axs[1].title.set_text("Normal(1,4/3)")
axs[2].hist(data, bins= 1000)
axs[2].title.set_text("Sum")

plt.show()