import numpy as np

print("=" * 50)
print("REAL-WORLD EXAMPLE : Students Dataset")
print("=" * 50)

# Multiple Rows = Multiple Students
# [CGPA , IQ , State , Placed]

students = np.array([
    [8.1 , 91 , 0 , 1],
    [7.2 , 85 , 1 , 0],
    [9.0 , 95 , 0 , 1]
])

print(f"Dataset Shape: {students.shape}")
print(f"Number of Students : {students.shape[0]}")
print(f"Number of Features: {students.shape[1]}")
print(f"\nDataset\n{students}\n")


# Statistics
print(f"- Average CGPA : {students[:,0].mean()}")
print(f"- Average IQ : {students[:,1].mean()}")
print(f"- Percentage Placed : {students[:,2].mean()*100}")