import numpy as np

# 1.1 Create a 1D array of integers from 5 to 25 using NumPy
array_1d = np.arange(5, 26)
print("1D Array:", array_1d)





# 1.2 Create a 2D array with 3 rows and 4 columns filled with random integers between 10 and 50
array_2d = np.random.randint(10, 51, size=(3, 4))
print("2D Array:\n", array_2d)
