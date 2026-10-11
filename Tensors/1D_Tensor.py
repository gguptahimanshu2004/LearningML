print('='*50)
print('REAL - WORLD EXAMPLE OF 1D TENSOR : Student Data')
print('='*50)

# Student Features : [CGPA , IQ , State , Placement]
# W = 0 (not placed) , K = 1 (placed
import numpy as np

student_1 = np.array([8.1,91,0,1])

print(f'Student 1 Data: {student_1}')
print(f'Shape : {student_1.shape}')
print("Interpretation:")
print(f" - CGPA: {student_1[0]}")
print(f" - IQ : {student_1[1]}")
print(f" - State : {student_1[2]} (0 = W , 1 = K)")
print(f" - Placed :{student_1[3]} (0 = N , 1 = Y)")


