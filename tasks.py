import numpy as np

# Follow the tasks below to practice basic Python concepts.
# Write your code in between the dashed lines.
# Don't import additional packages. Numpy suffices.

# Task 1: 
# Instructions:
#Write a function that takes one numeric argument as input. 
#If the number is larger than zero, the function should return 1, otherwise is should return -1.
#The name of the function should be step

# Your code here:
# -----------------------------------------------

def step(num):
    if type(num) == int or type(num) == float:
        if num > 0:
            return 1
        else:
            return -1
    else:
        return "Input should be numeric"


# -----------------------------------------------


# Task 2:
# Instructions:
#Write a function that takes in two arguments: a numpy array, and an integer (call argument "cutoff" and set default to 0).
#The function should return a numpy array of the same length, with all elements smaller than the cutoff being set to cutoff).
#The name of the function should be ReLu


# Your code here:
# -----------------------------------------------
def ReLu(numpy_array, cutoff=0):
    for i in range(len(numpy_array)):
        if numpy_array[i] < cutoff:
            numpy_array[i] = cutoff
    return numpy_array

a = np.array([1, 2, 3, -1, -4, 0, -5, 3, 8])
ReLu(a)

# -----------------------------------------------


# Task 3:
# Instructions:
#Write a function that takes in a two-dimensional numpy array of size (n, p) and a one-dimensional numpy array of size p.
#The function should start by multiplying the two numpy arrays (matrix multiplication).
#Next, apply the ReLu function from above to the resulting matrix and return the result.
#Name the function neural_net_layer

# Your code here:
# -----------------------------------------------

def neural_net_layer(two_dim, one_dim):
    mult_matrix = two_dim @ one_dim

    def ReLu(numpy_array, cutoff=0):
        for i in range(len(numpy_array)):
            if numpy_array[i] < cutoff:
                numpy_array[i] = cutoff
        return numpy_array
    output = ReLu(mult_matrix)
    return output

# ------------------------------------------