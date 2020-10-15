import numpy as np

def create_matrix (n,m,phi_m, phi_f):
  '''
    Returns a matrix of porosity of n x m 
    with the constants of phi_m and phi_f
  '''
  inter = []
  fracture = []
  matrix=[]
  for i in range(n):
      if i % 2 == 0:
          inter.append(phi_m)
      else:
          inter.append(phi_f)
      fracture.append(phi_f)

  for j in range(m):
      if j % 2 == 0:
          matrix.append(inter)
      else:
          matrix.append(fracture)
  
  return np.array(matrix)