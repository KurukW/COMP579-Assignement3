from math import dist
import numpy as np 
from matplotlib import pyplot as plt 
from numpy.random import normal


# Generation of a distribution
# data1 = []
# data2 = []
# data3 = []
# data4 = []

# for i in range(100000):
#     data1.append(normal(0,0.8))
#     data2.append(normal(2,2))
#     data3.append(normal(-4,1))
#     data4.append(normal(5,2))

# data = data1 + data2 + data3 + data4





def to_dirac(distribution, n_output):
    #Create the locations
    if n_output <= 1:
        return np.mean(distribution), len(distribution)
    

    # I make the choice to have dirac's impulsion at the end of the distribution. It could be a problem if the distribution is too wide
    # If I change it, I need to decide where I put my first impulsion (it could be a % of the number of element). I won't do it if not necessary
    min_range = np.min(distribution)
    max_range = np.max(distribution)

    gap_size = (max_range - min_range)/ (n_output - 1)

    x_dirac = [min_range + i * gap_size for i in range(n_output)]

    y_dirac = [0 for i in x_dirac]


    def h(i,z):
        if i == 1:
            if z <= 0:
                return 1
        elif i == len(x_dirac)-1:
            if z >= 0:
                return 1
        return max(0, 1-abs(z))

    #Assign value to locations
    for elt in distribution:
        #elt is the position of one elt of the distribution
        for e in range(len(x_dirac)-1):
            z = (elt - x_dirac[e])/(x_dirac[e+1] - x_dirac[e])
            #Position of our elt in regard to the categorical impulsion we're looking
            y_dirac[e] += h(e,z)
        

    return x_dirac, y_dirac 
        


def divide_list(my_list, factor):
    if type(my_list) is list:
        return [elt/factor for elt in my_list]
    if type(my_list) is int or float:
        return my_list/factor


# x, y = to_dirac(data, 20)
# y = divide_list(y, 400000.0) # Idk what could be a dynamic factor to have a meaningfull plot
#If I want to have the probabilities between 0 and 1, I have to divide by the number of data (in my case 4 * 100 000)


# fig, axs = plt.subplots(2)
# axs[0].hist(data,bins=1000)
# axs[1].scatter(x, y, color = 'red')
# plt.show()


#Solution to the question:
def categorical(mu, var, m):
    n_elt = 400000
    distr = [normal(mu,var) for i in range(n_elt)]
    # distr = data
    locations, probabilities = to_dirac(distr, m)
    probabilities = divide_list(probabilities, n_elt)

    fig, axs = plt.subplots(2)
    axs[0].hist(distr,bins=1000)
    axs[1].scatter(locations, probabilities, color = 'red')

    plt.show()


categorical(2, 4, 30)



#All the comment are for a random distribution. To prove the algo is working on any distribution


