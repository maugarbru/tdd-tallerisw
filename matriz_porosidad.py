import numpy as np

def create_matrix (n,m,phi_m, phi_f):
  '''
    Returns a matrix of porosity of n x m 
    with the constants of phi_m and phi_f
  '''
  assert type(n) == type(2) and n >= 0, "n must be an integer"
  assert type(m) == type(2) and m >= 0, "m must be an integer"
  matrix = []
  inter = []
  fracture = [phi_f]*n

  for i in range(n):
      value_to_add = phi_m if i % 2 == 0 else phi_f
      inter.append(value_to_add)

  for j in range(m):
      row_to_add = inter if j % 2 == 0 else fracture
      matrix.append(row_to_add)
      
  return np.array(matrix)