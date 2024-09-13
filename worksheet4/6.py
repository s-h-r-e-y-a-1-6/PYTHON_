import numpy as np

# 6.1 Create a 1D array with random integers between 20 and 40 (10 elements)
random_array = np.random.randint(20, 41, size=10)
print("THE ARRAY IS:\n", random_array)

# 6.2 Use Boolean indexing to find all elements greater than 30
greater_than_30 = random_array[random_array > 30]
print("Elements greater than 30:", greater_than_30)

