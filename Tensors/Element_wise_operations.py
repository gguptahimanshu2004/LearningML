import numpy as np

print("=" * 50)
print("REAL-WORLD EXAMPLE : Element Wise Operations")
print("=" * 50)

# Array A

A = np.array([[1,2,3],[5,6,7],[8,9,10]])

# Array B

B = np.array([[1,2,2],[3,4,4],[5,6,6]])

print(f"Array A is: {A}\nArray B is : {B}")

# Addition 
print(f"A+B is : {A + B}")

# Substraction
print(f"A-B is : {A-B}")

# Multiplication
print(f"A*B is : {A*B}")

# Division
print(f"A/B is : {A/B}")
