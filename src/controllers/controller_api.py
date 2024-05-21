import json
import sys
sys.path.append('.')

from src.controllers.calculadora import Calculadora
from src.models.pessoa import Pessoa
from src.models.pessoa_response import PessoaResponse

class ControllerApi:
    
    @classmethod
    def get_gasto_calorico_diario(self,sexo: int, peso: float, altura: float, idade: int, atividade_fisica: int):
        '''Calcula o gasto calórico diário de uma pessoa e retorna o dado como um objeto JSON

        Inputs:
        - sexo: INT sexo da pessoa (1 - Masculino, 2 - Feminino)
        - peso: FLOAT peso da pessoa em kilograma
        - altura: FLOAT altura da pessoa em centimetros
        - idade: INT idade da pessoa
        - atividade_fisica: INT (1 - Sedentário; 2 - Levemente Ativo; 3 - Moderadamente Ativo; 4 - Muito Ativo; 5 - Extremamente Ativo)

        Outputs:
        - {'daily_calories' : FLOAT}
        '''
        pessoa = Pessoa(
            sexo=sexo,
            peso=peso,
            altura=altura,
            idade=idade,
            atividade_fisica=atividade_fisica
        )
        calculadora = Calculadora(pessoa)
        calorias_diarias = calculadora.calcular_calorias_diarias()
        resposta = PessoaResponse(calorias_diarias)
        return resposta.to_dict