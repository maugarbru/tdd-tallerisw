import unittest
from matriz_porosidad import crear_matriz

class MatrizPorosidadTests(unittest.TestCase):
  def test_has_to_be_list(self):
    '''
      Should returns a python list
    '''
    self.assertIs(crear_matriz(6, 5, 'm', 'f'), list)
  
  def test_has_given_size(self):
    '''
      Should returns a matrix with certain size given parameters
    '''
    matriz = crear_matriz(6, 5, 'm', 'f')

    self.assertEqual(len(matriz), 6)
    self.assertEqual(len(matriz[0]), 5)


unittest.main()