import numpy as np
import unittest
from matriz_porosidad import crear_matriz

class MatrizPorosidadTests(unittest.TestCase):
  def test_has_to_be_list(self):
    '''
      Should returns a python list
    '''
    self.assertTrue(type(crear_matriz(6, 5, 'm', 'f')) is np.ndarray)
  
  def test_has_given_size(self):
    '''
      Should returns a matrix with certain size given parameters
    '''
    matriz = crear_matriz(6, 5, 'm', 'f')

    self.assertEqual(len(matriz), 5)
    self.assertEqual(len(matriz[0]), 6)


unittest.main()