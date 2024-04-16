import unittest
import sys
sys.path.append('.')

from src.controllers.calculadora import Calculadora
from src.models.pessoa import Pessoa

class TestCalculadora(unittest.TestCase):
    
    def setUp(self):
        pessoa = Pessoa(1,82.8,1.78,25,3)
        self._calculadora = Calculadora(pessoa)

    def test_calcular_geb(self):
        geb = self._calculadora.calcular_geb() 
        self.assertEqual(1044.9, geb)

    def test_calcular_calorias_diarias(self):
        total = 1044.9 * 1.55
        self.assertEqual(total, self._calculadora.calcular_calorias_diarias())

    def tearDown(self):
        self._calculadora = None

if __name__ == '__main__':
    unittest.main()