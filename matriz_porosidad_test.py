import numpy as np
import unittest
from matriz_porosidad import create_matrix

class MatrizPorosidadTests(unittest.TestCase):
  def test_has_to_be_list(self):
    '''
      Should returns a python list
    '''
    self.assertTrue(type(create_matrix(6, 5, 'm', 'f')) is np.ndarray)
  
  def test_has_given_size(self):
    '''
      Should returns a matrix with certain size given parameters
    '''
    matriz = create_matrix(6, 5, 'm', 'f')

    self.assertEqual(len(matriz), 5)
    self.assertEqual(len(matriz[0]), 6)

  def test_with_no_size(self):
    '''
      Should return an empty array
    '''
    matriz = create_matrix(0, 0, 'm', 'f')

    self.assertEqual(len(matriz), len([]))

  def test_has_correct_data(self):
    '''
      Only filled with correct data
    '''
    char1 = 'm'
    char2 = 'f'
    matriz = create_matrix(10, 10, char1, char2)
    correct = True

    for j in matriz:
      for i in j:
        if not i == char1 and not i == char2:
          correct = False
          continue

    self.assertEqual(correct, True)

  def test_no_number_size(self):
    '''
      Should return an error if the matrix doesn't receive a number in its dimensions
    '''
    self.assertEqual(create_matrix('ex', 10, 'm', 'f'), "n debe ser un número entero")

  def test_negative_size(self):
    '''
      Should return an error if the matrix receive a negative number in its dimensions
    '''
    self.assertRaises(IndexError, create_matrix(-1, -2, 'm', 'f'), 1, '1')

unittest.main()
