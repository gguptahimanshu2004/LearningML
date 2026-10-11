import numpy as np

print("=" * 50)
print("REAL-WORLD EXAMPLE : Video Data")
print("=" * 50)

# Simulating a batch of videos
# 2 videos , each 30 frames , 128*128 pixels , RGB

video_batch = np.random.rand(2,30,128,128,3)

print(f"Video Batch Shape : {video_batch.shape}")
print(f"Interpretration:")
print(f"- No. of Videos: {video_batch.shape[0]}")
print(f"- Frames per video: {video_batch.shape[1]}")
print(f"- Video Height : {video_batch.shape[2]}")
print(f"- Video Width : {video_batch.shape[3]}")
print(f"- Color Channels : {video_batch.shape[4]}")
print()

# Memory Calculations

print(f"Total no. of elements : {video_batch.size}")
elements = video_batch.size
memory_mb = (elements*8)/(1024*1024)
print(f"Total Memory Usage : {memory_mb}MB")

# Single Video

single_video = video_batch[0]
elements = single_video.size
print(f"Total no. of elements for one video: {elements}")
print(f"Total Memory Usage for one single video: {(elements*8)/(1024*1024)} MB" )
