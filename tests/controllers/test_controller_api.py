import unittest
import json
import sys
sys.path.append('.')

from src.controllers.controller_api import ControllerApi

class TestControllerApi(unittest.TestCase):

    def test_get_gasto_calorico_diario(self):
        total = 1044.9 * 1.55
        total_dict = {'daily_calories':total}
        gasto_calculado = ControllerApi.get_gasto_calorico_diario(1,82.8,1.78,25,3)
        self.assertEqual(json.dumps(total_dict, ensure_ascii=False), gasto_calculado)

if __name__ == '__main__':
    unittest.main()
