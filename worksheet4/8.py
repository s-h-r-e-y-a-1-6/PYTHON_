import numpy as np

# 8.1 Create two 2x2 matrices
Matrix_A = np.array([[1, 2], [3, 4]])
Matrix_B = np.array([[5, 6], [7, 8]])
print("MATRIX A IS:\n",Matrix_A)
print("MATRIX B IS:\n",Matrix_B)

# 8.2 Perform operations
matrix_multiplication = np.dot(Matrix_A, Matrix_B)
transpose_A = np.transpose(Matrix_A)

print("Matrix Multiplication:\n", matrix_multiplication)
print("Transpose of Matrix A:\n", transpose_A)