import numpy as np

# 7.1 Create a 1D array with 12 elements starting from 11
array_1d_reshaped = np.arange(11, 23)
print(" the original array is : \n",array_1d_reshaped)

# 7.2 Reshape it into a 2D array of shape (3, 4)
reshaped_array = array_1d_reshaped.reshape(3, 4)
print("Reshaped Array:\n", reshaped_array)
