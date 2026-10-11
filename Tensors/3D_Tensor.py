import numpy as np

print("=" * 50)
print("REAL-WORLD EXAMPLE : NLP DATA")
print("=" * 50)

# Text Data : " Hi Nitish" , "Hi , Rahul" , " Hi Ankit"
# One-hot encoding for words : Hi,Nitish,Rahul,Ankit

nlp_data = np.array([
    [[1 , 0 , 0 , 0],[0 , 1 , 0 , 0]],
    [[1 , 0 , 0 , 0],[0 , 0 , 1 , 0]],
    [[1 , 0 , 0 , 0],[0 , 0 , 0 , 1]]
])

print(f"NLP Tensor shape : {nlp_data.shape}")
print(f"Interpretation:")
print(f" - Number of sentences: {nlp_data.shape[0]}")
print(f" - Words per sentence: {nlp_data.shape[1]}")
print(f" - Embedding dimension: {nlp_data.shape[2]}")

print(f"\nFirst Sentence 'Hi Nitish' : {nlp_data[0]}")
print(f"\nFirst Sentence 'Hi Rahul' : {nlp_data[2]}")
print(f"\nFirst Sentence 'Hi Ankit' : {nlp_data[2]}")
