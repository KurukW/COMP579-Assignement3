import itertools
import numpy as np 
from matplotlib import pyplot as plt 
def process(data, value):
    data = [x+ value for x in data]
    data= list(itertools.chain.from_iterable(data))
    data =np.array(data)
    return data
entry = np.array([-1,0,1])
data = np.array([-1,0,1])

for _ in range(10):
    entry = 0.99 * entry
    data = process(data , entry)
plt.hist(data,bins=1000)
plt.show()