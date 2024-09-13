import numpy as np

# 5.1 Create a 2D array of shape (4, 4) with values ranging from 10 to 25
array_2d_slice = np.arange(10, 26).reshape(4, 4)
print("original array: \n", array_2d_slice)

# 5.2 Extract the second row and the last column of the array
second_row = array_2d_slice[1, :]
last_column = array_2d_slice[:, -1]
print("Second Row:", second_row)
print("Last Column:", last_column)

# 5.3 Replace the elements of the first row with zeros
array_2d_slice[0, :] = 0
print("Modified Array:\n", array_2d_slice)