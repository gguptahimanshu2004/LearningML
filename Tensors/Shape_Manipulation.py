import numpy as np

print("=" * 50)
print("REAL-WORLD EXAMPLE : Shape Manipulation")
print("=" * 50)

# Original Array
original = np.arange(24)
print(f"Original Array : \n{original}")
print(f"Original Shape : {original.shape}")

# Reshape to 2D 
reshaped_2D = original.reshape(6,4)
print(f"Reshaped 2D Array : \n{reshaped_2D}")
print(f"Reshaped 2D Array Shape : {reshaped_2D.shape}")

# Reshape to 3D
reshaped_3D = original.reshape(2,3,4)
print(f"Reshaped 3D Array : \n{reshaped_3D}")
print(f"Reshaped 3D Array Shape : {reshaped_3D.shape}")

# Reshape with -1 (auto-calculate)

auto_reshape = original.reshape(-1,6)
print(f"Auto Reshaped Array : \n{auto_reshape}")
print(f"Auto Reshaped Array Shape : {auto_reshape.shape}")

# Flatten 
flattened = reshaped_3D.flatten()
print(f"Flattened: {flattened}")
print(f"Fllttened array shape : {flattened.shape} ")

# TRanspose

transpose_array = reshaped_2D.transpose()
print(f"2D Array : \n{reshaped_2D}")
print(f"Transposed 2D array : {transpose_array}")
