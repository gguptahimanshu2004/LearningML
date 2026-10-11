import numpy as np

print("=" * 50)
print("REAL-WORLD EXAMPLE : Image Data")
print("=" * 50)

image_batch = np.random.rand(10,64,64,3) # Rand choses integer between 1  and 100

print(f"Image Batch Shape : {image_batch.shape}")
print(f"Interpretration:")
print(f"- No. of Images: {image_batch.shape[0]}")
print(f"- Image Height : {image_batch.shape[1]}")
print(f"- Image Width : {image_batch.shape[2]}")
print(f"- Color Channels : {image_batch.shape[3]}")
print()

# Memory Calculation
total_elements = image_batch.size
memory_mb = (image_batch.size * 8) / (1024*1024)
print(f"Memory Usage:")
print(f"- Total Elements : {total_elements}")
print(f"- Memory :  {memory_mb} MB")

# Single image 
single_image = image_batch[0]
total_elements = single_image.size
print(f"Single Image elements: {single_image.size}")
print(f"Total Memory for single image: {(total_elements*8)/ (1024*1024)}")
