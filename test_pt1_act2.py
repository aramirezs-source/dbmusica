import unittest
from xxx.pt1 import suma, resta, multiplica, divideix, arrel_quadrada

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        print("\nIniciant prova...")

    def tearDown(self):
        print("Prova finalitzada.")

    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(0, 0), 0)
        self.assertEqual(suma(-1, 1), 0)

    def test_resta(self):
        self.assertEqual(resta(5, 3), 2)
        self.assertEqual(resta(0, 0), 0)
        self.assertEqual(resta(-1, -1), 0)

    def test_multiplicacio(self):
        self.assertEqual(multiplica(2, 3), 6)
        self.assertEqual(multiplica(0, 999), 0)
        self.assertEqual(multiplica(-1, -1), 1)

    def test_divisio(self):
        self.assertEqual(divideix(6, 3), 2)
        self.assertEqual(divideix(3, 0), "Error: No es pot dividir per zero.") 
        self.assertEqual(divideix(0, 3), 0)

    def test_arrel_quadrada(self):
        self.assertEqual(arrel_quadrada(4), 2.0)
        self.assertEqual(arrel_quadrada(0), 0.0)
        self.assertEqual(arrel_quadrada(-4), "Error: No es pot calcular l'arrel quadrada d'un número negatiu.") 

if __name__ == '__main__':
    unittest.main()
