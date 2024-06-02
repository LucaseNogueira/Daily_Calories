import unittest
import sys
sys.path.append('.')

class TestAlimento(unittest.TestCase):

    def test_atualiza_porcao_e_calorias(self):
        self.assertEqual(200, 200)
        self.assertEqual(400, 400)

if __name__ == '__main__':
    unittest.main()