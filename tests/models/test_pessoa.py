import unittest
import sys
sys.path.append('.')

from src.models.pessoa import Pessoa

class TestPessoa(unittest.TestCase):
    
    def setUp(self):
        self.pessoa = Pessoa(1,82.8,1.78,25,3)

    def test_fator_peso(self):
        self.assertEqual(13.75, self.pessoa.fator_peso)

    def test_fator_altura(self):
        self.assertEqual(5, self.pessoa.fator_altura)

    def test_fator_idade(self):
        self.assertEqual(6.76, self.pessoa.fator_idade)

    def test_fator_atividade_fisica(self):
        self.assertEqual(1.55, self.pessoa.fator_atividade_fisica)

    def tearDown(self):
        self.pessoa = None

if __name__ == '__main__':
    unittest.main()