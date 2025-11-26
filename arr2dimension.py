import numpy as np
arr = np.array([[1,2],[3,4]])
arrasm = np.array([[1,1],[1,1]])
m = np.array([[2,2],[2,2]])
print("Matrix:")
print(arr)
print("Addition:")
print(np.add(arr,arrasm))
print("Subtraction:")
print(np.subtract(arr,arrasm))
print("Multiplication:")
print(np.matmul(arr,m))

