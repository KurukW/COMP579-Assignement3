import itertools
import numpy as np 
from matplotlib import pyplot as plt 
from numpy.random import normal


data1 = [0]
data2 = [0]
nbins = 100

for i in range(1,nbins):
    #Recurrent
    if i%2 == 0:
        data1.append(-data1[-1])
    else:
        data1.append(-data1[-1] + 1)


    #General
    data2.append((-1)**i * i)


print("data1:")
print(data1)

print("data2:")
print(data2)

fig, axs = plt.subplots(2)
axs[0].plot(data1,linestyle="None", marker = "o")
axs[0].title.set_text("Recurrent")
axs[1].plot(data2,linestyle="None", marker = "o")
axs[1].title.set_text("General")
plt.show()
