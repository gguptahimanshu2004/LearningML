import numpy as np

print("=" * 50)
print("REAL-WORLD EXAMPLE : Shape Manipulation")
print("=" * 50)

matrix = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(f"Matrix: \n {matrix}")

# Sum
print(f"Total Sum: {matrix.sum}")
print(f"Sum along axis 0 (columns) : {matrix.sum(axis = 0)}")
print(f"Sum along axis 1 (rows) : {matrix.sum(axis = 1)}")

# Mean
print(f"Total Mean: {matrix.mean}")
print(f"Mean along axis 0 (columns) : {matrix.mean(axis = 0)}")
print(f"Mean along axis 1 (rows) : {matrix.mean(axis = 1)}")

# Maximum and Minimum
print(f"Maximum: {matrix.max}")
print(f"Minimum: {matrix.min}")
print(f"Max along axis 0 (columns) : {matrix.max(axis = 0)}")
print(f"Max along axis 1 (rows) : {matrix.max(axis = 1)}")

# Argmax and Argmin (indices)
print(f"Index of max value: {matrix.argmax}")
print(f"Index of min value: {matrix.argmin}")