import numpy as np
def square_matrix_multiplication(matrix,m):
  rows = len(matrix)
  cols = len(matrix[0])
  new_matrix= matrix
  if rows == cols:
    for i in range(m-1):
      new_matrix=np.dot(new_matrix,matrix)
  return new_matrix
matrix =np.array([[1,2,3],[4,5,6],[7,8,9]])
m=2
result=square_matrix_multiplication(matrix,m)
print(result)