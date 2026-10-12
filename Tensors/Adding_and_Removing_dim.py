import numpy as np

print("=" * 50)
print("REAL-WORLD EXAMPLE : Adding and Removing Dimensions")
print("=" * 50)

# Original vector

vector = np.array([1,2,3,4,5])
print(f"Original vector : {vector}")
print(f"Original shape : {vector.shape}")

# Add Dimensions at beginning

with_batch = np.expand_dims(vector,axis = 0)
print(f"New vector (adding at beginning) : {with_batch}")
print(f"New shape : {with_batch.shape}")

# Add Dimensions at the end 

with_batch = np.expand_dims(vector,axis = -1)
print(f"New vector (adding at end) : {with_batch}")
print(f"New shape : {with_batch.shape}")

# Squeeze - remove dimensions of size 1

squeezable = np.array([[[1,2,3],[4,5,6]]])
print(f"Original (with size-1 dimensions): {squeezable} , shape : {squeezable.shape}")
squeezed = np.squeeze(squeezable)
print(f"After squeeze: {squeezed} , shape : {squeezed.shape}")


