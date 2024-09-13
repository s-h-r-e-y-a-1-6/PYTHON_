import numpy as np

# 9.1 Create a 1D array with random integers between 10 and 60 (15 elements)
random_array_stat = np.random.randint(10, 61, size=15)
print("original array: \n", random_array_stat)

# 9.2 Compute and print the following statistics
mean = np.mean(random_array_stat)
median = np.median(random_array_stat)
std_deviation = np.std(random_array_stat)

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_deviation)
