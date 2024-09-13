import numpy as np

# 3.1 Create two 1D arrays
Array1 = np.array([2, 4, 6, 8, 10])
Array2 = np.array([1, 3, 5, 7, 9])

# 3.2 Perform operations
addition = Array1 + Array2
subtraction = Array1 - Array2
multiplication = Array1 * Array2
division = Array1 / Array2

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Element-wise Multiplication:", multiplication)
print("Element-wise Division:", division)
