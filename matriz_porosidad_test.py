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

  def test_with_no_size(self):
    '''
      Should return an empty array
    '''
    matriz = crear_matriz(0, 0, 'm', 'f')

    self.assertEqual([matriz, []])

  def test_has_correct_data(self):
    '''
      Only filled with correct data
    '''
    char1 = 'm'
    char2 = 'f'
    matriz = crear_matriz(10, 10, char1, char2)
    correct = True

    for j in matriz:
      for i in j:
        print(i, char1, char2, i == char1, i == char2)
        if not i == char1 and not i == char2:
          correct = False
          continue

    self.assertEqual(correct, True)

unittest.main()