import numpy as np

# 10.1 Create a 3x3 matrix
Matrix_A_linear = np.array([[2, 1, 3], [0, 5, 6], [7, 8, 9]])
print(Matrix_A_linear)

# 10.2 Perform the following operations
determinant = np.linalg.det(Matrix_A_linear)
inverse = np.linalg.inv(Matrix_A_linear)
eigenvalues, eigenvectors = np.linalg.eig(Matrix_A_linear)

print("Determinant of Matrix A:", determinant)
print("Inverse of Matrix A:\n", inverse)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

