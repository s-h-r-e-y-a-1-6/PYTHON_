import numpy as np

# 4.1 Create a 2D array of shape (3, 3) with values starting from 1 to 9
array_2d_broadcast = np.arange(1, 10).reshape(3, 3)
print("original array: \n", array_2d_broadcast)

# 4.2 Multiply this 2D array by a scalar value of 5 using broadcasting
result = array_2d_broadcast * 5
print("Result after Broadcasting:\n", result)
