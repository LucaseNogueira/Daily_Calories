import json
import sys
sys.path.append('.')

from src.controllers.calculadora import Calculadora
from src.models.pessoa import Pessoa

class ControllerApi:
    
    @classmethod
    def get_gasto_calorico_diario(self,sexo: int, peso: float, altura: float, idade: int, atividade_fisica: int):
        pessoa = Pessoa(
            sexo=sexo,
            peso=peso,
            altura=altura,
            idade=idade,
            atividade_fisica=atividade_fisica
        )
        calculadora = Calculadora(pessoa)
        calorias_diarias = {'daily_calories':calculadora.calcular_calorias_diarias()}
        return json.dumps(calorias_diarias, ensure_ascii=False)